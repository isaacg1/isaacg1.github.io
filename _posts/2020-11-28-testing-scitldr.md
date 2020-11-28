---
layout: post
title: "Testing SciTLDR"
---
The Allen Institute for AI recently released [SciTLDR](https://scitldr.apps.allenai.org/),
a program which automatically creates one-sentence summaries of scientific papers.
It's currently only trained on Computer Science papers written in English,
which just so happens to be my field and language.
I decided to try it out on each of my own papers, to see how it would do.
The source text I used is simply copied from the PDF,
with nothing done to clean up the resulting formatting errors.
The input was the abstract, introduction and conclusion of each paper.
All of my papers are linked in my Publications tab.

Here the papers from my PhD so far, from oldest to newest,

#### Paper: SRPT for Multiserver Systems

Summary: "Stochastic analysis of multiserver SRPT in the heavy-traffic limit ."

This is quite good, almost as good as I could have done myself.
To  be completely correct,
we analysis SRPT at all loads, not just the heavy traffic limit.
We prove optimality specifically in the heavy traffic limit,
however.
Nonetheless, I'm quite impressed, to be honest.
Of note, this exact sentence appears nowhere in the original text.
"Stochastic analysis of multiserver SRPT" appears in the paper,
but not in the abstract, intoduction or conclusion.
I'll give it a pass on the weird space before the period,
that might be an artifact of the PDF copy-paste.

#### Paper: Load Balancing Guardrails: Keeping Your Heavy Traffic on the Road to Low Response Times

Summary: “We devise a simple fix that can be applied to any dispatching policy that yields optimal mean response time when used in a system with SRPT servers”

This is somewhat less impressive.
This is essentially a compression of the following two sentences from the abstract:
"In this paper, we devise a simple fix that can be applied to any dispatching policy. This fix,
called guardrails, ensures that the dispatching policy yields optimal mean response time under heavy traffic when used in a system with SRPT servers."

In the compression, the quality suffered somewhat.
In particular, in the TLDR, it's somewhat unclear whether the original policy
needs to already have optimal mean response time
or whether the fix causes the new policy to have optimal mean response time.
The quote from the abstact makes this clearer.
Also, it's weird to use "We" to refer to me and my collaborators.

#### Paper: The CacheLib Caching Engine: Design and Experiences at Scale

Summary: “A general-purpose caching engine that powers over 70 services including CDN, storage, and application-data caches.”

This is again less impressive. This time, the two sentences squished together from the abstract are "CacheLib is a general-
purpose caching engine, designed based on experiences with
a range of caching use cases at Facebook, that facilitates the
easy development and maintenance of caches. CacheLib was
first deployed at Facebook in 2017 and today powers over 70
services including CDN, storage, and application-data caches."

In doing so, SciTLDR removed the name of the caching engine (CacheLib),
which is important information in this case.
In addition, this summary purely consists of the "what", with no "how" or "why".

#### Paper: Optimal Multiserver Scheduling with Unknown Job Sizes in Heavy Traffic

Summary: "We introduce monotonic Gittins (M-Gittins) and show that it minimizes mean response time in the M/G"

This comes so close to being very good. If it merely changed "M/G" to "M/G/k",
I would rate it quite good.
Unfortunately, SciTLDR seems to have been tripped up by the fact that
our result about the "M/G/k" (a multiserver queueing system)
builds on results we prove about the "M/G/1" (a single-server queueing system).
It seems the TLDR program can't pick which to write, and chooses their intersection.

#### Paper: Stability for Two-Class Multiserver-job Systems

Summary: “We derive a closed-form analytical expression for the stability region of a two-class (non- dropping) multiserver-job system where”

Again, very close. If the final "where" was removed, I would rate it qiute good.
It seems the system gets caught in between reasonable alternatives fairly easily.
Here, it would be reasonable to either remove that final where
or add "each class can have distinct exponential service duration distributions".

#### Paper: The Gittins Policy is Nearly Optimal in the M/G/k under Extremely Geneneral Conditions

Summary: “We give the first general analysis of Gittins in the M/G/k.”

This is the worst yet. It's straight out of the introduction, which had the sentence
"In this work we give the first general analysis of Gittins in the M/G/k."
It makes no reference to anything that makes this paper special,
neither defining "general" nor mentioning optimality.

### Final grades

One success, two near misses, two so-so, one failure. OK, but not all that good just yet.
Lots of fun to mess around with.
Thanks to the team behind SciTLDR for making this publically available so I could mess around with it.
