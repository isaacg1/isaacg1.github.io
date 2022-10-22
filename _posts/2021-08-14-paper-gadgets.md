---
layout: post
title: >-
  Paper 2: Computational Complexity of Motion Planning of a Robot through Simple
  Gadgets
published: true
---

Next, my second paper: ["Computational Complexity of Motion Planning of a Robot through Simple Gadgets"](/assets/motion-planning.pdf).
This paper was written during my undergrad at MIT with my collaborator
[Jayson Lynch](https://www.linkedin.com/in/jayson-lynch-b6297ab),
then a PhD student at MIT and now a Postdoc at University of Waterloo,
and with [Erik Demaine](http://erikdemaine.org/), his advisor.
[Mikhail Rudoy](https://www.linkedin.com/in/mikhail-rudoy-135a91192)
also contributed to the paper.
We published in FUN 2018.

This paper followed immediately upon my first paper:
["Push-Pull Puzzles are Hard"](/assets/push-pull.pdf).
In that paper, we proved that mazes with with an gadget called a 4-toggle are
PSPACE-complete to solve (extremely difficult).
For comparison, normal mazes with no state-based objects
are NL-complete to solve (extremely easy).

Schematically, a 4-toggle has two states which look like this:

        1           2
     =======     =======
     |     |     |     |
     |---->|     |<----|
     |     |     |     |
     |---->|     |<----|
     |     |     |     |
     |---->|     |<----|
     |     |     |     |
     |---->|     |<----|
     |     |     |     |
     =======     =======

In state 1, any of the pathways can be traversed from left to right.
Doing so flips the 4-toggle into state 2,
where any of the pathways can be traversed from right to left.
Keep in mind that there are only 2 states, so all of the pathways stay in sync.

Note that this gadget is reversible, deterministic,
and restricted to pathways.
From any entrance,
there is at most 1 possible traversal,
that traversal can immediately be undone,
and all of the entrances are paired up.

Our question in this paper is:
Is this gadget as simple as possible, while still making mazes hard?

Well, the first answer is no.
All we used to actually prove the previous result was a simpler object,
called the 2-toggle-and-lock, which we constructed from the 4-toggle:


        1           2
     =======     =======
     |     |     |     |
     |---->|     |<----|
     |     |     |     |
     |---->|     |<----|
     |     |     |     |
     |--O--|     |--X--|
     |     |     |     |
     =======     =======

The first 2 pathways are toggles as in the 4-toggle, but the 3rd pathway
is a lock: Closed in one state, open in one state,
and traversals never affect the state.
For locks, O represents open, and X represents closed.

So we know that 3-pathway gadgets with 2 states can be hard.
The paper asks: Can 2-pathway gadgets with 2 states be hard as well?

There are 4 possible 2-pathway gadgets:
2-toggle (2T), toggle-and-lock (TL), tripwire-and-toggle (WT), tripwire-and-lock (WL)

       2T          TL          WT          WL   
     =======     =======     =======     =======
     |     |     |     |     |     |     |     |
     |---->|     |---->|     |--*--|     |--*--|
     |     |     |     |     |     |     |     |
     |---->|     |--O--|     |---->|     |--O--|
     |     |     |     |     |     |     |     |
     =======     =======     =======     =======

This new pathway, called a tripwire, is always open,
but traversals flip the state.

I've actually skipped a step. The previous paper focused on 3-dimensional space,
giving crossovers for free.
But we usually think of mazes as living in 2 dimensions,
so there are far more possibilities for gadgets.
Specifically, there are 9 possibilities:
Each of the 4 objects can be either crossing or noncrossing,
and the noncrossing 2-toggle can be either parallel or antiparallel.

Our goal is to characterize which of these gadgets is hard.
In other words, for which of the gadgets
is the problem of navigating mazes with a bunch of copies of this gadget
PSPACE-complete?
We show that all of them are hard.
My favorite starting gadget is the parallel 2-toggle,
so I'm going to walk you through the construction
that shows that the parallel 2-toggle (P2T) is hard.
As we go, I'll keep track of how many P2Ts are used to make each successive gadget.

First, we're going to need to construct the other two 2-toggles.
First, the antiparallel 2-toggle (AP2T) construction:

    =====   =====   =====   =====
    |-->|---|<--|---|<--|---|<--|
    |   |   |   | : |   |   |   |
    |   | /-|<--|---|<--|-\ |   |
    |   | : =====   ===== : |   |
    |   | :               : |   |
    |   | : =====   ===== : |   |
    |   | \-|-->|---|-->|-/ |   |
    |   |   |   | : |   |   |   |
    |-->|---|-->|---|-->|---|<--|
    =====   =====   =====   =====

Cost: 6 P2T.

This resulting gadget has two states:
With the central toggles circulating spin-out (counterclockwise, as here)
and spin-in (clockwise).

In this state, the top-left and bottom-right entrances are dead-ends,
so let's focus on the bottom-left and top-right entrances.

From the bottom-left, we can go to the right, cross into the inner loop at the bottom,
go around the loop spin-out, cross out of the inner loop at the top,
and exit at the top-left.
By performing this traversal,
we have flipped the state: The central toggles have all flipped.

From the top-right, the situation is the same - we can traverse to the bottom-right
while flipping the state.
In the other state, we can go back again.

We have thus produced an AP2T.
From the AP2T, we can construct a crossing 2-toggle:

    =====   =====
    |-->|\ /|<--|
    |   | X |   |
    |<--|/ \|-->|
    =====   =====

Cost: 12 P2T.

Here the X represents a 4-way connection, not a locked wire.

We can cross from top-left to bottom-right, and top-right to bottom-left,
both while flipping the state.

Now that we have all 3 kinds of 2-toggle,
we're ready to construct something new:
A noncrossing toggle-lock (NTL):

    /-------------------------------\
    : =====                   ===== :
    \-|-->|-------------------|<--|-/
      |   |         :         |   |
      |   |     /-------\     |   |
      |   |   =====   =====   |   |
      |   |   | : |   | ^ |   |   |
    --|-->|---|-+>|---|-+>|---|<--|--
      ===== : | V |   | : | : =====
            : =====   ===== :
            :   \-------/   :
            :       :       :
            : ===== : ===== :
            \-|-->|---|<--|-/
              |   |   |   |
    ----------|-->|---|-->|----------
              =====   =====

Cost: 33 P2T.

The upper region is collectively the lock,
while the lower pathway is the toggle.
The key point is that the upper pathways of the bottom two gadgets both point in.
This makes the upper region passable, in either direction.
If the lower pathway is toggled,
then those pathways point outward,
making the upper region unpassable.
For more details, see Lemma 4.4 in the paper.

From the NTL and the 2-toggles,
we can create a 2-toggle-lock, which is the object we're looking for to prove hardness!
Of course, we'll also need a crossover,
but we'll cross (ha) that bridge when we come to it.
Specifically, we'll create a "round" parallel 2-toggle-lock.
When it comes to 3-pathway objects, there are two possible geometries for the pathways:

     Round    Stacked
    =======   =====
    | : : |   |---|
    |-/ \-|   |   |
    |     |   |---|
    |-----|   |   |
    =======   |---|
              =====

Here's how we construct the round parallel-2-toggle-lock:

     =====   =======   =======
     |-->|---|\ /->|---|<-\ /|
     |   |   | X   |   |   X |
     |-->|---|/ \->|---|<-/ \|
     ===== : ======= : =======
           :         :
           :  =====  :
           \--|<--|--/
              |   |
     ---------|-O-|------------
              =====

Cost: 58 P2T.

The lowest pathway is clearly a lock.
The upper region is a bit more complicated.
Clearly, there's no way to go through it without
going through the NTL's toggle.
The bottom left entrance
and the bottom right entrance are dead ends.
If we start at the top left,
we can go through the middle C2T,
back through the NTL,
and leave through the bottom left.
Similarly, if we enter through the top right,
we can go through the NTL,
then back through the middle C2T,
and leave through bottom right.

Thus, the middle two gadgets flip to form the other state,
and the construction is complete.

Now we're only a crossover away from hardness.

Next, we're going to construct another 2-toggle-lock:
The stacked antiparallel 2-toggle lock.
Actually, there are 2 different stacked antiparallel 2-toggle locks,
with the lock in the middle and with the lock on the side:

    Middle  Side
    =====   =====
    |-->|   |-O-|
    |   |   |   |
    |-O-|   |-->|
    |   |   |   |
    |<--|   |<--|
    =====   =====

We're going to construct a stacked antiparallel 2-toggle side lock,
as follows:

    ======= =====
    |: :  | | ^ |
    |: \->|-|-+>|-\
    |O    | | : | :
    |:    | ===== :
    |: /->|---/   :
    |: :  |       :
    =======     =====
     : :        | : |
     : \--------|<+-|
     :          | v |
     :          =====

Cost: 82 P2T.

This one's very straightforward,
the character has no options.
The right side can be traversed from top-left to bottom-left,
or from bottom-right to top-right,
in each case flipping the states of all three gadgets.
The left is just a lock.

Now, we can construct our first gadget with a tripwire:
The noncrossing tripwire-lock.
It's very straightforward:

        =====
    ----|-O-|----
        |   |
      /-|-->|-\
    --: |   | :--
      \-|<--|-/
        =====

Cost: 82 P2T.

Now, we're going to construct another 3-pathway gadget, the stacked tripwire-lock-tripwire (SWLW):

        =====   =====
    ----|-*-|---|-*-|----
        |   |   |   |
      /-|-X-|---|-O-|-\
      : ===== | ===== :
    --:       |       :--
      : ===== | ===== :
      \-|-O-|---|-X-|-/  
        |   |   |   |
    ----|-*-|---|-*-|----
        =====   =====

Cost: 328 P2T.

The unlocked states of the SWLW are the ones like the diagrammed state,
where the inner 4 locks are in a checkerboard pattern - this pattern or all flipped.
In this state, the center pathway can clearly be traversed.
These two states are functionally indistinguishable,
and make up the unlocked state of the SWLW.

If the top or bottom pathways are traversed,
now the inner 4 locks are aligned, locked next to locked and unlocked next to unlocked.
As a result, the center pathway is untraversable, as desired.

Now, we're finally ready to make our crossover.
This gadget has a single state,
and it can be traversed top to bottom or left to right, but in no other way.


      =====
    --|-*-|--------------------\
      |   |              ===== |
      |   |       /------|-*-|-/
      |   |       :      |   |
    --|-O-|-----\ : /--\ |   |
      |   |    ======= : |   |
      |   |    |: : :| : |   |
      |   |    |* O *| : |   |
      |   |    |: : :| : |   |
      |   |    ======= : |   |
      |   |  /--/ : :  : |   |
      |   |  :    : :  : |   |
      |   |  :  /-+-/  : |   |
      |   |  :  : :    : |   |
      |   |  :  : : /--/ |   |
      |   |  : =======   |   |
      |   |  : |: : :|   |   | 
      |   |  : |* O *|   |   | 
      |   |  : |: : :|   |   | 
      |   |  : =======   |   |  
      |   |  \--/ : \----|-O-|--
      |   |       :      |   |
    /-|-*-|-------/      |   |
    | =====              |   |
    \--------------------|-*-|--
                         =====
Cost: 1312 P2T!

I know this looks complicated, but it's not so bad.
There's two pathways: From top left to bottom right,
and from middle left to middle right.
In both cases, we go straight at the center intersection.
The only danger is that it might be possible to turn at the middle intersection.
The locks are there to prevent this.

If we enter from the top left,
we close both of the outer two locks before we get to the center intersection.
This means that a turn at the center is blocked off, as desired.
Then, we open the outer two locks again on the way out, through their other tripwires.

If we enter from the middle left,
we close both of the inner two locks before we get to the center intersection,
again blocking off a turn in the center.
Again, we open the inner two locks on the way out through the other tripwires.

And that's it! We know that crossover + two-toggle-lock is PSPACE-complete,
so P2Ts are PSPACE-complete as well.

Retrospective
---

I liked this paper quite a bit. It felt like we said something pretty fundamental about the
complexity of "Walking around in stateful mazes",
which I thing is a pretty general paradigm.
We covered the gadgets that are reversible, deterministic and on pathways with at most 2 states.
This was generalized even further to an arbitrary number of states
by Erik Demaine, Dylan Hendrickson and Jayson Lynch in
["Toward a General Complexity Theory of Motion Planning: Characterizing Which Gadgets Make Games Hard"](https://drops.dagstuhl.de/opus/volltexte/2020/11747/), which was published in ITCS 2020.
In Chapter 2, they analyze all k-state gadgets, and characterize which ones are in NL (easy),
versus PSPACE-complete. They do so by a much simpler approach.
Their fundamental gadget is the locking 2-toggle, which is a 3-state object:

      1        2        3  
    =====    =====    =====
    | 3 |    |   |    | 1 |
    |<--|    |   |    |-->|
    |   |    |   |    |   |
    |   |    |<--|    |-->|
    |   |    | 3 |    | 2 |
    =====    =====    =====

They show any nontrivial gadget can construct this one, and this one is PSPACE-complete,
with crossovers.

Their reduction is via Nondeterministic Constraint Logic, naturally.
In my opinion, this construction is a lot less interesting, because the character
isn't really moving around the maze. The character always has access to all the
NCL gadgets, and just flips them around as needed to solve the NCL puzzle.
This is in contrast to our TQBF construction,
where the character goes through a global cycle an exponential number of times,
and updates one quantifier and solves one SAT problem each cycle.

That being said, it's a much cleaner construction than the one in this paper - less overhead,
far more general, etc.
I wish we'd found it for this paper.
It's a shame that this paper's focus on 2-state gadgets
blinded us to a much simpler result based on a 3-state gadget.

Of course, this doesn't cover crossovers.
To get crossovers, they construct parallel, antiparallel and crossing locking 2-toggles
(they assume free reflections),
using essentially the same constructions as the 2-toggle constructions in this paper.
They use this to construct an object they call an A/BA crossover,
which allows onetime crossing either of A or of B then A, where A and B are its two pathways.
I would call this a "toggle-locking-toggle".
Their construction is sufficient for the simpler movement of the NCL problem,
and it would not be sufficient for the TQBF construction.

In the end, we can rest easy, case closed.
Unless we  want to consider problems that aren't on pathways. Or aren't deterministic.
I think I'll keep reversible.
I'm happy with contributing to this line of work.
It was a good kind of undergraduate research.

Interesting future problem
---

All of this work was inspired by PushPull-1 with fixed walls.
What if there were no fixed walls, just blocks?
Let's assume that we're given a finite subset of the plain which is empty squares,
and the rest of the world is blocks.

If the character can construct a 2x3 empty space, the character can move anywhere.
Let "o" represent an empty space. Let "#" be a fixed reference point, so we can see movement.

    #ooo    #ooo    # ooo    # ooo
     oo  ->  ooo ->  ooo  ->   oo
     o                         o

This allows movement in any direction, by symmetry.
Since there are no fixed blocks, the movement will never end,
and so in this case, the problem of reaching any location reduces to constructing
a 2x3 rectangle.

Of course, there's no guarantee that it'll ever be possible to make a 2x3 rectangle.

Suppose that to start with, all empty spaces had at least one coordinate equal to 0 mod 3.
There's no way for this to ever change, and so there's no way to ever make a 2x3 rectangle.
Let's call the problem with this restriction "PushPull-1-div3":

With this restriction,
only a finite subset of the infinite plane can be accessed.
No square that is not orthogonally in line with a starting square can be accessed.
No square whose x coordinate exceeds all starting x coordinates by more than the number of starting squares can be accessed.

So PushPull-1-div-3 is space-bounded, and hence in PSPACE.
Is it PSPACE-complete? In NL? Something in between?
Honestly, I wouldn't be too surprised with any of the three answers.
