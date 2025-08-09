---
layout: page
toc:
  sidebar: left
# output: true

title: "Godot Helpers"
description: "<tt>godot-helpers</tt> is a Godot addon with various useful scenes and classes."
category: [godot, godot-addons]
github_url: https://github.com/potbanksoftware/godot-helpers
---

`godot-helpers` is an MIT Licenced Godot addon with various useful scenes and classes.

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

#### Class `PanelControl`

Base class for custom controls derived from panels. Provides a `focus()` method to grab focus on the underlying button, slider etc.

#### `checkbox_button.tscn`

`res://godot-helpers/controls/checkbox_button/checkbox_button.tscn`

A toggle button with a checkbox. The button is of class `CheckBoxButton`, inheriting from [`PanelControl`](#class-panelcontrol).


#### `volume_slider.tscn`

`res://godot-helpers/controls/volume_slider/volume_slider.tscn`

A toggle button with a checkbox. The button is of class `VolumeSlider`, inheriting from [`PanelControl`](#class-panelcontrol).


#### `controller_group_prompt_label.tscn`

`res://godot-helpers/controls/controller_group_prompt_label.tscn`

A label that shows a group of controller or keyboard input prompts and a label.

Options for `group` are:

* `WASD_LS` - The WASD keyboard keys and the left controller joystick, such as for movement.
* `ARROWS_DPAD` - The keyboard arrow keys and the controller D-pad.
* `MOUSE_RS` - Mouse movement and the right controller joystick, such as for aiming.

By default the prompt is shown for controllers if connected, otherwise for keyboards.
This can be overridden with the `controller_type` option.

The label is of class `ControllerGroupPromptLabel`.

#### `controller_prompt_label.tscn`

`res://godot-helpers/controls/controller_prompt_label.tscn`

A label that shows a controller or keyboard input prompt and a label.

The prompt icon is taken from the given `action`.

By default the prompt is shown for controllers if connected, otherwise for keyboards.
This can be overridden with the `controller_type` option.

The label is of class `ControllerPromptLabel`.


#### `controller_prompt_button.tscn`

`res://godot-helpers/controls/controller_prompt_button.tscn`

A button that shows a controller or keyboard input prompt and a label.
The prompt icon is taken from the given `action`.
When the button is pressed or the associated action is pressed (i.e. the corresponding key or controller button)
the `pressed` signal is emitted.

By default the prompt is shown for controllers if connected, otherwise for keyboards.
This can be overridden with the `controller_type` option.

The label is of class `ControllerPromptButton`.


#### Class `ButtonPress`

Helpers to visually simulate UI button presses when controller button or keyboard key pressed.
Requires the button to have a theme set.

Example Usage

```gdscript
if Input.is_action_just_pressed("ui_accept"):
	ButtonPress.set_simulate_press_texture(self)
	# Do something

if Input.is_action_just_released("ui_accept"):
	ButtonPress.unset_simulate_press_texture(self)
```
