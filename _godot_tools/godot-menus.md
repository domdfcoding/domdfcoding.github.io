---
layout: page
toc: true
output: true
excerpt: "<tt>godot-menus</tt> is a Godot addon with scenes for building basic menus."

title: "Godot Menus"
---

## [<i class="fa-brands fa-github"></i>](https://github.com/potbanksoftware/godot-menus)

`godot-menus` is an MIT Licenced Godot addon with scenes for building basic menus.

* [Demo](/godot-menus-demos)
* [Demo Source](https://github.com/potbanksoftware/godot-menus-demos)


### Installation

```bash
git submodules add https://github.com/potbanksoftware/godot-menus addons/godot-menus
```

This will add `godot-menus` as a git submodule.

Then install [`godot-helpers`](/godot-tools/godot-helpers).


### Addon Contents


#### `default_bus_layout.tres`

`res://addons/godot-menus/default_bus_layout.tres`

Sample bus layout containing Master, SFX, and Music busses.


#### `menu_button_font.tres`

`res://addons/godot-menus/menu_button_font.tres`

Theme for menu buttons, with PromptFont at 32pt.


#### Class `Menu`

Base class for menus, with functions to handle opening submenus.


#### `main_menu.tscn`

`res://addons/godot-menus/main_menu.tscn`

Basis of a main menu, with level select, save, load, options and quit buttons.

The menu is of class `MainMenu`, inheriting from `Menu`.


#### `pause_menu.tscn`

`res://addons/godot-menus/pause_menu.tscn`

Basis of a pause menu, with level select, save, load, options, main menu and quit buttons.

The menu is of class `PauseMenu`, inheriting from `Menu`.


#### `level_select_menu.tscn`

`res://addons/godot-menus/level_select_menu.tscn`

Menu for selecting a level.

Contains a series of ``LevelSelectButton`` for each level in the `levels.json` file in the project root.


#### `options_menu.tscn`

`res://addons/godot-menus/options_menu.tscn`

Basis of an options menu, with volume, vsync, touchscreen controls, and debug menu options.


#### `level_select_button.tscn`

`res://addons/godot-menus/level_select_button.tscn`

A button in a level select menu. `scene` is the path to the level scene to load.

When pressed the button emits the `pressed_with_node(button: Button)` signal.

The button is of class `LevelSelectButton`.


#### `menu_buttons/submenu_button.tscn`

`res://addons/godot-menus/menu_buttons/submenu_button.tscn`

A button to open a submenu, hide the parent menu, and show the parent menu when the submenu closes.

The button is of class `SubmenuButton`.


#### `menu_buttons/level_select_submenu_button.tscn`

`res://addons/godot-menus/menu_buttons/level_select_submenu_button.tscn`

`SubmenuButton` to open the level select menu and load the selected level.

The button is of class `LevelSelectSubmenuButton`, inheriting from `SubmenuButton`.


#### `menu_buttons/quit_button.tscn`

`res://addons/godot-menus/menu_buttons/quit_button.tscn`

A button to quit the game. Does not show in web exports.

The button is of class `MenuQuitButton`.
