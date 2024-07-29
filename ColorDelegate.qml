import QtQuick
import QtQuick.Controls as Controls
import QtQuick.Layouts
import Qt.labs.platform

import org.kde.kirigamiaddons.formcard as FormCard
import org.kde.kirigami as Kirigami

FormCard.AbstractFormDelegate {
    id: root

    property string codeText
    property string colorText
    property color color: "transparent"

    icon.name: "color-picker"
    onClicked: {
        colorDialog.currentColor = color;
        colorDialog.open();
    }

    contentItem: RowLayout {
        spacing: 0

        Kirigami.Icon {
            source: "color-picker"
            Layout.rightMargin: Kirigami.Units.largeSpacing + Kirigami.Units.smallSpacing
            implicitWidth: Kirigami.Units.iconSizes.small
            implicitHeight: Kirigami.Units.iconSizes.small
        }

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
            text: root.codeText
            elide: Text.ElideRight
            wrapMode: Text.Wrap
            maximumLineCount: 2
        }

        Controls.TextField {
            text: root.colorText ? root.colorText : root.color.toString()
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
            root.color = colorDialog.color;
        }
    }
}
