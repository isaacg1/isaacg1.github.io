---
published: true
layout: post
title: 'Entropy is not the Arrow of Time'
---
If you're curious about physics and science and so forth,
you might wonder: "what is time, really? Why does it always go forward?"
This is particularly mysterious, because the laws of physics are reversible,
on a particle-physics level:
They work just as well forward as backwards.
Particle-antiparticle pairs can be created from energy,
and they can annihilate into energy.
There is no fixed direction of time in the laws of physics.
Just looking at the underlying laws,
forward in time and backward in time are indistinguishable.

If you go looking a bit further,
you might hear about [Entropy as the Arrow of Time](https://en.wikipedia.org/wiki/Entropy_as_an_arrow_of_time): The idea that entropy always increases as you move forward in time.

What is entropy?
It's a measure of disorder.
In a system, there are few, rare states that are ordered, and these have low entropy.
Most typical states are disordered, and have high entropy.
And the system undergoes some random evolution over time.

You might hear the claim that entropy always increases.
But that "always" is more like a "very, very usually".
If you have a simple enough system, entropy will decrease sometimes,
just from random chance.
If your system is more complicated,
that decrease is possible, but so rare that you can't measure it.

So is this it? Rising entropy is common, falling entropy is rare, arrow of time?

Well, it's a little more complicated. To see why, let's set up a stochastic model where we can watch entropy rising and falling over time.

### Stochastic model

In this model, there are 5 balls, and 10 possible locations for those balls, arranged in a line. On each time step, a pair of neighboring locations are selected, uniformly at random. If one has a ball and the other doesn't, we'll move that ball from one location to the other.
Note that this is reversible: The chance of any state change is the same as the reverse state change.

Our measure of entropy (disorder) will be the number of alternations between balls and empty spots. The most ordered states, all the balls on the left (`BBBBB_____`) and all the balls on the right (`_____BBBBB`) will have 1 alternation, while a typical disordered state
might have 5 alternations (`__BB_BBB_`).

Let's set up our system in a low-entropy, highly-ordered state,
and run our system forward for 100 steps.
I'll do this 100,000 times and record the average entropy after each number of steps.

All of my code is available [in this repository](todo) if you want to adapt it. I'm currently talking about the `sim_start` function.

Here's what we get:

![todo](/assets/entropy/entropy-start.svg)

This is what people mean when they claim "entropy is the arrow of time" - look, the entropy is increasing as time goes forward!

But this isn't really fair - we didn't give backward in time a chance! It's not even on our plot! We're not even giving backward in time a chance to go up in entropy!

So let's add backward in time to our plot.

To do this, we'll initialize our system by sampling its initial state from its stationary distribution, which is just the state where all possible states are equally likely.
This is in the `sim_low` function in [the same repository](todo).

I'll run the system for 10,000 steps, which is enough time that we'll usually encounter all states, including the minimum entropy states, at least once. After all, there's only `10 choose 5 = 252` possible states.

Then, out of all the time spent in the minimum entropy states,
we'll sample one visit to those states uniformly at random,
to see what a typical visit to a minimum entropy state looks like.
We'll record the average entropy just before visiting a minimum entropy state,
and just after visiting it, and average over 100,000 runs.

And if entropy is really the arrow of time, this plot should be asymmetrical: Entropy forward in time from a minimum entropy state should behave differently from entropy backward in time from a minimum entropy state.

![todo](/assets/entropy/entropy-middle.svg)

Look at that! Entropy is symmetrical with respect to time!
If we start at an average visit to a minimum entropy state,
then whether we go forward or backward in time,
entropy rises along exactly the same curve!

Because entropy is just one measure of the behavior of a system,
and just like all other measures of the behavior of a system with reversible evolution,
it's reversible in time.

Entropy is not the arrow of time - it can't tell forward and backward in time apart!

### So why do people think of entropy as being the arrow of time?

The thing is, we often run simulations and experiments
where we start the experiment in low-entropy states.
We rarely run simulations and experiments that are low-entropy in the middle,
like the one I just ran above,
or low-entropy at the end.

This is because if we're setting up an experiment,
where in code or in the real world,
it's easy to set it up in a low-entropy state,
but it's hard to end it in a low-entropy state.
To set it up in a low entropy state,
we can use tools that are outside the system:
Writing the state of the system directly in code,
or producing the initial configuration in some other way in reality.

To end in a low-entropy state, or measure a low-entropy state in the middle,
we just have to wait and get lucky.
For this simulation, we're not waiting that long, because the system is so small:
These two simulations take 0.8s and 32s, respectively, to run.
But as we add more particles, waiting and getting lucky
just takes too long to run those experiments.
So we just have to imagine them - we can't run them.

So now we can see what direction entropy really increases:
Away from the part of the experiment we can control
(the starting, low entropy part of the experiment).

And thus we see a different interpretation of the arrow of time:
We can control the start of an experiment easily,
we can't control the end without getting lucky which takes way too long.
That's the real arrow of time.
Entropy is just a proxy.


