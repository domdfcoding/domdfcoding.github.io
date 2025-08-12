---
layout: post
title:  "Pirate Software Game Jam July 2024"
# excerpt: "A test of the blog."
date: 2024-07-29 18:06:43 +0100
categories: game-jam
tags: game game-jam itch cabal-chemist
author: Dominic Davis-Foster
toc:
  beginning: true

thumbnail: assets/img/cabal_chemist_screenshot.png
og_image:
  image: assets/img/cabal_chemist_screenshot.png
---

{% include captioned_figure.liquid
  path="assets/img/cabal_chemist_screenshot.png"
  alt="Cabal Chemist Screenshot"
  caption='Screenshot of my game jam entry "Cabal Chemist"'
%}


## Introduction

This month's [Pirate Software Game Jam](https://itch.io/jam/pirate) was the first I submitted a game for. (I previously participated in the [2021 js13kgames jam](https://js13kgames.com/entries/2021) but couldn't make my game fit the size limit.) This time the theme was "Shadows and Alchemy". "Shadows can relate to a number of different subjects outside of light levels. Think about shadow governments, secret societies, or elemental effects. Alchemy can also be used for much more than mixing potions. Alchemy is about transformation, synthesis, combination, and hidden knowledge." I decided on a more literal interpretation, with a shadow organisation attempting some aim through alchemy. Eventually that became world domination through soft drinks.

## Development

"Cabal Chemist" was developed in Godot 4. I've only been using Godot for about a month but as a Python programmer I found GDScript very approachable.

{% include captioned_figure.liquid alt="Screenshot of the first prototype" path="/assets/img/pirate-software-jam-july-2024-images/initial-prototype.png" %}

This is a screenshot of the first prototype of the game from 22nd July, before it even had a name.
The ingredients have their own randomised effects but they're not yet combined.
That came with the next prototype on the 23rd, together with the spot to enter the drink's name.

{% include captioned_figure.liquid
  alt="Screenshot of the second prototype"
  path="/assets/img/pirate-software-jam-july-2024-images/prototype-with-effects.png"
  caption="Screenshot of the 2nd Prototype"
  %}

The prototype from the 25th implemented the sticky-note display of previous drinks and scoring, which has an aggressive mountain-shaped curve for score (0-100) against overall drink effect (-100% to 100%), to have sharp drop-offs either side of the optimal value (which is a closely guarded secret.)

{% include captioned_figure.liquid
  alt="Screenshot of the third prototype"
  path="/assets/img/pirate-software-jam-july-2024-images/prototype-with-scoring.png"
  caption="Screenshot of the 3rd Prototype"
%}

By this point the game needs minimal polish for the jam. There's no art or sound, although if turned into a proper game it'd be styled with chemistry apparatus and an evidence board, with the combined drink effects shown on a clipboard, and bubbling sounds like you'd hear in a chemistry lab. It also needs a lot of balance as there are almost certainly some over powered ingredients and near impossible to actually "win" by getting enough points.

{% include captioned_figure.liquid
  alt="Mockup of the UI for the finished game"
  path="/assets/img/pirate-software-jam-july-2024-images/ui_mockup.png"
  caption='Mockup of the UI for the "finished" game'
%}

Apart from the ingredient sprite (["CC0 Potion Icons"](https://opengameart.org/content/cc0-potion-icons) by AntumDeluge on OpenGameArt.org) I made the game on my own spending about 2 hours a day on it.

## Finished Game

You can play the finished game over at [itch.io](https://potbanksoftware.itch.io/cabal-chemist).


<iframe frameborder="0" src="https://itch.io/embed/2860709" width="552" height="167"><a href="https://potbanksoftware.itch.io/cabal-chemist">Cabal Chemist by potbanksoftware</a></iframe>
