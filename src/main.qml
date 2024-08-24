pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import backend.kadwsettings as KAdwSettings
import org.kde.kirigami as Kirigami
import org.kde.kirigamiaddons.formcard as FormCard

import "PresetSchema.js" as PresetSchema

Kirigami.ApplicationWindow {
    id: root
    width: 40 * Kirigami.Units.gridUnit
    minimumWidth: 30 * Kirigami.Units.gridUnit
    height: 30 * Kirigami.Units.gridUnit
    visible: true

    pageStack.initialPage: paletteColorsPage

    Kirigami.Action {
        id: applyAction
        icon.name: "dialog-ok-apply"
        text: qsTr("Apply")
        onTriggered: KAdwSettings.Backend.save()
    }

    Kirigami.Action {
        id: loadPresetAction
        icon.name: "list-add"
        text: qsTr("Load Preset")
    }

    Kirigami.Action {
        id: savePresetAction
        icon.name: "document-save"
        text: qsTr("Save Preset")
    }

    FormCard.FormCardPage {
        id: paletteColorsPage
        title: qsTr("Palette Colors")
        visible: false
        actions: [loadPresetAction, savePresetAction, applyAction]

        Repeater {
            model: PresetSchema.data.palette

            ColumnLayout {
                id: palette
                required property var modelData

                FormCard.FormHeader {
                    title: palette.modelData.title
                }

                FormCard.FormCard {
                    Repeater {
                        model: palette.modelData.n_shades

                        ColorDelegate {
                            required property int index
                            readonly property int shade: index + 1
                            text: `${palette.modelData.title} #${shade}`
                            name: palette.modelData.prefix + shade
                        }
                    }
                }
            }
        }
    }

    FormCard.FormCardPage {
        id: namedColorsPage
        title: qsTr("Named Colors")
        visible: false
        actions: [loadPresetAction, savePresetAction, applyAction]

        Repeater {
            model: PresetSchema.data.groups

            ColumnLayout {
                id: group
                required property var modelData

                FormCard.FormHeader {
                    id: titleHeader
                    title: group.modelData.title
                    Layout.bottomMargin: 0
                }

                FormCard.FormSectionText {
                    text: group.modelData.description
                    leftPadding: titleHeader.leftPadding
                    rightPadding: titleHeader.rightPadding
                    Layout.topMargin: 0
                }

                FormCard.FormCard {
                    Repeater {
                        model: group.modelData.variables

                        ColorDelegate {
                            required property var modelData
                            text: modelData.title
                            name: modelData.name
                        }
                    }
                }
            }
        }
    }

    FormCard.FormCardPage {
        id: customStylePage
        title: qsTr("Custom Styles")
        visible: false
        actions: [loadPresetAction, savePresetAction, applyAction]

        FormCard.FormHeader {
            title: qsTr("Custom GTK 4 Styles")
        }

        FormCard.FormCard {
            CustomStylesDelegate {}
        }
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
                page: customStylePage
            }
        ]
    }
}
