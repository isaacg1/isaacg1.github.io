---
published: true
title: 'ChatGPT on Probability'
layout: post
---
[ChatGPT](https://chat.openai.com/) is a new natural-language-generation ML program.
Its training goal is to predict
the most likely human response to the question asked.
It is much better at this task than past programs,
particularly when it comes to mimic the form and style of human answers.

People are already trying to use ChatGPT to [cheat on university assignments](https://acoup.blog/2023/02/17/collections-on-chatgpt/).
I've recently read a couple of posts about how well ChatGPT
performs at answering university-level questions,
both factual and essay-writing assignments,
in the field of ancient history
([ACOUP](https://acoup.blog/2023/02/17/collections-on-chatgpt/),
[TOTF](https://talesoftimesforgotten.com/2023/02/19/chatgpt-is-impressive-for-an-ai-but-not-for-a-human/)).
ChatGPT performs atrociously at these tasks.
Its responses would receive failing grades
due to severe factual mistakes,
despite its ability to successful replicate the form of a typical submission.

I wanted to explore ChatGPT's generation capability on university-level assignments
in a class that I might teach, probability.
I evaluated ChatGPT on two novel probability questions that I invented for this post.
It is important to ask questions that have not appeared frequently in ChatGPT's training set
to get an accurate estimate of its generation capacity.

## Basic Markov chain

My first question was:

> Consider the following Markov chain: The states are the integers [0,4].
> At each step, transition by 1 in either direction with equal probability,
> except from 0 always go to 1, and from 4 always go to 3.
> Is this an ergodic Markov chain? What is its steady state probability distribution?

First, let me tell you the correct answer:
To be ergodic, a Markov chain must be irreducible and aperiodic.
This is not an ergodic Markov chain,
because it is periodic:
From any state,
the process can only return to that state in an even number of steps.
For instance, from state 1, we can return to state 1 in 2 steps with a sequence such as 1 to 2 to 1,
or 4 steps, or 6, etc.

To be completely accurate, I should have asked for the *stationary* distribution,
 not the steady state distribution. Because the chain is not ergodic,
 it will not necessarily converge to a steady state.
That being said, this imprecision didn't affect anything that follows.

To solve for the stationary distribution,
we can set up the balance equations,
where we equate the probability of being in each state to the probability of
having transitioned to that state on the most recent transition:

    p0 = p1/2, p1 = p0 + p2/2, p2 = p1/2 + p3/2, p3 = p2/2 + p4, p4 = p3/2

To solve this, we can notice that states 0 and 4 are symmetrical, as are 1 and 3.
As a result, `p0 = p4, p1 = p3`.
From the balance equations, we can derive the relations `p1 = 2 p0, p2 = p1 = p3`.
Using the fact that the total probability is 1,
we can find the stationary distribution:

    p0 = p4 = 1/8, p1 = p2 = p3 = 1/4.

Now, let's look at ChatGPT's response.
To capture the possibility of the program getting lucky or unlucky in its response,
I reran the program on the same input 4 times.
I broke up ChatGPT's response into segments for readability.

> To determine if a Markov chain is ergodic, we need to check if it is both irreducible and aperiodic.
> 
> Irreducibility means that it is possible to get to any state from any other state. In this case, since we can go from any state to any other state by moving one step at a time, the Markov chain is irreducible.
>
> Aperiodicity means that it is not stuck in a repeating pattern. In this case, it is clear that the chain is aperiodic since any state can be reached from any other state in a finite number of steps, and the chain does not have a repeating cycle.
>
> Therefore, the Markov chain is ergodic.

ChatGPT correctly recites the definitions of "ergodic", "irreducible", and "aperiodic".
It then falsely claims that the chain does not have a repeating cycle,
getting this part of the answer wrong.
Over the 4 runs, it got this step right once.

> To find the steady state probability distribution, we need to solve the system of equations:
>
    πP = π
>
> where P is the transition probability matrix and π is the steady state probability distribution.
>
> The transition probability matrix is:
>
    [1/2 1/2  0   0   0 ]
    [1/2  0  1/2  0   0 ]
    [ 0  1/2  0  1/2  0 ]
    [ 0   0  1/2  0  1/2]
    [ 0   0   0   1   0 ]
>
> We can set up the equations as follows:
>
    π0 = 1/2 π1
    π1 = 1/2 π0 + 1/2 π2
    π2 = 1/2 π1 + 1/2 π3
    π3 = 1/2 π2 + 1/2 π4
    π4 = π3
>
> We also know that the probabilities must add up to 1, so we can write:
>
    π0 + π1 + π2 + π3 + π4 = 1

ChatGPT now tries to set up a system of equations
to solve for the steady state probability distribution, which is the right next step.
Its transition probability matrix is incorrect --
the first line includes both a transition from 0 to 0, as well as 0 to 1.
It's also pointless to include both a transition probability matrix
and a system of equations.
Just the system of equations is sufficient when solving by hand,
and either one is sufficient when solving via computer.

Its balance equations are wrong -- it appears to be setting up one equation per row,
which is equivalent to using the forward transition probabilities,
when it should be setting up one equation per column, using the reverse transition probabilities.
This is a common beginner mistake in solving Markov chains.

Even given that it's attempting the wrong task,
the system of equations doesn't match the transition matrix --
the first equation has one term on the right hand side,
when the corresponding row of the transition matrix (incorrectly) has two entries in that row.
If the matrix had been correct, the single entry would have been a 1,
so the equation given still would be wrong,
even ignoring the fact that it should be using columns, not rows. 

Over the 4 runs, ChatGPT never got this step correct
for either the transition matrix or the balance equations.

ChatGPT now generates a lengthy working-out of solving these incorrect balance equations.
Rather than show you that generated text, I'll skip to the end.

Because the equations were set up wrong,
the equations are mutually inconsistent, and no solution to them exists.
Rather than realizing this, ChatGPT generates a claimed solution, as follows:

> Therefore, the steady state probability distribution is:
>
    π = [27/76, 18/76, 12/76, 8/76, 8/76]
>
> Note that these probabilities add up to 1, as expected.

These probabilities do not add up to 1.
Instead, they add up to `73/76`.
Not only did ChatGPT get this part wrong,
it failed to discover that it had gone wrong earlier,
and gave an answer that is yet more severely incorrect.

Over the 4 runs, it twice gave probabilities that summed to 1,
and twice gave probabilities that did not.
In every case, the system of equations had no valid solution,
and in no case did it give any indication of that fact.

## Mean and Variance

My second question was:

> Let X be a hyperexponential random variable with two branches.
With probability 1/3, X is Exp(1), and with probability 2/3, X is Exp(2).
What are X's mean and variance?

The correct answer is:
The mean of X is:

    E[X] = 1/3 * 1 + 2/3 * 1/2 = 1/3 + 1/3 = 2/3

The second moment of X is:

    E[X^2] = 1/3 * 2 * 1^2 + 2/3 * 2 * 1/2^2 = 2/3 + 1/3 = 1

The variance of X is:

    Var(X) = E[X^2] - E[X]^2 = 1 - (2/3)^2 = 1 - 4/9 = 5/9

Again, I ran ChatGPT on this question 4 times, to get a representative sample.

> The hyperexponential distribution is a mixture of exponential distributions with different rates, where the mixing probabilities are given. In this case, X has two branches, with probabilities 1/3 and 2/3 of being Exp(1) and Exp(2), respectively.

This is a restatement of the question.

> The mean and variance of a hyperexponential distribution can be calculated using the following formulas:
>
> Mean = ∑(pᵢ/λᵢ)
>
> Variance = ∑(pᵢ/λᵢ²) - (Mean)²
>
> where pᵢ and λᵢ are the probabilities and rates of the i-th
exponential distribution in the mixture.

This formula for the mean is correct.
The formula for the variance is close to correct, but subtly wrong.
The summation, which is calculating the second moment of X,
should be multiplied by 2.

Over the 4 runs, it encountered this step twice,
and twice went a different route involving integrals.
In two cases, one in each route,
it made a mistake around here, and in two cases it was correct through here.

> In this case, we have:
>
> * With probability 1/3, X is Exp(1), so p₁ = 1/3 and λ₁ = 1.
> * With probability 2/3, X is Exp(2), so p₂ = 2/3 and λ₂ = 2.
>
> Using the formulas above, we can calculate:
>
> Mean = (1/3)/1 + (2/3)/2 = 5/6
>
> Variance = (1/3)/1² + (2/3)/2² - (5/6)² = 11/18
>
> Therefore, the mean of X is 5/6 and the variance of X is 11/18.

The calculation of the mean is incorrect,
going wrong at the final manipulation of fractions.
The calculation of the variance is also incorrect.
Given the prior mistakes, it should have come out to `-7/36`.
Because the variance of any random variable is always nonnegative,
this should have prompted a realization that mistakes had been made previously.

Over the 4 runs, it never correctly calculated either the mean or the variance.
It said the mean was `5/6` three times, and once said the mean was `1.5`.
It said the variance was `11/18, 47/18, 7/36, 0.25` over the four runs.

## Wrap-up

ChatGPT performs very poorly on these questions.
Whenever the task consists of more than reciting a known formula,
ChatGPT rapidly diverges from the correct answer.
Once off the path of the correct answer, its generated text becomes increasingly nonsensical.
A human, having made a mistake, might at this point realize that they had made a mistake,
and go back to try to correct things.
ChatGPT never does this,
presumably because it was trained on text that didn't contain many mistakes,
and contained very few examples of people realizing mistakes halfway through and correct them.

ChatGPT performs worst of all on basic arithmetic such as working with fractions,
and basic algebra.
In particular, it tried 3 times to calculate `(1/3)/1 + (2/3)/2`,
and always incorrectly got `5/6`, when the correct answer is `2/3`.

To see if this issue remained in isolation, I asked it the question "What is (1/3)/1 + (2/3)/2?".
I repeated this question 4 times.
All 4 times, it gave the correct answer `2/3`, with different working-out text each time.
This indicates that the specific context of the probability problem
caused it to fail at basic arithmetic,
not just the content of the arithmetic itself.

In each of the 8 attempts at the two problems,
the response was thoroughly incorrect,
and would have received a failing grade.
If a student submitted these answers,
I would be concerned that they were unprepared for the course,
and had major gaps in their mathematical knowledge dating back to middle and high school.
