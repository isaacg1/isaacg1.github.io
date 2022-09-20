---
published: false
title: 'Post 3: SRPT for Multiserver Systems'
layout: post
---
## Post 3: SRPT for Multiserver Systems

Time for my third paper: ["SRPT for Multiserver Systems"](/assets/srpt.pdf). This was the first paper I wrote during my PhD at CMU, submitted around the end of my first year. My coauthors were [Ziv Scully](https://ziv.codes/), then a fellow PhD student, now a postdoc at the Simons institute, soon to be a professor at Cornell, and [Mor Harchol-Balter](https://www.cs.cmu.edu/~harchol/), my advisor (and Ziv's).

The problem that this paper focuses on is optimal stochastic multiserver scheduling. Let me break this down word by word.

In the *scheduling* problem, jobs arrive over time,
and we have a limited amount of resources to complete the jobs.
We have to decide what order to serve the jobs in.

Our *optimization* goal is to minimize the mean response time of the jobs.
A job's response time is the time from when the job arrives to when it completes.
In this paper, we think of each job as equally important,
so we just try to minimize the mean response time across all jobs.
