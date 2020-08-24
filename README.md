## The useless life story before the recipe you actually want to read
It's odd how my love of Turing machines has grown after leaving university.  While I was casually reading about complexity theory, grammars, and about the strangeness of undecideability/uncomputability, I got sucked into the realm of Turing machines.  There is just such a beauty to busy beavers, programmability, and halting.  This admiration was only deepened by seeing Richard Ridel's video of a wooden Turing Machine https://www.youtube.com/watch?v=vo8izCKHiF0 One day, after building a wooden clock, I hope to conquer a physical Turing machine.  I'd connect an escapement to this machine and let it run all day long - it'd feel alive!  In the meantime, I decided to quickly code up a quick Turing machine in python.

## What is a Turing machine?
https://en.wikipedia.org/wiki/Turing_machine can do a much better job than I ever could, but basically, a Turing machine is given an infinite tape and can read from the tape at its present location.  Based off the current state and current reading, the Turing machine will write, move, and change states.

## How to use
With the command line in the project directory, run `python3 turing.py`
This will show you your options
```
Turing machine options:
  0   - back and forth forever
  1   - increment non blank
  b22 - 2 state 2 symbol busy beaver (sigma=  4, s=   6) from Pascal Michel
  b32 - 3 state 2 symbol busy beaver (sigma=  6, s=  14) from wikipedia
  b42 - 4 state 2 symbol busy beaver (sigma= 13, s= 107) from wikipedia
  b23 - 2 state 3 symbol busy beaver (sigma=  9, s=  38) from Pascal Michel
Which turing machine do you want?
```
Then type one of the following options:

### 0
One of my first self-discovered (and very much not novel!) ideas would be a machine that just goes back and forth, writing nothing.
<details>
  <summary>Click to see results!</summary>

```
00000: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                           a
00001: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                         a
00002: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                       a
00003: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                     a
00004: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                   a
00005: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                 a
00006: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                   b
00007: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                     b
00008: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                       b
00009: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                         b
00010: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                           b
00011: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                             b
00012: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                               b
00013: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                                 b
00014: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                                   b
00015: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                                     b
00016: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                                   a
00017: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                                 a
00018: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                               a
00019: 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
                    [...]
```
</details>

### 1
Machine that keeps incrementing by one until overflow - if I had a physical Turing machine, I'd just let it run indefinitely.  This is a fun and simple one to derive yourself!
<details>
  <summary>Click to see results!</summary>

```
00000: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                                         a
00001: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                                       b
00002: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 1 _ _ _
                                         a
00003: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 1 _ _ _
                                       b
00004: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                                     b
00005: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 1 0 _ _ _
                                       a
00006: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 1 0 _ _ _
                                         a
00007: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 1 0 _ _ _
                                       b
00008: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 1 1 _ _ _
                                         a
00009: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 1 1 _ _ _
                                       b
00010: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 1 0 _ _ _
                                     b
00011: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                                   b
00012: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 0 _ _ _
                                     a
00013: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 0 _ _ _
                                       a
00014: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 0 _ _ _
                                         a
00015: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 0 _ _ _
                                       b
00016: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 1 _ _ _
                                         a
00017: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 1 _ _ _
                                       b
00018: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 0 _ _ _
                                     b
00019: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 1 0 _ _ _
                                       a
00020: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 1 0 _ _ _
                                         a
00021: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 1 0 _ _ _
                                       b
00022: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 1 1 _ _ _
                                         a
00023: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 1 1 _ _ _
                                       b
00024: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 1 0 _ _ _
                                     b
00025: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 1 0 0 _ _ _
                                   b
00026: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                                 b
00027: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                   a
00028: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                     a
00029: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                       a
00030: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                         a
00031: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                       b
00032: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 1 _ _ _
                                         a
00033: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 1 _ _ _
                                       b
00034: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                     b
00035: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 1 0 _ _ _
                                       a
00036: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 1 0 _ _ _
                                         a
00037: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 1 0 _ _ _
                                       b
00038: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 1 1 _ _ _
                                         a
00039: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 1 1 _ _ _
                                       b
00040: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 1 0 _ _ _
                                     b
00041: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                   b
00042: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 0 _ _ _
                                     a
00043: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 0 _ _ _
                                       a
00044: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 0 _ _ _
                                         a
00045: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 0 _ _ _
                                       b
00046: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 1 _ _ _
                                         a
00047: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 1 _ _ _
                                       b
00048: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 0 _ _ _
                                     b
00049: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 1 0 _ _ _
                                       a
00050: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 1 0 _ _ _
                                         a
00051: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 1 0 _ _ _
                                       b
00052: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 1 1 _ _ _
                                         a
00053: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 1 1 _ _ _
                                       b
00054: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 1 0 _ _ _
                                     b
00055: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 1 0 0 _ _ _
                                   b
00056: _ _ _ _ _ _ _ _ _ _ _ _ _ 1 0 0 0 _ _ _
                                 b
00057: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                               b
00058: _ _ _ _ _ _ _ _ _ _ _ _ _ 0 0 0 0 _ _ _
                                 HALT
end counts: {0: 4, '_': 16}

```
</details>

### bXX
The reasonable Busy Beavers are here!  It's incredible how so much thought had to go into proving longest-running/most-outputting busy beavers.
<details>
  <summary>Click to see one of the beavers (2 state, 3 symbol)!</summary>

```
00000: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                               a
00001: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                                 b
00002: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                               a
00003: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00004: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                           a
00005: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00006: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                           b
00007: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00008: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                               b
00009: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00010: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                           b
00011: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                         b
00012: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                       a
00013: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 1 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                         b
00014: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                       b
00015: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 1 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                         b
00016: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 1 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                           b
00017: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 1 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00018: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                               b
00019: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                                 b
00020: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                               b
00021: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00022: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                           b
00023: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                         b
00024: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                       b
00025: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                     b
00026: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                   a
00027: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                     b
00028: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                   b
00029: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                     b
00030: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                       b
00031: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                         b
00032: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                           b
00033: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                             b
00034: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                               b
00035: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                                 b
00036: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                                   b
00037: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                                 a
00038: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                                                   HALT
end counts: {0: 31, 1: 1, 2: 8}

```
</details>

Note - you will have to press enter every 30 iterations, this is to give you time to admire the changes.