---
published: true
title: 'Betting for the Median'
layout: post
---
Let's suppose we're playing a game.
We start with 1 dollar, then there are a series of betting rounds.
In each round, we can bet any amount, from nothing to all of our money.
After we bet, we flip a fair coin.
If heads, we receive *triple* the money we bet.
If tails, we lose the money we bet.
Finally, there's a limited number of rounds,
so we can't just slowly accumulate money over a long time.


## Strategy

Now, the question is, how much money should we bet?
Well, it depends on our goal.

If the goal is to maximize our *mean money*,
the best strategy is to bet all of our money every round.
Suppose there were 9 rounds.
This strategy would have a 0.2% chance of making about $20,000,
and would otherwise end with $0,
for a mean final money of about $38.

But maybe we don't want to only make any money 0.2% of the time.
In that case, we can change our goal.

Maybe our goal is to maximize the *geometric mean* of our final money.
The geometric mean is the weighted *product* of our outcomes,
where the traditional (arithmetic) mean is the weighted *sum*.
This is equivalent to maximizing the expected logarithm of the final money.

For this goal,
the optimal strategy is the
[Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion),
which in this setting states that we should always wager
1/4 of our current money.
By doing so, our geometric mean rises by a factor of about 6% each round.
After 9 rounds, our geometric mean will be $1.70.

But maybe this growth rate is too slow - too conservative.
Again, we can change our goal.

## Goal: Median

Let's set our goal to be to maximize our median final money.
In other words, let's maximize our 50th percentile outcome.
To handle ties, we'll actually focus on our (50+eps)th percentile outcome.

This goal addresses the problem with the "bet it all" strategy,
which only makes money 0.2% of the time,
as well as with the Kelly Criterion,
because we're OK losing it all some of the time, just not most of the time.

The optimal strategy for the median is a bit trickier to write down.
I initially found it with a dynamic program exponential-time search,
but I've managed to find the underlying pattern,
so that one can calculate the optimal strategy with no external aid.

Unlike the previous two strategies, this is a state-dependent strategy:
It relies on knowing how many rounds are left, and how many heads or tails you've flipped so far.
In the end, you'll make a fixed amount of money half the time, if you flip more heads than tails,
and lose it all the other half of the time, if you flip more tails than heads.

### Optimal Median Strategy

To calculate the optimal median strategy, you need two pieces of information:
The number of flips remaining (which we'll call `f`) and the number of remaining tails you can afford
(which we'll call `t`). `t` starts at `(f-1)/2` (we'll assume `f` is odd), and goes down by 1 whenever we flip a tails.
If `t` goes negative, that means we've flipped more tails than we can possibly flip heads, and we'll have lost all our money.
If `t` reaches `f`, that means we've flipped enough heads to reach our target, and we won't bet any more money.

Our bet size is a fraction of our total money:

* The numerator of our bet fraction is `(f-1 choose t) * 2^t`
([A013609](https://oeis.org/A013609)).

* The denominator of our bet fraction is `sum (i=0 to t) of (f choose i) * 2^i`
([A193860](https://oeis.org/A193860)).

For example, with f=9 flips to go, and t=4 tails remaining, our bet fraction would be:

* Numerator: (8 choose 4) * 2^4 = 1120.

* Denominator: 1 + 18 + 144 + 672 + 2016 = 2851

Our final median money will be 3^f/denominator = 19683/2851 ≈ $6.90.

### Example playthrough

Let's do an example playthrough of the game, trying to maximize our median.
Note that "bet" is the fraction of our current money that we're betting,
not an absolute quantity.

f=9, t=4, bet = 1120/2851 ≈ 39%.

Win! Money: 5091/2851 = 3 * 1697/2851 ≈ $1.79

f=8, t=4, bet = 560/1697 ≈ 33%.

Win! Money: 8451/2851 = 9 * 939/2851 ≈ $2.96

f=7, t=4, bet = 240/939 ≈ 26%.

Lose! Money: 6291/2851 = 27 * 233/2851 ≈ $2.21

f=6, t=3, bet = 80/233 ≈ 34%.

Lose! Money: 4131/2851 = 81 * 51/2851 ≈ $1.45

f=5, t=2, bet = 24/51 ≈ 47%.

Win! Money: 8019/2851 = 243 * 33/2851 ≈ $2.81

f=4, t=2, bet = 12/33 ≈ 36%.

Win! Money: 13851/2851 = 729 * 19/2851 ≈ $4.86

f=3, t=2, bet = 4/19 ≈ 21%.

Win! Money: 19683/2851 ≈ $6.90

We've reached our target,
so we won't bet any more money to avoid losing it.

### Median: Single bet

One way of looking at the effect of this strategy is that we've taken our 9 rounds of 3x bets
with a 50% chance of success
and turned them into one round of a 6.9x bet, still with a 50% chance of success.
We're compressing our repeated bets to have the same effect as a single bet with a better payoff,
but the same odds of success.
This is in contrast to the "bet it all" strategy, which turns the 9 rounds
into a single round of a 19683x payoff, with a 1/512 chance of success.

## Comparing different goals

Here's the optimal return under each of these different goals:

|flips|mean   |median|geometric mean|
|-----|-------|------|--------------|
|1    |1.50   |3.00  |1.06          |
|3    |3.38   |3.86  |1.19          |
|5    |7.59   |4.76  |1.34          |
|7    |17.09  |5.77  |1.51          |
|9    |38.44  |6.90  |1.70          |
|11   |86.50  |8.19  |1.91          |
|13   |194.62 |9.66  |2.15          |
|15   |437.89 |11.33 |2.42          |
|17   |985.26 |13.25 |2.72          |
|19   |2216.84|15.44 |3.06          |

The overall mean has the fastest growth, while both median and geometric mean grow much slower.
Median grows slightly faster than geometric mean, going up by about 5x from 1 to 19 flips,
versus geometric mean's ~3x growth.

Which of these goals feels like the best measure of a "typical" outcome to you?

