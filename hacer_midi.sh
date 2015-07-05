#!/bin/sh

ROOT=$1
FILES_DIR=files
MIDI_DIR=midi
IN_SUFFIX=_input.txt
OUT_SUFFIX=_output.txt

FILE_IN=$FILES_DIR/$ROOT$IN_SUFFIX
FILE_OUT=$ROOT$OUT_SUFFIX
FILE_MIDI=$MIDI_DIR/$ROOT.mid

MUSILENG=./musileng
MIDICOMP='midicomp -c'
PMIDI=wildmidi

$MUSILENG $FILE_IN $FILE_OUT

if [ $? -eq 0 ]; then
	$MIDICOMP $FILE_OUT $FILE_MIDI
	rm $FILE_OUT

	echo "Hecho"
	if [ $# -gt 1 ]; then
		if [ $2 = "-p" ]; then
			$PMIDI $FILE_MIDI
		fi
	fi
else
	echo "Falló"
fi

