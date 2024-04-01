# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Agregados Startup
import os
import subprocess
from libqtile import hook

# Originales
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.layout import floating
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import WindowName
import re
from libqtile.widget import backlight
from libqtile.widget import GenPollText
from libqtile.config import Key

# Variales
fuente = "HackNerdFont"
blanco = "ffffff"
morado = "a15cef"
plomo = "404040"
arch_size = 24
arch_color = "#1793D1"
iconos_sizes = 17
path_archivos = "/home/pablo/.config/qtile/Complementos/"


# Funciones
# Separador
def separador():
    return widget.Sep(
        linewidth=1,
        padding=10,
        size_percent=70,
    )


# texto Utilizado para modificar widget.WindowName
def texto(text):
    if ("pablo@arch:" in text) | ("root@arch:" in text):
        text = text.replace("pablo@arch:", "Terminal: ")
        text = text.replace("root@arch:", "Terminal(root): ")
    if "Mozilla Firefox" in text:
        text = "Firefox"
    if "nvim " in text:
        text = "Nvim"
    if "/home/pablo/Documents/Calibre Library/" in text:
        text = "Zathura"
    return text


def obtener_nota():
    try:
        with open(path_archivos + "nota.txt", "r") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        contenido = "Empty file"
    return contenido


def obtener_ip():
    try:
        with open(path_archivos + "ip.txt", "r") as archivo:
            contenido = archivo.readline().strip()
    except FileNotFoundError:
        contenido = "Empty file"
    return contenido


widget_nota = GenPollText(func=obtener_nota, update_interval=5)
widget_ip = GenPollText(
    func=obtener_ip,
    update_interval=60,
)

# Configuracion
mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "c", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Open kitty terminal"),
    Key(
        [mod, "control"], "Return", lazy.spawn("alacritty"), desc="Open kitty terminal"
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Previous layout"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Comandos propios
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Open Rofi"),
    Key([mod, "shift"], "f", lazy.spawn("firejail firefox"), desc="Open Firefox"),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("i3lock -u -i /home/pablo/Pictures/i3.png"),
        desc="Open i3lock",
    ),
    Key([mod], "e", lazy.spawn("thunar"), desc="Open Thunar"),
    Key([mod], "y", lazy.hide_show_bar("top")),
    Key(
        [mod],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Run flameshot"),
    Key([mod], "q", lazy.spawn("qalculate-gtk"), desc="Run flameshot"),
    Key(
        ["control", "mod1"],
        "t",
        lazy.spawn("alacritty --class Alacritty-float"),
        desc="Open Alacritty Float",
    ),
    Key(
        [mod, "shift"],
        "t",
        lazy.window.toggle_floating(),
        lazy.window.set_size_floating(600, 400),
        lazy.window.center(),
        desc="Move the floating window at the center",
    ),
    Key(
        [mod, "control"],
        "t",
        lazy.window.toggle_floating(),
        lazy.window.set_size_floating(600, 400),
        lazy.window.set_position(989, 41),
        desc="Move the floating window at the top right",
    ),
    Key([mod], "o", lazy.window.move_to_bottom(), desc="Mover la ventana hacia atras"),
    Key(
        [mod, "shift"],
        "o",
        lazy.window.move_to_top(),
        desc="Mover la ventana hacia adelante",
    ),
    Key([mod], "b", lazy.group.focus_back(), desc="Mover la ventana hacia atras"),
    # Mover apps entre ventanas
    Key([mod], "bracketright", lazy.screen.next_group(), desc="Move to next group"),
    Key([mod], "bracketleft", lazy.screen.prev_group(), desc="Move to previous group"),
    Key([mod, "shift"], "1", lazy.window.togroup("1")),
    Key([mod, "shift"], "2", lazy.window.togroup("2")),
    Key([mod, "shift"], "3", lazy.window.togroup("3")),
    Key([mod, "shift"], "4", lazy.window.togroup("4")),
    Key([mod, "shift"], "5", lazy.window.togroup("5")),
    Key([mod, "shift"], "6", lazy.window.togroup("6")),
    # Ventanas flotantes
    Key(
        [mod, "mod1"],
        "t",
        lazy.window.center(),
        desc="Move the floating window at the center",
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.window.move_floating(-20, 0),
        desc="Mover ventana flotante izquierda",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.window.move_floating(20, 0),
        desc="Mover ventana flotante derecha",
    ),
    Key(
        [mod, "shift"],
        "Up",
        lazy.window.move_floating(0, -20),
        desc="Mover ventana flotante arriba",
    ),
    Key(
        [mod, "shift"],
        "Down",
        lazy.window.move_floating(0, 20),
        desc="Mover ventana flotante abajo",
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.window.resize_floating(-20, 0),
        desc="Resize ventana flotante izquierda",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.window.resize_floating(20, 0),
        desc="Resize ventana flotante izquierda",
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.window.resize_floating(0, -20),
        desc="Resize ventana flotante izquierda",
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.window.resize_floating(0, 20),
        desc="Resize ventana flotante izquierda",
    ),
]

groups = [Group(i) for i in ["", "", "󰝰", "", "󱓞", "", "", "󰙯", ""]]

for i, group in enumerate(groups):
    escritorio = str(i + 1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                escritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                escritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_width=0,
        margin=8,
    ),
    layout.Max(
        margin=8,
    ),
    layout.Spiral(
        border_width=0,
        margin=8,
    ),
    layout.MonadWide(
        border_width=0,
        margin=8,
    ),
    layout.RatioTile(
        border_width=0,
        margin=8,
    ),
]

widget_defaults = dict(
    font=fuente,
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text=" 󰣇 ",
                    fontsize=arch_size,
                    foreground=arch_color,
                ),
                separador(),
                widget.GroupBox(
                    active=blanco,
                    inactive=plomo,
                    disable_drag=True,
                    highlight_method="text",
                    center_aligned=True,
                    fontsize=iconos_sizes,
                    hide_unused=False,
                    padding=6,
                    this_current_screen_border=morado,
                    urgent_border="#010000",
                ),
                separador(),
                widget.WindowName(
                    parse_text=texto,
                ),
                widget.Spacer(),
                separador(),
                widget.WidgetBox(
                    [
                        separador(),
                        widget.Net(
                            format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}",
                        ),
                        separador(),
                        widget.DF(
                            measure="G",
                            partition="/",
                            warn_space=10,
                            visible_on_warn=False,
                        ),
                        separador(),
                        widget.Memory(
                            measure_mem="G",
                        ),
                        separador(),
                        widget.CPU(
                            padding=5,
                            foreground=blanco,
                        ),
                        separador(),
                        widget_ip,
                    ],
                    text_open="[>] System",
                    text_closed="[<] System",
                ),
                separador(),
                widget_nota,
                separador(),
                widget.CurrentLayout(),
                separador(),
                widget.TextBox(
                    text="󱂬 ",
                    fontsize=19,
                ),
                widget.WindowCount(
                    show_zero=True,
                ),
                separador(),
                widget.Systray(
                    icon_size=iconos_sizes,
                    padding=5,
                ),
                separador(),
                widget.Clock(
                    format="%a %d-%m-%Y %H:%M",
                    foreground=blanco,
                ),
                separador(),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "es"],
                ),
                separador(),
                widget.Spacer(length=10),
            ],
            30,
            background="#010000",
            opacity=0.85,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            border_color=[
                "ffffff",
                "ffffff",
                "404040",
                "ffffff",
            ],  # Borders are magenta
            margin=[5, 10, 0, 10],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    # Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Alacritty-float"),
        Match(wm_class="Qalculate-gtk"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# Parte de Startup
# Al iniciar ejecuta autostart.sh
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])
    subprocess.Popen([home + "/.config/qtile/ip.sh"])
