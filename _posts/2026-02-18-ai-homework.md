---
published: true
title: "Can Current LLMs Answer University-Level Questions? (No)"
layout: post
---

There's an ongoing debate in the world of teaching over whether LLMs
are an effective educational tool.
Whether it is pedagogically appropriate to encourage students to use LLMs,
either like a textbook, as a source of presumed-accurate information,
or to teach students to use LLMs as a tool to completing a given task
in lieu of teaching students to complete that task.

Both of these use cases presume two key assumptions:

1. That the LLM will typically provide correct answers to the questions that arise in the course of university-level classes, and
2. That if the LLM provides an incorrect answer, even a student who doesn't yet understand the material will be able to tell that the answer is incorrect.

I am currently teaching two courses: Stochastic Processes 1 (IEMS 460-1), a 1st-year core PhD course, and Advanced Queueing Theory (IEMS 464), a 2nd-year special-topics PhD course.

I'm going to show you one question and one response for each class.
I want you, the reader, to try to figure out which response(s) are correct,
and which response(s) are incorrect,
to see if you can tell apart correct and incorrect answers.
After you've decided which are which, please read on, and I will give an overall correct or incorrect, as well as a specific assessment of the points made in the response.

**Note:** Currently, I only use LLMs when re-evaluating my current decision not to use them.

## Question from Stochastic Process 1 (1st-year PhD course)

This a question from the midterm I just gave in the class:

<hr>

Query:

This is a question I'm testing out for a class I'm running. Please solve part (b).

Ama and Bol are walking around town, each according to their own walking style. This town is laid out as an infinite square grid, roads running north-south and east-west. Each intersection has a pair of coordinates (x, y). These coordinates indicate that the (x, y) intersection is x blocks north and y blocks east of the town center.

Define An to be the coordinates of the nth intersection that Ama visits, and define Bn to be the coordinates of the nth intersection that Bol visits. Both start at town center, so A0 = B0 = (0, 0). Both {An} and {Bn} are discrete-time stochastic processes.

(b) Each time Bol reaches an intersection, he doesn’t pause. He picks either left, right, or straight ahead. Based on his choice, he either turns left at the intersection, turns right, or continues straight ahead. In any case, he proceeds to the next intersection in the direction he has chosen. He picks among these three options uniformly at random, i.i.d. Bol approaches his starting intersection, B0 = (0, 0), from the north.

Does Bol’s stochastic process {Bn} form a discrete-time Markov chain? Prove your answer is correct.

<hr>

Response (ChatGPT 5.2-Instant):

Yes — **the coordinate process ({B_n}) *does* form a discrete-time Markov chain.**

### Key idea

Although Bol’s rule is phrased in terms of “left / right / straight”, which depends on the direction he was traveling just before reaching the intersection, that direction is actually determined by the last two positions. Hence the distribution of the next position depends only on the present coordinate (B_n), not on the entire earlier history.

We formalize this below.

---

### Step 1: What must be checked

A process ({B_n}) is Markov if for every (n) and all lattice points (b_0,...,b_n,b_{n+1}),

    Pr(B_{n+1}=b_{n+1} | B_n=b_n , B_{n-1}=b_{n-1}, ..., B_0=b_0)
    = Pr(B_{n+1}=b_{n+1} | B_n=b_n).


So we must show the conditional distribution of the next intersection depends only on the current one.

---

### Step 2: Observe that Bol never backtracks

At each intersection Bol chooses:

* left,
* right,
* straight,

relative to the direction from which he arrived.

None of these options sends him back along the road he just used.
Hence

    B_{n+1} != B_{n-1} for all n >= 1.

So once Bol leaves the origin, he **never revisits any intersection**.
Therefore every visited coordinate occurs at most once in the sequence.

---

### Step 3: The incoming direction is determined by the current coordinate

Because no intersection is ever revisited, if we know the present location (B_n=(x,y)), then:

* there is exactly one neighbor from which Bol must have arrived,
* therefore his incoming direction at (B_n) is uniquely determined.

In other words, the current coordinate already encodes which road he entered on.

Thus the three possible outgoing neighbors (left/right/straight relative to that incoming direction) are uniquely determined by (B_n).

---

### Step 4: Transition probabilities depend only on (B_n)

Given the current intersection (B_n),

* exactly three neighboring intersections are feasible next steps,
* Bol chooses among them uniformly.

Hence for those three neighbors (z),

    Pr(B_{n+1}=z | B_n) = 1/3,

and all other points have probability (0).

Because this distribution is completely determined by (B_n), the Markov property holds:

    Pr(B_{n+1} | B_n, B_{n-1}, ..., B_0)
    = Pr(B_{n+1} | B_n).

---

### Step 5: Initial step

The first step is also determined:

* Bol approaches ((0,0)) from the north,
* so his initial incoming direction is southbound,
* hence the three possible first moves are fixed, each with probability (1/3).

This again depends only on (B_0).

---

### ✅ Conclusion

    Bol’s coordinate process B_n is a discrete-time Markov chain.

The reason is that Bol never revisits intersections, so the direction from which he entered the current intersection — and therefore the distribution of his next move — is uniquely determined by the current state alone.

---

If you want, I can also show:

* **Why many students incorrectly think it is *not* Markov**, and
* **How to construct the “expanded-state” Markov chain that explicitly includes direction**

(these are great teaching points for a stochastic processes class).

<hr>

That's the end of the response. Please reflect on whether you think this answer is right or wrong. If you're unfamiliar with the material, put yourself in the shoes of an uncertain student who has been recommended to use the LLM by their teacher. 

Once you're done pondering, let's turn to our second class.

## Question from Advanced Queueing Theory (2nd-year PhD course)

This is a simplified version of a question from one of the homeworks.

<hr>

Query:

Consider a coupled pair of queueing systems: an M/G/1/SRPT system and a M/G/k/SRPT system, both with total service rate 1 and arrival processes coupled to be identical. Let `W_<=x^1` be the total remaining size of all jobs with remaining size at most x in the 1-server system, and `W_<=x^k` be the same r.v. in the k-server system, both in stationarity. What is the supremum of the support of `W_<x^k-W_<x^1`? Justify your answer.

<hr>

Response (ChatGPT 5.2-Instant):

Let the two systems be coupled on the same arrival sequence and job sizes.
Both use **SRPT** (shortest-remaining-processing-time). The single–server system has rate (1); the (k)-server system has total rate (1) (so each server works at rate (1/k)).

For a fixed threshold (x>0), define

    W_{<=x}^1, W_{<=x}^k

as the total remaining work of jobs whose remaining sizes are (<=x).

We want the supremum of the support of
    \Delta_x = W_{<=x}^k-W_{<=x}^1.

---

### 1. A universal upper bound: (\Delta_x <= (k-1)x)

Order the jobs (at any time (t)) by increasing remaining size:

    r_1 <= r_2 <= r_3 <= ...

Under SRPT:

* the **M/G/1** system serves only job (1);
* the **M/G/k** system serves jobs (1, ... ,k).

Because both systems have identical arrivals and total rate (1),

* the single server concentrates the whole rate on the smallest job,
* the (k)-server system spreads the rate over up to (k) jobs.

Hence, compared at the same time, the only way the (k)-server system can have *more* small-job work is that some jobs have already completed in the 1-server system but are still unfinished in the (k)-server system.

Call such jobs **lagging jobs**.

---

#### Key observation

At any time, there can be **at most (k-1)** lagging jobs.

Why?

* If (k) jobs were unfinished in the (k)-system but already completed in the 1-system,
* then earlier the single server must have processed at least (k) different jobs fully,
* while the (k)-system was simultaneously working on at most those same (k) smallest jobs.
* Because total service rates are equal, the cumulative service given to the smallest (k) jobs cannot be smaller in the (k)-system by more than the work of at most (k-1) jobs.

Intuitively:

> the only discrepancy comes from the fact that one system works on 1 job at a time while the other splits effort among (k) jobs.

Thus the extra unfinished jobs in the (k)-system relative to the 1-system is at most (k-1).

---

Each such lagging job contributes at most (x) to (W_{<=x}).

Therefore,

    W_{<=x}^k-W_{<=x}^1 <= (k-1)x.

So the support is contained in

    (-\infty,(k-1)x].

---

### 2. Achievability: values arbitrarily close to ((k-1)x)

We now construct sample paths where the difference approaches ((k-1)x).

#### Construction idea

1. At time (0), release (k-1) jobs each of size exactly (x).
2. Release one tiny job of size (\varepsilon).

Under SRPT:

* Both systems first process the tiny job.
* After that:

  * In the **M/G/1** system
    the full rate (1) works on one (x)-job at a time, finishing them sequentially at times
    x, 2x, ..., (k-1)x.

  * In the **M/G/k** system
    the (k-1) large jobs are processed simultaneously, each at rate (1/k).

---

#### Look just after time (x)

* In the 1-server system:

  * the first large job has completed,
  * remaining (k-2) jobs still exist.

* In the (k)-server system:

  * all (k-1) jobs remain unfinished,
  * each still has size (x(1-1/k)).

All these sizes are (<=x).

Hence

    W_{<=x}^{k} ~= (k-1)x(1-1/k), W_{<= x}^1 ~= (k-2)x.

The difference is

    x[(k-1)(1-1/k)-(k-2)] = x[1-(k-1)/k]

Not yet maximal—but we can repeat this idea with a longer sequence of jobs arranged so that:

* the 1-server finishes many jobs completely,
* the (k)-system still has those same jobs unfinished and each still close to size (x).

By taking a block of (k-1) jobs all of size arbitrarily close to (x), released sufficiently far in the past, and inserting a stream of slightly smaller jobs to keep SRPT priorities arranged appropriately, we can produce times where

* those (k-1) jobs have already completed in the 1-server system,
* while in the (k)-server system they are all still unfinished with remaining sizes arbitrarily close to (x).

Thus

    W_{<=x}^{k}-W_{<=x}^{1} >= (k-1)(x-\delta)

for arbitrarily small (\delta>0).

Hence values arbitrarily close to ((k-1)x) occur with positive probability in stationarity.

---

### 3. Final conclusion

Combining:

* universal upper bound (\Delta_x<=(k-1)x),
* attainability arbitrarily close to ((k-1)x),

we obtain

    sup supp(W_{<=x}^k-W_{<=x}^1) = (k-1)x

---

If you'd like, I can also give:

✅ A **short 4-line intuitive proof** suitable for lecture notes

✅ A **fully rigorous coupling argument** using SRPT work conservation

✅ A **diagrammatic explanation** showing how the (k-1) extra unfinished jobs arise

Tell me which version you'd like next.

<hr>

That's the end of the response.
Once again, please reflect on whether you think this answer is right or wrong.
Again, if you're unfamiliar with the material, put yourself in the shoes of an uncertain student who has been recommended to use the LLM by their teacher. 

Once you're done pondering, let's get some extra information.

## Additional information available to an uncertain student

If a student isn't sure whether an LLM is reliable for a given topic, there's a few ways they could gather additional information. One option is to run the LLM repeatedly, and see if the answer is consistent. The version of ChatGPT I'm testing here makes 10 queries available for free every 5 hours, so I ran each query four times to see if the answers were consistent at a high level.

For the first query (IEMS 460-1, 1st-year PhD), every response started with "Yes, Bol's stochastic process is a DTMC", as in this response. However, in two of the responses, the high-level answer stayed consistent throughout the response, as shown here, sticking with "Bol's Stochastic process is a DTMC" by the end of the response. In the other two responses, the high-level answer flipped by the end of the response, finishing with "Bol's stochastic process is not a DTMC".

With this additional information, do you have a better sense of whether this answer is correct or incorrect?

For the second query (IEMS 464, 2nd-year PhD), three of the four responses had the same high-level answer of a supremum of (k-1)x for the difference in total remaining size, while the fourth response had a high-level answer of x. No answers flip-flopped.

With this additional information, do you have a better sense of whether this answer is correct or incorrect?

One final piece of information that might help an uncertain student guess if this answer is correct or incorrect:

In the answer, the response used the notation \Delta_x for the difference in total remaining size between the two systems. That notation wasn't in the query: It was introduced by the response. It comes from some information that the LLM has access to. I know why it uses this notation: I introduced the \Delta_x notation in my paper ["SRPT for Multiserver Systems"](/publications/#srptk), and more specifically the 3-page work-in-progress paper at the MAMA 2018 workshop. This was my first queueing paper, so I remember the details well. This paper was the first to ever use the \Delta_x notation for this difference.

Since then, I've always used \Delta_x for this quantity, including in my 464 class. A student who sees this notational choice can be confident that the LLM had access to something I wrote when generating this answer. Moreover, whenever I use the \Delta_x notation, it's in the context of giving a correct rigorous answer to this very question - this is the question that is answered by the lemma in which I invented this notation.

With this additional information, do you have a better sense of whether this answer is correct or incorrect?

Make up your mind now, because I'm about to reveal the answers to both questions. Please firmly lock in your assessment for each question:

* LLM is correct,
* LLM is incorrect, or
* LLM is unreliable.

Which do you think? Is this based on direct knowledge of the material, or just going off side indicators? Did your assessment change with the additional information (more samples, notational choice?)

## The correct answers

I'm putting a little bit of padding to decrease the chance of an accidental spoiling of the answer.

This is padding.

This is also padding.

This is correct padding.

This is incorrect padding.

This is unreliable padding.

Once you write a word frequently enough,

like "padding",

it ceases to feel like a word,

and feels more like a collection of sounds.

Padding.

Alright, let's reveal the answer: For both the Stochastic Processes 1 (IEMS 460-1) question and the Advanced Queueing Theory (IEMS 464) question, the LLM got it completely wrong. Not just wrong in the sense of missing proof rigor, which was certainly the case, but wrong in the sense of a wrong high-level answer. I'll give more detailed breakdowns of the problems with the responses, the gaps in the proofs, but let's start with the high-level answers.

For the Stochastic Processes 1 question, the correct answer was that the stochastic process is not a DTMC. It's fairly straightforward to write down a counterexample to the Markov property:

    P(X_3 = (-1, 0) | X_2 = (-1, 1), X_1 = (-1, 0), X_0 = (0, 0)) = 0
    P(X_3 = (-1, 0) | X_2 = (-1, 1), X_1 = (0, 1), X_0 = (0, 0)) = 1/3

The difference in probability is due to the fact that Bol cannot backtrack: `X_3` cannot match `X_1`.

In the four overall trials, the LLM answered the high-level yes-or-no question correctly twice, exactly the same as the average result with random guessing.

For the Advanced Queueing Theory question, the correct answer is that the supremum of possible values of the difference in total relevant size between the two systems is `kx`, not `(k-1)x` or `x`, which were the claimed answers in 3 and 1 of the responses, respectively. A sample path matching that `kx` value:

At time 0, k jobs of size `kx/(k-1)` arrive to both systems.
Consider the difference at time `kx/(k-1)`.
At this time, in the single-server system 1 job has just completed,
while in the k-server system all k jobs have just reached remaining size x,
owing to the 1/k speed of each server in the k-server system.
As a result, the difference at time `kx/(k-1)` is `kx`.

So, how were your assessments? Did you correctly guess that the LLM was incorrect in both instances?

## Point-by-point tear-down of response to Stochastic Processes 1 question

I'm going to go through the answer and discuss all of the ways in which is was wrong.

First, the use of formatting is atrocious. There's entirely too much bolding, random italics, bullet points are not used intentionally, there's random emoji. This is not a sign of a well-put together answer, though it's not incorrect in itself.

I'll now start quoting parts of the answer, with my commentary below each part.

    Yes — the coordinate process ({B_n}) does form a discrete-time Markov chain.

As I said up front, this answer is wrong, I gave a counterexample.
Let's see what the (incorrect) argument is.

    Although Bol’s rule is phrased in terms of “left / right / straight”, which depends on the direction he was traveling just before reaching the intersection, that direction is actually determined by the last two positions.

This is enough information to determine that the correct answer is no, `{B_n}` does is not a DTMC. A DTMC must be determined by the single last position, not the last two. So this sentence contradicts the answer above.

    Hence the distribution of the next position depends only on the present coordinate (B_n), not on the entire earlier history.

Alas, the very next sentence flips back again, now claiming that the next position only depends on the present position, not the last two.

    We formalize this below.

When you've already contradicted yourself twice in three sentences, formalizing isn't necessarily going to help.

    Step 1: What must be checked

This section is an (accurate) recitation of the definition of a Markov chain. This might seem trivial, but in the Advanced Queueing Theory case it can't even manage to recite a statement from a document that it cleared was trained on, so it's not automatic.

    None of these options sends him back along the road he just used. Hence B_{n+1} != B_{n-1} for all n >= 1.

This line correctly states the no-backtracking property which was at the core of the counterexample I gave above. This could be part of a valid counterexample.

    So once Bol leaves the origin, he never revisits any intersection. Therefore every visited coordinate occurs at most once in the sequence.

And alas again, the answer immediately goes wrong again. The no-backtracking property stated above correctly states that Bol can't revisit an intersection after two steps. But on this line, that's transmuted into a claim that Bol can never revisit anywhere, which is just false: Bol can go around a block, turning left three times, and end up where he started.

    Step 3: The incoming direction is determined by the current coordinate

This section is more nonsense built off of the final line of the last section, which itself was nonsense.

    Because no intersection is ever revisited, if we know the present location (B_n=(x,y)), then: there is exactly one neighbor from which Bol must have arrived, therefore his incoming direction at (B_n) is uniquely determined.

This reasoning does not follow. "No revisiting" is a separate property from "unique predecessor", and neither implies the other.

Consider a path that, if the current direction is west, randomly chooses between straight and right, if the current direction is north randomly chooses between right and left, and if the current direction is east randomly chooses between left and straight. This path with zig-zag back and forth in the east-west direction, but always progressing towards the north. It will never revisit a position on any sample path. But it does not have unique predecessors: Each position can be visited from the west, east, or south.

    Step 4: Transition probabilities depend only on (B_n)

The argument now progresses with this "unique predecessor" nonsense, which is the nonsense that's necessary to justify the original answer, rather than realize it was wrong.

There's another few paragraphs, but no new material, and it ends with complete confidence in its false conclusion.

## Point-by-point tear-down of response to Advanced Queueing Theory question

Once again, I'll just mention off the bat that the formatting is terrible. Too much bold, too much bulleting, random line quotes, random emojis. It shows a lack of care and intentionality, skills that are essentially for answering these sorts of questions correctly.

Now, into the line-by-line breakdown.

Let's skip the restatement of the question. The first fresh material is:

    1. A universal upper bound: (\Delta_x <= (k-1)x)

As before, the first nontrivial statement is the crucial wrong answer, and it will spend the rest of the response justifying that crucial wrong answer.

    Order the jobs (at any time (t)) by increasing remaining size: r_1 <= r_2 <= r_3 <= ...

This notation is introduced only to be immediately discarded and never used again. It's just padding.

The next non-fluff sentence is:

    Hence, compared at the same time, the only way the (k)-server system can have more small-job work is that some jobs have already completed in the 1-server system but are still unfinished in the (k)-server system.

This is nonsense. There are several other ways that the k-server system can have more small-job work. For one, jobs can have remaining size >x in the 1-server system and <=x in the k-server system. For another, jobs can have remaining size <=x in both systems, but a larger remaining size in the k-server system. This is just silly.

    Call such jobs lagging jobs.

Now we've given a name to our silly nonsense that isn't useful.

    Key observation: At any time, there can be at most (k-1) lagging jobs.

This is not true. It's very straightforward to generate an unbounded number of lagging jobs. There's a good example in the worst-case paper that preceded my stochastic paper, "Approximating total flow time on parallel machines" by Leonardi and Raz, 1997. That example is also given in chapter 24.3 of the [Performance Modeling](https://www.cs.cmu.edu/~harchol/PerformanceModeling/book.html) textbook by Mor Harchol-Balter, which I use in both of my classes. These examples show that the difference in total remaining size can be spread out over an unlimited number of jobs, and all of those jobs can be what the LLM calls "lagging jobs".

    Why?

    If (k) jobs were unfinished in the (k)-system but already completed in the
    1-system, then earlier the single server must have processed at least (k)
    different jobs fully, while the (k)-system was simultaneously working on
    at most those same (k) smallest jobs. Because total service rates are equal,
    the cumulative service given to the smallest (k) jobs cannot be smaller
    in the (k)-system by more than the work of at most (k-1) jobs.

This is the kind of vague, intuitive argument that is frequently wrong. In this case, the problem is the assumption that the jobs arrive all at the same time, so that all k are available to be served in the k-server system during any of the time when any of the k jobs are serving in the 1-server system.

In fact, in the counterexamples mentioned above, each job only arrives once the previous job in the 1-server system is complete.

Let's fast-forward through the problem to the sample-path construction side of things.

    Construction idea: At time (0), release (k-1) jobs each of size exactly (x).
    Release one tiny job of size (\varepsilon).

This sample path will never achieve a difference of (k-1)x, unless k=2. With no more jobs arriving, the difference will be maximized at time (k-1)x, with a difference of just under x.

    Look just after time (x)

The LLM doesn't pick the time that maximizes the difference

    The difference is x[(k-1)(1-1/k)-(k-2)] = x[1-(k-1)/k]

and the difference achieved is x/k (written complicatedly), far far away from the desired target, or the true upper bound.

    Not yet maximal—but we can repeat this idea with
    a longer sequence of jobs arranged so that:
    the 1-server finishes many jobs completely,
    the (k)-system still has those same jobs unfinished
    and each still close to size (x).

Again, switching to vague, intuitive, frequently-wrong arguments.

    By taking a block of (k-1) jobs all of size arbitrarily close to (x),
    released sufficiently far in the past, and inserting a stream
    of slightly smaller jobs to keep SRPT priorities arranged appropriately,
    we can produce times where

    those (k-1) jobs have already completed in the 1-server system,
    while in the (k)-server system they are all still unfinished
    with remaining sizes arbitrarily close to (x).

It's just stating the conclusion it's previously committed to, and declaring that things work out, with no actual proof.

The rest is again worthless fluff.

And I want to emphasize again: The correct answer was in the training set! Right next to the notation \Delta_x, which it surfaced! And yet, it couldn't even regurgitate that answer properly, much less solve something new.

## Conclusion

LLMs have no place in the classroom. An uncertain student cannot differentiate a correct answer from an incorrect answer, not when both are stated with complete confidence and similarly poor justifications. And LLMs are not remotely reliable, or even typically-correct, for the questions that typically arise in these classes. Do not use them -- I tell every student not to use them, and I beseech my faculty colleagues to avoid them as well.
