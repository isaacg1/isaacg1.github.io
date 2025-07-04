---
layout: page
title: Project Ideas
permalink: /project-ideas/
published: true
---

These are queueing research ideas that I'm interested in, but haven't gotten around to yet. If you're interested in any of them as a potential collaborator or advisee, let me know!

I'm particularly interested in working with either Northwestern students,
undergrad or grad,
or people who already have a background in queueing theory research.

Last updated: July 3rd, 2025.

## Table of contents

I've separated my ideas into five categories:

* Ideas that I think are quite promising,
where I have promising directions for a result.

* Ideas that are just starting out, or where I don't quite know how I'd prove a result.

* Ideas that I'm actively pursuing.

* Ideas I pursued to some kind of completion, and am not currently pursuing.
I'm keeping these around for archival purposes.

* Ideas I'm no longer interested in. I'm keeping these around for archival purposes.

I'm most interested in collaborating on ideas in the "quite promising" category,
but all of them are worth looking at and discussing.

This page is for ideas that look promising but I'm not pursuing yet,
or were in that stage earlier but I am now pursuing.
I typically have several more projects that I'm actively pursuing,
that never went through the "look promising but not pursuing" stage,
and so aren't listed here.

The order within a category is roughly chronological.

### [Quite promising](#promising)

1. [Optimal Relative Completions in the Multiserver-job system](#optimal-relative)

2. [Hybrid ServerFilling and MSJ FCFS to avoid starvation](#hybrid-sf-fcfs)

3. [Scheduling with epsilon prediction errors](#epsilon-error)

4. [Tails for ServerFilling](#sf-tails)

5. [Largest Remaining Size in the M/G/k](#mgk-lrs)

6. [Product-Form Distributions in Closed Queues with Front-Order-Independence](#front-oi)

### [Starting out/Not sure how to proceed](#starting-out)

1. [Scheduling in the low-load limit](#low-load)

2. [Value function service and dispatching](#value-function)

3. [Multiserver Nudge](#multi-nudge)

4. [Optimal dispatching to Gittins queues](#gittins-dispatch)

5. [Optimal Nonpreemptive MSJ scheduling](#nonpreemptive-msj)

6. [Starvation and Closed-system Tails](#starvation-closed)

7. [Parameterized Optimization Equivalence](#param-opt)

### [Active projects](#active)

1. [Relative arrivals/completions with infinite state spaces](#infinite-ra)

2. [Beating SRPT-k](#beating-srptk)

3. [Half-batch MSJ](#half-batch-msj)

4. [Continuous MSJ](#continuous-msj)

### [Archive: Submitted or Completed](#archive-done)

1. [M/G/k response time lower bounds (known size)](#mgk-lower)

2. [Product form steady-state distributions from graph structure](#graph-product-form)

3. [Optimal scheduling in the general MSJ model](#general-msj)

4. [Known size dispatching to FCFS queues](#disp-fcfs)

### [Archive: No longer interested](#archive-nope)

1. [The Time Index scheduling policy](#time-index)

2. [Optimal Transform](#optimal-transform)

3. [General constrained-service queue](#constrained-service)

4. [Restless MDPs for tail scheduling](#restless-tail)

5. [Scheduling to minimize E[T^2]](#t2)

## Quite promising {#promising}

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
Find the Pareto-optimal tradeoff of relative completions vs. throughput,
perhaps corresponding to best policies at a variety of loads.
Solve symbolically for throughput and relative completions.

Mean-variance tradeoff: Follow up with Shubhada.


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

### Scheduling with epsilon prediction errors {#epsilon-error}

**Setting**: M/G/1 scheduling for the mean.
Predictions are given, and there's a small (epsilon-sized) error in the predictions.

**Goal**: Schedule to achieve a mean response time performance of the form E\[T^SRPT](1+f(epsilon)), for some function f that goes to zero as epsilon goes to zero. This is called "Consistency".

**Twist**: There are many kinds of epsilon-error to consider. In our [SRPT-Bounce](/publications/#estimates) paper,
we show that our SRPT-Bounce policy can handle the situation where all predictions may be off by a multiplicative error of epsilon.
Adam Wierman and Misja Nuyens have a paper,
["Scheduling despite inexact job-size information"](https://dl.acm.org/doi/abs/10.1145/1375457.1375461),
looking at predictions being off by an additive error - consistency is not possible there.

I'd like to instead consider the situation where an epsilon fraction of jobs may have seriously poor predictions, but all other predictions are accurate. There are two natural scenarios:

1. Epsilon-fraction of jobs have null predictions. In this case, we know that we're getting no prediction information.

2. Epsilon-fraction of jobs have predictions that are incorrect by an arbitrary magnitude. In this case, we don't know that we're getting no prediction information.

We could also look at load-fractions rather than job fractions.

Even in scenario 1, which is much simpler, things aren't trivial by any means. If we did something simple like put the null-prediction jobs at the end of the queue, their response time would be something horrible like 1/(1-rho)^2 in the epsilon->0 limit, which would dominate mean response time and not remotely achieve consistency.

**Initial question:**
What's the mean response time impact of a misprediction from true size x to predicted size x', under a policy like SRPT-Checkmark or SRPT-Bounce?

**Longer-term question**: Can we achieve consistency against rare large errors? Can we define a useful misprediction-distance metric such that if that metric is small, we have consistent performance?

### Tails for ServerFilling {#sf-tails}

**Setting**: MSJ Scheduling, ServerFilling policy (or generally WCFS scheduling).
Want to analyze tail of response time.

In our [WCFS](/publications/#server-filling) paper, we analyze the ServerFilling policy's mean response time, and more generally any WCFS policy's mean response time, showing that it is near that of resource-pooled FCFS. Because these policies are near-FCFS, we would like to analyze their tail of response time, which is likely quite good in the light-tail-sizes/bounded expected remaining size setting of the paper.

Our analysis separates response time into two pieces: Time in the "front" and time in the "back" (the back is called the queue in the paper, but we've since changed terminology to clarify that some of the jobs in the front are not in service).

Time in the back dominates mean response time in heavy traffic, and our analysis could likely be generalized to tightly bound the transform of time in the front to be near that of resource-pooled FCFS. We would just have to change out the W^2 test function in the paper for an exponential test function.

For time in the front, things are trickier. In the paper, we used Little's law, which allows us to bound mean time in front but does not say anything about the distribution of time in the front.
Because ServerFilling prioritizes the largest server-need jobs in the front, we have to worry about the smallest server-need jobs and the tail of their time in the front.

In the worst-case, a 1-server job can only be guaranteed to run
once there are k 1-server jobs in the front.
Thus, the time-in-front of 1-server jobs could be about k times the interarrival time of 1-server jobs. The k-times is fine, but the issue is the interarrival time of 1-server jobs.

If 1-server jobs are very rare, then their interarrival time will be very large. However, because these jobs are so rare, that won't have a big impact on metrics like the transform or the tail probability. If 1-server jobs are exceptionally rare, then we can bound their response time by the excess of a busy period, at which point the system will run low on jobs and all jobs remaining in the system will be in service.

**Initial question:** Let's bound the transform or tail probability of time in front, either for a specific policy or uniformly over all policies.

### Largest Remaining Size in the M/G/k {#mgk-lrs}

In our recent [MAMA paper](/publications/#mgk-lower-short),
and [subsequent submission](/publications/#mgk-lower),
Ziyuan and I introduced the WINE lower-bounding framework,
which proves lower bounds on mean response time in the M/G/k under arbitrary scheduling
via lower bounds on mean relevant work under arbitrary scheduling.

The optimal policy for mean total work under arbitrary scheduling is the largest remaining size (LRS or LRPT) policy.
The reasoning is fairly simple: Total work is minimized if as many servers are running as possible at each moment in time.
The only thing that can get in the way of that is too much work concentrated into too few jobs.
So, we should schedule the job of largest remaining size. This is the opposite of the SRPT policy.

**First step:** Can we prove rigorously that LRS minimizes total work in the M/G/k?
This should be true in a sample-path sense, which should make the proof relatively straightforward.

Intuition: Consider the function describing the total work in the system at all future points in time, if there are no arrivals. LRS minimizes this function, so it's optimal.

See [this proof sketch](/assets/notes/lrpt-proof-sketch.jpg).

**Next step:** Can we analyze LRS for the M/D/k, or even just the M/D/2? (D for Deterministic).
I think that the ISQ methods described in the same MAMA paper might be useful.
In particular, drift functions derived via differential equations to give constant drift might be useful.

More specifically, for the 2-server system, the system state can be described by 2 continuous parameters: The work in the "parallel pool", and the work in the "largest job leftover" pool. Equivalently, the time until one server will run empty, and the time until the second server will run empty. The system state changes deterministically except for stochastic jumps on arrivals. This is very similar to the ISQ-2 dynamics, so the DiffeDrift approach should work.

See the discussion of DiffeDrift in the ISQ-2 in Section 8
of the [lower bounds paper](/publications/#mgk-lower)
and my notes of the derivation of the ISQ analysis:
[page 1](/assets/notes/isq-pg-1.jpg),
[page 2](/assets/notes/isq-pg-2.jpg),
[page 3](/assets/notes/isq-pg-3.jpg),
[page 4](/assets/notes/isq-pg-4.jpg).

**Future:** The above approach will bound total work in the LRPT system, and hence total work in the M/G/k. But we really want to bound total *relevant* work in the LRPT system, so we need the Sep-ISQ and AR-ISQ equivalents.

### Product Form Distributions in Closed Queues with Front Order Independence {#front-oi}

**Setting:** Closed queuing systems where job completions depend on job class and
on queue position.

As a starting point, consider the single-exponential
multiserver-job model discussed in Section 3 of
[this MAMA paper](/publications/#product-form-msj).
Here, jobs have a general distribution of server need between 1 and k,
and each job has duration Exp(μ).
Jobs are placed into service in FCFS order, with a variable number in service based on
the server needs of those jobs.
Whenever a job completes, a new job is sampled from a server-need distribution p. 
We examine the embedded Markov chain that updates on each completion-arrival pair.
In the embedded chain, the completion is sampled uniformly at random among the
jobs in service.

This chain has a product form stationary distribution, π(m) = Prod_i(p(m_i)), where m is a length-k vector of server needs.

The system obeys a partial balance property: The rate of entering state m due to transitions that involve class l completions equals the rate of leaving state m due to transitions that involve class l arrivals.
See [the MAMA paper](/publications/#product-form-msj) for the proof.

**Generalization**: This product-form property is preserved if we generalize the system as follows:
There is a function s(m) which specifies how many jobs are in service
in state m.
This function s(m) must be *front-order-independent*, which means that it must satisfy the following property:

> For any pair of state vectors m, m' such that the first s(m) entries of m are a permutation of the first s(m) entries of m', and all other entries of m and m' are identical, we must have s(m) = s(m').

As long as the service function s(m) is front-order-independent, the product-form holds.

See my notes on this subject: [page 1](/assets/notes/front-oi-pg-1.jpg), [page 2](front-oi-pg-2.jpg).

**Further generalization**: This product-form property is further preserved if we generalize the system even further as follows:
There is a function Δ\_j(m) which maps a vector m and an index j, 1 <= j <= k,
and outputs a probability that this position is the next completion.
We require that Sum_j Δ\_j(m) = 1.
For example, in the above "number of jobs in service" setting with the function s(m),
we would have Δ\_j(m) = 1/s(m) if j <= s(m), and 0 otherwise.

This function Δ\_j(m) must be *front-order-independent*, which means that it must satisfy the following property:

> For any pair of state vectors m, m' and any index j such that the first j entries of m are a permutation of the first j entries of m', and all other entries of m and m' are identical , we must have Δ\_j(m) = Δ\_j(m').

Actually, we can weaken this property a bit further, to front-cyclic-order-independent:
The equality only needs to hold if the first j entries of m are a *cyclic* permutation of the first j entries of m', not a general permutation.

If Δ\_j(m) is front-cyclic-order-independent for all j, then the product-form holds.

See my further notes: [page 3](/assets/notes/front-oi-pg-3.jpg).

**Question:** Can we generalize this any further? How is this related to the theory of product-form behavior in *open* order-independent product-form queues, such as in [Krzesinski, Anthony E. "Order independent queues." Queueing networks: A fundamental approach.](https://www.utwente.nl/en/eemcs/sor/boucherie/education/mqsn/editorhandbook.pdf#page=105).


## Starting out/Not sure how to proceed {#starting-out}

### Scheduling in the low-load limit {#low-load}

**Setting:** The known-size M/G/k, under low load.

**Intuition:** The dominant term comes from jobs arriving alone, then two-job interactions, etc. We find which policy is optimal, for which number of jobs. It's similar to the no-arrivals setting, for which SRPT-k is optimal, but more stochastic.
SRPT-k was proven to be optimal in the no-arrivals setting by Robert McNaughton in
"[Scheduling with deadlines and loss functions](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.6.1.1)."

**Basics:** For at most k jobs, there are no nontrivial decisions. For k+1 jobs, just be sure to serve the smallest job. For k+2, it becomes nontrivial.

**First step:** If k=2, and we consider 4-job sequences, I believe we find that we must serve the smallest pair of any 3 jobs. Confirm?

**Future steps:** Is SRPT-2 uniquely optimal at low load? Is SRPT-k? Expand to dispatching, MSJ, unknown sizes?

### Value function service and dispatching {#value-function}

Can define a SRPT value function, which quantifies the total future response time impact of a set of jobs. If we started two systems, one from empty and one from this set of jobs, and then ran both forever, in expectation by how much would the total response time go up? Relatively simple function, e.g. using WINE.

Using this value function, in systems with constrained service such as MSJ or the switch, serve the subset of jobs that most rapidly decreases the value function. Or dispatch to minimize the value function impact.

**First step**: Derive the value function.

**Future steps**: Implement the policy.
Compare against [ServerFilling-SRPT](/publications/#sf-srpt), [Guardrails](/publications/#guardrails), etc.

### Multiserver Nudge {#multi-nudge}

[Nudge](/publications/#nudge) was defined for the single-server setting.
However, much of the analysis of Nudge relative to FCFS only relied on the arrival process,
not the departure process. Does Nudge have better asymptotic tail than FCFS in the M/G/k?
Stochastic dominance?

**First step:** Simulate Nudge in the M/G/k.

**Future step:** Port the analysis to the M/G/k. How much transfers?

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
Send to the server where the total expected added waiting time is minimized.
We can use
[SOAP](https://ziv.codes/publications/#soap-one-clean-analysis-of-all-age-based-scheduling-policies)
to do this analysis.

There are also work balance considerations. Ideally, we should be balancing the amount of low-rank work at both servers, in the style of Gittins.
This would push us towards sending a job to a server where there's not much low-rank work present, in the style of Guardrails. But as we can't differentiate jobs at time of dispatch, there's much less we can do.

**First step:** Choose a size distribution for which Gittins is simple.
A good choice is a Decreasing Hazard Rate distribution,
such as a hyperexponential distribution,
where Gittins is simply Foreground-Background (FB), a.k.a. Least Attained Service (LAS).
Try the above greedy policy. Compare against e.g. Join the Shortest Queue (JSQ).


**Future steps:** Can we prove that unbalancing isn't worth it,
if the dispatcher and the server have the same information?
Can we prove any convergence to resource-pooled Gittins, if the distribution is simple enough?

### Optimal Nonpreemptive MSJ scheduling {#nonpreemptive-msj}

An important aspect of MSJ scheduling in the really world
is that we often want to scheduling nonpreemptively -- jobs that need lots of resources simultaneously tend to be expensive to set up and shut down.

The challenge of nonpreemptive scheduling in the MSJ is that it's expensive to switch between service configurations.

Consider an MSJ system, where we have 10 servers and jobs either take 1 or 10 servers. If we feel like serving 10-server jobs, we can keep serving 10-server jobs for as long as we have them available,
with no wasted capacity.
If we want to switch to serving 1-server jobs, we can wait until a 10-server job finishes, and put 10 1-server jobs into service, again without wasting capacity.
But if we now want to switch back to serving 10-server jobs, we're going to have to wait until all of the 1-server jobs finish, to free up space.
Due to stochasticity, we'll waste a substantial amount of capacity in the process. If the 1-server jobs take Exp(1) seconds,
it'll take an average of 2.93 seconds to empty out the system,
and we'll only complete 10 jobs, compared to the average completion rate of 29.3 jobs in that time.
We've wasted an amount of capacity equal to 19 job completions in this process.

This raises the question: When is it worth it to waste this capacity and perform this switch, towards the goal of reducing response times?

The advantage of doing a switch is that we can start on a different class of jobs without waiting for the system to empty.
The different class of jobs could have lower mean size (or higher importance), aiding response times.

If we waste capacity too often, the system will become unstable. As we approach that boundary, response times will suffer.

**Question:** What's the optimal threshold (# of small and large jobs in the queue) to switch configurations?

**Starter question:** Let's simulate a variety of thresholds and see what seems good.

**Alternate approach:** In heavy traffic, how often should we be switching, optimally?
We could get into cycles, where we wait until we accumulate x jobs of one class, then serve then all, paying the overhead, then switch back to the other class, which has a very long queue.
The response time of the higher-priority class will be determined by the cycle length,
while the response time of the lower-priority class will be determined by the amount of wasted capacity pushing the system closer to the capacity boundary.
Can we (approximately) determine how long these cycles should optimally be, given the switching overhead?

### Starvation and Closed-system Tails {#starvation-closed}

Many operators of practical computing systems care about a performance criterion
which they call "starvation".
They don't want their systems to experience starvation.
This is a concern that arises when evaluating priority-based policies,
where practitioners describe the lowest-priority jobs as never completing.

In open queueing models where the arrival process
is not dependent on the state of the queue,
this behavior cannot occur:
A key behavior of such open systems is the concept of a *busy period*,
the duration until the system is completely empty.
In a single-server system, busy periods are not very long,
and as a result, no job experiences very severe response time.
See for instance the [all can win](https://www.cs.cmu.edu/~harchol/Papers/Sigmetrics01.pdf)
result for M/G/1/SRPT and M/G/1/PS.

Extremely long response times for deprioritized jobs get more common in
multiserver settings such as the M/G/k/SRPT,
where under large job size variability,
the largest job in the system may take a very long time to complete,
because the system is rarely completely empty.
The [ServerFilling](/publications/#server-filling) policy
likewise exhibits this behavior if 1-server jobs are very rare.

These long-tail dynamics get much more severe when there is feedback
from the system state to the arrival rate, with lower arrival rates as queue lengths increase.
This leads to the system stabilizing around a fixed number of jobs present,
but with nothing ensure that the system stabilizes frequently.
The time for the system to empty will typically be exponentially long, as a function of the mean queue length.
I think this is most similar to how real systems operate.

These dynamic become most extreme in a closed system, where there are a constant number of jobs in the system
and sufficiently deprioritized jobs never finish.
I think this is the clearest and most tractable setting where starvation can be observed:
starvation simply means closed-system tail response time, or feedback-system tail response time.

I think that these dynamics are particularly important in the nonpreemptive Multiserver-Job (MSJ) setting,
as we can examine the tradeoff curve between throughput and tail response time,
in the feedback or closed settings.
Policies such as Randomized Timers achieve optimal throughput in an open setting,
at the cost of very high mean response time in some parameterizations.
In a closed setting, this corresponds to high throughput at the cost of high tail response time.

**First steps:** Simulate some basic MSJ policies in a simple closed MSJ setting.
Find their tradeoff between utilization and tail response time.

### Parameterized Optimization Equivalence {#param-opt}

Consider distribution optimization problems, of the form:

"Over a class of distributions *C*,
what distribution D minimizes a real-valued objective function f(D)"?

For instance, the class of distributions *C* might be all stationary response time
distributions achievable by M/G/1 scheduling policies for a given arrival rate λ
and job size distribution S,
and the objective function f(D) might be the mean f(D) = E[D].
Then the optimal distribution D would be the stationary response time
under the SRPT policy.

Two important families of optimization problems are:

1. **CDF Minimization**: The objective function f(D) = P(D > t) = F_D(t), for some threshold t > 0.

2. **Quantile Minimization**: The objective function f(D) = max_t s.t. P(D < t) < δ = F_D^{-1}(δ), for some threshold δ, 0 < δ < 1.

Note that these are both one-dimensional parameterized families of optimization functions.
Note that these parameterized families are equivalent in the following sense:
The set of all distributions D that appear as solutions to the CDF minimization problem for some t > 0 is the same as the set of distributions D' that appear as solutions to the Quantile minimization problem.

Intuitively, this is because if D_t is the CDF minimizer for t, and F_{D_t}(t) = δ,
then D_t is also the quantile minimizer for δ.

While equivalent in this sense,
the CDF minimization problem is easier to solve in stochastic control
scenarios such as the scheduling situation described above.
This is because it is easy to calculate the marginal impact of each job on the P(D > t)
objective: 0 if the job's response time is below t, 1 above.
It's harder to calculate the marginal impact of a job on the quantile objective
\- it requires access to the distribution D, which the policy typically does not have.

Any objective function of the form f(D) = E[g(D)], 
has this property, as long as the function g does not depend on D.
Instead, g should be parameterized.
As a result, such objectives are more useful, when available.
We'll call these objectives *expectation objectives*.

There's another important one-dimensional parameterized family of optimization functions:

{:start="3"}
3. **Conditional Value at Risk (CVaR)**: The objective function f(D) = E[D \| D > F_D^{-1}(δ)], for some threshold δ, 0 < δ < 1. This is the mean value of the top δ fraction of the distribution. It has a variety of advantageous properties - see Nico Christianson's ["Risk-Sensitive Online Algorithms"](https://virtual.oxfordabstracts.com/event/74044/submission/180) talk and paper.

This raises the question: Is there are parameterized family of expectation objectives
which matches the CVaR family of objectives in the same sense as above?
More generally, is there a parameterized family of expectation objectives
that covers the CVaR family of objectives, in the sense that
each CVaR-optimal distribution can be guaranteed to fall within the
new family's set of distributions?

**Starting point**: In the quantile case, the marginal impact of shifting an epsilon
of probability mass is 0 if the shift is below or above the quantile,
and a constant if it crosses the quantile. This hints at the corresponding
expectation objective.
What is the marginal impact of shifting an epsilon of probability mass on CVaR?
What is the corresponding guess of an expectation objective?

## Active projects {#active}


### Relative arrivals/completions with infinite state spaces {#infinite-ra}

**Setting**: Markovian arrivals/markovian service systems.

In my [RESET and MARC](/publications/#reset) paper, the MARC technique allows us to characterize the mean response time of systems with markovian service rates, if those service rate process is finite. See also my [SNAPP talk](https://www.youtube.com/watch?v=Zr6cf4p83AA), which is a cleaner presentation of the idea and focuses on markovian arrivals.

The "finite modulation chain" assumption isn't really necessary - the actual assumptions needed are much more minor. In particular, we should be able to analyze systems like the N-system or Martin's system by thinking of the non-heavily-loaded server as a modulation process on the service rate of the main server.

A good starting point would an N-system where the recipient server is critically loaded, but the donor server is not.

**Starting point**: Compute relative completions in the aforementioned N-system, compare against simulation. Perhaps pursue with Hayriye?

### Beating SRPT-k {#beating-srptk}

See [my talk](/talks/#sek) on this subject from APS 2025.

See Section 8.3.1 of [my thesis](/assets/isaac-thesis.pdf).

See our [MAMA paper](/publications/#mgk-lower).

**Setting**: SRPT-k (M/G/k/SRPT) is heavy-traffic optimal for mean response time,
as I proved in [SRPT for Multiserver Systems](/publications/#srptk),
but it can be beaten outside of heavy traffic.

**Idea**: Consider a 2-server system with 3 jobs in it: Two are small, one is large. There are two scheduling options: Run both small jobs first (SRPT), or one small and one large first (New concept). Once a small job finishes, start running the third job. If no new jobs arrive before the long job finishes, both options have the same total response time. If new jobs arrive after the small jobs finish but before the large job finishes, starting the large job sooner (New concept) is better. If new jobs arrive before both small jobs are done, SRPT is preferable.

**Policy**: Flip-3. (A variant of this is the SEK policy from my thesis and the MAMA paper). In an M/G/2, if there are at least 4 jobs, just run SRPT. If there are 3 jobs, and 2 have remaining size below a, and the third has size above b, run the smallest and largest jobs. Otherwise, SRPT. Set a at roughly 20% of the mean job size, and b at roughly the mean job size.

**First step**: Implement this policy. Compare it against SRPT-k. Fiddle around with job size distributions, loads, and a and b thresholds to find a relatively large separation (0.1% is normal, 1% is good).

**Future steps**: Use a [Nudge](/publications/#nudge)-style argument to prove that if a is small enough and b is large enough, the Flip-3 policy has lower mean response time than SRPT-2.

**Details**: Consider the case where we have jobs of size ε, ε, 1. The SEK policy runs ε, 1 for ε time, then ε, 1 for ε time, at time 2ε having the state 1-2ε. SRPT-k runs ε, ε for ε time, then 1 for ε time, at time 2ε having the state 1-ε. This is worse.

To prove that SEK in this specific instance is beneficial, proof sketch:

1. 1-2ε sample-path dominates 1-ε, by at least ε response time.
2. If a job arrives in the first 2ε time to disrupt things,
there is a coupling for SRPT-k and SEK such that until the end of the busy period,
system states differ by at most ε at all times,
resulting in only O(ε) worse total response time in the SEK system.
3. 1-2ε achieves ε+Omega(ε) better total response time that 1-ε, because more jobs could arrive.

### Continuous MSJ {#continuous-msj}

Existing theoretical multiserver-job research has overwhelmingly focused on the case of a discrete, finite set of resource requirements (e.g. numbers of servers). Moreover, policies make heavy use of this fact, often selecting a job to serve based on the number of identical jobs that are present in the system (e.g. MaxWeight). To learn more, see my [MSR MAMA paper](/publications/#simple-mrj) with Ben and Zhongrui.
In the real world, it's common for resource requirements to be real-valued (e.g. 0.35 CPUs), and for no two jobs to be completely identical.

**Model:** A natural model to capture this is: The total capacity of the system is 1. Jobs have a server need which is in the interval (0, 1]. Any set of jobs with total server need at most 1 can be served simultaneously. Jobs arrive according to a Poisson process with fixed rate λ, and have server need and duration sampled i.i.d. from some joint distribution.

**Goal:** A natural goal is throughput optimality -- stabilizing the system whenever it is possible to do so.

**Example setting:** A concrete example setting is: Server needs are Uniform(0, 1), and durations are Exp(1), independent of server need. This setting should be stabilizable for any λ<2.

**Policies:** One way to construct a policy which is definitely stable is to discretize the server needs by rounding them up to the nearest multiple of 1/n, for some large integer n chosen as a function of the system load. Then, we apply a standard policy like MaxWeight or the [MSR policies](/publications/#simple-mrj) on the discretized system.

This is fine as far as it goes, but these policies have poor performance as a function of n, the discretization parameter. It would be nice to have a throughput-optimal policy that isn't discretization-based.

One could empirically evaluate the performance of existing non-identical-job-based policies, such as best-fit backfilling (most servers first) and first-fit backfilling.

However, a policy worthy of further investigation is the infinite-n limit of the infinite-switching version of the MSR policy. MaxWeight doesn't have a natural infinite-n limit, it relies on having many jobs of the same class to function. MSR can be adapted to a continuous policy. For instance, with uniform server need, one version of the policy would be:

* For each threshold x in (0, 0.5], find the job with largest server need below x, and with largest server need below 1-x.

* For each interval of thresholds of width dx, serve that pair of jobs at rate 2dx.

Concretely, if the jobs in the system are of sizes {0.21, 0.41, 0.61, 0.81},
this policy would serve:

* [0.81] at rate 0.38 (thresholds [0, 0.19]),

* [0.61] at rate 0.04 (thresholds (0.19, 0.21)),

* [0.61, 0.21] at rate 0.36 (thresholds [0.21, 0.39]),

* [0.41, 0.21] at rate 0.22 (thresholds (0.39, 0.5)).

Note that this policy is straightforwardly suboptimal. It would be better to serve [0.61, 0.21] rather than ever serving [0.61], for instance.
Nonetheless,
I believe that this policy would be throughput optimal via a simple discretization proof,
along the same lines as the discretized MSR policy, but without requiring actual discretization.

**Project:** Define the limit-MSJ policy concretely, and prove that it is throughput optimal,
likely using a discretization proof.

**Further direction:** Define a strictly-better version of the policy which doesn't do silly things like idle servers, and show the result carries over.

## Half-Batch MSJ {#half-batch-msj}

In large-scale computing systems, such as high-performance computing clusters, there are often two types of jobs:

* **Large jobs**: High priority, latency-sensitive jobs which need a large amount of resources (e.g. compute nodes) at once, often a large fraction of the capacity of the entire system.
* **Small jobs**: Low priority, batch jobs (non-latency sensitive), which need a small amount of resources at once - many nodes, but a small fraction of the entire system.

The large jobs are the reason the cluster exists, at the size that it does. These jobs need to run on a very large cluster, and they're the jobs the cluster cares about.

However, there aren't enough karge jobs to utilize a large fraction of the capacity of the cluster.

So the cluster is also available for use by small jobs. Small jobs could run on this cluster, or on another lower resource system. They're not the priority, but they help keep the utilization high.

One challenge is that typically,  either type of job is preemptible.

**Model**: We will model this scenario with a MSJ system with two types of jobs, with two different arrival process: Large jobs arrive according to an external stochastic arrival process (e.g. Poisson process). Small jobs are always available. Neither type of job can be preempted.

There are two objects: Response time of large jobs and overall throughput, or equivalently throughput of small jobs. The goal is to optimize the tradeoff between the two.

In general, we would want general distributions of resource requirements and durations for small and large jobs. As a starting point, we can consider small jobs that take one server and large jobs that take n/k servers where n is the number of servers and k is a small integer, and exponential service times specific to the class.

As an extreme first step, we can consider the k=1 case.

**Starting point**: In the k=1 case, the default policy is: While there are large jobs in the system, no small jobs may enter service - we need to free up space. When all large jobs are done, small jobs may enter service.

There are two variations worth considering, to improve each objective:

* **Reserved capcity**: We can avoid using some of the capacity on small jobs even when there are no large jobs present. With exponential durations, it's more efficient to sometimes allow no small jobs to run, sometimes allow all small jobs to run, rather than only using some of the servers.
* **Batching together large jobs**: Rather than serving large jobs whenever they arrive, wait to accumulate many large jobs before servjng them all in a row. This avoids the overhead of emptying out the servers for each job. It's optimal to always batch up to a threshold, rather than a variety of batch sizes.

**First step**: Derive the optimal tradeoff curve between mean response time of large jobs and throughput of small jobs.

## Archived: Completed {#archive-done}

### M/G/k response time lower bounds (known size) {#mgk-lower}

See [our submitted paper](/publications/#mgk-lower).

See [our preliminary work on this topic](/publications/#mgk-lower-short).

See Section 8.3.2 of [my thesis](/assets/isaac-thesis.pdf).

There are two straightforward lower bounds on mean response time for the M/G/k: kE[S], the mean service duration, and E[T^SRPT-1], response time in an M/G/1/SRPT. Empirically, as ρ->1, SRPT-k achieves a mean response time around E[T^SRPT-1] + kE[S]. Can we prove a lower bound that's asymptotically additively larger than E[T^SRPT-1]?

**Idea**: Use WINE (see my thesis), with M/G/1 and M/G/infinity work bounds at different sizes. Mainly only improves things at lower loads.

**Idea**: Look at the "Increasing Speed Queue", which starts at speed 1/k at the beginning of a busy period, then 2/k, etc., capping at speed 1 until the end of the busy period. Provides a lower bound on work. A higher lower bound than the M/G/1. Incorporate into the WINE bound.

**First step**: Derive the WINE bound.

**Future step**: Quantity expected work in the increasing-speed queue, perhaps with renewal-reward.

**Update**: We can analyze the increasing-speed queue via the constant-drift/affine-drift method,
akin to the MARC method from my [RESET and MARC paper](/publications/#reset)
and my [SNAPP talk](https://www.youtube.com/watch?v=Zr6cf4p83AA).

See my photo-notes on the subject. For the 2-server setting, the constant-drift test function is:

    f(w, 1) = w, f(0, 0) = 0,
    f(w, 1/2) = w + (1-e^(-2lw))/2l

The affine-drift test function is:

    f(w, 1) = w^2, f(0, 0) = 0,
    f(w, 1/2) = w^2 + w/l + (1-e^(-2lw))/2l^2

These should be sufficient to compute mean work!

If we make the state space consist of work, time until next arrival, and speed,
we can simplify this considerably. The constant-drift test function is now:

    f(w, 1) = w, f(0, 0) = 0,
    f(w, a, 1/2) = w + min(w, a/2)

If we plug in `a = Exp(l)` and take expectations, we get the first expression above.

### Product form steady-state distributions from graph structure {#graph-product-form}

See our [submitted paper](/publications/#graph-structure).

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

**Update:** Elimination ordering seems better for summation-form relative arrivals/relative completions. Instead, for product-form you need something slightly stronger: A sequence of cuts such that on each side of the cut, there's exactly one vertex with transitions across the cut.

### Optimal scheduling in the general MSJ model {#general-msj}

See [our paper which is under revision](/publications/#seb).

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

### Known size dispatching to FCFS queues {#disp-fcfs}

This paper has been accepted to SIGMETRICS 2024: [Heavy-Traffic Optimal Size-and State-Aware Dispatching](/publications/card)!

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

Lower bound waiting time. Argument: All servers must have 1/k of the load going through them. The work has to be somewhere, and there's theta (1/(1-ρ)) of it in total. Best case scenario is that the largest jobs are the only jobs delayed by the work. This should dominate waiting time. This should match the waiting time of MASS, up to ratio 1, if the distribution is not too crazy.
## Archived: No longer interested {#archive-nope}

These are projects that I was once interested in, but I'm not interested in any more.
Maybe the approaches that I wanted to pursue didn't pan out,
maybe others took it in more interesting directions.
Either way, you can see my old ideas here.

### The Time Index scheduling policy {#time-index}

**Setting**: M/G/1 scheduling for the tail, especially the asymptotic tail, especially in comparison to FCFS.

**Policy**: Time Index. Priority is s - t, where s is a job's size and t is the job's time in system.Lower is better. Relatively simple proof that waiting time dominates FCFS waiting time.

**First step**: Implement this policy. Compare against FCFS, [Nudge](/publications/#nudge).

**Future steps**: By how much does it dominate FCFS? Characterize leading constant of asymptotic?

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

### General constrained-service queue {#constrained-service}

The Multiserver-job system and the switch can both be thought of as special cases of the "Constrained service queue": Jobs have classes, and a certain multisets of classes can be served at once. In the 2x2 switch, the service options are (ad, bc), while in the 2-server MSJ setting, the service options are (aa, b).

What policies and analysis make sense in the general constrained-service queue?
MaxWeight, used e.g. in
"[Stochastic models of load balancing and scheduling in cloud computing clusters](
https://core.ac.uk/download/pdf/4836445.pdf)", seems to be always throughput-optimal.
When does a [ServerFilling](/publications/#server-filling)
equivalent exist?
My [RESET paper](/publications/#reset) seems like it always applies to FCFS-type service.

### Restless MDPs for tail scheduling {#restless-tail}

In our [Gittins-k](/publications/#gittins-k) paper and in Ziv Scully's Gittins paper, ["The Gittins Policy in the M/G/1 Queue"](https://ziv.codes/publications/#the-gittins-policy-in-the-mg1-queue),
we relate the Gittins policy to that of the Gittins Game,
a corresponding MDP whose optimal solution describes the Gittins scheduling policy,
and gives rise to the optimality of the scheduling policy.
This relationship is at the heart of Gittins' original paper,
["Bandit Processes and Dynamic Allocation Indices"](https://doi.org/10.1111/j.2517-6161.1979.tb01068.x),
which introduces both the MDP policy and the scheduling policy.

For the mean response time objective, the corresponding MDP is a *restful* MDP,
giving the optimal solution strong enough properties to carry over to the scheduling setting.
In contrast, for a *tail* response time objective such as T^2,
the corresponding MDP is a *restless* MDP.
Recently, there have been advances in the theory of multiarmed restless MDPs,
such as the Follow-the-Virtual-Leader (FTVL) policy of Yige Hong and Weina Wang,
in their paper ["Restless Bandits with Average Reward: Breaking the Uniform Global Attractor Assumption"](https://arxiv.org/abs/2306.00196).

**Question**: Can we formulate a restless Gittins game, solve the single-arm version,
and use the FTVL policy or something similar to design a scheduling policy?

### Scheduling to minimize E[T^2] {#t2}

**Update**: I'm no longer particularly excited about this policy. It'd be a lot of work to analyze and it's not that close to an optimal policy - it doesn't incorporate lookahead at future increases in holding cost, for instance.

See Section 8.3.5 of [my thesis](/assets/isaac-thesis.pdf).

**Setting**: M/G/1 scheduling for tail, e.g. minimize E[T^2].

#### **Scheduling policy: t/s**

**Policy**: Priority is t/s, where t is a job's time in system and s is the job's size.
Higher is better. Without preemption to start, for simplicity of analysis.
Note that this is an "Accumulating Priority Queue", but with infinite continuous classes, not 2 classes.

[Waiting time distributions in the accumulating priority queue](https://link.springer.com/article/10.1007/s11134-013-9382-6),
David A. Stanford, Peter Taylor & Ilze Ziedins

**First step**: Implement this policy. Compare it against FCFS, SRPT. Poisson arrivals, medium variance, medium load. Does it do well empirically for E[T^2]?

**Future steps**: Use APQ methods to characterize steady state. Poisson point process of (size, time in system). Characterize for arbitrary joint (Size, Accumulation rate) distribution, specialize to above setting. Characterize transform of response time, moments of response time.

#### **Achievable region method of lower bounds**

**Background**: The key idea behind E[T] lower bounds is that if you prioritize jobs by remaining size, you minimize the amount of work below a given remaining size in the system. Using WINE, this bound can be converted into a response time bound, proving that SRPT is optimal. Similar proofs work for Gittins and in various multiserver systems.

We can call this the "achievable region" method - for each relevant work threshold, there is an achievable region of how much relevant work there can be in steady state, depending on the policy.

**Idea**: If you prioritize jobs by time in system (FCFS), you minimize the amount of work above each time threshold in the system. "Work with time-in-system above t". However, this cannot be converted into a bound on tail metrics such as E[T^2], because there is not a conversion from work to number of jobs or response time or anything like that.

However, we can get additional bounds by assigning jobs different deadlines based on their sizes, and then prioritizing jobs in a Earliest Deadline First fashion, where jobs reach maximum priority when they are past their deadline. Each such policy minimizes the amount of work of jobs past their deadline.

If jobs are classed exponential jobs (Exp(μ\_1), Exp(μ\_2), ...), then we can convert directly from an amount of work to a number of jobs. We'll get bounds of the form "N_1^t/μ\_1 + N_2^t/μ\_1 \ge x", where N_i^t is the number of jobs of class i that have been in the system for over t time. Perhaps we can integrate results like this, incorporating different deadlines for different classes of job, to get a good T^2 lower bound.

