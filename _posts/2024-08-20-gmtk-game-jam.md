---
layout: post
title:  "Game Maker's Toolkit Game Jam August 2024"
# excerpt: "A test of the blog."
date: 2024-08-20 08:00:00 +0100
categories: game-jam
tags: game game-jam itch size-matters gmtk
author: domdfcoding
featured: true
toc:
  beginning: true

thumbnail: assets/img/gmtk-game-jam-2024-images/key-art-800x600.png
---

{% include captioned_figure.liquid
  path="assets/img/gmtk-game-jam-2024-images/key-art-800x600.png"
  alt="Size Matters Screenshot"
  caption='Screenshot of my game jam entry "Size Matters"'
%}


## Introduction

Two game jams in two months. Following [last month's Pirate Software Game Jam](/game-jam/pirate-software-game-jam/)
I decided to enter this month's [Game Maker's Toolkit Game Jam](https://itch.io/jam/gmtk-2024) too.
The theme was "Built to Scale". "It's up to you how you interpret the theme. While the idea is to make games about size, scale, and dimensions, you could make a game about weighing scales, scaling a building, fish scales, musical scales, or whatever!"

My original idea was a fighting game like Mortal Kombat but with Matryoshka nesting dolls.
As your health degrades the wooden shell cracks, and eventually shatters open.
But wait! There's another doll inside. You're not out of the fight yet.
You're on the back foot though as each doll is progressively smaller.

{% capture dolls_caption %}
<i>Matryoshka Dolls by <a title="Dennis G. Jarvis
, CC BY-SA 2.0 &lt;https://creativecommons.org/licenses/by-sa/2.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:DGJ_4705_-_Russian_Matryoshka_(4312413546).jpg">Dennis G. Jarvis, via Wikimedia Commons</a></i>
{% endcapture %}

{% include captioned_figure.liquid
  path="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/DGJ_4705_-_Russian_Matryoshka_%284312413546%29.jpg/512px-DGJ_4705_-_Russian_Matryoshka_%284312413546%29.jpg?20180302202234"
  alt="DGJ 4705 - Russian Matryoshka (4312413546)"
  caption=dolls_caption
%}

I put together a prototype, but the control scheme (there's a ragdoll underneath the static sprite) wasn't very easy to control with AI.
It needs to fling itself at your doll, then reset back to a neutral position and try to dodge attacks.
I've parked the game for now and might revisit it in the future.
I think it'll work much better as a 2 player game.

Looking for an alternative idea 2 hours in, I remembered the [fox pixel art by Elthen on itch.io](https://elthen.itch.io/2d-pixel-art-fox-sprites) I'd seen before, and thought would be cool to make a game with in the future.
I settled on the idea of having animals of different sizes (the fox, a squirrel and a bear), each with unique attributes.
The squirrel can climb trees but can't jump as high. The bear became a deer, which can jump very high to cross fences.

## Development

"Size Matters" was developed in Godot 4 . I've been using Godot for about 2 months now.

I decided to use the new Godot 4.3 release, which came out just before the jam.
However, I've found it much less stable than 4.2, with frequent segmentation faults.
Hopefully things improve in a patch.
A key change to the engine is the addition of `TileMapLayer` nodes to replace the old `TileMap`.
I wanted to try this out as I may migrate my other game over.
I'm not yet convinced there's great improvement over `TileMap`.

I started by following the [2D Platformer Quick Start Guide](https://www.youtube.com/watch?v=43c-Sm5GMbc) tutorial
by [Chris' Tutorials](https://www.youtube.com/@ChrisTutorialsYT) on YouTube.
That uses the [Pixel Art Asset Pack](https://anokolisa.itch.io/sidescroller-pixelart-sprites-asset-pack-forest-16x16)
by [Anokolisa](https://anokolisa.itch.io/) on itch.io.


## Finished Game

You can play the finished game over at [itch.io](https://potbanksoftware.itch.io/size-matters).


<iframe frameborder="0" src="https://itch.io/embed/2907555" width="552" height="167"><a href="https://potbanksoftware.itch.io/size-matters">Size Matters by potbanksoftware</a></iframe>
