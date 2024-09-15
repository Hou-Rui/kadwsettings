import QtQuick
import QtQuick.Controls
import Qt.labs.platform

import kadwsettings.backend as KAdwSettings
import org.kde.kirigami as Kirigami

Item {
    id: root
    required property Kirigami.ApplicationWindow window
    readonly property list<Kirigami.Action> actions: [changePresetName, apply, loadPreset, savePreset]
    readonly property list<string> nameFilter: [
        `${qsTr("Preset JSON files")} (*.json)`,
        `${qsTr("All files")} (*)`,
    ]

    Kirigami.Action {
        id: apply
        icon.name: "dialog-ok-apply"
        text: qsTr("Apply")
        onTriggered: KAdwSettings.Preset.saveCss()
    }

    Kirigami.Action {
        id: changePresetName
        icon.name: "document-edit"
        text: qsTr("Change Preset Name")
        onTriggered: changePresetNameDialog.open()
    }

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

    Kirigami.Action {
        id: loadPreset
        icon.name: "list-add"
        text: qsTr("Load Preset")
        onTriggered: loadPresetDialog.open()
    }

    FileDialog {
        id: loadPresetDialog
        title: qsTr("Load Preset File")
        nameFilters: root.nameFilter
        onAccepted: KAdwSettings.Preset.loadJson(file)
    }

    Kirigami.Action {
        id: savePreset
        icon.name: "document-save"
        text: qsTr("Save Preset")
        onTriggered: savePresetDialog.open()
    }

    FileDialog {
        id: savePresetDialog
        title: qsTr("Save Preset File")
        nameFilters: root.nameFilter
        fileMode: FileDialog.SaveFile
        onAccepted: KAdwSettings.Preset.saveJson(file)
    }
}
