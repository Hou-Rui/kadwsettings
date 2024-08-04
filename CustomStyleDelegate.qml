import QtQuick.Controls as Controls

import backend.kgradience as KGradience
import org.kde.kirigamiaddons.formcard as FormCard

FormCard.AbstractFormDelegate {
    contentItem: Controls.ScrollView {
		Controls.TextArea {
			text: KGradience.Backend.getCustomStyle()
			font.family: "monospace"
		}
	}
}