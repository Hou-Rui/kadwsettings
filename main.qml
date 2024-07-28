pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

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
                model: ['Blue', 'Red', 'Light', 'Dark']

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
                            FormCard.FormColorDelegate {
                                required property int index
                                text: `${modelItem.modelData} #${index + 1}`
                                color: {
                                    const c = 1.0 / 10 * (5 - index);
                                    return Qt.rgba(c, c, c, 1);
                                }
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
                FormCard.FormTextFieldDelegate {
                    label: qsTr("Standalone Color")
                }
                FormCard.FormTextFieldDelegate {
                    label: qsTr("Background Color")
                }
                FormCard.FormTextFieldDelegate {
                    label: qsTr("Foreground Color")
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
                iconName: "settings"
                page: customStylesPage
            }
        ]
    }
}
