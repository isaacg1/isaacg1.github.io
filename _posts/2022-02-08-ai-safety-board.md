---
layout: post
title: "Learning from Partial AI Failures"
draft: true
---

## AI Alignment

I know a good number of people who care a lot about [AI Alignment](https://en.wikipedia.org/wiki/AI_alignment):
the problem of ensuring that an AI system optimizes for good outcomes,
outcomes that the creator wants,
or at the very least non-disastrous outcomes.

For instance, consider a system that is extremely optimized for maximal effectiveness
on some computational task,
and suppose that the system has free access to the internet.
After enough optimization,
the system might happen upon the strategy of exploiting insecure internet-accessible machines,
and perform the computational task on those machines as well.
After even more optimization,
the system might block messages to those machines that might shut them down,
to better perform its task.

After a few iterations of this optimization,
the behavior of the system might be very far away from the original intent of the designer,
which might have been
"perform this computational task, but don't commit crimes, and shut down if commanded".
One could imagine this having disastrous outcomes.
Others have explained it better than I,
but there is essentially no limit to how disastrous such outcomes might be,
given sufficient optimization power.

## One Approach: Advance Frameworks

One approach to grappling with this problem
that I have seen explored is to develop mathematical and computational frameworks
around ensuring that AI systems behave in ways
that match both the implicit and explicit intentions of the designer.
The hope is that if such frameworks exist,
people will use them in their AI systems,
either voluntarily or under legislative pressure,
lowering the probability of bad outcomes.

Personally, I'm not a strong believer in the approach of "create frameworks in advance".
It feels like trying to figure out how to build safe bridges,
before anyone's ever built a bridge,
to prevent bridge collapses.
It's worth trying, but I don't hold much faith in its success.
I do think this is a very important problem,
so I think it's important to find better approaches.

## A Better Approach: Learning from Partial Failures

Fundamentally, I think learning from past mistakes
is an extremely important part of the
process of making something safe,
and we need to harness it as much as we can.

In particular, I think we need to learn from partial failures,
that are short of full catastrophes.
Before a maximally bad event, such as a situation
where an AI system exports itself across the internet
to insecure devices, prevents itself from being shut down,
and does arbitrarily bad things,
we're likely to see partial failures.
For instance, an AI system not intended for the purpose of exploiting insecure systems
might stumble upon a method to do so, but not export itself onto that device.
Because this has less moving parts, it's likely to happen sooner.

I think it's critical that we learn from these partial failures,
and ensure that the insights gained are communicated to everyone who works on
highly optimized AI systems like these.
Right now, I think there's many ways
in which we might not learn from these partial failures,
allowing more and more failures to occur.

* Partial failures might take place with companies or research groups
that do not publicize these events.

* The developers and researchers might not realize that such events
are important learning opportunities.

* Organizations might learn from their own partial failures,
but not effectively pool that knowledge across organizations.

* Effective investigation of the root causes of the partial failure,
and how to prevent recurrence,
might take more resources than
the organization where the failure occurred is able or willing to apply.

To overcome these problems,
I'd like to look at how safety was improved in other fields.

## Safety Boards

There are several fields in which extremely difficult and potentially dangerous activities
have been made much safer than that baseline.
Two such fields that come to mind for me are
aviation and chemical engineering.

In each case, a critical component of the process of improving safety
is an investigatorial organization known as a "safety board".
In the US, we have the [National Transportation Safety Board](https://en.wikipedia.org/wiki/National_Transportation_Safety_Board) for aviation and transportation in general,
and the [Chemical Safety Board](https://en.wikipedia.org/wiki/U.S._Chemical_Safety_and_Hazard_Investigation_Board),
for industrial chemical safety.

These safety boards have the responsibility, the resources, and the legal authority
to investigate accidents in their field,
exhaustively sift through all of evidence to find the root cause,
publish the results and documentation of those findings,
and publish findings on how to prevent such accidents from recurring.
Other organizations implement those findings,
either legislatively, voluntarily, or through other processes.

These safety boards have been extremely effective for improving safety in their areas.
Many of their discoveries have directly lead to major safety improvements
which are now essentially universal in their fields.

What makes safety boards so effective is their exhaustive 
documentation.
If an investigation is successful,
it is often so well documented that no reasonable person who engages with their report
can doubt its conclusion.
This is a major part of what drives the implementation of their recommendations.

I think safety boards are crucial from learning how to do difficult,
high risk activities as safely as possible,
learning as quickly as possible from the fewest number of mistakes.

## Safety Boards for AI Alignment

I think now is the time to start creating such organizations
to investigate failures of alignment-safety in highly-optimized AI systems.
While an organization with governmental power would be preferable,
a non-profit would already be a major step forward.
I imagine that if one freely offers such an investigation,
some organizations would accept that offer.

Better yet would be many investigatorial bodies,
so that we can find out how to more effectively
learn from these failures, and disseminate the resulting insights.

Learning from failures found in the wild has a completely different character from
hypothesizing failures and trying to proactively stop those.
While advance research is worth trying,
learning from experience is a necessary component of safety.
Ultimately,
we're not going to know what alignment failures look like
until we see them happen,
so we need to thoroughly investigate the failures that do happen.
