---
published: true
layout: post
title: 'Paper 6: Multiserver Gittins Scheduling'
---
Continuing my paper summary series 
([1](/2021/08/12/paper-push-pull),
[2](/2021/08/14/paper-gadgets),
[3](/2022/09/17/recap-srptk),
[4](/2022/10/26/recap-guardrails),
[5](/2023/12/22/recap-m-gittins)),
it's time for sixth paper,
[The Gittins Policy is Nearly Optimal in the M/G/k under Extremely General Conditions](/assets/gittins-extremely-general.pdf).
This is another heavy-traffic scheduling paper,
just like my first 3 queueing papers,
papers #3, #4, and #5 above.
My coauthors were Ziv Scully and Mor Harchol-Balter, once again.

This paper overcame the issue in our previous paper,
on [Monotonic Gittins](/2023/12/22/recap-m-gittins),
where we couldn't figure out how to prove a heavy traffic optimality result
for index scheduling policies where the index underlying scheduling policy isn't monotonic
-- if it goes up and down. Read the previous recap (#5) if those concepts don't make sense.

So how did we overcome this issue? How did we figure out how to analyze index policies where the index goes up and down?

Well, we didn't, not really. Our old technique, which I call the "multiserver tagged job" technique, is pretty broadly applicable. We were able to analyze a lot of different policies with it. But our bounds were only good in heavy traffic if the policy was monotonic.

By contrast, our new technique, the "WINE technique" (which Ziv came up with), is much more specialized. It only works for *Gittins policies*. Nothing else. No flexibility.

Fortunately, there are actually a lot of different Gittins policies, because the Gittins policy is flexible to different information environments. In paper #5, we were focusing on the no-information Gittins policy, where the scheduler makes decisions based only on the age of a job, the amount of time it's been served so far.

But my other two queueing papers, #3 and #4, are in the full information setting, where the scheduler knows exactly how long each job has left to run. In this case, Gittins is equivalent to the SRPT policy we studied in both of those papers. So this new WINE technique also applies to multiserver SRPT policies, which will come in handy in a few papers.

And Gittins can also be applied to partial information settings, like when you have an estimate for how long the job will take, or you find out when it's half done.

These are the "Extremely general conditions" mentioned in the title of the paper, by the way.

This paper, and more specifically the WINE technique, apply to any Gittins policy, in any information setting, and nothing else.

### The WINE Technique

So what is the WINE technique?

Well, it all starts with the Gittins rank (i.e. Gittins index) of a job.

The Gittins rank of a job is basically a completion frequency:
A Gittins rank of x means if I served this job for some amount of time,
I would need to spend at least x seconds per completion.

And to be clear, that might look like serving x seconds for a guaranteed completion,
or 1 second for a 1/x chance at a completion, or any combination of service duration
and completion probability.

My service rule might also be randomized: I'll serve for 1 second,
unless I get an information update about the job's predicted duration,
in which case I'll recalculate.

The Gittins rank of a job is the best possible ratio of expected time spent serving the job to probability of completing the job, over all service rules.

The Gittins policy looks at every job's Gittins rank, and serves the job of least Gittins rank.

Now, it's important to note that the Gittins rank can change over time.

For instance, in the perfect information case, a job's Gittins rank is its remaining size. We can achieve 1 completion by running the job until it completes. So the Gittins rank is always decreasing.

As another example, in the no-information case, if a job has decreasing hazard rate,
its Gittins rank is equal to the reciprocal of that hazard rate.
So the Gittins rank is always increasing.

It's pretty rare to have a constant Gittins rank, but exponential job sizes with no information is one example. The Gittins rank is equal to the mean job size, and all service rules are equally good.

Next, we need to define Gittins relevant work.

The idea is as follows: Suppose we're using the Gittins policy, and my rank is x,
and your rank is currently below x. I'm going to have to wait until either:
* You complete, or
* your rank is bigger than x, so I can run ahead of you.

We're always thinking about preemptive policies, in this whole discussion and this whole paper.

There's some random distribution of how long you'll take to complete or reach a rank above x, and we'll call that your *relevant size* with respect to the cutoff x.

For example, in the perfect information case, this is simply your remaining size if your remaining size is less than x, and 0 otherwise. But we can define relevant size in any informational context.

And this is where the important WINE concept comes in! Ziv proved a really cool theorem, which holds in any informational setting. For a given job i, let `S_i(x)` be its relevant size at threshold x. Then, no matter the job and no matter the informational setting,

```
∫_0^∞ E[S_i(x)]/x^2 dx = 1
```

The integral of `E[S_i(x)]/x^2` over x from 0 to infinity is 1!

This really cool and awesome!

Why is it cool and awesome?

Well, it gives us a way to count jobs in the system.

How? Well, let's define the relevant work W(x) in the system to be the total of S_i(x) over all jobs in the system. Then adding up the previous equation gives us

```
∫_0^∞ E[W(x)]/x^2 dx = N,
```
where N is the number of jobs in the system.

This is even cooler and more awesome! This is the WINE formula!

Why is it even cooler?

Well, it's one of the key steps in our overall goal, bounding mean response time.
The thing is, we already have Little's Law, which says that `λ E[T] = E[N]`,
where λ is the arrival rate, and T is the response time.
So the WINE formula really tells us the relationship between mean work and mean response time!

The old method (that we also invented), the multiserver tagged job approach,
had two key steps:

1. Bound relevant work
2. Use the bound on relevant work to bound response time

Our new WINE approach is going to use the same two steps, and we've just completed the second step, translating relevant work into response time!

Now, we just need to bound relevant work!

### Relevant Work Decomposition Law

The relevant work decomposition law (section 7) breaks down relevant work in the multiserver Gittins system into three sources:

1. Relevant work in the single-server Gittins system,
2. Work due to capacity left idle while relevant work is present, which doesn't happen in the single server system, and
3. Work due to jobs recycling while relevant work is present, which doesn't happen int he single server system.

What's recycling? That means a job which previously had rank above x, and then due to service its rank decreased down to rank x.

For work sources 2 and 3, the expected cross product is the important term:
The expected amount of idle capacity times relevant work when that capacity is idle,
and the expected size of the freshly recycled job times relevant work when that job recycles.

We bound these cross products, taking care to ensure that our bounds are tight both for thresholds that are large relative to the typical rank of jobs in the system, as well as thresholds that are small in this same scale. Putting it all together gives our heavy traffic optimality result, as desired. Very exciting!

The new ideas from this paper, especially the WINE formula but also the relevant work decomposition law, will go on to have bright futures in subsequent papers.

See you next time!
