---
layout: post
title: 'Paper 1: Push-Pull Block Puzzles are Hard'
published: true
---

I'm going to write recaps of all of the papers I've written,
in chronological order.

I'm starting with my first paper: ["Push-Pull Block Puzzles are Hard"](/assets/push-pull.pdf).
This paper was written during my undergrad at MIT with my collaborator
[Jayson Lynch](https://www.linkedin.com/in/jayson-lynch-b6297ab),
then a PhD student at MIT and now a Posdoc at University of Waterloo,
and with [Erik Demaine](http://erikdemaine.org/), his advisor.
We published in CIAC 2017.

The paper studies a block pushing and pulling game,
similar to the classic video game [Sokoban](https://en.wikipedia.org/wiki/Sokoban).
The character is in a maze on a grid,
with blocks in some squares and walls in others.
The character can push or pull blocks, but walls are fixed.
The goal of the game is for the character to reach a designated square.
Another variant of the game involves placing each box on a designated square.

This game is called "Pukoban", and was invented by Dries De Clercq.
An ancient flash version could be found on the internet for many years at
[this link](http://puzzles.net23.net/pukoban.htm),
but it went down sometime between 2018 and 2021.
A clone is hosted at [sokoban.cn](http://sokoban.cn/variant/psokoban.php),
which runs natively on Windows and can be run on Linux through [wine](https://www.winehq.org/).
I've taken the liberty of hosting a copy on this blog at [pukoban.zip](/assets/pukoban.zip).

The game is quite difficult to play casually.
A memorably hard level (Level 1 of the flash game!) starts in the following state:

    _oC#
    _o#_
    o___
    #___

Here `#` is a wall, `_` is an empty square, `C` is the character, and `o` is a block.
This is an instance of the variant where each box must end up on a target square.
The desired final configuration is:

    __C#
    __#_
    o___
    #oo_

If you want to solve this on your own, please do so! It's definitely a fun puzzle.

A useful fact about this game is that the state space is undirected - any move can be undone.
We called the game "reversible" as a result,
though note that we're not talking about logical reversibility, as in "reversible computing".
As a result, it is completely valid to solve backwards from the end state to the starting state,
or to try to meet in the middle.
This fact makes the game much easier,
but it is still quite difficult.

Here's a solution path for this level (left to right, top to bottom):

    _oC#     o__#     o__#     o__#     o__#     oo_#     oo_#
    _o#_     __#_     __#_     __#_     __#_     _C#_     __#_
    o___     oC__     o___     o___     _oC_     ____     ____
    #___     #o__     #_oC     #_Co     #__o     #__o     #Co_


    oo_#     oo_#     oo_#     oo_#     o__#     o__#     o__#
    __#_     _C#_     __#_     __#o     __#o     __#o     __#o
    ____     _o__     __Co     ___C     _o__     __oC     __Co
    #oC_     #___     #___     #___     #C__     #___     #___


    ___#     ___#     ___#     _o_#     _Co#     __o#     _Co#
    o_#o     C_#o     __#o     _C#o     __#o     __#o     _o#o
    C__o     o__o     _oCo     ___o     ___o     Co__     ____
    #___     #___     #___     #___     #___     #___     #___


    _oo#     _oo#     _oo#     _oo#     _oo#     _oo#     __o#
    _C#o     __#_     __#_     __#_     __#_     __#_     _o#_
    ____     ___o     Co__     _C__     ____     ____     _C__
    #___     #__C     #___     #o__     #_oC     #_Co     #__o


    __o#     __o#     Co_#     ___#     ___#     C__#     o__#
    _C#_     __#_     __#_     __#_     __#_     o_#_     C_#_
    _o__     __Co     ___o     _o_o     oC_o     ___o     ___o
    #__o     #__o     #__o     #C_o     #__o     #__o     #__o


    o__#     o__#     o__#     ___#     ___#
    __#_     __#_     __#_     o_#_     C_#_
    ___o     Co__     _C__     C___     o___
    #Co_     #_o_     #oo_     #oo_     #oo_

Given how hard the game can be casually,
we were interested in the computational complexity of the game:
could we prove that the game is hard or complete for some well-known complexity class?
This would be quite difficult, because to the best of my knowledge,
people had previously only characterized the complexity of non-reversible variants of the game.
In such settings, it's often a lot easier to construct hard levels,
because one can force the character to move through the level in a certain direction
by including one-way features.
In reversible games, no one-way features can exist.

We weren't able to tackle the standard version of the game,
but we managed to characterize the 3D variant of the game with thin walls,
proving that it is PSPACE-complete.
Here "thin walls" are walls on an edge, rather than occupying a full square.
Our construction relied exclusively on the following gadget:

    #######
    ##_#_##
    #_o_o_#
    ##o#o##
    #_ooo_#
    ##_#_##
    #######

The outer 8 openings are all accessible via the third dimension.
The NNW and SSW openings are connected,
as are the NNE and SSE openings.

The other four openings connect to the outside.
In its current state, it's possible to traverse the gadget from
WNW to WSW or from ENE to ESE,
in either case transforming the state to

    #######
    ##_#_##
    #_ooo_#
    ##o#o##
    #_o_o_#
    ##_#_##
    #######

From here, one can return via either traversal.
We call this gadget a "two-toggle".
There are two pathways, with a shared internal state.
Each pathway is traversable in one direction in a given state,
and traversing it flips the internal state.
These 2-toggles are very fundamental objects in the theory of reversible motion games.

At the time, we did not know how to make interesting constructions out of 2-toggles.
That would be remedied in [our later paper](assets/load-balancing.pdf).

Fortunately, we can push the above gadget further.
Imagine taking another copy of the above gadget and rotate it in the third dimension
by 90 degrees, around the axis of symmetry.
The resulting gadget is now a 4-toggle.
This, we did figure out how to use.

We used our 4-toggle to construct a 2-toggle-and-lock gadget,
by linking a pair of pathways together.
The resulting gadget has three pathways:
2 toggle pathways, and a "lock" pathway,
which can only be traversed in one state,
and does not affect the state when traversed.

This 2-toggle-and-lock was exactly what we needed to prove that the game was
[PSPACE-complete](https://en.wikipedia.org/wiki/PSPACE-complete),
which essentially means "as hard as possible" in this context.
We did so by directly reducing to the [Quantified Boolean Formula problem](https://en.wikipedia.org/wiki/True_quantified_Boolean_formula),
which is a famous PSPACE-complete problem.

Essentially, to solve our special levels,
the player would be forced to solve a problem that's known to be super hard,
making the game itself super hard as well.

Retrospective
---

Overall, I'm happy with the paper.
We developed a new way of proving PSPACE-completeness besides Nondeterministic Constraint Logic,
which Erik developed and which was the previous standard.
We also opened the world of "Gadget motion planning", which my next paper would further explore.

That being said, I was rather dissatisfied with how abstract and inapplicable
the setting was, which led to me doing my Master's degree in cryptography,
which I had similar issues with,
and then my PhD in Queueing Theory, which I've found to hit a better balance of
theory goodness and applicability.

Beaten to the punch
---

Unfortunately, our paper was dead before it lived.

We had written the paper by 2015,
as can be seen by its inclusion in Jayson's [Master's thesis](https://dspace.mit.edu/handle/1721.1/105999), in Chapter 3, which was submitted in September 2015.
I'm pretty sure we completed the work by the prior spring (April 2015),
when Jayson submitted it to the MOVES 2015 conference.
However, we didn't submit the paper until 2017.

In July 2015, Pereira, Ritt and Buriol submitted a paper titled [Pull and PushPull are PSPACE-complete](https://www.researchgate.net/profile/Luciana-Buriol/publication/297750476_Pull_and_PushPull_are_PSPACE-complete/links/5f027ebea6fdcc4ca44e8cda/Pull-and-PushPull-are-PSPACE-complete.pdf),
which completely subsumed our result by showing that PushPull-1,
in 2D, with no thin walls, is already PSPACE-complete.

We neglected to redo our prior-work review
to see if anything was discovered between when we wrote the paper and when we submitted it,
so we didn't realise that by the time we submitted this paper in January 2017,
it was already obsolete.
The peer reviewers missed this as well, and so it was published.
It's pretty embarrassing to learn that our paper was obsolete before it was submitted,
and I didn't realise this for many years.

That being said, I still think this paper is novel and interesting
for its introduction of the "gadget framework",
and for reducing to TQBF instead of the standard reduction to Nondeterministic Constraint Logic,
as was done by Pereira et al.
