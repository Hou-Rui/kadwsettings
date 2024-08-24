pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import backend.kadwsettings as KAdwSettings
import org.kde.kirigami as Kirigami
import org.kde.kirigamiaddons.formcard as FormCard

FormCard.AbstractFormDelegate {
    contentItem: RowLayout {
        spacing: 0

        ListView {
            id: lineNumbers
            property TextMetrics textMetrics: TextMetrics {
                text: "99999"
                font: codeEdit.font
            }

            Layout.fillHeight: true
            Layout.preferredWidth: textMetrics.width
            Layout.topMargin: codeEdit.topPadding
            Layout.bottomMargin: codeEdit.bottomPadding

            model: codeEdit.text.split(/\n/g)
            clip: true

            delegate: Label {
                required property string modelData
                required property int index

                width: lineNumbers.width
                height: lineText.height
                padding: 0

                Text {
                    id: lineNumber
                    text: parent.index + 1
                    anchors.horizontalCenter: parent.horizontalCenter
                    font: codeEdit.font
                    color: Kirigami.Theme.disabledTextColor
                }

                Text {
                    id: lineText
                    visible: false
                    text: parent.modelData
                    font: codeEdit.font

                    width: codeEdit.width
                    leftPadding: codeEdit.leftPadding
                    rightPadding: codeEdit.rightPadding
                    wrapMode: Text.WordWrap
                }
            }
        }

        TextEdit {
            id: codeEdit
            Layout.fillHeight: true
            Layout.fillWidth: true

            color: Kirigami.Theme.textColor
            selectedTextColor: Kirigami.Theme.highlightedTextColor
            selectionColor: Kirigami.Theme.highlightColor

            text: KAdwSettings.Backend.custom
            textFormat: Text.PlainText
            font.family: "monospace"
            wrapMode: Text.WordWrap

            Binding {
                target: KAdwSettings.Backend
                property: "custom"
                value: codeEdit.text
            }
        }
    }
}
