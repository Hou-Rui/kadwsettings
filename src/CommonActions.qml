import QtQuick
import QtQuick.Controls
import Qt.labs.platform

import kadwsettings.backend as KAdwSettings
import org.kde.kirigami as Kirigami

Item {
    id: root
    required property Kirigami.ApplicationWindow window
    readonly property list<string> nameFilter: [
        `${qsTr("Preset JSON files")} (*.json)`,
        `${qsTr("All files")} (*)`
    ]

    readonly property list<Kirigami.Action> actions: [
        Kirigami.Action {
            displayComponent: Label {
                text: qsTr(`Preset: <b>${KAdwSettings.Preset.name}</b>`)
                rightPadding: Kirigami.Units.largeSpacing
            }
        },
        Kirigami.Action {
            icon.name: "dialog-ok-apply"
            text: qsTr("Apply")
            onTriggered: KAdwSettings.Preset.saveCss()
        },
        Kirigami.Action {
            icon.name: "document-edit"
            text: qsTr("Change Preset Name")
            displayHint: Kirigami.DisplayHint.AlwaysHide
            onTriggered: changePresetNameDialog.open()
        },
        Kirigami.Action {
            icon.name: "list-add"
            text: qsTr("Load Preset")
            displayHint: Kirigami.DisplayHint.AlwaysHide
            onTriggered: loadPresetDialog.open()
        },
        Kirigami.Action {
            icon.name: "document-save"
            text: qsTr("Save Preset")
            displayHint: Kirigami.DisplayHint.AlwaysHide
            onTriggered: savePresetDialog.open()
        },
        Kirigami.Action {
            separator: true
            displayHint: Kirigami.DisplayHint.AlwaysHide
        },
        Kirigami.Action {
            icon.name: "help-about"
            text: qsTr("About")
            displayHint: Kirigami.DisplayHint.AlwaysHide
            onTriggered: root.window.pageStack.layers.push(aboutPage)
        }
    ]

    Kirigami.Dialog {
        id: changePresetNameDialog
        title: qsTr("Change Preset Name")
        standardButtons: Kirigami.Dialog.Ok | Kirigami.Dialog.Cancel
        padding: Kirigami.Units.largeSpacing
        Kirigami.FormLayout {
            TextField {
                id: nameField
                Kirigami.FormData.label: "Preset Name:"
                text: KAdwSettings.Preset.name
            }
        }
        onAccepted: KAdwSettings.Preset.name = nameField.text
    }

    FileDialog {
        id: loadPresetDialog
        title: qsTr("Load Preset File")
        nameFilters: root.nameFilter
        onAccepted: KAdwSettings.Preset.loadJson(file)
    }

    FileDialog {
        id: savePresetDialog
        title: qsTr("Save Preset File")
        nameFilters: root.nameFilter
        fileMode: FileDialog.SaveFile
        onAccepted: KAdwSettings.Preset.saveJson(file)
    }

    AboutPage {
        id: aboutPage
    }
}
