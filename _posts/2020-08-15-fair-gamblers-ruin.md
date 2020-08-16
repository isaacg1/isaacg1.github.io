---
published: false
title: Fair Gambler's Ruin
layout: post
---
The fair gambler's ruin problem is as follows: Suppose a gambler is repeatedly betting a dollar on the flip of a coin. The gambler starts with one dollar, and stops if they ever drop to zero dollars. How likely is it that the gambler is still going after n flips?

We'll try and answer this in two ways: With a rough, heuristic argument, and via simulation. I'll also show an attempt at an exact analysis, though I did not succeed.

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

Let's perform a z-transform. The z-transform of an positive-integer-valued random variable X is defined as `x(z) = E[z^X]`. Let's call the number of steps until the gambler loses L. We can use the fact that after one step, L is either 0 or L+L, each with probability 1/2. Thus the z-transform of L is

``l(z) = z/2 (1 + l(z)^2)``

Solving for `l(z)`, we find that

``l(z) = (1 - (1 - z^2)^.5)/z``

We chose this branch because `l(z) < 1`.

We can now extract the moments of `L`.

``E[L] = l'(1) = ∞``

And here I'm stuck. I suspect a better answer involves martingales, but I'm unsure what it is.
