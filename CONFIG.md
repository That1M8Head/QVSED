# QVSED Configuration

When QVSED is started, it looks for a configuration file. If it can't find one, it creates one and populates it with defaults.

On Windows, the configuration file will be stored at `C:\Users\<username>\AppData\Roaming\QVSED\config.py`, where `<username>` is your Windows username.

On *nix systems, the configuration file will be stored at `~/.config/QVSED/config.py`, where `~` is your home directory (`/home/<username>`).

You can open your config up in QVSED by using the **Open File** command and typing in `~/AppData/Roaming/QVSED/config.py` (Windows) or `~/.config/QVSED/config.py` (*nix).

## Font

Config options pertaining to the font.

| Option        | Description                         | Type   | Default                                                                 |
|---------------|-------------------------------------|--------|-------------------------------------------------------------------------|
| `font_family` | The font families QVSED should use. | `list` | `["JetBrains Mono", "Cascadia Code", "Consolas", "Menlo", "monospace"]` |
| `font_size`   | The default font size for QVSED.    | `int`  | 11                                                                      |

Keep in mind that `font_family` *must* be a list. If you want only one font, specify `font_family = ["My Font"]`.

## Options

Config options that change QVSED's functionality.

Option              | Description                                              | Type  | Default
--------------------|----------------------------------------------------------|-------|---------
`tab_stop_width`    | Specifies the Text Area's tab stop width.                | `int` | 4
`echo_area_timeout` | Specifies the Echo Area's clear timeout in milliseconds. | `int` | 3000

## Colours

For colour scheme configuration, see [COLOURS.md](COLOURS.md).

## Default Config

```python
# Font
font_family = ["JetBrains Mono", "Cascadia Code", "Consolas", "Menlo", "monospace"]
font_size = 11

# Options
tab_stop_width = 4
echo_area_timeout = 3000

# Colours
colors = {
    "window": {
        "text": "#FFFFFF",
        "background": "#282C34"
    },
    "button": {
        "text": "#FFFFFF",
        "background": "#393F4A",
        "hover": "#31353F",
        "pressed": "#282C34"
    },
    "text_area": {
        "text": "#FFFFFF",
        "background": "#31353F"
    },
    "echo_area": {
        "text": "#FFFFFF",
        "background": "#393F4A"
    },
    "scroll_bar": {
        "text": "#363D49",
        "background": "#282F3B",
        "hover": "#4F5664",
        "pressed": "#262B34"
    }
}
```
