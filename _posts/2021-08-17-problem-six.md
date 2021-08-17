---
published: true
title: Problem six of the 1988 IMO
layout: post
---
Inspired by this [Numberphile video](https://youtu.be/Y30VF3cSIYQ), I decided to try to solve problem six of the 1988 International Mathematics Olympiad. It was the hardest IMO problem ever posed for many years. I did not solve it from scratch, however. I've seen the solution before, but long enough ago that I've forgotten the details. This shouldn't be too hard, but still fun.

The problem is as follows: let a, b be positive integers such that (a^2+b^2)/(ab+1) is an integer. Show that it is a square.

Equivalently, let (k,a,b) be a positive integer solution to

    k(ab+1) = a^2 + b^2.

Show that k is a square.

If you haven't seen this problem before, consider trying it now. At the very least, it'll make reading the solution more fun.

First, let's try find some solutions, just by futzing about. (1,1,1) is a solution, but a boring one. (4,2,8) is a more interesting solution:

    4(2*8+1) = 68 = 2^2 + 8^2
    
I notice something about this solution: 2, 4, and 8 are powers of 2. This isn't a coincidence. For any integer x, (x^2, x, x^3) is a solution:

    x^2(x*x^3+1) = x^6 + x^2 = x^2 + (x^3)^2.
    
Can we find more solutions? Let's try to find more solutions with k=4.

    4(ab+1) = a^2 + b^2
    
The left side is a multiple of four, and squares mod 4 are 0 or 1, so a and b need to be even. Let's start trying even numbers.

    a=2
    4(2b+1) = 4 + b^2
    8b+4 = 4 + b^2
    8b = b^2
    b=0 or 8
    
    a=4
    4(4b+1) = 16 + b^2
    16b = 12 + b^2
    no solutions

    a=6
    4(6b+1) = 36 + b^2
    24b = 32 + b^2
    no solutions
    
    a=8
    4(8b+1) = 64 + b^2
    32b = 60 + b^2
    b=2 or 30
    
Alright, we have another solution, (4, 8, 30):
 
    4(8*30+1) = 964 = 8^2 + 30^2.

I notice something about this solution, as compares to the previous solution. `4 * 8 = 2 + 30`.
This isn't a coincedence: the general form of the above analysis is

    k(ab + 1) = a^2 + b^2
    (ka)b = (a^2 - k) + b^2
    b^2 - (ka)b + (a^2 - k) = 0

This is a quadratic function of b.
Its two roots r and s must obey

    r + s = ka
    rs = a^2 - k

If either r or s is an integer, the other must be an integer as well.
Specifically, the roots must be b and ak-b.
Whenever we have a solution (k, a, b), we must also have a solution (k, a, ak-b),
unless ak-b is 0 or negative.

For instance, from (4, 8, 30), choosing a = 30, we get (4, 30, 112) as another solution.
I notice that if we choose the larger of a and b, we get a larger solution,
and if we choose the smaller, we get a smaller solution.
If b > ak/2, and we choose a, then ak-b < b.
Suppose b => a. Must b > ak/2?
Suppose a <= b <= ak/2.

    a^2 + b^2 <= a^2 + kab/2
    kab + k <= a^2 + kab/2
    kab/2 + k <= a^2
    kab/2 < a^2
    kb/2 < a

Because a <= b, we must have k=1.
But if k = 1, a <= b <= ak/2 is impossible.
So if b >= a, then b > ak / 2,
and b > ak-b.

So from any solution (k, a, b) with a < b and ak-b > 0,
we can get another smaller solution (k, ak-b, a).
Therefore, any k that has a solution
must have a solution with ak-b <= 0,
because the descent can't go on forever.

If ak-b <= 0, or equivalently ak <= b, then

    a^2 + b^2 >= a^2 + kab
    kab + k >= a^2 + kab
    k >= a^2

If k = a^2, then we have our standard solution (x^2, x, x^3)
and the almost-solution (x^2, 0, x).
Suppose there's a solution with a^2 < k.

    kab + k = a^2 + b^2
    k - a^2 = b^2 - kab

The left side is divisible by b, so k - a^2 is also divisible by b.
Because k - a^2 is positive, b <= k - a^2. In particular, b < k.

    b < k
    b^2 < kb
    b^2 < kab
    b^2 + a^2 < kab + k

So no solution exists with a^2 < k.
Thus, solutions only exist for k such that a^2 = k for some a.

That was fun!

