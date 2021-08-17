---
published: false
title: Problem six of the 1988 IMO
layout: post
---
Inspired by this [Numberphile video](https://youtu.be/Y30VF3cSIYQ), I decided to try to solve problem six of the 1988 International Mathematics Olympiad. I did not solve it from scratch, however. I've seen the solution before, but long enough ago that I've forgotten the details. This shouldnt be too hard, but still fun.

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