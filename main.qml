pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import backend.kgradience as KGradience
import org.kde.kirigami as Kirigami
import org.kde.kirigamiaddons.formcard as FormCard

Kirigami.ApplicationWindow {
    id: root
    width: 800
    height: 600
    visible: true

    pageStack.initialPage: paletteColorsPage

    Kirigami.ScrollablePage {
        id: paletteColorsPage
        title: qsTr("Palette Colors")
        visible: false

        ColumnLayout {
            implicitWidth: parent.width

            Repeater {
                model: ["blue", "green", "yellow", "orange", "red", "purple", "brown", "light", "dark"]

                ColumnLayout {
                    id: modelItem
                    Layout.fillWidth: true
                    required property string modelData

                    FormCard.FormHeader {
                        title: modelItem.modelData
                    }

                    FormCard.FormCard {
                        Layout.fillWidth: true
                        Repeater {
                            model: 5
                            ColorDelegate {
                                required property int index
                                text: `#${index + 1}`
                                codeText: `${modelItem.modelData}_${index + 1}`
                                color: backend.getColor(codeText)
                            }
                        }
                    }
                }
            }
        }
    }

    Kirigami.ScrollablePage {
        id: namedColorsPage
        title: qsTr("Named Colors")
        visible: false

        ColumnLayout {
            implicitWidth: parent.width

            FormCard.FormHeader {
                title: qsTr("Header Color")
            }

            FormCard.FormCard {
                Repeater {
                    model: ['accent_color', 'accent_bg_color', 'accent_fg_color', 'destructive_color', 'destructive_bg_color', 'destructive_fg_color', 'success_color', 'success_bg_color', 'success_fg_color', 'warning_color', 'warning_bg_color', 'warning_fg_color', 'error_color', 'error_bg_color', 'error_fg_color', 'window_bg_color', 'window_fg_color', 'view_bg_color', 'view_fg_color', 'headerbar_bg_color', 'headerbar_fg_color', 'headerbar_border_color', 'headerbar_backdrop_color', 'headerbar_shade_color', 'card_bg_color', 'card_fg_color', 'card_shade_color', 'dialog_bg_color', 'dialog_fg_color', 'popover_bg_color', 'popover_fg_color', 'shade_color', 'scrollbar_outline_color', 'sidebar_bg_color', 'sidebar_fg_color', 'sidebar_backdrop_color', 'sidebar_shade_color', 'secondary_sidebar_bg_color', 'secondary_sidebar_fg_color', 'secondary_sidebar_backdrop_color', 'secondary_sidebar_shade_color', 'thumbnail_bg_color', 'thumbnail_fg_color', 'popover_shade_color']
                    ColorDelegate {
                        required property string modelData
                        codeText: modelData
                        colorText: backend.getRuleText(modelData)
                        color: backend.getColor(`@${codeText}`)
                    }
                }
            }
        }
    }

    Kirigami.Page {
        id: customStylesPage
        title: qsTr("Custom Styles")
        visible: false
    }

    component NavigationTabAction: Kirigami.Action {
        required property string iconName
        required property Page page

        icon.name: iconName
        text: page.title
        checked: page.visible
        onTriggered: {
            if (!page.visible) {
                while (root.pageStack.depth > 0) {
                    root.pageStack.pop();
                }
                root.pageStack.push(page);
            }
        }
    }

    footer: Kirigami.NavigationTabBar {
        actions: [
            NavigationTabAction {
                iconName: "draw-brush"
                page: paletteColorsPage
            },
            NavigationTabAction {
                iconName: "format-text-color"
                page: namedColorsPage
            },
            NavigationTabAction {
                iconName: "code-context"
                page: customStylesPage
            }
        ]
    }

    KGradience.Backend {
        id: backend
    }
}
