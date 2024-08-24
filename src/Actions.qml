pragma Singleton

import QtQuick
import Qt.labs.platform

import kadwsettings.backend as KAdwSettings
import org.kde.kirigami as Kirigami

Item {
    readonly property var common: [apply, loadPreset, savePreset]

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
        nameFilters: [ "Preset files (*.json)", "All files (*)" ]
    }

    Kirigami.Action {
        id: savePreset
        icon.name: "document-save"
        text: qsTr("Save Preset")
        onTriggered: savePresetDialog.open()
    }

    FileDialog {
        id: savePresetDialog
        defaultSuffix: "json"
    }
}
