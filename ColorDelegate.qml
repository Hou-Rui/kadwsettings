import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform

import backend.kgradience as KGradience
import org.kde.kirigamiaddons.formcard as FormCard
import org.kde.kirigami as Kirigami

FormCard.AbstractFormDelegate {
    id: root

    required property string name
    property var rule: KGradience.Backend.getColorRule(name)

    onClicked: {
        colorDialog.currentColor = rule.color;
        colorDialog.open();
    }

    contentItem: RowLayout {
        spacing: 0

        Label {
            text: root.text
            elide: Text.ElideRight
            wrapMode: Text.Wrap
            maximumLineCount: 2
            Layout.rightMargin: Kirigami.Units.largeSpacing
        }

        Label {
            Layout.fillWidth: true
            color: "gray"
            text: root.name
            elide: Text.ElideRight
            wrapMode: Text.Wrap
            maximumLineCount: 2
        }

        TextField {
            id: codeField
            text: root.rule.code
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

        FormCard.FormArrow {
            Layout.leftMargin: Kirigami.Units.smallSpacing
            Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
            direction: Qt.RightArrow
            visible: root.background.visible
        }
    }

    ColorDialog {
        id: colorDialog
        onAccepted: {
            root.rule.code = colorDialog.color.toString();
        }
    }
}
