---
published: false
---
One of the hardest problems in mathematics is understanding things which are deterministic, but look random.

For instance, take the primes. A good model of the primes for guessing the answer to many number-theory questions is the Cramer model, which models each number `x` as prime with probability `1/log x`. When I say this is a good model, I mean that it is a good empirical match for many high-level propeties of the primes, such as asymptotic properties. Unfortunately, the model couldn't be more different than the reality in its low-level properties. As a result, much of the research into the primes consists of showing that the primes are pseudorandom enough for the result needed.

An impressive success in that endeavor was the celebrated [Green-Tao theorem](https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem). The theorem showed that any "sufficiently pseudorandom" subset of the integers has the desired propety, and then proved that a set closely related to the primes is sufficiently pseudorandom.

The problem of deterministic randomness also shows up repeatedly in computer science. An expander graph achieves the same mixing properties as a random graph, but in a deterministic fashion. More broadly, many complexity theoriats believe that P=BPP, which losely means that randomness can always be replaced by a deterministic operation.

Another example of this phenomenon that I enjoy is the [Kolakoski sequence](https://en.m.wikipedia.org/wiki/Kolakoski_sequence). It is the sequence of 1s and 2s that is its own run-lengrh encoding:

```1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, ...
```

If we look at a window of this sequence far from the beginning