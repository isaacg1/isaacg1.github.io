---
published: true
layout: post
title: Deterministic Randomness
---
One of the hardest problems in mathematics is understanding things which are deterministic, but look random.

For instance, take the primes. A good model of the primes for guessing the answer to many number-theory questions is the Cramer model, which models each number `x` as prime with probability `1/log x`. When I say this is a good model, I mean that it is a good empirical match for many high-level propeties of the primes, such as asymptotic properties. Unfortunately, the model couldn't be more different than the reality in its low-level properties. As a result, much of the research into the primes consists of showing that the primes are pseudorandom enough for the result needed.

An impressive success in that endeavor was the celebrated [Green-Tao theorem](https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem). The theorem showed that any "sufficiently pseudorandom" subset of the integers has the desired propety, and then proved that a set closely related to the primes is sufficiently pseudorandom.

The problem of deterministic randomness also shows up repeatedly in computer science. An expander graph achieves the same mixing properties as a random graph, but in a deterministic fashion. More broadly, many complexity theoriats believe that P=BPP, which losely means that randomness can always be replaced by a deterministic operation.

Another example of this phenomenon that I enjoy is the [Kolakoski sequence](https://en.m.wikipedia.org/wiki/Kolakoski_sequence). It is the sequence of 1s and 2s that is self-describing, in that the numbers in the sequence are also the lengths of the runs of identical numbers within the sequence:

```1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, ...
```

If we look at a window of this sequence far from the beginning, the window looks roughly like a random admissible sequence of 1s and 2s. Admissible here means that the lengths of the runs are also an admissible sequence of 1s and 2s.

One of the key "random" properties that seems obvious but is currently an open problem is whether the density of 1s in the sequence is 1/2. One way to prove this would be to show that the "numbers" window and its corresponding "run lengths" window are uncorrelated, in some sense, and so a window is just as likely to have many 1s as it is to have many 2s. Unfortunately, an analogue of statistical independence is hard to transfer to a deterministic setting, and so to the best of my knowledge, all bounds on the densisty currently use other techniques. I'll talk more about this in my next post.

It's common for mathematical objects to be well-modelled by random objects, but their fundamentally deterministic natures forces us to use very different techniques to prove results about them.
