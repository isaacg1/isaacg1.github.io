---
published: false
title: 'Paper 4: Load Balancing Guardrails'
---
Time for my fourth paper: [Load balancing guardrails](/assets/guardrails.pdf). This was the second paper I wrote during my PhD at CMU, and it builds upon my first paper on [SRPT-k](/assets/srpt.pdf). My coauthors once again were [Ziv Scully](https://ziv.codes/), then a fellow PhD student, now a postdoc at the Simons institute, soon to be a professor at Cornell, and [Mor Harchol-Balter](https://www.cs.cmu.edu/~harchol/), my advisor (and Ziv’s).

### Setting

My previous paper, which I [wrote a post about](/2022/09/17/recap-srptk.html), dealt with a central queue model, where the scheduler could run any k jobs of its choice. In this paper, we focus on an immediate dispatch model, where jobs must be sent to one of the k servers immediately on arrival, and the job must eventually run at that server.

As a result, we must design both a dispatching policy and a scheduling policy: where should jobs be sent on arrival, and which job should be run at a given time?

Otherwise, the setting is the same as in the SRPT-k paper: Poisson arrivals, i.i.d. job sizes, fixed number of servers k, variable load rho. We are again interested in the mean response time behavior in the rho to 1 limit.