---
published: true
title: 'Myopic queueing policies with superexponential switching'
layout: post
---

This post is about an unsuccessful research exploration that I undertook.
I wanted to share my thoughts, even if they didn't lead to any breakthrough.

I've been thinking about Yuan Zhong's talk at the RL&MAS workshop at performance. He considered myopic policies for the X system with unknown service rates, and proved that several classes of myopic policies cannot have full stability region. One class of policies left open were policies where the service threshold curves switched back and forth infinitely often, with the switching points getting rarer and rarer sufficiently fast. I want to examine these policies.

## Simplification: the 112 system

As a simpler subcase, if the queue lengths were always equal, the X system would simplify to a system with one queue, one server, and two service options. Let's call this the 112 system. One service rate is guaranteed to be above λ, one below.

The arguments for the X system all carry over to this simpler system. If we could find a stabilizing myopic policy for the 112 system, it would go a long way towards finding a stabilizing myopic policy for the X system. If the X system cannot be stabilized by a myopic policy, then the 112 system shouldn't be able to be stabilized by a myopic policy either.

By "myopic policy", I mean that the policy maps each queue length q to either service 1 or service 2. The policy cannot adapt to which service rate is above λ.

## Switching points

A myopic policy can be defined by its switching points, the queue lengths at which the service option changes. Let's say that we use service 1 between switching points 2i and 2i+1, and option 2 between points 2i+1 and 2i+2.

Suppose (without loss of generality) that service option 1 has rate above λ, but service option 2 has rate below λ.
Let's call service option 1 rate μ, and service option 2 rate ε, where μ > λ > ε.


If the difference between switching points is large, the system will accumulate around even switching points of the form 2i, having drift away from odd switching points.

Consider the embedded chain consisting of the instants where the system visits even switching points. Starting from switching point 2i, what's the chance that it next visits 2i-2?

To go from s2i to s2i-2, the system would have to first move from s2i to s2i-1, against an upward drift of λ-ε. Moving from s2i-1 to s2i-2 happens with constant probability.

So this would have probability of about Exp(-(s2i - s2i-1)(λ-ε)).

Moving from s2i to s2i+2 would have to move against a downward drift of μ - λ to get to s2i+1, at a probability of about Exp(-(s2i+1 - s2i)(μ - λ)).

## Choosing a policy

Let's choose the switching points such that (s2i+1 - s2i)/(s2i - s2i-1) > (μ - λ)/(λ - ε). Equality would mean exponentially growing switching points, so to cover all μ, λ, ε, let's set the switching points to grow superexponentially, like Exp(q^2), for instance.

Then the probability of moving down will exceed the probability of moving up. Moreover, the expected change in queue length is also negative, for sufficiently large switching points.

Concretely, here's the policy:

Given a queue length q, calculate floor(sqrt(ln(q))). If the result is even, use service option 1. If the result is odd, use service option 2.

So far, I've just made heuristic arguments - does this policy actually achieve full stability?

## Next steps

First, I want to simulate this policy. I'll measure the mean queue length over different intervals of time, for μ = 1, λ = 0.9, ε = 0.1. If the policy is stabilizing, mean queue length should converge. If the policy is unstable, mean queue length should diverge as we examine longer and longer integrals.

Answer: I can't really tell - the simulations take too long to clearly indicate whether it's stable or not.

Second, I want to calculate the stationary distribution. A stable policy gives rise to a stationary probability distribution, and an unstable system doesn't. Does this policy have a stationary probability distribution?

Answer: It doesn't look stable. The relative state probabilities are diverging, at least in a liminf sense. This seems inevitable or even provable: If most states up until q have received epsilon service rate, the relative state probability has grow exponentially in q, which is incompatible with having a stationary distribution.

So how does this jibe with the analysis above? I think the answer might be that the system isn't stable, but that the embedded chain corresponding to visiting new switching points is stable. In other words, E[Q] might be infinite, but E[ln(Q)] might be finite.
