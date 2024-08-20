#!/bin/sh

PREFIX="${1:-/usr}"
PROJECT='kadwsettings'
TMPRUN='run.sh'

SHARE_DIR="$PREFIX/share/$PROJECT"
ICON_DIR="$PREFIX/share/icons/hicolor"
APPL_DIR="$PREFIX/share/applications"

install -Dm 644 ./*.py -t "$SHARE_DIR"
install -Dm 644 ./*.qml -t "$SHARE_DIR"
install -Dm 644 ./*.js -t "$SHARE_DIR"
install -Dm 644 ./*.desktop -t "$APPL_DIR"

for size in icons/*; do
  sub_dir="$(basename "$size")/apps"
  install -Dm 644 "icons/$sub_dir/"* -t "$ICON_DIR/$sub_dir"
done

echo '#!/bin/sh' >"$TMPRUN"
echo "python \"$SHARE_DIR/main.py\"" >> "$TMPRUN"
install -Dm 755 "$TMPRUN" -T "$PREFIX/bin/$PROJECT"
rm "$TMPRUN"
