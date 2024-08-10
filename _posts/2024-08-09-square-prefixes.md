---
published: true
title: 'Squares, as quick as possible'
layout: post
---

Terry Tao has a new [blog post](https://terrytao.wordpress.com/2024/08/09/a-result-of-bui-pratt-zaharescu-and-erdos-problem-437/) about [Erdös problem number #437](https://www.erdosproblems.com/437)
that was essentially solved by [a new paper of Bui, Pratt, and Zaharescu](https://zbmath.org/7806815).
The probelm is as follows:

> Let `1 ≤ a_1 < ... < a_k ≤ x` be integers.
How many of the partial products `a_1`, `a_1 a_2`, `a_1 a_2 ... a_k` can be squares?
Is it true that, for any ε > 0, there can be more than x^(1-ε)` squares?

Tao shows in that post that the reason BPZ result is strong enough to resolve this problem,
and give quite tight bounds on the maximum number of squares among the prefixes.

I wanted to explore this question a bit more, especially for small values of x.

For me, it's easiest to think of trying to reach squares as quickly as possible.
We're basically looking at each integer in increasing order, and asking: will this help me reach a square? Will this? Will this?

This problem has optimal substructure:
The fastest way to reach `n` squares is to reach `n-1` squares as fast as possible,
and then reach another square as fast as possible.
There's never any benefit in delaying one square to reach the next sooner - it can't help to do so.

As a result, we can talk about a single optimal sequence,
which reaches the first square product as quickly as possible,
then the second square product as quickly as possible,
and so on, where "as quickly as possible" means
while the value in the sequence is as small as possible.
Also, it's impossible for there to be two equal-fastest ways to reach a square product -
given two ways equally quick ways to reach a square product,
their symmetric difference will reach a square product even faster.

Here's the initial part of the sequence, which I calcaulated by hand,
with the index where each square product is reached marked with a `*`.

`1* 4* 9* 16* 25* 27 28 30 32 35* 36* 49* 50 56 63* 64* 65 66 70 72 77 78* 81* 88 98 99* 100* 102 104 108 112 117 119* 121*`

Some interesting things to note:

1. Every square number is present in the sequence, has a `*`
and is immediately preceeded by a `*` as well.
It's easy to prove that both of these are the case, because a single square integer is always a maximally quickly way to reach a new square product.

2. The sequences of numbers between each square are all relatively [smooth](https://en.wikipedia.org/wiki/Smooth_number) numbers, meaning that they have no large prime factors. One can show that between `n^2` and `(n+1)^2`, all numbers that appear in the sequence must be `2n-1`-smooth.
As it turns out, we have the following actual smoothness:

* `25=5^2` to `36=6^2`: 7-smooth, the maxmimum possible: `27=3^3`, `28=2^2*7`, `30=2*3*5`, `32=2^5`, `35=5*7`.

* `49=7^2` to `64=8^2`: 7-smooth: `50=2*5^2`, `56=2^3*7`, `63=3^2*7`.

* `64=8^2` to `81=9^2`: 13-smooth: `65=5*13`, `66=2*3*11`, `70=2*5*7`, `72=2^3*3^2`, `78=2*3*13`.

* `81=9^2` to `100=10^2`: 11-smooth: `88=2^3*11`, `98=2*7^2`, `99=3^2*11`.

* `100=10^2` to `121=11^2`: 17-smooth: `102=2*3*17`, `104=2^3*13`, `108=2^2*3^3`, `112=2^4*7`, `117=3^2*13`, `119=7*17`

This smoothness property gives rise to a fairly straightforward way to hand-calculate this sequence for these small values. Between each pair of squares, find all the numbers that meet the smoothness cutoff. For instance, in the interval [49, 64], the numbers that meet the smoothness cutoff of 13 are
`50, 52, 54, 55, 56, 60, 63`.

A number can be discarded even if it meets the smoothness cutoff if it's close to the center of the interval and hence has no other numbers in the interval sharing its largest prime factor - for instance, 55 can be discarded this way, even though it meets its interval's smoothness cutoff of 13, because 44 and 66 both lie outside the interval [49, 64].
Our candidates are now down to `50, 54, 56, 60, 63`,
all of which are 7-smooth.

We're now going to think of each number in terms of whether it has an odd number of prime factors for each prime under the smoothness cutoff, `2, 3, 5, 7`. This can be thought of as a bitstring, 1 for odd and 0 for even. So we have `50 → 1000`, `54 →  1100`, `56 → 1001`, `60 → 0110`, `63 → 0001`.
Taking the product of two numbers takes the XOR of their bitstrings.
We can now perform Gaussian elimination over this vector space to try to find a product
which is a square.
In this case, we can know in advance that we'll suceed, because there are more numbers to multiply
than there are primes.
Sure enough, we find that `1000, 1100, 0001` XOR to `0000`, and likewise `50, 56, 63` multiply to a square, namely `176400=420^2`.

In this case, there is only one way to reach a square in this interval, but as the numbers get larger there will be several ways, though there will always be a unique quickest way to reach a square. This will probably make it harder to find more terms of this sequence with this method,
but I didn't reach that point when simply calculating by hand.

It's a fun sequence, and I invite you to explore it yourself!

