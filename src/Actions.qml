pragma Singleton

import QtQuick
import Qt.labs.platform

import kadwsettings.backend as KAdwSettings
import org.kde.kirigami as Kirigami

Item {
    id: root
    readonly property list<Kirigami.Action> common: [apply, loadPreset, savePreset]
    readonly property list<string> nameFilter: [`${qsTr("Preset files")} (*.json)`, `${qsTr("All files")} (*)`]

    Kirigami.Action {
        id: apply
        icon.name: "dialog-ok-apply"
        text: qsTr("Apply")
        onTriggered: KAdwSettings.Preset.saveCss()
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
