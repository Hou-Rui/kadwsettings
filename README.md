# KAdwSettings

`KAdwSettings` is a utility to adjust the appearance of GTK4 libadwaita programs, written in PySide6 + Kirigami. It can be seen as a Qt alternative to abandoned [Gradience](https://github.com/GradienceTeam/Gradience). Pull requests are welcome.

## Requirements

- Python 3.9+
- PySide 6.7+
- Kirigami 2.0+
- Kirigami Addons 1.1+

## Installation

Simply run `./install.sh ~/.local` to install locally or `sudo ./install.sh /usr/local` to install globally. Proper packaging for distributions is planned for future.

## Features

- Customize palette and named colors for libadwaita programs
- Edit custom styles using CSS
- Read & save Gradience presets

## Target Users

- Users seeking a maintained alternative to Gradience
- Users using libadwaita programs in non-GNOME desktops (especially KDE Plasma) and want them to blend in aesthetically.

## Not Planned

- Be a full clone for Gradience
- Support GTK 3 (or adw-gtk3)
- Support GNOME Shell customization / Firefox GNOME theme
