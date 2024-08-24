from PySide6.QtCore import QObject


class Schema(QObject):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def data(self):
        return {
            "groups": [
                {
                    "name": "accent_colors",
                    "title": self.tr("Accent Colors"),
                    "description": self.tr(
                        "These colors are used across many different widgets, " +
                        "often to indicate that a widget is important, interactive, " +
                        "or currently active."
                    ),
                    "variables": [
                        {
                            "name": "accent_color",
                            "title": self.tr("Standalone Color"),
                            "explanation": self.tr(
                                "The standalone colors are similar to the background " +
                                "ones, but provide better contrast when used as " +
                                "foreground color on top of a neutral background - " +
                                "for example, colorful text in a window."
                            ),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "accent_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "accent_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                    ],
                },
                {
                    "name": "destructive_colors",
                    "title": self.tr("Destructive Colors"),
                    "description": self.tr(
                        "These colors are used to indicate dangerous actions, such " +
                        "as deleting a file."
                    ),
                    "variables": [
                        {
                            "name": "destructive_color",
                            "title": self.tr("Standalone Color"),
                            "explanation": self.tr(
                                "The standalone colors are similar to the background " +
                                "ones, but provide better contrast when used as " +
                                "foreground color on top of a neutral background - " +
                                "for example, colorful text in a window."
                            ),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "destructive_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "destructive_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "partial",
                        },
                    ],
                },
                {
                    "name": "success_colors",
                    "title": self.tr("Success Colors"),
                    "description": self.tr(
                        "These colors are used across many different widgets, " +
                        "to indicate success or a high level."
                    ),
                    "variables": [
                        {
                            "name": "success_color",
                            "title": self.tr("Standalone Color"),
                            "explanation": self.tr(
                                "The standalone colors are similar to the background " +
                                "ones, but provide better contrast when used as " +
                                "foreground color on top of a neutral background - " +
                                "for example, colorful text in a window."
                            ),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "success_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "success_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "partial",
                        },
                    ],
                },
                {
                    "name": "warning_colors",
                    "title": self.tr("Warning Colors"),
                    "description": self.tr(
                        "These colors are used across many different widgets, " +
                        "to indicate warning or a low level."
                    ),
                    "variables": [
                        {
                            "name": "warning_color",
                            "title": self.tr("Standalone Color"),
                            "explanation": self.tr(
                                "The standalone colors are similar to the background " +
                                "ones, but provide better contrast when used as " +
                                "foreground color on top of a neutral background - " +
                                "for example, colorful text in a window."
                            ),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "warning_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "warning_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "partial",
                        },
                    ],
                },
                {
                    "name": "error_colors",
                    "title": self.tr("Error Colors"),
                    "description": self.tr(
                        "These colors are used across many different widgets, " +
                        "to indicate a failure."
                    ),
                    "variables": [
                        {
                            "name": "error_color",
                            "title": self.tr("Standalone Color"),
                            "explanation": self.tr(
                                "The standalone colors are similar to the background " +
                                "ones, but provide better contrast when used as " +
                                "foreground color on top of a neutral background - " +
                                "for example, colorful text in a window."
                            ),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "error_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "error_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "partial",
                        },
                    ],
                },
                {
                    "name": "window_colors",
                    "title": self.tr("Window Colors"),
                    "description": self.tr("These colors are used primarily for windows."),
                    "variables": [
                        {
                            "name": "window_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "window_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                    ],
                },
                {
                    "name": "view_colors",
                    "title": self.tr("View Colors"),
                    "description": self.tr(
                        "These colors are used across many different widgets, " +
                        "such as text views and entries."
                    ),
                    "variables": [
                        {
                            "name": "view_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "view_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                    ],
                },
                {
                    "name": "headerbar_colors",
                    "title": self.tr("Header Bar Colors"),
                    "description": self.tr(
                        "These colors are used for header bars, as well as widgets " +
                        "that are meant to be visually attached to it, such as " +
                        "search bars or tab bars."
                    ),
                    "variables": [
                        {
                            "name": "headerbar_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "headerbar_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "headerbar_border_color",
                            "title": self.tr("Border Color"),
                            "explanation": self.tr(
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
                            "title": self.tr("Backdrop Color"),
                            "explanation": self.tr(
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
                            "title": self.tr("Shade Color"),
                            "explanation": self.tr(
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
                    "title": self.tr("Sidebar Colors"),
                    "description": self.tr(
                        "These colors are used for sidebars, generally attached to the left " +
                        "or right sides of a window. They are used by AdwNavigationSplitView " +
                        "and AdwOverlaySplitView when they are not collapsed."
                    ),
                    "variables": [
                        {
                            "name": "sidebar_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "sidebar_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "sidebar_backdrop_color",
                            "title": self.tr("Backdrop Color"),
                            "explanation": self.tr(
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
                            "title": self.tr("Shade Color"),
                            "explanation": self.tr(
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
                    "title": self.tr("Secondary Sidebar Colors"),
                    "description": self.tr(
                        "These colors are used for middle panes in triple-pane layouts,  " +
                        "created via nesting two split views within one another."
                    ),
                    "variables": [
                        {
                            "name": "secondary_sidebar_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "no",
                        },
                        {
                            "name": "secondary_sidebar_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "no",
                        },
                        {
                            "name": "secondary_sidebar_backdrop_color",
                            "title": self.tr("Backdrop Color"),
                            "explanation": self.tr(
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
                            "title": self.tr("Shade Color"),
                            "explanation": self.tr(
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
                    "title": self.tr("Card Colors"),
                    "description": self.tr("These colors are used for cards and boxed lists."),
                    "variables": [
                        {
                            "name": "card_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "card_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "card_shade_color",
                            "title": self.tr("Shade Color"),
                            "explanation": self.tr(
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
                    "title": self.tr("Thumbnail Colors"),
                    "description": self.tr("These colors are used for Tab Overview thumbnails."),
                    "variables": [
                        {
                            "name": "thumbnail_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "thumbnail_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                    ],
                },
                {
                    "name": "dialog_colors",
                    "title": self.tr("Dialog Colors"),
                    "description": self.tr("These colors are used for message dialogs."),
                    "variables": [
                        {
                            "name": "dialog_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "dialog_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                    ],
                },
                {
                    "name": "popover_colors",
                    "title": self.tr("Popover Colors"),
                    "description": self.tr("These colors are used for popovers."),
                    "variables": [
                        {
                            "name": "popover_bg_color",
                            "title": self.tr("Background Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "popover_fg_color",
                            "title": self.tr("Foreground Color"),
                            "adw_gtk3_support": "yes",
                        },
                        {
                            "name": "popover_shade_color",
                            "title": self.tr("Shade Color"),
                            "explanation": self.tr(
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
                    "title": self.tr("Miscellaneous Colors"),
                    "description": self.tr("Colors that don't fit in any particular group."),
                    "variables": [
                        {
                            "name": "shade_color",
                            "title": self.tr("Shade Color"),
                            "explanation": self.tr(
                                "The shade color is used by inline tab bars, as well " +
                                "as the transitions in leaflets and flaps, and info " +
                                "bar borders."
                            ),
                            "adw_gtk3_support": "no",
                        },
                        {
                            "name": "scrollbar_outline_color",
                            "title": self.tr("Scrollbar Outline Color"),
                            "explanation": self.tr(
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
                {"prefix": "blue_", "title": self.tr("Blue"), "n_shades": 5},
                {"prefix": "green_", "title": self.tr("Green"), "n_shades": 5},
                {"prefix": "yellow_", "title": self.tr(
                    "Yellow"), "n_shades": 5},
                {"prefix": "orange_", "title": self.tr(
                    "Orange"), "n_shades": 5},
                {"prefix": "red_", "title": self.tr("Red"), "n_shades": 5},
                {"prefix": "purple_", "title": self.tr(
                    "Purple"), "n_shades": 5},
                {"prefix": "brown_", "title": self.tr("Brown"), "n_shades": 5},
                {"prefix": "light_", "title": self.tr("Light"), "n_shades": 5},
                {"prefix": "dark_", "title": self.tr("Dark"), "n_shades": 5},
            ],
            "custom_css_app_types": ["gtk4", "gtk3"]
        }
