---
layout: page
permalink: /godot-tools/
toc: true

title: "Godot Addons and Tools"
---

## godot-helpers [<i class="fa-brands fa-github"></i>](https://github.com/potbanksoftware/godot-helpers)

`godot-helpers` is a Godot addon various useful scenes and classes.

* [Demo](/godot-helpers-demos)
* [Demo Source](https://github.com/potbanksoftware/godot-helpers-demos)


### Installation

```bash
git submodules add https://github.com/potbanksoftware/godot-helpers addons/godot-helpers
```

This will add `godot-helpers` as a git submodule.
You can then [enable the plugin in your project settings](https://docs.godotengine.org/en/4.4/tutorials/plugins/editor/installing_plugins.html#enabling-a-plugin).


### Addon Contents


#### `blur_colour_rect.tscn`

`res://addons/godot-helpers/blur/blur_colour_rect.tscn`

Adds a blur to all `CanvasItem`s behind it. The amount of blur can be adjusted with the `lod` variable.


#### `promptfont.ttf`

`res://addons/godot-helpers/promptfont/promptfont.ttf`

Font with icons for controller input prompts.

PromptFont by Yukari "Shinmera" Hafner, available at https://shinmera.com/promptfont


#### `ambient_music_player.gd`

`res://addons/godot-helpers/ambient_music_player.gd`

Recommended use as an autoload called `AmbientMusicPlayer`.

Controls looped ambient music playback, with the option to start at a random point.


#### Class `UserPreferences`

Resource for user preferences, such as audio level and vsync.


#### Class `RichTextOffset`

`RichTextEffect` to allow text to be offset vertically.

**Example**

```bbcode
This [offset y=-7]text[/offset] makes [offset y=15]use[/offset] of [offset y=-3]RichTextOffset[/offset]"
```


#### Class `ControllerImpl`

Provides access to the currently connected controller type, and the appropriate prompt icon for actions.


##### Function `controller_connected() -> bool`

Returns whether any controllers are connected.


##### Function `controller_type() -> ControllerType`

Returns the type of the first connected controller, or `ControllerType.NONE` if none are connected.


##### Function `get_action_button(action: String) -> String`

Returns the prompt icon for the given action.


##### Function `is_touchscreen() -> bool`

Returns whether the display is a touchscreen.


##### Enum `ControllerType`

Represents the type of the currently connected controller.

Options are `XBOX_360`, `XBOX`, `PLAYSTATION`, `PS4`, `PS5`, `SWITCH`, and `NONE`.

