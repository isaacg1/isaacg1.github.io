---
layout: post
title: "Intuitive Mathematics: Brownian Motion"
---

I study [stochastic processes](https://en.wikipedia.org/wiki/Stochastic_process).
In simpler words, "things that change randomly over time".
In order to research something, it is vital to understand it intuitively, not just procedurally.
To be able to get good estimates fast (or in your head), not just the correct answer slowly.
Having a good intuition is a superpower:
You can predict what answers will be correct before working it out rigorously.
Having a bad intuition can be worse than nothing,
because it'll send you down the wrong path.

Unfortunately, intuition is rarely taught.
Most teaching, whether in a class or online, teaches procedural understanding:
how to get the exact answer slowly.

To start changing that,
I'm going to teach you how to intuitively think about
[Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion),
an important stochastic process.

## Brownian Motion

We'll specifically look at
single-particle discrete Brownian motion.
In Brownian motion,
for each time step,
the particle moves in one of the cardinal directions (up, down, left, right, etc.)
with equal probability.
For instance,
in one dimension, the particle might move

    left, right, right, left, ...

In two dimensions, the particle might move

    left, up, up, down, left, right, ...

## The puzzle

Here's the question we're going to investigate about Brownian motion:

In each of 1, 2, and 3 dimensional Brownian motion,
what's the chance that the particle ever returns to the origin,
its starting point? Is it probability 1, or something less?
In expectation, by time step t, roughly how many times has the particle returned to the origin?

## Some time to ponder

If you've never seen this puzzle before,
or if you have seen it and don't remember the solution,
I'd recommend pondering it, maybe for a minute.

It's a very good puzzle,
and feeling the shape of the puzzle on your own
will help you engage with it.

## Intuitive solution

Let's start solving.
Every step in this solution should be doable in one's head,
given appropriate background knowledge.

First, notice that each dimension basically functions independently.
The particle has some probability of increasing by 1,
some of decreasing by 1,
and some of staying constant (except for 1 dimension).

These dimensions aren't independent,
but the correlation is confined to a single step,
so as t gets large it shouldn't matter.
Let's treat them as independent.

At this point, we're asking:
"What's the chance that the particle is at its staring point along a given dimension
after t steps?".
If we can answer that,
we can multiply the probabilities for each independent dimension.

Well, each step is independent, so we can apply the Central Limit theorem.
The Central Limit theorem
states that if we add the same random variable to itself
many times,
the sum converges to a Gaussian distribution
(Note: only works for finite-variance random variables).
To determine that Gaussian distribution,
we only need to know its mean and variance.

The mean of the position distribution is 0,
because the mean of each step is 0 and expectation is linear:
the expectation of a sum is the sum of the expectations.
A less well-known fact is that variance is linear for independent random variables:
the variance of a sum of independent random variables is the sum of the variances.
The variance of each step is a constant:
1 for 1 dimension,
1/2 for 2 dimensions,
and 1/3 for 3 dimensions.
The variance of the position distribution is therefore roughly t,
dropping constant factors.

Now that we've identified the right Gaussian distribution,
we need to know the density of the Gaussian distribution near 0.
I don't remember the pdf of the Gaussian distribution,
but I know that a bell curve
is flattish towards the middle.
In particular, I remember that the flattish bit spans about a standard deviation,
the square root of the variance.
Also, the flattish bit makes up about half of the probability mass of the distribution,
or at any rate a constant fraction.
Therefore, I'm pretty sure that the density around the middle
is about the reciprocal of the standard deviation.
In this case, that's `1/t^0.5`.

We've basically solved the problem for 1 dimension:
The particle is at the origin on step t with probability about `1/t^0.5`.
To add this up over all steps up to t,
we can integrate this expression.
Integrating and summing are almost the same.
We find that the particle returns to the origin
about `t^0.5` times by step t.
In particular, we can by fairly sure that the particle returns to the origin with probability 1.


Using our independence guess, we can also solve the problem for 2 and 3 dimensions.
In 2 dimensions,
the particle is at the origin on step t
with probability about `(1/t^0.5)^2 = 1/t`.
Integrating,
the particle returns to the origin about `ln t` times by step t.
Much less often, but still infinitely often,
and with probability 1.

In 3 dimensions,
everything changes.
The particle is at the origin on step t
with probability about `1/t^1.5`.
Integrating,
the particle returns to the origin a constant number of times by step t.
Correspondingly, there's a nonzero probability
that the particle never returns to the origin.

## Wrapup

Through this intuitive analysis, we find different qualitative behaviors in dimensions 1, 2, and 3.
In 1 dimension, the particle returns often. In 2, it returns less often, but it still returns eventually.
In 3, the particle eventually stops returning at all.

All of these results are correct up to constant factors,
which can be confirmed through simulation or exact analysis.

Some takeaways, in my opinion:

* Intuitive analysis is fun. You can fly through a problem,
engaging enough to see the truth, without getting bogged down.

* Intuitive analysis isn't easy.
You have to know which terms can be safely thrown away without ruining the result.
You have to know what assumptions are safe to make.
And you have to have an intuitive understanding of many other concepts,
in order to apply them while in an intuitive mode of thought.

* Intuitive analysis involves very little symbol-manipulation.
Writing formulas and manipulating symbols
is the hallmark of procedural mathematics.
Intuitive mathematics avoids such things as much as possible,
because they almost always bog you down, and rarely aid the intuition.

I hope you enjoyed this taste of intuitive mathematics!
I definitely did.
