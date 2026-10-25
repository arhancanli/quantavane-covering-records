"""Check every covering in this folder from scratch. Plain Python 3, no other packages.

A (v,k,t) covering design is a set of blocks, each k distinct points from 1..v, such that every t-element subset of
{1..v} lies inside at least one block. A (v,k,t,m) covering, with m > t, needs only that every m-element subset meets
some block in at least t points. For each file this script checks the block count, the size and range of every block,
and coverage: for (v,k,t) it lists all C(v,t) t-subsets; for (v,k,t,m) it searches exactly for an m-subset that meets
every block in at most t-1 points and reports that none exists. Run: python3 verify.py"""
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def covers_everything(blocks, v, k, t):
    for b in blocks:
        if len(b) != k or len(set(b)) != k or not all(1 <= p <= v for p in b):
            return False, f"bad block {b}"
    seen = set()
    for b in blocks:
        seen.update(itertools.combinations(sorted(b), t))
    missing = math.comb(v, t) - len(seen)
    return missing == 0, f"{missing} of {math.comb(v, t)} {t}-subsets uncovered" if missing else "every subset covered"


def no_bad_m_subset(blocks, v, k, t, m):
    """True if every m-subset of 1..v meets some block in at least t points. Points with the same set of blocks are
    interchangeable, so the search picks how many points of each such type a bad m-subset would use, never more than
    t-1 from any block, by depth-first search with a counting bound."""
    for b in blocks:
        if len(b) != k or len(set(b)) != k or not all(1 <= p <= v for p in b):
            return False, f"bad block {b}"
    member = {p: frozenset(i for i, b in enumerate(blocks) if p in b) for p in range(1, v + 1)}
    count = {}
    for p, ty in member.items():
        count[ty] = count.get(ty, 0) + 1
    free = count.pop(frozenset(), 0)
    types = sorted(count, key=lambda ty: -len(ty))
    cap = [t - 1] * len(blocks)
    nodes = 0

    def room(ty):
        return min([count[ty]] + [cap[i] for i in ty])

    def search(j, size):
        nonlocal nodes
        nodes += 1
        if size >= m:
            return True
        if size + sum(room(ty) for ty in types[j:]) < m:
            return False
        ty = types[j]
        for x in range(room(ty), -1, -1):
            for i in ty:
                cap[i] -= x
            found = search(j + 1, size + x)
            for i in ty:
                cap[i] += x
            if found:
                return True
        return False

    bad = search(0, free) if types else free >= m
    return (not bad), (f"no {m}-subset misses every block ({nodes} search nodes)" if not bad
                       else f"some {m}-subset meets every block in fewer than {t} points")


def main():
    ok_all = True
    with open(os.path.join(HERE, "records.json")) as f:
        records = json.load(f)
    for r in records:
        with open(os.path.join(HERE, "coverings", r["file"])) as f:
            blocks = [[int(x) for x in line.split()] for line in f if line.strip()]
        m = r.get("m", r["t"])
        if m == r["t"]:
            ok, note = covers_everything(blocks, r["v"], r["k"], r["t"])
            name = f"C({r['v']},{r['k']},{r['t']})"
        else:
            ok, note = no_bad_m_subset(blocks, r["v"], r["k"], r["t"], m)
            name = f"C({r['v']},{r['k']},{r['t']},{m})"
        ok = ok and len(blocks) == r["blocks"]
        ok_all &= ok
        print(f"{name} <= {len(blocks):3}  (previous best {r['previous']})  {'VALID' if ok else 'INVALID'}: {note}")
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
