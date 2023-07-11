# QVSED Colour Schemes

These colour schemes can be applied to QVSED in its [config file](README.md#configuration).

## Colour Scheme List

The following colour schemes are arranged in ascending order, from the earliest to the latest.

If this file gets too big I'll reorganise them in alphabetical order or something.

Themes made before QVSED v1.4.1 did not include `text_area_color`, `echo_area_color`
or `button_pressed_color`, so QVSED will replace the old themes' missing colour
definitions with [equivalents](#equivalents).

Colour options relating to the scroll bar also didn't exist before v1.4.2, so it's
the same thing in that case.

### Monokai

![QVSED v1.3.7 in Monokai](colour-schemes/monokai-classic.png)

```python
# Monokai, taken from sampling Doom Emacs' doom-monokai-classic theme
text_color = "#F8F8F2"
background_color = "#1D1F19"

button_color = "#272822"
button_hover_color = "#171819"
```

### Codebreaker

![QVSED v1.3.9 in Codebreaker](colour-schemes/codebreaker.png)

```python
# Codebreaker, That1M8Head named this one himself
text_color = "#00FF00"
background_color = "#000000"

button_color = "#000000"
button_hover_color = "#111111"
```

### Buttercream

![QVSED v1.4.0 in Buttercream](colour-schemes/buttercream.png)

```python
# Buttercream, a light-yellow theme
text_color = "#000000"
background_color = "#ffffda"

button_color = "#fff7b1"
button_hover_color = "#fffad3"
```

### Banana

![QVSED v1.4.0 in Banana](colour-schemes/banana.png)

```python
# Banana, a light theme inspired by bananas
text_color = "#331f00"
background_color = "#fff3bf"

button_color = "#b7eb76"
button_hover_color = "#f0ee82"
```

### ASMED

![QVSED v1.4.2 in ASMED](colour-schemes/asmed.png)

```python
# ASMED, inspired by the original ASMED, QVSED's predecessor
text_color = "#FFFFFF"
background_color = "#21222D"

button_color = "#40455A"
button_hover_color = "#4C526C"
button_pressed_color = "#878DA2"

text_area_color = button_color
echo_area_color = button_color

scroll_bar_color = "#5B6074"
scroll_bar_hover_color = "#757A91"
scroll_bar_pressed_color = "#43475A"
```

## Equivalents

If the following definitions aren't found in config.py, they'll be replaced
with their equivalents.

| Definition                    | Equivalent             |
| ----------------------------- | ---------------------- |
| `button_pressed_color`        | `background_color`     |
| `text_area_color`             | `button_hover_color`   |
| `echo_area_color`             | `button_hover_color`   |
| `scroll_bar_color`            | `button_color`         |
| `scroll_bar_background_color` | `button_hover_color`   |
| `scroll_bar_hover_color`      | `button_pressed_color` |
| `scroll_bar_pressed_color`    | `button_pressed_color` |

This may or may not look good, so it's recommended to set these values yourself.

For any of the other definitions, if their values aren't specified, your config.py
will be reset.
