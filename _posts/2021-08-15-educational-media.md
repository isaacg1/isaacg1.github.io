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

* Research Article: [NEXP not in ACC](https://people.csail.mit.edu/rrw/acc-lbs.pdf), Appendix A, by Ryan Williams. I wanted to see what was up with majority of XORs. The real statement is that majority of XORs can be simulated a symmetric function of ANDs, with polylog overhead or so. For instance, `MAJ(a xor b, c xor d) = f((a+b)^2+(c+d)^2) = f(a+2ab+b+c+2cd+d)`, where f is the "not 0 mod 4" function and MAJ breaks ties towards 1. Here I'm using `x^2` as my degree-amplifying function. There are only 6 different inputs after symmetry, so this is easy to check.

* Wikipedia Article: [Haven](https://en.m.wikipedia.org/wiki/Haven_(graph_theory)). I know understand treewidth better. A graph has treewidth at most k iff k + 1 pursuers can chase down a pursued, where the pursued can move through the graph edges, but can't move through the pursuers' nodes, and both sides know where the other is. Pursuers occupy k nodes while 1 pursuer moves. Tree decompositions are strategies for the pursuers, while havens are strategies for the pursued.

* Tutorial Video: [FPT Algorithms](https://youtu.be/tpBxUmfagsY), by Daniel Mark at the Simons Institute.

* Research Discussion: [On the purported inconsistency of Peano arithmetic](https://golem.ph.utexas.edu/category/2011/09/the_inconsistency_of_arithmeti.html#c039523), by Edward Nelson and Terry Tao. Tao points out the flaw in Nelson's proposed proof of the inconsistency of Peano arithmetic. High-level, polite, effective discussion.

* Research essay: [Two Cultures of Mathematics](http://www.dpmms.cam.ac.uk/~wtg10/2cultures.pdf), by Timothy Gowers. I think a similar split between problem solvers and theory builders exists in TCS, though not nearly as severe. Also, I think problem-solvers have more representation in TCS, while theory builders dominate in math.

* Tutorial Video: [Prime Gaps](https://youtu.be/pp06oGD4m00) by Terry Tao at UCLA. Very nice intro to the area.

* Puzzle Video: [The Legend of Question Six](https://youtu.be/Y30VF3cSIYQ) by Simon Pampena on Numberphile. The question, from the 1988 IMO, is "Let a, b be positive integers such that (a^2+b^2)/(ab+1) is an integer. Prove that it is a square." I paused the video when they posed question and solved it, based on ill-remembered intuitions from hearing about the question previously. Lots of fun to solve that way, obviously way easier than solving from scratch.

* Research Article: [Gradient descent = CLS = PPAD ∩ PLS](https://arxiv.org/abs/2011.01929), by Fearnley, Goldberg, Hollender, and Savani. This paper is very exciting, but a bit less exciting than it sounds. PPAD, PLS, and CLS are well known and important complexity classes. This paper shows that CLS is equal to the intersection of PPAD and PLS, which was not previously known, by showing that the problem of "Find a local approximate optimum of the gradient descent algortihm" is equal to both. Note that this is not the same as the problem "sample the distribution of Gradient Descent's output given a random initializer", which is the algorithm people actually use in practice. But nonetheless, this is a super cool result.

* Research review: [Large scale quantum experiments](https://www.quantamagazine.org/how-big-can-the-quantum-world-be-physicists-probe-the-limits-20210818/), by Quanta Magazine. Experimenters are working on placing ever larger objects into quantum superposition. The previous record was several thousand atoms. Now, they're working on hundreds of millions. If this works, it could probe the regime of quantum gravity for the first time.

* Tutorial Video: [Circuit Complexity and Connections I](https://youtu.be/1S8fKlR28Go) and [II](https://youtu.be/i4pQ9DYpdEo), by Ryan Williams, at the Simons Institute. Algorithms for circuit analysis and bounds on the power of circuits are very closely connected.

* Blog post: [More number gossip](https://blog.tanyakhovanova.com/2021/08/1-is-the-only-square-free-square/), by Tanya Khovanova, the creator of [Number Gossip])(http://numbergossip.com/).

* Textbook chapter: [Algebra of Orders](http://jdh.hamkins.org/an-algebra-of-orders/), by Josh Hawkins. A very gentle introduction to order theory.

* Blog post: [Meta-rationaliy](https://metarationality.com/bongard-meta-rationality), by David Chapman. All about Bingard problems, which consist of coming up with good explanations for why two sets are divided the way they are. I think the nebulosity stuff is overblown and high-faluting.

* Research essay: [Fraud in Honesty Study](https://datacolada.org/98), by Uri, Joe, Leif and an anonymous team of researchers. Proves that a major study on honesty was fradulent, in extensive detail. Responses from the original authors are very interesting, with none disputing the analysis.

* Research Interview: [Black Hole Information Paradox Resolved] (https://www.quantamagazine.org/netta-engelhardt-has-escaped-hawkings-black-hole-paradox-20210823/), interviewing Netta Engelhardt.

* Tutorial Video: What makes average-case NP problems hard? [I](https://youtu.be/NoLYzVd2ycg) and [II](https://youtu.be/aWKbWMCpC8w) Boaz Barak at the Simons Institute. From both the physics and CS perspectives.

* Explanatory Blog Post: [Pin and Unpin in Rust](https://blog.adamchalmers.com/pin-unpin/), by Adam Chambers. Explaining one of Rust's trickier concepts.

* Research Paper: [Discovery of glycoRNA](https://news.stanford.edu/2021/05/17/stanford-study-reveals-new-biomolecule/), by Ryan Flynn et al. Discovery of glycoRNA, RNAs with sugars attached. Previously unknown because no one was looking. 

* Research Blog Post: [Narrowing in on Planet Nine](http://findplanetnine.blogspot.com/2021/08/the-orbit-planet-nine.html?m=1), by Konstantin Batygin and Mike Brown. Overview of a research Article which narrows down the potential locations of Planet Nine and shows the observed clustering of asteroids is not produced by observational bias.

* Educational Podcast: [Dysentery](http://thispodcastwillkillyou.com/2021/08/24/episode-80-dysentery-loves-a-disaster/), by Erin Welsh and Erin Allman Updyke. A wonderfully friendly and well-searched podcast about disease, especially epidemic disease. This episode is similarly great.

* Research Slides: [Erdos's Ternary Digits Conjecture](http://www.math.lsa.umich.edu/~lagarias/TALK-SLIDES/ternary-fields-2009sep.pdf), by Jeff Lagarias. Erdos conjectured that all powers of 2 above 256 have a 2 when written in base 3. Amenable to SAT solving?

* Research Popularization: [Clocks and Entropy](https://www.quantamagazine.org/the-new-science-of-clocks-prompts-questions-about-the-nature-of-time-20210831/), by Natalie Walchover. The fundamental limits of clocks.

* Research Popularization: [Cardinals between \|N\| and \|R\|](https://www.scientificamerican.com/article/a-deep-math-dive-into-why-some-infinities-are-bigger-than-others/), by Martin Goldstern and Jakob Kellner. Exploring cardinalities between that of the naturals and the reals.

Updated through 08/31.
