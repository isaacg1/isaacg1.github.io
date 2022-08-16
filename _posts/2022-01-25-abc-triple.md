---
layout: post
title: My Very Own ABC Triple
published: true
---

I like the [abc conjecture](https://en.wikipedia.org/wiki/Abc_conjecture).
It says that numbers that are multiplicatively pretty can't be too closely additively related,
in a very precise mathematical way.

The conjecture is about abc triples and a function called the "radical".

The radical of an integer is the product of its prime factors.
For instance, radical(800) = 10.

Consider a triple a + b = c,
where radical(abc) < c.
For instance, 1 + 8 = 9,
and radical(72) = 6 < 9.
We call such a triple an abc triple.
The quality of an abc triple is

    log(c)/log(radical(abc))

For instance, the quality of 1 + 8 = 9
is log(9)/log(6) = 1.23.

The abc conjecture says that the limsup of quality over all abc triples, as c goes to infinity,
is 1.
In other words, for any epsilon > 0,
the number of abc triples with with quality at least 1 + epsilon is finite.

There's a [website](https://abc.tngtech.com/) where you can use your computer
to find fresh abc triples.
I used it, and found the following three abc triples:

    64009 + 282361946544470016 = 282361946544534025,
    q=1.0075342812802697

    167521249 + 7015842132869376 = 7015842300390625,
    q=1.2556682988478818

    15177592680649 + 75611195698334976 = 75626373291015625,
    q=1.0206163223672695

I was interested in the middle abc triple,
because its quality is so high. Let's do some factorization:

    167521249 + 7015842132869376 = 7015842300390625
    12943^2 + 83760624^2 = 83760625^2
    (7 * 43^2)^2 + (2^4 * 3^2 * 719 * 809)^2 = (5^4 * 13^3 * 61)^2

As a result, my radical(abc) is

    2 * 3 * 5 * 7 * 13 * 43 * 61 * 719 * 809
        = 4165223880090
        < 7015842300390625

As you can see, radical(abc) is 3 digits shorter than c,
so this is an abc triple!

This triple has a very special form.
It's a [Pythagorean triple](https://en.wikipedia.org/wiki/Pythagorean_triple):

    a = x^2, b = y^2, c=z^2, x^2 + y^2 = z^2.

Moreover, it's a Pythagorean triple where y and z differ by 1,
helping keep x small.

We can construct such a special Pythagorean triple for any odd x.
Let x = 2d + 1.
Then these special Pythagorean triples are of the form

    x = 2d+1
    y = 2d^2 + 2d
    z = 2d^2 + 2d + 1
    x^2 + y^2 = (2d+1)^2 + (2d^2 + 2d)^2
        = 4d^2 + 4d + 1 + 4d^4 + 8d^3 + 4d^2
        = 4d^4 + 8d^3 + 8d^2 + 4d + 1
    z^2 = (2d^2 + 2d + 1)^2
        = 4d^4 + 8d^3 + 4d^2 + 4d^2 + 4d + 1
        = 4d^4 + 8d^3 + 8d^2 + 4d + 1

Are these special Pythagorean triples often abc triples?
I'll pick a random 4-digit number for d to find out.
My random number generator gave me
d=2201.
This gives rise to the following triple:

    x = 4403
    y = 9693204
    z = 9693205
    a = 19386409
    b = 93958203785616
    c = 93958223172025
    radical(abc)
        = 3390967327436430
        > 93958223172025

It's close, but it's not an abc triple.
Let's try again, but this time choose a d such that x is very, very factorizable.
I picked d = 3280,
which gives the following triple:

    43046721 + 463255025689600 = 463255068736321
    (3^8)^2 + (2^5 * 5 * 17 * 41 * 193)^2 = 21523361^2
    radical(abc)
        = 86860321352430
        < 463255068736321
    quality = 1.052156400142

I found an abc triple, this time by hand!

But my favorite is still the one that my computer found:

    167521249 + 7015842132869376 = 7015842300390625
    (7 * 43^2)^2 + (2^4 * 3^2 * 719 * 809)^2 = (5^4 * 13^3 * 61)^2

I really like the wide variety of small prime factors that it uses.
Thanks for exploring abc triples with me!
