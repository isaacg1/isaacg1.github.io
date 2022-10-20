---
published: true
title: 'Post 3: SRPT for Multiserver Systems'
layout: post
---
## Post 3: SRPT for Multiserver Systems

Time for my third paper: ["SRPT for Multiserver Systems"](/assets/srpt.pdf). This was the first paper I wrote during my PhD at CMU, submitted around the end of my first year. My coauthors were [Ziv Scully](https://ziv.codes/), then a fellow PhD student, now a postdoc at the Simons institute, soon to be a professor at Cornell, and [Mor Harchol-Balter](https://www.cs.cmu.edu/~harchol/), my advisor (and Ziv's).

### Setting

The problem that this paper focuses on is optimal stochastic multiserver scheduling. Let me break this down word by word.

In the *scheduling* problem, jobs arrive over time,
and we have a limited amount of resources to complete the jobs.
We have to decide what order to serve the jobs in.
To help us schedule, we assume that we know a job's *size*,
the amount of time it will take to serve.
We assume preempt-resume service, meaning we can always pause a job
and come back to it later, with no loss of progress.

Our *optimization* goal is to minimize the mean response time of the jobs.
A job's response time is the time from when the job arrives to when it completes.
In this paper, we think of each job as equally important,
so we just try to minimize the mean response time across all jobs.

This paper studies *multiserver* scheduling,
where there are several servers available.
Specifically, there are k servers available,
and we must choose which k jobs to serve at a given point in time.

This paper studies *stochastic* scheduling,
specifically an M/G/k model.
We assume a Poisson arrival process,
which means that jobs arrive at uncorrelated moments in time at some fixed rate,
which we write λ.
We also assume i.i.d. job sizes, drawn from some general distribution S.

### Prior results

The stochastic multiserver scheduling problem was poorly understood before this paper.
More was known if we simplify one setting or the other.

Optimal single-server scheduling has been well understood since the 60s,
thanks to Linus Schrage's papers on Shortest Remaining Processing Time (SRPT),
the policy which serves the job of least remaining size.
First, Schrage characterized SRPT's mean response time in 1966,
in
[The Queue M/G/1 with the Shortest Remaining Processing Time Discipline](https://pubsonline.informs.org/doi/abs/10.1287/opre.14.4.670).
He thought it was obvious that SRPT achieves optimal mean response time,
but others disagreed, so he wrote down the proof in 1968,
in
[A Proof of the Optimality of the Shortest Remaining Processing Time Discipline](https://pubsonline.informs.org/doi/abs/10.1287/opre.16.3.687).

Optimal multiserver scheduling in a worst-case (non-stochastic) setting
was figured out in 1997,
when Stefano Leonardi and Danny Raz wrote
[Approximating total flow time on parallel machines](https://dl.acm.org/doi/abs/10.1145/258533.258562).
"Flow time" is another word for response time,
and "parallel machines" is another word for this type of multiserver system.
Leonardi and Raz studied SRPT scheduling in this worst-case multiserver system,
and proved two results:

* SRPT achieves achieves an O(log(min(n, P))) competitive ratio
with respect to the optimal offline policy,
where n is the number of jobs, and P is the ratio of the sizes of the largest and smallest jobs.

* Any online policy's competitve ratio with respect to the optimal offline policy is at least
Ω(log n) and at least Ω(log P).

Combining these results, we find that SRPT is within a constant factor fo the optimal online policy,
but also that no online policy can achieve a constant competitive ratio,
for general adversarial arrivals.

### My approach

We prove two major results in our paper: A bound on multiserver SRPT's mean response time,
and an asymptotic optimality result which follows from the bound.

Let's start by talking about how we prove the bound.

To prove this bound, we use a *tagged job* approach.
This means we select a generic job, and watch it make its way through the system,
and try to bound its response time.

Key to our analysis is the concept of *relevant work*.
A relevant job is one which our tagged job might have to wait behind.
We'll say that our tagged job has size x,
and a relevant job is one with size at most x.
The total relevant work in the system at a given point in time
is the sum of the remaining sizes of all jobs in the system with remaining size at most x.

My key idea is that relevant work gets completed at a constant rate
whenever the tagged job is in the system (with a caveat I'll address shortly).
If we're waiting in the queue, all of the servers are busy with relevant work.
Let's rescale things so that the k servers each run at rate 1/k,
making the total service rate 1.
Then the total amount of relevant work completed while the tagged job is in the system
is simply the response time of the tagged job.

The one caveat is that while the tagged job is in service,
the other servers might be empty, or working on irrelevant jobs.
We'll call this "virtual work", and we'll account for it in the bound.

We break up the work in the system into four categories:

* Old work: The relevant work in the system when the tagged job arrives.

* New work: Relevant work that arrives while the tagged job is in the system.
