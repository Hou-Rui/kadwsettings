#!/bin/sh

PREFIX="${1:-/usr}"
PROJECT='kadwsettings'
TMPRUN='run.sh'

SRC_DIR="$PREFIX/share/$PROJECT/src"
ICON_DIR="$PREFIX/share/icons/hicolor"
APPL_DIR="$PREFIX/share/applications"

install -Dm 644 src/*.py -t "$SRC_DIR"
install -Dm 644 src/*.qml -t "$SRC_DIR"
install -Dm 644 ./*.desktop -t "$APPL_DIR"

for size in icons/*; do
  sub_dir="$(basename "$size")/apps"
  install -Dm 644 "icons/$sub_dir/"* -t "$ICON_DIR/$sub_dir"
done

printf "#!/bin/sh\npython \"%s\"" "$SRC_DIR/main.py" >"$TMPRUN"
install -Dm 755 "$TMPRUN" -T "$PREFIX/bin/$PROJECT"
rm "$TMPRUN"
