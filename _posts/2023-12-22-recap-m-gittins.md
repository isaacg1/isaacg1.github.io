---
published: true
layout: post
title: 'Paper 5: Multiserver Monotonic-Gittins Scheduling'
---
Let's return to this series.
Time for my fifth paper: [Optimal Multiserver Scheduling with Unknown Job Sizes in Heavy Traffic](/assets/m-gittins-k.pdf)
This was the third queueing paper I contributed to,
and it builds upon my first queueing paper, on [Muliserver SRPT](/2022/09/17/recap-srptk.html).
My coauthors once again were [Ziv Scully](https://ziv.codes/), then a fellow PhD student,
now a professor at Cornell,
and [Mor Harchol-Balter](https://www.cs.cmu.edu/~harchol/), my advisor (and Ziv’s).

### Setting

My previous paper on SRPT-k, which I [wrote a post about](/2022/09/17/recap-srptk.html),
dealt with a central queue model, where the scheduler could run any k jobs of its choice,
and where the scheduler knows each job's size (its service requirement) in advance.
In this paper, we focus the setting where the job size *distribution* is known, but the actually size of a job is unknown.
With respect to a specific job, the only information we have available is the job's *age*,
the amount of service it has received so far.

We want to design a scheduling policy which looks at those ages, looks at the job size distribution,
and decide which jobs to run.

Otherwise, the setting is once again the same as in the SRPT-k paper: Poisson arrivals, i.i.d. job sizes, fixed number of servers k, variable load rho, preemption allowed. We are again interested in the mean response time behavior in the rho to 1 limit.

### Building blocks

In this paper, we decided to build off of three building blocks:
The [Gittins policy](https://ziv.codes/pdf/wiopt2021-scully.pdf)
for the single-server queue, dating back to 1980,
the [SOAP](https://ziv.codes/pdf/sigmetrics2018-scully.pdf) analysis by my coauthors,
and the multiserver tagged-job approach from the SRPT-k paper.

The Gittins policy is the policy which minimizes mean response time in the single-server setting.
It works as follows:

1. Look at all jobs in the system, and all durations for which we could run those jobs.

2. Using the job size distribution and the current ages of the jobs,
calculate the probability that the job will finish within the duration,
and the expected time for which the job will be served
-- the minimum of the service duration and the job size.

3. Rank jobs by the ratio of expected service time to probability of completion. Serve the job with lowest ratio -- the least time to complete a job, in expectation.

The Gittins scheduling policy is an *index* policy, which means it maps job ages to a priority and serves the job of best priority. This priority can go up and down as a job increases in age, depending on the job size distribution.

To analyze the mean response time of single-server policies such as the Gittins policy,
my coauthor Ziv developed the SOAP analysis.
SOAP stands for "Schedule Ordered by Age-based Priority".
It gives a unified analysis of mean response time
for all age-based index policies in the single-server setting,
and in particular it gave the first mean response time analysis for the Gittins policy.
Despite the Gittins policy having been known to achieve optimal mean response time
for about 40 years, this was the first mean response time analysis.

All of that prior work was in the single-server setting.
To prove a result in the multiserver setting,
we decided to use the multiserver tagged-job analysis from the SRPT-k paper,
which essentially transfered SOAP-type results from the single-server settting
to the multiserver setting.

### Challenge: Monotonicity

Unfortunately, as we explored the multiserver tagged-job analysis in this setting,
we encountered an obstacle:
The method only produces tight results for *monotonic* index policies.

There are two kinds of monotonic index policies:
Monotonically increasing, and monotonically decreasing.
Monotonically increasing means that as a job's age increases,
its priority only stays constant or gets worse, never better.
On the flipside, a monotonically decreasing index policy is one like SRPT where a job's priority
only gets better, never worse.
Non-monotonic policies are ones where priority goes both up and down.

In the paper, because we focus on the unknown job-size setting, the index policies of interest
are monotonically increasing policies, and non-monotonic policies.

In Theorem 5.1 of the paper, we use the mutliserver tagged-job approach
to give a tight analysis of mean response time for monontonically increasing policies,
following the SRPT-k approach quite closely.
In particular, we show that any monotonically increasing scheduling policy
in the multiserver setting
achieves mean response time not much larger than the same scheduling policy
in the resource-pooled single-server setting,
combining all servers together into one giant server that runs a single job at k times the speed.

In Appendix A, we show that the same approach cannot give a tight mean response time analysis
for nonmonotonic policies:
The resulting bound on mean response time will not be particularly tight,
as the method makes too many worst-case bounds along the way.
We tried several times to replace those worst-case steps with stochastic analyses,
but it never worked out.

So, in the end, we decided to restrict our attention to monotonic scheduling policies,
even if that meant we wouldn't be able to use the Gittins scheduling policy.

### Policy: Monotonic Gittins

Instead, we selected the Monotonic Gittins (M-Gittins) scheduling policy.
This policy starts with the Gittins policy,
but then adds the additional caveat that a job's priority is never allowed to improve (decrease).
Formally, a job's priority is the maximum of all priorities up to that age under the Gittins policy.

Thanks to our work with the multiserver tagged-job method, we knew that multiserver M-Gittins
performed nearly as well as single-server M-Gittins.
Now, it remained to analyze single-server M-Gittins in comparison to
true, optimal single-server Gittins.

This part of the paper was less my focus - I mostly focused on the multiserver tagged-job method.
Our analysis of M-Gittins lead through the SERPT and M-SERPT policies:
Shortest Expected Remaining Processing Time
and the monotonic variant thereof, which were essentially
simpler proxies for the Gittins and M-Gittins policies in the single-server setting.

We couldn't analyze these policies for fully general job size distributions,
just for certain important classes of distributions,
with lots of effort needed for each class of distribution.

### Results

Our main result was Theorem 3.1,
where we proved that in several important classes of job size distributions,
the Monotonic Gittins scheduling policy achieves asymptotically optimal mean response time
in the multiserver central queue setting.

### Retrospective and future directions

This work was a little underwhelming. We weren't able to analyze the proper multiserver Gittins policy, as we would hae liked, and we weren't able to analyze fully general job size distributions,
but had to settle for classes with more structure.
And finally, this paper focused only on the setting where jobs are undifferentiated except for their ages. It couldn't handle different classes of jobs with their own size distributions, for instance.

Nonetheless, this paper represents about as far as one could get with the techniques that we'd developed at the time: multiserver tagged-job + SOAP.
For futher results, we'd need to develop new techniques.
And in our next paper, on [multiserver Gittins](/assets/gittins-extremely-general.pdf),
we did just that.
