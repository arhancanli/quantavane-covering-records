# Covering design records from Quantavane

A (v,k,t) covering design is a collection of k-point blocks drawn from v points such that every set of t points lies
inside at least one block. C(v,k,t) is the fewest blocks possible. For most parameters the exact value is unknown, so
public tables record the best covering anyone has found.

These coverings each use one block fewer than the best known before them:

| Entry | Blocks | Previous best |
|---|---|---|
| C(41,9,2) | 27 | 28 |
| C(52,11,2) | 29 | 30 |
| C(65,14,2) | 28 | 29 |
| C(66,12,2) | 38 | 39 |
| C(67,15,2) | 26 | 27 |
| C(69,11,2) | 50 | 51 |
| C(70,21,2) | 15 | 16 |
| C(71,16,2) | 26 | 27 |
| C(75,17,2) | 26 | 27 |
| C(76,14,2) | 38 | 39 |
| C(82,18,2) | 27 | 28 |
| C(84,19,2) | 26 | 27 |
| C(87,16,2) | 38 | 39 |
| C(92,16,2) | 42 | 43 |
| C(94,14,2) | 54 | 55 |
| C(94,17,2) | 39 | 40 |
| C(96,22,2) | 25 | 26 |
| C(98,21,2) | 28 | 29 |
| C(98,22,2) | 26 | 27 |
| C(99,17,2) | 43 | 44 |
| C(36,10,3) | 80 | 81 |
| C(41,17,3) | 26 | 27 |
| C(42,12,3) | 76 | 77 |
| C(47,21,3) | 21 | 22 |
| C(49,13,3) | 81 | 82 |
| C(58,23,3) | 30 | 31 |
| C(70,25,3) | 37 | 38 |
| C(72,23,3) | 51 | 52 |
| C(28,17,4) | 20 | 21 |
| C(40,23,4) | 24 | 25 |

"Previous best" is the value in the La Jolla Covering Repository's final data (Daniel M. Gordon, CC BY 4.0,
doi:10.5281/zenodo.19735294). Fifteen of the previous values came from general constructions. Thirteen came from
computer searches: C(41,9,2) by Colin Barker, C(70,21,2), C(94,14,2), C(96,22,2), C(47,21,3) and C(28,17,4) by Jan de
Heer and Steve Muir, C(41,17,3), C(49,13,3), C(70,25,3), C(72,23,3) and C(40,23,4) by Franco Atzeni in 2024,
C(99,17,2) by Franco Atzeni in 2025, and C(58,23,3) by Giovanni Acerbi with his Wheeling Systems Checker in 2023. For
the other two, C(69,11,2) by Flavio Perona (2015) and C(36,10,3) by Marco Meoli (2019), the repository records no
method.

C(52,11,2) = 29 and C(94,14,2) = 54 meet the known lower bounds, so both are optimal.

On 25 October 2026, 25 of these coverings were uploaded to coveringrepository.com, which tracks improvements made
after the La Jolla repository froze, as Arhan Canli (Quantavane), where they are the listed records and free to
download. The other five had been reached independently and uploaded there shortly before: C(47,21,3) by Hossein
Farahani on 22 October, C(71,16,2) and C(76,14,2) by Hossein Farahani on 23 October, and C(66,12,2) and C(75,17,2) by
Franco Atzeni on 24 October.

## (v,k,t,m) coverings

A (v,k,t,m) covering, with m > t, asks less: every set of m points must share at least t points with some block.
The Covering Repository (coveringrepository.com) keeps a table of these too. Each of these uses one block fewer than
the value it listed when we uploaded it there (25 and 26 October 2026):

| Entry | Blocks | Previous best |
|---|---|---|
| C(25,9,8,19) | 10 | 11 |
| C(35,12,7,18) | 7 | 8 |
| C(25,15,13,20) | 7 | 8 |
| C(27,15,3,4) | 5 | 6 |
| C(39,13,3,5) | 12 | 13 |
| C(42,15,3,6) | 6 | 7 |
| C(57,15,3,8) | 7 | 8 |
| C(22,13,5,6) | 16 | 17 |
| C(22,9,8,16) | 16 | 17 |

C(25,9,8,19), C(25,15,13,20), C(27,15,3,4), C(39,13,3,5), C(22,13,5,6) and C(22,9,8,16) came from a bit-parallel local search. The other three
are unions with one block holding the first k points: C(35,12,7,18) adds a (23,12,7,12) covering with 6 blocks that
the same search found, C(42,15,3,6) adds our C(27,15,3,4), and C(57,15,3,8) adds our C(42,15,3,6).
Taking complements turns any (22,9,8,16) covering into a (22,13,5,6) covering with the same number of blocks, and back.

## Check them yourself

```sh
python3 verify.py
```

The script uses only the Python standard library. For each file it checks the block count, that every block has k
distinct points from 1 to v, and that every one of the C(v,t) t-subsets is covered. For a (v,k,t,m) covering it
searches exactly for an m-subset that meets every block in fewer than t points and confirms there is none. Each covering was also checked by
two other independent checkers before release.

## How they were found

A compiled local search in the style of Nurmela and Östergård (1993). With the number of blocks fixed, it minimises the
number of uncovered t-subsets by swapping one point of a block at a time. It alternates simulated annealing with
breakout weighting, the clause-weighting idea from SAT local search. It ran on a laptop at no cost, starting from
random blocks. The engine is open source: https://github.com/arhancanli/quantavane

## Files

- `coverings/C_v_k_t_b.txt` and `coverings/C_v_k_t_m_b.txt`: one block per line, points numbered from 1.
- `records.json`: the table above in machine-readable form.
- `verify.py`: the checker.

## Licence

CC BY 4.0 (see `LICENSE`). Please credit "Arhan Canli, Quantavane" when you use these coverings.

Arhan Canli, Quantavane · quantavane.com
