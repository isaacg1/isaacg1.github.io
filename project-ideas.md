---
layout: page
title: Project Ideas
permalink: /project-ideas/
published: true
---

These are queueing research ideas that I'm interested in, but haven't gotten around to yet. If you're interested in any of them as a potential collaborator or advisee, let me know!

I'm particularly interested in working with either students at the school I am at, or people who already have a background in queueing theory research.

Last updated: May 17, 2023.

### Known size dispatching to FCFS queues

**Setup**: Imagine web requests are arriving to a server farm. Jobs arrive, are dispatched to servers, and are served. Let's optimize this.

When a job arrives, it must be dispatched to one of several servers. At dispatch time, the size of the job is known (or estimated), and that size is used for the dispatching decision. Once at a server, jobs are served in FCFS order.

What's a good dispatching policy to minimize mean response time? What's optimal? I'm especially interested in heavy traffic (arrival rate near capacity)

**Idea**: There's an unavoidable amount of work in the system, M/G/1 lower bound. However, if we concentrate almost all of the work onto one server, and only dispatch large jobs to that server, then almost all of the jobs will avoid that long delay. Of course, we need to keep the other servers busy to avoid wasting capacity, but we'll keep their queue lengths short.

**Concrete policy**: "Many Short Servers" (MASS). Based on size, divide jobs into classes small, medium, and large. Set these cutoffs so that the small jobs make up (k-1)/k - ε fraction of the load, where k is the number of servers, the large jobs are 1/k - ε of the load, and the medium jobs are the other 2ε of the load. ε is a small constant to be determined.

Designate k-1 servers as the short servers (low workload), and one as the long server (high workload). Small jobs go to the short server, large jobs go the long server, and for medium jobs it depends.

Designate a target amount of work for the short servers. This should be o(1/(1-ρ)), to be smaller than the long server, and it should be omega(log(1/(1-ρ))), so it doesn't run empty due to bad luck. sqrt(1/(1-ρ)), for instance.

Whenever a small job arrives, send it to the short queue with least work. Whenever a large job arrives, send it to the long server. When a medium job arrives, if the short server with the least work is below the target amount of work, send the medium job there. If all short servers are above the target, send the medium job to the long server.

**First step**: Implement this policy. Start with k=2, for simplicity. Compare it against JSQ, LWL, SITA. Poisson arrivals, high variance sizes, high load. Does it do well empirically, for appropriate settings of ε and the target work?

**Refinement**: Dynamic relabeling. Whenever a job arrives, the long server is whichever has the most work at that moment, not static.

**Future steps**: Prove state space collapse. The system is almost always close to having all short servers at the target, or all servers below the target.

Use SSC to bound response time/waiting time.

Lower bound waiting time. Argument: All servers must have 1/k of the load going through them. The work has to be somewhere, and theres theta (1/(1-ρ)) of it in total. Best case scenario is that the largest jobs are the only jobs delayed by the work. This should dominate waiting time. This should match the waiting time of MASS, up to ratio 1, if the distribution is not too crazy.

### Scheduling for E[T^2]

**Setting**: M/G/1 scheduling for tail, e.g. minimize E[T^2].

**Policy**: Priority is (time in system)/size (TOS, Time Over Size). Higher is better. Without preemption, to start. Note that this is an "Accumulating Priority Queue", but with infinite continuous classes, not 2 classes.

[Waiting time distributions in the accumulating priority queue](https://link.springer.com/article/10.1007/s11134-013-9382-6),
David A. Stanford, Peter Taylor & Ilze Ziedins

**First step**: Implement this policy. Compare it against FCFS, SRPT. Poisson arrivals, medium variance, medium load. Does it do well empirically for E[T^2]?

**Future steps**: Use APQ methods to characterize steady state. Poisson point process of (size, time in system). Characterize for arbitrary joint (Size, Accumulation rate) distribution, specialize to above setting. Characterize transform of response time, moments of response time.

### Time Index

**Setting**: M/G/1 scheduling for the tail, especially the asymptotic tail, especially in comparison to FCFS.

**Policy**: Time Index. Priority is (size - time-in-system), lower is better. Relatively simple proof that waiting time dominates FCFS waiting time.

**First step**: Implement this policy. Compare against FCFS, Nudge.

**Future steps**: By how much does it dominate FCFS? Characterize leading constant of asymptotic?

### Beating SRPT-k

**Setting**: SRPT-k (M/G/k/SRPT) is heavy-traffic optimal for mean response time, but it can be beaten outside of heavy traffic.

**Idea**: Consider a 2-server system with 3 jobs in it: Two are small, one is large. There are two scheduling options: Run both small jobs first (SRPT), or one small and one large first (New concept). Once a small job finishes, start running the third job. If no new jobs arrive before the long job finishes, both options have the same total response time. If new jobs arrive after the small jobs finish but before the large job finishes, starting the large job sooner (New concept) is better. If new jobs arrive before both small jobs are done, SRPT is preferable.

**Policy**: Flip-3. In an M/G/2, if there are at least 4 jobs, just run SRPT. If there are 3 jobs, and 2 have remaining size below a, and the third has size above b, run the smallest and largest jobs. Otherwise, SRPT. Set a at roughly 20% of the mean job size, and b at roughly the mean job size.

**First step**: Implement this policy. Compare it against SRPT-k. Fiddle around with job size distributions, loads, and a and b thresholds to find a relatively large separation (0.1% is normal, 1% is good).

**Future steps**: Use a Nudge-style argument to prove that if a is small enough and b is large enough, the Flip-3 policy has lower mean response time than SRPT-2.

### M/G/k response time lower bounds (known size)

There are two straightforward lower bounds on mean response time for the M/G/k: kE[S], the mean service duration, and E[T^SRPT-1], response time in an M/G/1/SRPT. Empirically, as ρ->1, SRPT-k achieves a mean response time around E[T^SRPT-1] + kE[S]. Can we prove a lower bound that's asymptotically additively larger than E[T^SRPT-1]?

**Idea**: Use WINE, with M/G/1 and M/G/infinity work bounds at different sizes. Mainly only improves things at lower loads.

**Idea**: Look at the "Increasing Speed Queue", which starts at speed 1/k at the beginning of a busy period, then 2/k, etc., capping at speed 1 until the end of the busy period. Provides a lower bound on work. A higher lower bound than the M/G/1. Incorporate into the WINE bound.

**First step**: Derive the WINE bound.

**Future step**: Quantity expected work in the increasing-speed queue, perhaps with renewal-reward.

### General constrained-service queue

The Multiserver-job system and the switch can both be thought of as special cases of the "Constrained service queue": Jobs have classes, and a certain multisets of classes can be served at once. In the 2x2 switch, the service options are (ad, bc), while in the 2-server MSJ setting, the service options are (aa, b).

What policies and analysis make sense in the general constrained-service queue? MaxWeight seems to be always throughput-optimal. When does a ServerFilling equivalent exist? <Upcoming paper> seems like it always applies.

### Value function service and dispatching

Can define a SRPT value function, which quantifies the total future response time impact of a set of jobs. If we started two systems, one from empty and one from this set of jobs, and then ran both forever, in expectation by how much would the total response time go up? Relatively simple function, e.g. using WINE.

Using this value function, in systems with constrained service such as MSJ or the switch, serve the subset of jobs that most rapidly decreases the value function. Or dispatch to minimize the value function impact.

**First step**: Derive the value function.

**Future steps**: Implement the policy.
Compare against ServerFilling-SRPT, Guardrails, etc.

### Coming soon: An idea based on a paper to appear.

Analyze RC in the PFSS for the MF.

### Optimal Transform
  
My Nudge paper works very hard to do even the most basic analysis of the tail probability P(T>t). But maybe the reason this is hard is because we're effectively comparing the response time random variable against a constant, and the constant random variable is obnoxious to work with -- it has a sharp cutoff.
  
The smoothest random variable is the exponential random variable. If we use that as our cutoff, we get P(T>Exp(s)), which is the [Laplace-Stieltjes Transform](https://en.wikipedia.org/wiki/Laplace%E2%80%93Stieltjes_transform) of response time. This still captures similar information, if we set s=1/t. It is also much easier to analyze: All SOAP policies and Nudge have transform analysis. So let's try to optimize the transform.
  
**Intuition:** Effectively, jobs abandon at rate s, and we want to maximize the fraction that we complete before they abandon. If jobs told us when they abandoned, the optimal policy is straightforward: run the small job that hasn't abandoned yet. But we don't know which jobs have abandoned. We need to use time in system as a proxy.
  
**First step:** Compute the transform for some common policies, like FCFS, SRPT, Nudge, via simulation and/or formula. Compare against simulated P(T>t), which we can call the "hard tail".
  
**Future steps:** Is the transform a good proxy for the hard tail?
  
Is the inverse transform a good proxy for the inverse hard tail, e.g. a percentile?
  
For a given pair of (time in system, remaining size), what's the optimal 2-job policy? Is it that index policy I came up with a while back? What's a semantic understanding of that policy? Can we analyze it? Is it empirically optimal in the full M/G/1? Does it perform well for the hard tail/percentiles?