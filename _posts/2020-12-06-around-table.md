---
layout: post
title: "Last Around the Circle"
---
I saw an interesting puzzle in [FiveThirtyEight's Riddler Classic](https://fivethirtyeight.com/features/can-you-pass-the-cranberry-sauce/).
They sovled the problem and gave a proof, but the proof felt incomplete to me,
so I decided to give my own proof.

Here's the problem:

We're taking random walk around a circle with N vertices.
Relative to the starting vertex, which vertex is most likely
to be the last vertex to be visited?

The answer is that each vertex is equally like to be the last one visited.

In order to prove this, we're going to prove something stronger.
We're going to characterize the first k vertices to be visited.
Note that after k vertices are visited,
the k vertices form an interval,
and the current location is one end of the interval.
Also, this interval always includes the starting vertex.

We will number the vertices starting at 0 at the starting point,
and increasing to the right and decreasing to the left.
A positive number indicates that the vertex was reached
from the starting vertex by proceeding to the right from the start,
and vice versa.
We will stop when all vertices are first visited,
so this numbering is unique.

We will show that the probability that the
kth vertex to be visited is vertex x
is |x|/((k-1)\*k).

Note that the last vertex to be visited
uniquely indentifies the entire set of 
vertices that have been visited.

W.l.o.g. let's focus on positive x.

First, let's verify the base case, where k=2.
Here x=1, and this occurs with probability 1/2.
Base case verified.

Now, let's prove the inductive case.
Let's assume that the statement is true up to k vertices visited.
In what ways can x be the k+1th vertex visited?
There are two possibilities:
Either x-1 was the kth vertex visited,
or x-k was the kth vertex visited.
Note that x-k is zero or negative,
and if x-k is zero, then it cannot be the kth vertex visited.

From the [fair gambler's ruin problem](https://en.wikipedia.org/wiki/Gambler%27s_ruin#Fair_coin_flipping),
we know that there is a k/(k+1) probability that the k+1th vertex to be visited
is the vertex next to the kth vertex to be visited,
and a 1/k probability that the vertex neighboring the other end of the interval
is the k+1th vertex to be visited.

Using our inductive hypothesis,
we find that the chance that x is the k+1th vertex to be revealed is
```
  (x-1)/((k-1)*k) * k/(k+1) + (k-x)/((k-1)*k) * 1/(k+1)
= (xk/(k+1) - k/(k+1) + k/(k+1) - x/(k+1))/((k-1)*k)
= ( x(k-1)/(k+1) )/((k-1)*k)
= x/((k+1)*k)
```
as desired.

Now, we can calculate the probability that vertex x is the last one to be revealed.
This must occur if the n-1th vertex to be revealed is either x-1 or x+1-n.
This occurs with probability
```
  (x-1)/((n-2)*(n-1)) + (n-x-1)/((n-2)*(n-1))
= (n-2)/((n-2)*(n-1))
= 1/(n-1)
```
which is identical for all final vertices, as desired.
