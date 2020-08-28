---
published: true
title: Fair Gambler's Ruin
layout: post
---
The fair gambler's ruin problem is as follows: Suppose a gambler is repeatedly betting a dollar on the flip of a coin. The gambler starts with one dollar, and stops if they ever drop to zero dollars. How likely is it that the gambler is still going after n flips?

We'll try and answer this in two ways: With a rough, heuristic argument, via simulation, and an exact analysis.

Note the game is "fair" in the sense that the expected amount of money that the gambler has is always 1, however many flips have occurred. Nonetheless, the gambler eventually stops with probability 1. This is a null-recurrent Markov chain.

## Heuristic

Let's approach this from the other side: after how many flips does the probability that the gambler is still flipping drop to p? Think of p as a small probability like 1%.

Since the game is fair, conditioning on the game not being over, the gambler has 1/p dollars on average. The evolution of the gambler's money resembles Brownian motion. K steps of Brownian motion have a variance of `k^.5`. Thus, for the Brownian motion to have reached 1/p with probability p took about 1/p^2 flips.

Thus, the chance that the gambler is still going after n steps is about `1/n^.5`.

## Simulation

I simulated the Fair Gambler's Ruin problem to see how likely it would be for the gambler to reach `n` flips.
Here's the code I used:

````
import random
trials = 1000000

random.seed(0)
targets = [10, 100, 1000, 10000]
success = [0 for _ in targets]
for i in range(trials):
    m = 1
    i = 0
    stop = max(targets)
    while m > 0 and i < stop:
        i += 1
        if random.randrange(2):
            m += 1
        else:
            m -= 1
    for index, target in enumerate(targets):
        if i >= target:
            success[index] += 1
for s, t in zip(success, targets):
    print("{}: {}, {:.5} guess, {:.5} ratio"
            .format(t,
                s/trials,
                1/(t**0.5),
                (s/trials)*(t**0.5)))

````

The results, after a million trials:

````
10: 0.245665, 0.31623 guess, 0.77686 ratio
100: 0.079766, 0.1 guess, 0.79766 ratio
1000: 0.025075, 0.031623 guess, 0.79294 ratio
10000: 0.007923, 0.01 guess, 0.7923 ratio
````

Empirically, it seems like the correct formula might be `0.79/n^.5`.

## Exact

This argument is a paraphrasement of this one from
[lonza leggiera](https://math.stackexchange.com/questions/3792480/fair-gamblers-ruin-tail-probability)
on Mathematics Stack Exchange,
since I had trouble figuring it out myself.

Let's write `p_{i,n}` for the probability that the gambler has `i` dollars after `n` flips.
We can write this recursively:

````
p_{1,0} = 1
p_{i,n} = (p_{i-1,n} + p_{i+1,n})/2 if i>2
p_{0,n} = p_{0,n-1} + p_{1,n-1}/2
p_{1,n} = p_{2,n-1}/2
````

Let's multiply the probabilities by `2^n` and write this in a chart:

````
 i  0  1 2 3 4 5 6 7 8 9
n ---------------------
0|     1
1|  1    1
2|  2  1   1
3|  5     2   1
4| 10  2   3   1
5| 22    5   4   1
6| 44  5   9   5   1
7| 93   14  14   6   1
8|186 14  28  20   7   1
````
We can observe, and it is fairly easy to prove, that the 1 column is the catalan numbers. The probability we care about is the sum over all `i>0` for a given `n`.
This turns out to be n choose n/2, divided by `2^n`. The asymptotic growth is `(2/(pi n))^0.5`, which is about 0.798 `n^0.5`, matching the observations in simulation.
