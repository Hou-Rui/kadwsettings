// preset_schema.py
//
// Change the look of Adwaita, with ease
// Copyright (C) 2022-2023, Gradience Team
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.

const PresetSchema = {
    "groups": [
        {
            "name": "accent_colors",
            "title": qsTr("Accent Colors"),
            "description": qsTr(
                "These colors are used across many different widgets, " +
                "often to indicate that a widget is important, interactive, " +
                "or currently active."
            ),
            "variables": [
                {
                    "name": "accent_color",
                    "title": qsTr("Standalone Color"),
                    "explanation": qsTr(
                        "The standalone colors are similar to the background " +
                        "ones, but provide better contrast when used as " +
                        "foreground color on top of a neutral background - " +
                        "for example, colorful text in a window."
                    ),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "accent_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "accent_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "destructive_colors",
            "title": qsTr("Destructive Colors"),
            "description": qsTr(
                "These colors are used to indicate dangerous actions, such " +
                "as deleting a file."
            ),
            "variables": [
                {
                    "name": "destructive_color",
                    "title": qsTr("Standalone Color"),
                    "explanation": qsTr(
                        "The standalone colors are similar to the background " +
                        "ones, but provide better contrast when used as " +
                        "foreground color on top of a neutral background - " +
                        "for example, colorful text in a window."
                    ),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "destructive_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "destructive_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "partial",
                },
            ],
        },
        {
            "name": "success_colors",
            "title": qsTr("Success Colors"),
            "description": qsTr(
                "These colors are used across many different widgets, " +
                "to indicate success or a high level."
            ),
            "variables": [
                {
                    "name": "success_color",
                    "title": qsTr("Standalone Color"),
                    "explanation": qsTr(
                        "The standalone colors are similar to the background " +
                        "ones, but provide better contrast when used as " +
                        "foreground color on top of a neutral background - " +
                        "for example, colorful text in a window."
                    ),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "success_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "success_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "partial",
                },
            ],
        },
        {
            "name": "warning_colors",
            "title": qsTr("Warning Colors"),
            "description": qsTr(
                "These colors are used across many different widgets, " +
                "to indicate warning or a low level."
            ),
            "variables": [
                {
                    "name": "warning_color",
                    "title": qsTr("Standalone Color"),
                    "explanation": qsTr(
                        "The standalone colors are similar to the background " +
                        "ones, but provide better contrast when used as " +
                        "foreground color on top of a neutral background - " +
                        "for example, colorful text in a window."
                    ),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "warning_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "warning_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "partial",
                },
            ],
        },
        {
            "name": "error_colors",
            "title": qsTr("Error Colors"),
            "description": qsTr(
                "These colors are used across many different widgets, " +
                "to indicate a failure."
            ),
            "variables": [
                {
                    "name": "error_color",
                    "title": qsTr("Standalone Color"),
                    "explanation": qsTr(
                        "The standalone colors are similar to the background " +
                        "ones, but provide better contrast when used as " +
                        "foreground color on top of a neutral background - " +
                        "for example, colorful text in a window."
                    ),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "error_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "error_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "partial",
                },
            ],
        },
        {
            "name": "window_colors",
            "title": qsTr("Window Colors"),
            "description": qsTr("These colors are used primarily for windows."),
            "variables": [
                {
                    "name": "window_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "window_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "view_colors",
            "title": qsTr("View Colors"),
            "description": qsTr(
                "These colors are used across many different widgets, " +
                "such as text views and entries."
            ),
            "variables": [
                {
                    "name": "view_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "view_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "headerbar_colors",
            "title": qsTr("Header Bar Colors"),
            "description": qsTr(
                "These colors are used for header bars, as well as widgets " +
                "that are meant to be visually attached to it, such as " +
                "search bars or tab bars."
            ),
            "variables": [
                {
                    "name": "headerbar_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "headerbar_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "headerbar_border_color",
                    "title": qsTr("Border Color"),
                    "explanation": qsTr(
                        "The border color has the same default value as a " +
                        "foreground color, but doesn't change along with it. " +
                        "This can be useful if a light window has a dark " +
                        "header bar with light text; in this case it may be " +
                        "desirable to keep the border dark. This variable is " +
                        "only used for vertical borders - for example, " +
                        "separators between the two header bars in a split " +
                        "header bar layout."
                    ),
                    "adw_gtk3_support": "no",
                },
                {
                    "name": "headerbar_backdrop_color",
                    "title": qsTr("Backdrop Color"),
                    "explanation": qsTr(
                        "The backdrop color is used instead of the " +
                        "background color when the window is not focused. By " +
                        "default it's an alias of the window's background " +
                        "color and changes together with it. When changing " +
                        "this variable, make sure to set it to a value " +
                        "matching your header bar background color."
                    ),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "headerbar_shade_color",
                    "title": qsTr("Shade Color"),
                    "explanation": qsTr(
                        "The shade color is used to provide a dark border " +
                        "for header bars and similar widgets that separates " +
                        "them from the main window."
                    ),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "sidebar_colors",
            "title": qsTr("Sidebar Colors"),
            "description": qsTr(
                "These colors are used for sidebars, generally attached to the left " +
                "or right sides of a window. They are used by AdwNavigationSplitView " +
                "and AdwOverlaySplitView when they are not collapsed."
            ),
            "variables": [
                {
                    "name": "sidebar_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "sidebar_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "sidebar_backdrop_color",
                    "title": qsTr("Backdrop Color"),
                    "explanation": qsTr(
                        "The backdrop color is used instead of the " +
                        "background color when the window is not focused. By " +
                        "default it's an alias of the window's background " +
                        "color and changes together with it. When changing " +
                        "this variable, make sure to set it to a value " +
                        "matching your header bar background color."
                    ),
                    "adw_gtk3_support": "no",
                },
                {
                    "name": "sidebar_shade_color",
                    "title": qsTr("Shade Color"),
                    "explanation": qsTr(
                        "The shade color is used to provide a dark border " +
                        "for header bars and similar widgets that separates " +
                        "them from the main window."
                    ),
                    "adw_gtk3_support": "no",
                },
            ],
        },
        {
            "name": "secondary_sidebar_colors",
            "title": qsTr("Secondary Sidebar Colors"),
            "description": qsTr(
                "These colors are used for middle panes in triple-pane layouts,  " +
                "created via nesting two split views within one another."
            ),
            "variables": [
                {
                    "name": "secondary_sidebar_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "no",
                },
                {
                    "name": "secondary_sidebar_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "no",
                },
                {
                    "name": "secondary_sidebar_backdrop_color",
                    "title": qsTr("Backdrop Color"),
                    "explanation": qsTr(
                        "The backdrop color is used instead of the " +
                        "background color when the window is not focused. By " +
                        "default it's an alias of the window's background " +
                        "color and changes together with it. When changing " +
                        "this variable, make sure to set it to a value " +
                        "matching your header bar background color."
                    ),
                    "adw_gtk3_support": "no",
                },
                {
                    "name": "secondary_sidebar_shade_color",
                    "title": qsTr("Shade Color"),
                    "explanation": qsTr(
                        "The shade color is used to provide a dark border " +
                        "for header bars and similar widgets that separates " +
                        "them from the main window."
                    ),
                    "adw_gtk3_support": "no",
                },
            ],
        },
        {
            "name": "card_colors",
            "title": qsTr("Card Colors"),
            "description": qsTr("These colors are used for cards and boxed lists."),
            "variables": [
                {
                    "name": "card_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "card_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "card_shade_color",
                    "title": qsTr("Shade Color"),
                    "explanation": qsTr(
                        "The shade color is used for shadows that are used " +
                        "by cards to separate themselves from the window " +
                        "background, as well as for row dividers in the cards."
                    ),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "thumbnail_colors",
            "title": qsTr("Thumbnail Colors"),
            "description": qsTr("These colors are used for Tab Overview thumbnails."),
            "variables": [
                {
                    "name": "thumbnail_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "thumbnail_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "dialog_colors",
            "title": qsTr("Dialog Colors"),
            "description": qsTr("These colors are used for message dialogs."),
            "variables": [
                {
                    "name": "dialog_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "dialog_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
            ],
        },
        {
            "name": "popover_colors",
            "title": qsTr("Popover Colors"),
            "description": qsTr("These colors are used for popovers."),
            "variables": [
                {
                    "name": "popover_bg_color",
                    "title": qsTr("Background Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "popover_fg_color",
                    "title": qsTr("Foreground Color"),
                    "adw_gtk3_support": "yes",
                },
                {
                    "name": "popover_shade_color",
                    "title": qsTr("Shade Color"),
                    "explanation": qsTr(
                        "The shade color is used for scroll undershoot styles within popovers, " +
                        "as well as transitions in AdwNavigationView, AdwOverlaySplitView, " +
                        "AdwLeaflet and AdwFlap."
                    ),
                    "adw_gtk3_support": "no",
                },
            ],
        },
        {
            "name": "misc_colors",
            "title": qsTr("Miscellaneous Colors"),
            "description": qsTr("Colors that don't fit in any particular group."),
            "variables": [
                {
                    "name": "shade_color",
                    "title": qsTr("Shade Color"),
                    "explanation": qsTr(
                        "The shade color is used by inline tab bars, as well " +
                        "as the transitions in leaflets and flaps, and info " +
                        "bar borders."
                    ),
                    "adw_gtk3_support": "no",
                },
                {
                    "name": "scrollbar_outline_color",
                    "title": qsTr("Scrollbar Outline Color"),
                    "explanation": qsTr(
                        "The scrollbar outline color is used by scrollbars " +
                        "to ensure that overlay scrollbars are visible " +
                        "regardless of the content color."
                    ),
                    "adw_gtk3_support": "no",
                },
            ],
        },
    ],
    "palette": [
        {"prefix": "blue_", "title": qsTr("Blue"), "n_shades": 5},
        {"prefix": "green_", "title": qsTr("Green"), "n_shades": 5},
        {"prefix": "yellow_", "title": qsTr("Yellow"), "n_shades": 5},
        {"prefix": "orange_", "title": qsTr("Orange"), "n_shades": 5},
        {"prefix": "red_", "title": qsTr("Red"), "n_shades": 5},
        {"prefix": "purple_", "title": qsTr("Purple"), "n_shades": 5},
        {"prefix": "brown_", "title": qsTr("Brown"), "n_shades": 5},
        {"prefix": "light_", "title": qsTr("Light"), "n_shades": 5},
        {"prefix": "dark_", "title": qsTr("Dark"), "n_shades": 5},
    ],
    "custom_css_app_types": ["gtk4", "gtk3"]
}
