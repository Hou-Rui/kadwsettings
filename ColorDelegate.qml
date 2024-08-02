import QtQuick
import QtQuick.Controls as Controls
import QtQuick.Layouts
import Qt.labs.platform

import backend.kgradience as KGradience
import org.kde.kirigamiaddons.formcard as FormCard
import org.kde.kirigami as Kirigami

FormCard.AbstractFormDelegate {
    id: root

    required property string name
    property string code: KGradience.Backend.getCode(name)
    property color color: KGradience.Backend.getColor(name)

    onCodeChanged: {
        KGradience.Backend.setCode(name, code);
        color = KGradience.Backend.getColor(name);
    }

    icon.name: "color-picker"
    onClicked: {
        colorDialog.currentColor = color;
        colorDialog.open();
    }

    contentItem: RowLayout {
        spacing: 0

        Controls.Label {
            text: root.text
            elide: Text.ElideRight
            wrapMode: Text.Wrap
            maximumLineCount: 2
            Layout.rightMargin: Kirigami.Units.largeSpacing
        }

        Controls.Label {
            Layout.fillWidth: true
            color: "gray"
            text: root.name
            elide: Text.ElideRight
            wrapMode: Text.Wrap
            maximumLineCount: 2
        }

        Controls.TextField {
            text: root.code
            Layout.rightMargin: Kirigami.Units.largeSpacing
        }

        Rectangle {
            id: colorRect
            radius: height
            color: root.color
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
            root.code = colorDialog.color.toString();
        }
    }
}
