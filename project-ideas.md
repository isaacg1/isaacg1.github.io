---
layout: page
title: Project Ideas
permalink: /project-ideas/
published: true
---

These are queueing research ideas that I'm interested in, but haven't gotten around to yet. If you're interested in any of them as a potential collaborator or advisee, let me know!

I'm particularly interested in working with either students
at the school I am at (Georgia Tech, UIUC, or Northwestern),
or people who already have a background in queueing theory research.

Last updated: July 15, 2023.

1. [Known size dispatching to FCFS queues](#disp-fcfs)

2. [Scheduling to minimize E[T^2]](#t2)

3. [The Time Index scheduling policy](#time-index)

4. [Beating SRPT-k](#beating-srptk)

5. [Scheduling in the low-load limit](#low-load)

6. [M/G/k response time lower bounds (known size)](#mgk-lower)

7. [General constrained-service queue](#constrained-service)

8. [Value function service and dispatching](#value-function)

9. [Optimal Relative Completions in the Multiserver-job system](#optimal-relative)

10. [Optimal Transform](#optimal-transform)

11. [Multiserver Nudge](#multi-nudge)

12. [Product forms steady-state distributions from graph structure](#graph-product-form)

13. [Optimal dispatching to Gittins queues](#gittins-dispatch)

14. [Optimal scheduling in the general MSJ model](#general-msj)

### Known size dispatching to FCFS queues {#disp-fcfs}
Starting point:
[CRAB](https://ziv.codes/publications/#reducing-heavy-traffic-response-time-with-asymmetric-dispatching)
by Runhan Xie and Ziv Scully,
initial work presented at [MAMA 2023](https://www.sigmetrics.org/mama/index.shtml).

**Setup**: Imagine web requests are arriving to a server farm. Jobs arrive, are dispatched to servers, and are served. Let's optimize this.

When a job arrives, it must be dispatched to one of several servers. At dispatch time, the size of the job is known (or estimated), and that size is used for the dispatching decision. Once at a server, jobs are served in FCFS order.

What's a good dispatching policy to minimize mean response time? What's optimal? I'm especially interested in heavy traffic (arrival rate near capacity).

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

### Scheduling to minimize E[T^2] {#t2}

See Section 8.3.5 of [my thesis](/assets/isaac-thesis.pdf).

**Setting**: M/G/1 scheduling for tail, e.g. minimize E[T^2].

**Policy**: Priority is t/s, where t is a job's time in system and s is the job's size.
Higher is better. Without preemption to start, for simplicity of analysis.
Note that this is an "Accumulating Priority Queue", but with infinite continuous classes, not 2 classes.

[Waiting time distributions in the accumulating priority queue](https://link.springer.com/article/10.1007/s11134-013-9382-6),
David A. Stanford, Peter Taylor & Ilze Ziedins

**First step**: Implement this policy. Compare it against FCFS, SRPT. Poisson arrivals, medium variance, medium load. Does it do well empirically for E[T^2]?

**Future steps**: Use APQ methods to characterize steady state. Poisson point process of (size, time in system). Characterize for arbitrary joint (Size, Accumulation rate) distribution, specialize to above setting. Characterize transform of response time, moments of response time.

### The Time Index scheduling policy {#time-index}

**Setting**: M/G/1 scheduling for the tail, especially the asymptotic tail, especially in comparison to FCFS.

**Policy**: Time Index. Priority is s - t, where s is a job's size and t is the job's time in system.Lower is better. Relatively simple proof that waiting time dominates FCFS waiting time.

**First step**: Implement this policy. Compare against FCFS, [Nudge](/publications/#nudge).

**Future steps**: By how much does it dominate FCFS? Characterize leading constant of asymptotic?

### Beating SRPT-k {#beating-srptk}

See Section 8.3.1 of [my thesis](/assets/isaac-thesis.pdf).

**Setting**: SRPT-k (M/G/k/SRPT) is heavy-traffic optimal for mean response time,
as I proved in [SRPT for Multiserver Systems](/publications/#srptk),
but it can be beaten outside of heavy traffic.

**Idea**: Consider a 2-server system with 3 jobs in it: Two are small, one is large. There are two scheduling options: Run both small jobs first (SRPT), or one small and one large first (New concept). Once a small job finishes, start running the third job. If no new jobs arrive before the long job finishes, both options have the same total response time. If new jobs arrive after the small jobs finish but before the large job finishes, starting the large job sooner (New concept) is better. If new jobs arrive before both small jobs are done, SRPT is preferable.

**Policy**: Flip-3. In an M/G/2, if there are at least 4 jobs, just run SRPT. If there are 3 jobs, and 2 have remaining size below a, and the third has size above b, run the smallest and largest jobs. Otherwise, SRPT. Set a at roughly 20% of the mean job size, and b at roughly the mean job size.

**First step**: Implement this policy. Compare it against SRPT-k. Fiddle around with job size distributions, loads, and a and b thresholds to find a relatively large separation (0.1% is normal, 1% is good).

**Future steps**: Use a [Nudge](/publications/#nudge)-style argument to prove that if a is small enough and b is large enough, the Flip-3 policy has lower mean response time than SRPT-2.

### Scheduling in the low-load limit {#low-load}

**Setting:** The known-size M/G/k, under low load.

**Intuition:** The dominant term comes from jobs arriving alone, then two-job interactions, etc. We find which policy is optimal, for which number of jobs. It's similar to the no-arrivals setting, for which SRPT-k is optimal, but more stochastic.
SRPT-k was proven to be optimal in the no-arrivals setting by Robert McNaughton in
"[Scheduling with deadlines and loss functions](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.6.1.1)."

**Basics:** For at most k jobs, there are no nontrivial decisions. For k+1 jobs, just be sure to serve the smallest job. For k+2, it becomes nontrivial.

**First step:** If k=2, and we consider 4-job sequences, I believe we find that we must serve the smallest pair of any 3 jobs. Confirm?

**Future steps:** Is SRPT-2 uniquely optimal at low load? Is SRPT-k? Expand to dispatching, MSJ, unknown sizes?

### M/G/k response time lower bounds (known size) {#mgk-lower}

See Section 8.3.2 of [my thesis](/assets/isaac-thesis.pdf).

There are two straightforward lower bounds on mean response time for the M/G/k: kE[S], the mean service duration, and E[T^SRPT-1], response time in an M/G/1/SRPT. Empirically, as ρ->1, SRPT-k achieves a mean response time around E[T^SRPT-1] + kE[S]. Can we prove a lower bound that's asymptotically additively larger than E[T^SRPT-1]?

**Idea**: Use WINE (see my thesis), with M/G/1 and M/G/infinity work bounds at different sizes. Mainly only improves things at lower loads.

**Idea**: Look at the "Increasing Speed Queue", which starts at speed 1/k at the beginning of a busy period, then 2/k, etc., capping at speed 1 until the end of the busy period. Provides a lower bound on work. A higher lower bound than the M/G/1. Incorporate into the WINE bound.

**First step**: Derive the WINE bound.

**Future step**: Quantity expected work in the increasing-speed queue, perhaps with renewal-reward.

### General constrained-service queue {#constrained-service}

The Multiserver-job system and the switch can both be thought of as special cases of the "Constrained service queue": Jobs have classes, and a certain multisets of classes can be served at once. In the 2x2 switch, the service options are (ad, bc), while in the 2-server MSJ setting, the service options are (aa, b).

What policies and analysis make sense in the general constrained-service queue?
MaxWeight, used e.g. in
"[Stochastic models of load balancing and scheduling in cloud computing clusters](
https://core.ac.uk/download/pdf/4836445.pdf)", seems to be always throughput-optimal.
When does a [ServerFilling](/publications/#server-filling)
equivalent exist?
My [RESET paper](/publications/#reset) seems like it always applies to FCFS-type service.

### Value function service and dispatching {#value-function}

Can define a SRPT value function, which quantifies the total future response time impact of a set of jobs. If we started two systems, one from empty and one from this set of jobs, and then ran both forever, in expectation by how much would the total response time go up? Relatively simple function, e.g. using WINE.

Using this value function, in systems with constrained service such as MSJ or the switch, serve the subset of jobs that most rapidly decreases the value function. Or dispatch to minimize the value function impact.

**First step**: Derive the value function.

**Future steps**: Implement the policy.
Compare against [ServerFilling-SRPT](/publications/#sf-srpt), [Guardrails](/publications/#guardrails), etc.

### Optimal Relative Completions in the Multiserver-job system {#optimal-relative}

As I showed in my preliminary [RESET](/publications/#reset) paper,
the mean response time in the First-Come First-Served Multiserver-job system
is controlled by the throughput and relative completions of the corresponding saturated system.
It is therefore natural to find the optimal scheduling policy,
minimizing throughput and relative completions,
under some scheduling restriction,
such as the restriction that only the k oldest jobs in arrival order can be served.

**First step**: Implement a way to specify a such a policy and compute its throughput and relative completions, perhaps in a 3 server system.

**Future steps**:
Search over all possible policies with an MDP solver.
Find the pareto-optimal tradeoff of relative completions vs. throughput,
perhaps corresponding to best policies at a variety of loads.
Solve symbollically for throughput and relative completions.

### Optimal Transform {#optimal-transform}
  
My [Nudge](/publications/#nudge) paper works very hard
to do even the most basic analysis of the tail probability P(T>t).
But maybe the reason this is hard is because we're effectively
comparing the response time random variable against a constant,
and the constant random variable is obnoxious to work with -- it has a sharp cutoff.
  
The smoothest random variable is the exponential random variable.
If we use that as our cutoff, we get P(T>Exp(s)), which is the
[Laplace-Stieltjes Transform](https://en.wikipedia.org/wiki/Laplace%E2%80%93Stieltjes_transform)
of response time (Technically, it's P(T<Exp(s)), not P(T>Exp(s)).
This still captures similar information, if we set s=1/t.
It is also much easier to analyze:
All
[SOAP](https://ziv.codes/publications/#soap-one-clean-analysis-of-all-age-based-scheduling-policies/)
policies and Nudge have transform analysis. So let's try to optimize the transform.
  
**Intuition:** Effectively, jobs abandon at rate s, and we want to maximize the fraction that we complete before they abandon. If jobs told us when they abandoned, the optimal policy is straightforward: run the small job that hasn't abandoned yet. But we don't know which jobs have abandoned. We need to use time in system as a proxy.
  
**First step:** Compute the transform for some common policies, like FCFS, SRPT, Nudge, via simulation and/or formula. Compare against simulated P(T>t), which we can call the "hard tail".
  
**Future steps:** Is the transform a good proxy for the hard tail?
  
Is the inverse transform a good proxy for the inverse hard tail, e.g. a percentile?
  
For a given pair of (time in system, remaining size), what's the optimal 2-job policy? Is it that index policy I came up with a while back? What's a semantic understanding of that policy? Can we analyze it? Is it empirically optimal in the full M/G/1? Does it perform well for the hard tail/percentiles?
  
**Update:** The optimal 2-job strategy is to serve the job that maximizes e^-st e^-sr/(1-e^-sr).
  
Semantically, this is the probability of not abandoning prior to the time of the decision, times the probability of not abandoning while run, divided by the probability of abandoning while being run.
  
Note that this is a "conveyor belt" policy: jobs never interchange priority. This is a class containing SOAP and Nudge.
  
**Further steps:** Implement this policy in simulation. What's its empirical transform? Is it empirically optimal?
  
Is the policy the optimal 3-job policy? Optimal without arrivals?

**Important update:** This is a pretty bad tail metric, and hence a pretty bad policy.
This metric gives jobs *diminishing* importance as they age, while a good tail metric
should give jobs *increasing* importance as they age.
This issue is reflected in the policy,
which rates jobs as *less* important the larger their time in system.

Instead, one should consider the metric E[T^(st)], in contrast
to the above discussion of E[e^(-st)]. The optimal 2-job strategy is then
to maximize e^st e^sr / (1-e^sr).
This is a better metric and a better policy.
It's equivalent to using negative inputs to the transform,
so it's still extractable from the transform.
One must be careful to only consider values of s for which the metric is finite.

### Multiserver Nudge {#multi-nudge}

[Nudge](/publications/#nudge) was defined for the single-server setting.
However, much of the analysis of Nudge relative to FCFS only relied on the arrival process,
not the departure process. Does Nudge have better asymptotic tail than FCFS in the M/G/k?
Stochastic dominance?

**First step:** Simulate Nudge in the M/G/k.

**Future step:** Port the analysis to the M/G/k. How much transfers?

### Product forms steady-state distributions from graph structure {#graph-product-form}

The 2-class MSJ saturated system has a [product form](/publications/#product-form-msj) steady-steady distribution,
as a consequence of the graph structure of the Markov chain.
This is in contrast to the single-exponential saturated system,
for which the transition rates are also important to the product-form argument.

In general, a directed graph has a product form if there is an "directed elimination ordering"
to its vertices, defined as follows:

* For each vertex i, define its neighborhood to be all vertices j for which there exists an edge j->i, as well as i itself.

* Start with a source vertex, and place it in the "eliminated" set.

* Repeatedly select vertex neighborhoods that contains exactly one uneliminated vertex.
Each time such a neighborhood is selected, eliminate the new vertex.

* If this process can be continued until all vertices are eliminated,
the directed graph has a "directed elimination ordering".

All Markov chains with such an underlying graph have product form steady-state distributions.
Moreover, such chains have summation-form relative completions,
a new concept which allows relative completions to be characterized in closed-form.

**First step:** What are some classes of graphs that have elimination orderings?
I know undirected trees and the ladder graphs are examples. What others?

**Future steps:** Have these graphs been studied already, likely under a different name?
Can we give a closed-form characterization of this family of graphs?
Are they closed under any operations, such as taking minors?

### Optimal dispatching to Gittins queues {#gittins-dispatch}

See Section 8.3.3 of [my thesis](/assets/isaac-thesis.pdf).

In my [guardrails](/publications/#guardrails) paper, I studied optimal dispatching with full size information.
But what if we just have estimates? Or no info?
A good candidate for the scheduling policy is the
[Gittins index](https://en.wikipedia.org/wiki/Gittins_index#Queueing_theory) policy,
and we are trying to match resource-pooled Gittins,
which intuitively
requires that we always spread out the jobs of each rank across all of the servers.

If estimates are relatively good,
a combination that makes sense is estimated-Gittins + PSJF with estimates.

If we have no information, we might just use the greedy policy.
For each server, calculate how long the arriving job
will have to wait behind all other jobs at that server, in expectation.
Also calculate how long other jobs will have to wait behind the arriving job, in expectation.
Send to the server were the total expected waiting is minimized.
We can use
[SOAP](https://ziv.codes/publications/#soap-one-clean-analysis-of-all-age-based-scheduling-policies)
to do this analysis.

**First step:** Choose a size distribution for which Gittins is simple.
Try the above greedy policy. Compare against e.g. Join the Shortest Queue (JSQ).

**Future steps:** Can we prove that unbalancing isn't worth it,
if the dispatcher and the server have the same information?
Can we prove any convergence to resource-pooled Gittins, if the distribution is simple enough?

### Optimal scheduling in the general MSJ model {#general-msj}

See Section 8.3.4 of [my thesis](/assets/isaac-thesis.pdf).

Outside of the divisible server need setting behind the
[DivisorFilling-SRPT](/publications/#sf-srpt) policy,
we can't guarantee that all of the servers can be filled by an arbitrary set of k jobs.
This can cause problems in two ways:

1. The smallest jobs might not pack well.

2. If we prioritize the smallest jobs,
the jobs that are left over might not be able to fill the servers.

For example, consider a system with k=3 servers and jobs of server need 1 and 2.
If the 2-server jobs have smaller size, we can't fill the servers with just 2-server jobs.
If the 1-server jobs have smaller size, and we prioritize them,
we'll run out of 1-server jobs and have just 2-server jobs left,
which can't fill the servers.

To fix problem 1, we should just find the set of jobs with smallest sizes
that can fill the servers, and serve those jobs.
Proving that this is optimal will be challenging.

To fix problem 2, we should set a floor on the number of 1-server jobs
that we want to keep in the system,
in the style of
[CRAB](https://ziv.codes/publications/#reducing-heavy-traffic-response-time-with-asymmetric-dispatching),
and when we reach the floor, use the least 1-server-intensive strategy.
Proving this is optimal will also be hard.

**First step:** Find a prospective policy for the k=3 setting that "feels" optimal.

### Hybrid ServerFilling and MSJ FCFS to avoid starvation {#hybrid-sf-fcfs}

I think I now understand what practitioners mean when they talk about "starvation".
Consider a job that encounters a system where there are relatively few jobs present,
but the arrival rate is high, around the critical load.
The response time of that job should be relatively low: Proportionate to the number of jobs
that were present on arrival, ideally.
Practical systems often have feedback mechanisms on the arrival rate,
resulting in this pattern of high load but relatively short queue lengths.

MSJ FCFS satisfies this "no starvation" goal, as do many backfilling policies.
In contrast, [ServerFilling](/publications/#server-filling)
does not: A small-server-need job can be delayed until the system empties.

To overcome this, consider a policy which serves a 95%/5% mixture of ServerFilling and FCFS,
or ServerFilling and a backfilling policy.
We could then give a sample-path bound on job's response time
in terms of the number of jobs seen on arrival,
and the size of the job.
Load doesn't enter into it.
We could define this as "no starvation".
We could analyze this policy with our [finite-skip analysis](/publications/#reset).
