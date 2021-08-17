---
layout: post
title: 'Educational media list, 08/15  to 08/31'
published: true
---
Here I'm listing much of the media I've read/watched/listed to/etc., and learned something from. This list will cover the next half month. Generally, if I list something here I'm recommending it. If not, I'll try to mention it.

I'm not going to give a big explanation of each item, because that'll probably get in the way of me posting. Generally, I'm just going for media type, creator, title, possibly venue, possibly a brief description.

* Review Video: [Debunking Pentagon UFO Videos](https://youtu.be/jHDlfIaBEqw) by Corridor Crew. VFX artists review videos of Unidentified Arial Phenomena, conclude that they are camera artifacts/birds/etc.

* Experiment Video: [Gauge Blocks under Vacuum](https://youtu.be/Z5XOk1oMFh0) by Applied Science. Gauge Blocks are highly polished metal blocks that stick together when they are pressed against each other.

* Law Podcast: [Pearls are in the Eye of the Beholder](https://www.nationalsecuritylawpodcast.com/), by Bobby Chesney and Steve Vladek, law professors at UT Austin. Usual round-up of topics, at a really high level, very enjoyable, multiple perspectives.

* Tutorial Video: [Beyond Worst-Case Analysis I](https://www.youtube.com/watch?v=thHt1lhLqJA) and [Beyond Worst-Case Analysis II](https://www.youtube.com/watch?v=_6-gMLvCxWw), by Tim Roughgarden at the Simons Institute. Lots of different kinds of analysis of algorithms beyond worst-case analysis. My research fits nicely in this model - adversary chooses the distribution, nature samples the distribution. I think there's something interesting that could be done with a smoothed analysis of multiserver SRPT where arrival times/sizes have a little bit of noise.

* Tutorial Video: [Understanding the Empirical Hardness of NP-Complete Problems I](https://www.youtube.com/watch?v=ZrXipcqpuxc) and [Understanding the Empirical Hardness of NP-Complete Problems II](https://www.youtube.com/watch?v=Jpiq3pphls4), by Kevin Leyton-Brown at the Simons Institute. Follow-up to the above, but more heuristic.

* Tutorial Video: [The Mathematics of Lattices I](https://www.youtube.com/watch?v=LlPXfy6bKIY) and [The Mathematics of Lattices II](https://www.youtube.com/watch?v=SZkTJMorxnM), by Vinod Vaikunatanathan, my Master's thesis advisor, at the Simons Institute. An introduction to Lattice Cryptography.

* Website & Game: [OriMaze](http://tromp.github.io/orimaze.html), by John Tromp. Also known as Unit Rush Hour. A game with very interesting and open complexity.

* Book: [The Scout Mindset](https://juliagalef.com/), by Julia Galef, cofounder of the Center for Applied Rationality. Listening on audiobook. This is the best explanation of rationality I've seen. Much better than more famous ones.

* Research Article: [The Gittins Policy in the M/G/1 Queue](https://www.cs.cmu.edu/~harchol/Papers/WIOPT21.pdf), by Ziv Scully and Mor Harchol-Balter, my frequent collaborators. The first fully general proof of the optimality of the Gittins policy in the M/G/1. Scheduling-first, not multi-armed-bandit-first.

* Tutorial Video: [Hardness of easy problems](https://youtu.be/0ndSu9TqrgI), by Virginia Williams, at the Simons Institute. A gentle introduction to fine-grained complexity.

* Tutorial Video: [Circuit Analysis Algorithms](https://youtu.be/adJvi7tL-qM), by Ryan Williams at the Simons Institute. Apparently Majority-of-XORs is a symmetric function? This isn't literally true.

* Blog Article: [Crawl Doubling Damage](https://desystemize.substack.com/p/desystemize-7), by Collin. In an incredibly hard game that never changes, will anyone notice if something does change?

* Research Article: [NEXP not in ACC](https://people.csail.mit.edu/rrw/acc-lbs.pdf), Appendix A, by Ryan Williams. I wanted to see what was up with majority of XORs. The real statement is that majority of XORs can be simulated a symmetric function of ANDs, with polylog overhead or so. For instance, MAJ(a xor b, c xor d) = f((a+b)^2+(c+d)^2) = f(a+2ab+b+c+2cd+d), where f is the "not 0 mod 4" function and MAJ breaks ties towards 1. Here I'm using x^2 as my degree-amplifying function. There are only 6 different inputs after symmetry, so this is easy to check.

Updated through 08/16.
