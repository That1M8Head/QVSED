# QVSED - Qt-based Volatile Small Editor

QVSED is a volatile text editor.

![QVSED screenshot, showing the help message](qvsed-screenshot.png)

"Volatile" means that QVSED is entirely stateless - once you open a file, QVSED doesn't store any file paths or any other data other than the text contents of the file you loaded.
Additionally, QVSED won't prompt you if you're about to potentially lose an unsaved file, since it doesn't know of any file metadata.

QVSED follows the philosophy of ultra-minimalism, with its heavy emphasis on just editing text and nothing more.
QVSED's editing style is text-based, not file-based like basically every other editor out there.
Text goes in, from a file, and then text later comes out, into another or perhaps the same file.

QVSED works well as a simple scratchpad, but it's also quite useful for more involved editing operations, providing a seamless experience without posing prompts for potentially destructive actions.
It's not as powerful as something like Vim or even ed, but it provides a unique editing experience you won't find anywhere else. Whether or not this is a good thing is up to you.

QVSED is a PyQt5 rewrite of my older project, [ASMED (Another SMol EDitor)](https://github.com/That1M8Head/ASMED), which was written using Windows Forms, and was quite obviously only for Windows.

QVSED aims to replace ASMED by offering cross-platform support and the advantages of a lightweight editor without the overhead of .NET, as well as provide features that I never thought to add to ASMED because it was .NET only.

## Installing

QVSED [is available on PyPI](https://pypi.org/project/QVSED/). You can install it using the following command:

```bash
pip install --upgrade qvsed
```

To run QVSED, use the `qvsed` command. Feel free to make a shortcut/alias/symlink to it if you find that convenient.

## License

QVSED is free software, licensed under the GNU General Public License version 3 or later.

## Usage

QVSED is broken up into three parts - the Action Deck, the Text Area and the Echo Area.

The Action Deck contains editing commands, the Text Area is where the text content goes, and the Echo Area is where messages will be printed.

There's also the File Picker, for whenever QVSED prompts you to open or save a file. It provides a simple text entry and a button to open your system's file picker.

## Keyboard Shortcuts

QVSED contains a mix of bindings from the original ASMED, Vim-style bindings and Emacs-style bindings.

### Key Prefixes

+ `C-` - `Ctrl` (Windows, Linux), `⌘` (macOS)
+ `A-` - `Alt` (Windows, Linux), `⌥` (macOS)

When you see `<C-n>`, for instance, that means pressing `Ctrl+N` on Windows/Linux, or `⌘N` on macOS.

`Ctrl` being `⌘` and `Alt` being `⌥` is a Qt thing, not a QVSED thing, and there isn't much of a reason to change it.

This kind of notation was inspired by Emacs (though, QVSED uses `A-` instead of `M-` to be clearer).

### Action Deck bindings

These bindings are evolutions of the original ASMED key bindings.

+ **Clear Text** - `<C-n>` - Clear the Text Area. Think of it like New File.
+ **Open File** - `<C-f>` - Launch a file picker and load the chosen file's contents into the Text Area.
+ **Save File** - `<C-s>` - Launch a file picker and save the contents of the Text Area to the chosen file name.
+ **Full Screen** - `<A-f>` - Toggle full screen mode.
+ **Get Help** - `<C-h>` - Show a help message in the Text Area. This will overwrite your current work.
+ **Quit QVSED**  - `<A-q>` - Quit QVSED on the spot with no confirmation dialog.

### File Picker bindings

+ **Open/Save** - `<RET>` - Load from/save to the specified file path.
+ **Cancel** - `<ESC>` or `<A-q>` - Cancel and go back to QVSED.
+ **System File Picker**  - `<C-d>` - Launch your OS file picker.

### Motion bindings

These bindings are for the most part inspired by Vim, if not Emacs.

+ `<A-h>` - Move left a character. Inspired by Vim's `h`.
+ `<A-j>` - Move down a character. Inspired by Vim's `j`.
+ `<A-k>` - Move up a character. Inspired by Vim's `k`.
+ `<A-l>` - Move right a character. Inspired by Vim's `l`.

+ `<A-u>` - Move up half a page. Inspired by Vim's `<C-u>`.
+ `<A-d>` - Move up half a page. Inspired by Vim's `<C-d>`.

+ `<A-w>` - Move forward a word. Inspired by Vim's `w`.
+ `<A-b>` - Move back a word. Inspired by Vim's `b`.

+ `<A-a>` - Move to the start of the line. Inspired by Emacs' `<C-a>`.
+ `<A-e>` - Move to the end of the line. Inspired by Emacs' `<C-e>`.

## Action Deck

The Action Deck, positioned on the left side of the QVSED window, containing commands to clear the Text Area, open or save a file, display this help text, toggle in and out of full screen mode or quit QVSED.

The Action Deck is on the left rather than on the top like a traditional menu bar, so that the buttons can be bigger while still providing enough screen real estate for the Text Area.

## Text Area

The Text Area is where the actual text editing takes place.

You can enter and delete text, scroll down and up, cut, copy, paste, all that standard Notepad stuff.

QVSED is intentionally simplistic, and so there's not much to the Text Area.

## Echo Area

The Echo Area is the small bar at the bottom of the QVSED window that prints information.

For example, when a file is opened, it prints its file name. If a config file was not found, it'll generate one and give you the path.

QVSED inherited the name from Emacs. Well, less "inherited" and more "stolen from."

## File Picker

The File Picker is displayed when you use the **Open File** or **Save File** Action Deck commands.

It consists of the following elements:

+ A label instructing you to enter the file path, relative or absolute.
+ Another label that shows the current working directory.
+ A text box where you can enter the file path.
+ Three buttons:
  + **System File Picker** opens your operating system's file picker, so you can select the file you want without having to type in its path, just like in pre-1.5.0 QVSED versions. This can also be accessed with the `<C-d>` key binding.
  + **Open** or **Save** (depending on the Action Deck command you used) opens or saves the file at the specified path.
  + **Cancel** closes the dialog without saving any changes.

The File Picker makes it simple to load the file you want, simply by typing in its path.

If this is too oversimplified for you, or you just need to use your system file picker for whatever reason, you can always use the System File Picker option.

## Configuration

When QVSED is started, it looks for a configuration file. If it can't find one, it creates one and populates it with defaults.

On Windows, the configuration file will be stored at `C:\Users\<username>\AppData\Roaming\QVSED\config.py`, where `<username>` is your Windows username.

On *nix systems, the configuration file will be stored at `~/.config/QVSED/config.py`, where `~` is your home directory (`/home/<username>`).

As of QVSED 1.3.0, you can customise the colour scheme in addition to the font. For a list of sample colour schemes, [go here](COLOURS.md).

```python
# The default QVSED config.

# Font
font_family = ["JetBrains Mono", "Cascadia Code", "Consolas", "Menlo", "monospace"]
font_size = 11

# Colours
text_color = "#FFFFFF"
background_color = "#282C34"

button_color = "#393F4A"
button_hover_color = "#31353F"
button_pressed_color = "#282C34"

text_area_color = "#31353F"
echo_area_color = "#393F4A"

scroll_bar_color = "#363D49"
scroll_bar_background_color = "#282F3B"
scroll_bar_hover_color = "#4F5664"
scroll_bar_pressed_color = "#262B34"
```

Keep in mind that `font_family` *must* be a list. If you want only one font, specify `font_family = ["My Font"]`.
