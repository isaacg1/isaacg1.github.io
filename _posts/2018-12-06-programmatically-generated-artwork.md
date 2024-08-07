---
layout: post
title: "Programmatically generated artwork"
---

I have made seventeen rust programs for programmatically generating artwork in different styles.
Here is a sample in each style, along with an explanation of the algorithms:

## Dual Colors

This is the dual algorithm to my [very first algorithm, Circles](#circles).

That algorithm iterated randomly through colors, found the most similar used color, found its location, found the most similar open location, and put the color at the location.

In contrast, this algorithm iterates randomly through locations, finds the most similar used location, finds its color, finds the most similar unused color, and puts the color at the location.

[Repository](https://github.com/isaacg1/dual-colors/tree/main)

![Dual Colors: Rainbow watercolors with a sprinkling of darkness](/assets/art/dual-colors.png)

## Plaid

Check straight-line triples of pixels, swap pixels to make lower distance. Optimize L-half norm.

[Repository](https://github.com/isaacg1/walk-exchange)

![Plaid](/assets/art/plaid.png)

## Spirals

Iterate over colors in a random order. For each, find the most similar color. Walk in a gentle spiral to nearest open pixel. Record final angle, start from there.

[Repository](https://github.com/isaacg1/spiral/)

![Spirals](/assets/art/spiral.png)
## Streams

Forces are generated at certain points, some inward, some outward, some linear.
Then faucets are generated, which are associated with certain colors at certain points.
Streams are generated, with colors similar to their faucet, flowing according to the forces.
Colors are summed, past through a sigmoid-type function,
and transformed into the [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space) color space.

[Repository](https://github.com/isaacg1/streams/)

![Streams](/assets/art/streams.png)

## Watercolors

Points are seeded. Colors initially diffuse wildly, then more gently as distance from seed increases. Mixture of DFS and Random selection of pixels to fill in. Small amount of fuzzing to smooth edges and fill in gaps.

[Repository](https://github.com/isaacg1/water-me)

![Watercolors](/assets/art/watercolors.png)

## Sand Walk

Iterate over colors in a random order.
For each, find the most similar color, take a random walk, biased towards similar colors.
If we find an unoccupied location, place there.
If can't find a free slot in a reasonable number of steps,
sample some random unoccupied locations
and choose the closest one to the final location of the random walk.

[Repository](https://github.com/isaacg1/angles)

![Sand walk](/assets/art/sand-walk.png)

## Fans

Revisting the "place pixels close to similarly colored pixels" from circles.
Every pixel has a facing angle.
Place a few seed pixels with random facing angles, spread over the image.
Iterate over all colors in random order.
For each color, find the most similarly colored pixel already placed.
Find the closest uncolored pixel withtin a small angle of the facing angle of the similar pixel, wrapping around toroidally.
Place the new color there.
If no such pixel exists, as close as possible.

[Repository](https://github.com/isaacg1/angles)

![Fans](/assets/art/fans.png)

## Orbits

Revisiting the "color-force" idea from threads.
Objects are attracted by a force proportionate to their masses,
their color similarity and inverse radius squared.

[Repository](https://github.com/isaacg1/log-gravity)

![Orbits](/assets/art/orbits.png)

## Fractal

Algorithm: Make a list of transformations, of the form:

* Take a source circle.

* Translate

* Rotate

* Tint

Sample transformations with a triangle distribution.

[Repository](https://github.com/isaacg1/fractal)

![Fractal](/assets/art/fractal.png)

## Subdivide, exchange

Algorithm: Start with a very small image. Subdivide each pixel into 4.
Add random Gaussian noise to each pixel's color.
Less noise once more pixels.
Then pick many random pairs of pixels,
and check if neighboring colors would be more similar
if swapped.
If so, swap.
Repeat until desired size.

[Repository](https://github.com/isaacg1/subdivide-exchange)

![Subdivide, exchange](/assets/art/subdivide-exchange.png)

## Midline

Algorithm: Generate seed pixels, place new pixels randomly on the line between those pixels, or as close as possible.

[Repository](https://github.com/isaacg1/midline)

![Midline](/assets/art/midline.png)

## Threads

Algorithm: Generate particles with "color charges".
Atoms move relative to each other according to a gravity-like force,
with a distance metric adapted for a square-torus topology.
Force is proportional to color similarity and inverse-square of distance.
Draw traces of each particle.

[Repository](https://github.com/isaacg1/torus)

![Toroidal Gravity](/assets/art/torus.png)

## Brushstrokes

Algorithm: Color the pixels randomly.
Choose locations in a random order. At each location, test a collection of "brushes",
each a rectangle of pixels.
Find the brush whose pixels have the least average color distance from the middlemost color.
Set the pixel at that location to the middlemost color.
Repeat this process a couple of times.

![Brushstrokes](/assets/art/brush-1600.png)

## Smeared Mandelbrot

Algorithm: Generate mandelbrot-like sets by iterating f(z) = z^p + c, for each p in (1.333, 3). Color them by the relative movement of the point, from start to convergence.

[Repository](https://github.com/isaacg1/mandel)

![Smeared Mandelbrot](/assets/art/mandel-1000-400.png)

## Disrupted continuity

Algorithm: Choose locations in a random order. At each location, choose the pixel color with the smallest possible color distance from that of the surrounding pixels that have been placed, weighted by the distance of the surrounding pixels.

[Repository](https://github.com/isaacg1/color-cont)

![Disrupted continuity](/assets/art/continuous.png)

## Peaks

Algorithm: Add together many circles of colors, measured relative to gray, where the intensity is a bell curve going away from the center, and the radii are lognormally distributed.

[Repository](https://github.com/isaacg1/peaks)

![Peaks](/assets/art/peaks.png)

## Broken Glass

Algorithm: Split one region in half with a black line. Color each side a variation of the region's prior color.

[Repository](https://github.com/isaacg1/broken_glass)

![Broken Glass](/assets/art/broken-glass.svg)

## Circles {#circles}

Algorithm: Place pixels of each possible color in a random order,
each at the nearest unoccupied location to the most similar color placed thus far.

[Repository](https://github.com/isaacg1/colors)

Note that this one looks better at larger scales. A very large image can be found in the repository readme.

![Circles](/assets/art/circles.png)
