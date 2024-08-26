---
published: true
layout: post
title: 'Paper 4: Load Balancing Guardrails'
---
Time for my fourth paper: [Load balancing guardrails](/assets/load-balancing.pdf). This was the second paper I wrote during my PhD at CMU, and it builds upon my first paper on [SRPT-k](/assets/srpt.pdf). My coauthors once again were [Ziv Scully](https://ziv.codes/), then a fellow PhD student, now a postdoc at the Simons institute, soon to be a professor at Cornell, and [Mor Harchol-Balter](https://www.cs.cmu.edu/~harchol/), my advisor (and Ziv’s).

### Setting

My previous paper on SRPT-k, which I [wrote a post about](/2022/09/17/recap-srptk.html), dealt with a central queue model, where the scheduler could run any k jobs of its choice. In this paper, we focus on an immediate dispatch model, where jobs must be sent to one of the k servers immediately on arrival, and the job must eventually run at that server.

As a result, we must design both a dispatching policy and a scheduling policy: where should jobs be sent on arrival, and which job should be run at a given time?

Otherwise, the setting is the same as in the SRPT-k paper: Poisson arrivals, i.i.d. job sizes, fixed number of servers k, variable load rho, preemption allowed. We are again interested in the mean response time behavior in the rho to 1 limit.

Once again, there's prior work in the worst-case setting. The same result competitive ratio result is known as in the central queue setting: an O(log(min(n, P))) competitive ratio,
where n is the number of jobs and P is the ratio of largest and smallest job sizes.
This result was proven in 2013 by Mir Avrahami and Yossi Azar
in their paper [Minimizing total flow time and total completion time with immediate dispatching](https://dl.acm.org/doi/abs/10.1145/777412.777415).

### Policy choice

We have two decisions to make:

1. *Dispatching*: How should we send jobs to servers when jobs arrive?

2. *Scheduling*: How should we select a job to serve at each server?

To make these decisions, we have access to the complete system state,
including knowing how long jobs will take to run.
The answer to question (2), how to schedule the jobs, is actually pretty straightforward:
Shortest Remaining Processing Time (SRPT)
where we serve the job of least remaining size,
is the optimal scheduling policy.

We just have to decide how to dispatch the jobs.
This isn't straightforward.
For instance, one natural dispatching policy is called Least Work Left (LWL),
where each arriving job is dispatched to the server with least total work.
While it sounds reasonable,
LWL can result in very poor performance for some job size distributions.
In fact, for some job size distributions,
LWL is worse than *random* dispatching, as we show in the paper.

LWL has bad performance when some servers end up with nothing but a single very large job,
while others are packed with tons of small jobs.
The whole point of SRPT is prioritize small jobs,
and that's not possible if some servers don't have any small jobs.
Therefore, the goal of our dispatching policy will be to ensure that
all sizes of jobs are evenly spread across all of the servers.
We do this with a dispatching policy called "guardrails",
or more accurately a class of dispatching policies collectively called guardrails policies.

### Guardrails

Our goal is to ensure that a generic job of size x in our dispatching system
has about the same response time as in a resource pooled SRPT system,
where the server runs k times faster.
OUr analysis focuses on "relevant work",
the total remaining size of jobs of remaining size at most x.
To ensure the similarity of mean response time,
we're going to ensure that two things are true in our dispatching system:

1. At the server the tagged job is dispatched to,
the amount of relevant work is 1/k 
of the amount of relevant work in the resource-pooled SRPT system (plus a negligible term).

2. After the tagged job arrives, the amount of relevant work
that is dispatched to its server is 1/k
of the amount of relevant work that arrives to the system (plus a negligible term).

We will ensure (1) by ensuring that each server has the same amount of relevant work,
plus a negligible term.

As a first step, we divide up jobs by sizes into buckets of constant multiplicative width.
For instance, if the width was 2, the buckets would be

    ..., [0.5, 1), [1, 2), [2, 4), [4, 8), ...

We'll actually make the multiplicative much smaller, very close to 1, and approaching 1 as load approaches capacity.

Now, the most straightforward way to ensure (1)
would be to simply dispatch each job j to the server that has the
amount of work of j's bucket currently present.
While (1) would hold, (2) would not necessarily hold.
One server could have a lot of jobs from the same bucket dispatched to it,
if each job completed before the next arrived.

Therefore, we instead define the guardrails policy
to dispatch each job j to the server
that has so far received the least work of j's bucket from past dispatches.
More generally, we define the guardrails class of policies
to be any policy which dispatches jobs in such a way that the difference in work dispatched to
any pair of servers is never more than a constant multiple of the minimum possible.

Any policy in this class ensures (1) and (2),
and as we show in the paper this guarantees asymptotic
optimality.

The worst-case Avrahami and Azar paper uses a close variant of this dispatching policy,
but with a fixed multiplicative width of 2.
Having the multiplicative width shrink towards 1 as load increases is an innovation of this paper,
as is the whole proof technique.

### Last minute frenzy

After we thought that we had everything sorted,
had the paper was basically written,
and the deadline was approaching,
we realized we had neglected to prove a critical theorem,
which is Lemma 4 in the paper, proven in Appendix B.

This lemma is purely about M/G/1 scheduling, nothing multiserver at all.
It compares Priority-c, the scheduling policy which simply runs the job in the smallest bucket,
with FCFS tiebreaking, with PSJF, the scheduling policy which runs the job of smallest original size,
with no reference to buckets.
The lemma proves that these two policies have about the same mean response time,
up to a bound that becomes tight as the multiplicative width approaches 1.

This lemma is critical because the rest of our paper actually proves that our guardrails policy
has about the same mean response time as single-server Priority-c,
and we need to compare against single-single SRPT.
We know that single-server PSJF has about the same response time as SRPT,
so we use that as a convenient stepping stone.

We had thought that this lemma would be easy to prove with existing techniques,
because we can write a formula for the mean response time of each policy with existing techniques.
Unfortunately, this formula has too complex to prove
any sort of comparison between the two policies.

Instead, at the last minute, we invented a completely new technique to compare the mean response time of the policies.
Instead of looking at response time,
we invented a new quantity called *delay*,
defined as follows:
When a job j of size x arrives,
its delay is the total remaining size of jobs prioritized ahead of j,
plus x times the number of jobs  prioritized behind j,
plus x for j itself.

The key point is that the sum of delays for all jobs is the same as the sum of response times for all jobs. Therefore, the two random variables have the same mean.
We then prove that in a coupled pair of systems with the same arrivals,
a generic job causes about the same delay in both systems,
even though its response time can be very different.

I think this technique, "analyze delay to analyze response time",
is really cool, and I hope that it one day makes the body of a paper, not just the appendix.

### Retrospective

I'm really proud of this paper. It's one of my most "technically dense" papers,
but that density feels appropriate, not stuffed in to seem cool.
The motivation, where LWL can be worse than Random when dispatching to SRPT servers,
is really surprising and counterintuitive, 
and leads into our policy well.

The key idea of our paper is really "worst-case work bounds imply stochastic optimality".

This paper won the Best Student Paper Award at ACM SIGMETRICS \& IFIP Performance 2019
(they were collocated) in Pheonix, Arizona.
I'm really proud of this.

### Future problem

In the setting where job sizes are unknown are estimated, there's an analogue of SRPT
called the Gittins policy.
We later proved the asymptotic optimality of [multiserver Gittins](/publications/#gittins-k)
in a central queue setting.
How should we dispatch in a setting where we don't know job sizes?

In the empirical section of the Guardrails paper,
we found that the policy of dispatching to the server with the least jobs present (JSQ)
has great performance when combined with SRPT scheduling.
This is despite the fact that JSQ doesn't use size information at all when dispatching.
Can we prove or disprove the conjecture that JSQ/SRPT is asymptotically optimal?
Is JSQ/Gittins asymptotically optimal?

I thought that JSQ's good performance might come from the fact that JSQ is fairly similar
to the "least delay" dispatching policy,
and mean delay is the same as mean response time.
Can we prove that the two policies have similar performance?
