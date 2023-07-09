# QVSED Colour Schemes

These colour schemes can be applied to QVSED in its [config file](README.md#configuration).

## Colour Scheme List

The following colour schemes are arranged in ascending order, from the earliest to the latest.

If this file gets too big I'll reorganise them in alphabetical order or something.

Themes made before QVSED v1.4.1 did not include `text_area_color` or `echo_area_color`,
so their updated variants set them to `button_hover_color` like how they were before.
Similarly, `button_pressed_color` didn't exist before v1.4.1, so the older themes use
`background_color`.

### Monokai

![QVSED v1.3.7 in Monokai](colour-schemes/monokai-classic.png)

```python
# Monokai, taken from sampling Doom Emacs' doom-monokai-classic theme
text_color = "#F8F8F2"
background_color = "#1D1F19"
button_color = "#272822"
button_hover_color = "#171819"
button_pressed_color = background_color
text_area_color = button_hover_color
echo_area_color = button_hover_color
```

### Codebreaker

![QVSED v1.3.9 in Codebreaker](colour-schemes/codebreaker.png)

```python
# Codebreaker, That1M8Head named this one himself
text_color = "#00FF00"
background_color = "#000000"
button_color = "#000000"
button_hover_color = "#111111"
button_pressed_color = background_color
text_area_color = button_hover_color
echo_area_color = button_hover_color
```

### Buttercream

![QVSED v1.4.0 in Buttercream](colour-schemes/buttercream.png)

```python
# Buttercream, a light-yellow theme
text_color = "#000000"
background_color = "#ffffda"
button_color = "#fff7b1"
button_hover_color = "#fffad3"
button_pressed_color = background_color
text_area_color = button_hover_color
echo_area_color = button_hover_color
```

### Banana

![QVSED v1.4.0 in Banana](colour-schemes/banana.png)

```python
# Banana, a light theme inspired by bananas
text_color = "#331f00"
background_color = "#fff3bf"
button_color = "#b7eb76"
button_hover_color = "#f0ee82"
button_pressed_color = background_color
text_area_color = button_hover_color
echo_area_color = button_hover_color
```
