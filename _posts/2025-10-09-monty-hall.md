---
published: true
title: "Monty Hall: More Complicated"
layout: post
---

The [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
is typically stated as follows:

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

The standard answer is yes: If you switch to door No. 2, you'll win the car 2/3 of the time, while if you hold your original choice of door No. 1, you'll win the car 1/3 of the time.

But this standard answer rests on a couple of additional assumptions:
An assumption about how the car is placed,
and an assumption about the host's decision-making policy.
Let's spell out these assumptions, and see how they affect the probabilities.

## Detailed version 1: Always open a door

Here's one possible expanded version of the problem, with the assumptions spelled out:

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. **The car is equally likely to be behind any of the doors.** **The host, who knows what's behind the doors, decides that regardless of which door you pick, he'll pick a door with a goat behind it to show you.** You pick a door, say No. 1, and the host, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Two assumptions are made here: That the door we picked is as likely as any other to have the car, namely a 1/3 chance, and that the host will open a goat door regardless of which door we pick.

Under these assumptions, the standard analysis goes through: The initial selection has a 1/3 chance to be correct, a door with a goat behind it will always be opened, and so the initial selection still has a 1/3 chance to be correct, with a 2/3 success rate for switching.

The first assumption seems reasonable: No information about the car's placement is given when we initially select a door, so equally likely for each door is a fine assumption.

The second assumption is rather more suspicious: Sure, that's one policy the host could adopt, but it's hardly the only plausible policy. In particular, game show hosts rarely commit to providing an option to a contestant, regardless of the contestant's actions.
Instead, they frequently decide which options to offer the contestant based on the secret knowledge they possess.
With regards to the game show [Let's Make a Deal](https://en.wikipedia.org/wiki/Let%27s_Make_a_Deal),
which this problem is based on,
the host [Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall),
who is the namesake of this problem,
was interviewed about this very problem.
In that interview,
he [specifically mentioned](https://en.wikipedia.org/wiki/Let%27s_Make_a_Deal#Monty_Hall_problem)
that he decided which trades to offer based on the contestant's past choices.

So let's see how a different policy by the host could change the outcome.

## Detailed version 2: Deceptive host

Here's a different possible expanded version of the problem,
with a game show host who wants to prevent us from winning.

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. The car is equally likely to be behind any of the doors. **The host, who knows what's behind the doors, decides that if and only if your first pick has the car behind it, he'll pick a door with a goat behind it to show you. Otherwise, he'll just open the door you first picked and show that you've lost.** You pick a door, say No. 1, and the host, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Under this assumption, the answer is clearly no: He only opened a door because your first pick was correct.

Notice that either assumption is consistent with the original setup:
We don't know why the host decided to open a door and make an offer to switch,
and these are both plausible stories.

This assumption is plausible specifically if we think the host doesn't want us to win: If he can just open our first pick and show us we've lost, he does so. He only offers us the option to switch if he can't reveal our loss immediately.

There are still other assumptions about the host's behavior that could produce scenarios where it is advantageous either to switch or stay, or neutral between the two.

## Conclusion

The original Monty Hall problem is underspecified, as a probability/statistics problem. It can be expanded into a fully specified problem, but only by adding additional information, in the form of a decision-making procedure for the game show. In its original underspecified form, the problem pulls in guesswork about the entertainment mindset: On this game show, is the host more likely to use a decision procedure more like version 1? Version 2? Something else? What's the probabilities distribution over these possibilities? What would make the best show for the least cost?

It's not really a probability problem at all.
