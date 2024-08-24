import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform

import kadwsettings.backend as KAdwSettings
import org.kde.kirigamiaddons.formcard as FormCard
import org.kde.kirigami as Kirigami

FormCard.AbstractFormDelegate {
    id: root

    required property string name
    property var rule: KAdwSettings.Preset.rule(name)

    contentItem: RowLayout {
        spacing: 0

        ColumnLayout {
            Layout.rightMargin: Kirigami.Units.largeSpacing
            Layout.fillWidth: true
            Label {
                text: root.text
                elide: Text.ElideRight
                Layout.fillWidth: true
            }
            Label {
                text: root.rule.name
                color: Kirigami.Theme.disabledTextColor
                elide: Text.ElideRight
                Layout.fillWidth: true
            }
        }

        Label {
            visible: !editCodeButton.checked
            text: root.rule.code
            color: Kirigami.Theme.disabledTextColor
            Layout.rightMargin: Kirigami.Units.largeSpacing
        }

        TextField {
            id: codeField
            visible: editCodeButton.checked
            text: root.rule.code
            Layout.fillWidth: true
            Layout.rightMargin: Kirigami.Units.largeSpacing
            Binding {
                target: root.rule
                property: 'code'
                value: codeField.text
            }
        }

        Rectangle {
            id: colorRect
            radius: height
            color: root.rule.color
            Layout.preferredWidth: Kirigami.Units.iconSizes.small
            Layout.preferredHeight: Kirigami.Units.iconSizes.small
            Layout.rightMargin: Kirigami.Units.largeSpacing
        }

        Button {
            id: editCodeButton
            checkable: true
            icon.name: "document-edit"
            Layout.rightMargin: Kirigami.Units.largeSpacing
        }

        Button {
            icon.name: "color-picker"
            onClicked: {
                colorDialog.currentColor = root.rule.color;
                colorDialog.open();
            }
        }
    }

    ColorDialog {
        id: colorDialog
        onAccepted: {
            root.rule.code = colorDialog.color.toString();
        }
    }
}
