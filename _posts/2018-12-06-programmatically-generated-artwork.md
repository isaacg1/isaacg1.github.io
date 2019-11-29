---
layout: post
title: "Programmatically generated artwork"
---

I have made five rust programs for programmatically generating artwork in different styles. Here is a sample in each style, along with an explanation of the algorithms:

## Brushstrokes

Algorithm: Color the pixels randomly.
Choose locations in a random order. At each location, test a collection of "brushes",
each a rectangle of pixels.
Find the brush whose pixels have the least average color distance from the middlemost color.
Set the pixel at that location to the middlemost color.
Repeat this process a couple of times.

![Brushstrokes](/assets/brush-1600.png)

## Smeared Mandelbrot

Algorithm: Generate mandelbrot-like sets by iterating f(z) = z^p + c, for each p in (1.333, 3). Color them by the relative movement of the point, from start to convergence.

[Repository](https://github.com/isaacg1/mandel)

![Smeared Mandelbrot](/assets/mandel-1000-400.png)

## Disrupted continuity

Algorithm: Choose locations in a random order. At each location, choose the pixel color with the smallest possible color distance from that of the surrounding pixels that have been placed, weighted by the distance of the surrounding pixels.

[Repository](https://github.com/isaacg1/color-cont)

![Disrupted continuity](/assets/continuous.png)

## Peaks

Algorithm: Add together many circles of colors, measured relative to gray, where the intensity is a bell curve going away from the center, and the radii are lognormally distributed.

[Repository](https://github.com/isaacg1/peaks)

![Peaks](/assets/peaks.png)

## Broken Glass

Algorithm: Split one region in half with a black line. Color each side a variation of the region's prior color.

[Repository](https://github.com/isaacg1/broken_glass)

![Broken Glass](/assets/broken-glass.svg)

## Circles

Algorithm: Place pixels of each possible color in a random order,
each at the nearest unoccupied location to the most similar color placed thus far.

[Repository](https://github.com/isaacg1/colors)

Note that this one looks better at larger scales. A very large image can be found in the repository readme.

![Circles](/assets/circles.png)

