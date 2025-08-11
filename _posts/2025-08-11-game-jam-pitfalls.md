---
layout: post
title: "Common Game Jam Pitfalls To Avoid"
date: 2025-08-11 21:27:00 +0100
# last_updated: 2025-08-11 21:27:00 +0100
categories: game-jam
tags: game game-jam
author: domdfcoding
featured: true
toc:
  beginning: true

thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Computer_mouse_trap.jpg/330px-Computer_mouse_trap.jpg
---

{% capture mousetrap_caption %}
<i>Computer mouse trap by <a title="Karen Rustad
, CC BY-SA 2.0 &lt;https://creativecommons.org/licenses/by-sa/2.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Computer_mouse_trap.jpg">Karen Rustad, via Wikimedia Commons</a></i>
{% endcapture %}

{% include captioned_figure.liquid
  path="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Computer_mouse_trap.jpg/960px-Computer_mouse_trap.jpg"
  alt="A photograph of a computer mouse caught in a mousetrap"
  caption=mousetrap_caption
%}

Having entered four game jams and played over 100 game jam entries, I've noticed several mistakes developers (myself included) make.
I get that there's only limited time during the jam, but addressing these - which don't take long -
can make the difference between a game not running or the player being so confused they move on, and the player playing and enjoying your game.
That's the end goal, right?

So here's my continuously growing list of pitfalls to avoid.

*Comments? Suggestions? Any pitfalls of your own you'd like to share? [Open an issue on GitHub](https://github.com/potbanksoftware/potbanksoftware.github.io/issues/new).*


## Uploading a Debug Build

Godot's debug builds are great for testing your game and finding bugs, but they're not what you want your released game to be, as they're necessarily slower to allow for debugging.

You can tell you're running a debug build because it will say `(DEBUG)` in the title bar.

When you export your game, make sure to untick the `Export With Debug` button in the `Save a File` window where you choose where to save the game. If you use `Export All...`, click `Release` in the small window that appears instead.

{% include captioned_figure.liquid
  path="assets/img/game-jam-pitfalls/godot-export-screen.png"
  alt="Screenshot of Godot showing the export window and the checkbox to untick for a Release build."
  caption='Screenshot of Godot with the option that must be unticked for a release build.'
  class="col-12 mt-3 mt-md-0"
%}


## Barren Itch.io Pages

Your itch.io game page, and especially the cover image, are a player's first impression of your game.
Make sure you've got at least the cover image set, but also some screenshots too if possible.
[This guide by Star West](https://hedgiespresso.itch.io/itch-page-image-templates) is a good reference for creating images.

But you also need some text about your game - what is it? A platformer?
First person? Puzzle? Roguelike? What can the player expect once they click play or install the game?
And how do they play? Include this in the game too (see below) but put this on the game's page so players can refer back.

Also include how many people were on your team (or if you worked alone) and how long you worked on the game.
Did you put it together in the last two days or did you use the whole time available?
This helps with player expectations.

## No Details on Controls and How To Play

Make sure to include a screen at the beginning of your game or in the main menu
explaining how to play the game. Which controls are move? Which interact? 
What's the objective? Don't leave the player guessing what they have to do,
as they could lose interest. 

If your game has a pause menu I would include these there as well so the player can refresh their memory.


## Filename Case Sensitivity

Many Windows users forget that on other operating systems (including Linux, and macOS in some circumstances)
have case sensitive filesystems. So if you have a player sprite file called `Player.png`, 
while on Windows you can access it as `player.png` as well, on Linux that will fail.

Godot and Unity will not warn you that this is the case (one could call that a bug) and so your export for Linux won't run (properly).
This is most often a problem when loading files through code, rather than through the editor's tools.

Before exporting, double check all files you're importing through code have the exact same filename as the file on disk.
Sticking to a rule, such as always using `snake_case` and having all filenames lowercased, can help avoid this issue.

For godot, see [this section](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html#case-sensitivity) of the documentation.


