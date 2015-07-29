#!/bin/sh
echo "ej1"
./hacer_midi.sh ej1
echo "ej2"
./hacer_midi.sh ej2
echo "ej3"
./hacer_midi.sh ej3
echo "ej4"
./hacer_midi.sh ej4
echo "jijiji"
./hacer_midi.sh jijiji
echo "post_crucifixion_riff"
./hacer_midi.sh post_crucifixion_riff
echo "4\:33"
./hacer_midi.sh 4\:33
echo "erroneo_1 $(head -1 files/erroneo_1_input.txt)"
./hacer_midi.sh erroneo_1
echo "erroneo_2 $(head -1 files/erroneo_2_input.txt)"
./hacer_midi.sh erroneo_2
echo "erroneo_3 $(head -1 files/erroneo_3_input.txt)"
./hacer_midi.sh erroneo_3
echo "erroneo_4 $(head -1 files/erroneo_4_input.txt)"
./hacer_midi.sh erroneo_4
echo "erroneo_5 $(head -1 files/erroneo_5_input.txt)"
./hacer_midi.sh erroneo_5
echo "erroneo_6 $(head -1 files/erroneo_6_input.txt)"
./hacer_midi.sh erroneo_6
echo "erroneo_7 $(head -1 files/erroneo_7_input.txt)"
./hacer_midi.sh erroneo_7
echo "erroneo_8 $(head -1 files/erroneo_8_input.txt)"
./hacer_midi.sh erroneo_8
echo "erroneo_9 $(head -1 files/erroneo_9_input.txt)"
./hacer_midi.sh erroneo_9
echo "erroneo_10 $(head -1 files/erroneo_10_input.txt)"
./hacer_midi.sh erroneo_10
echo "erroneo_11 $(head -1 files/erroneo_11_input.txt)"
./hacer_midi.sh erroneo_11
echo "erroneo_12 $(head -1 files/erroneo_12_input.txt)"
./hacer_midi.sh erroneo_12
echo "tempo_0 $(head -1 files/tempo_0_input.txt)"
./hacer_midi.sh tempo_0
echo "instrumento_fuera_rango $(head -1 files/instrumento_fuera_rango_input.txt)"
./hacer_midi.sh instrumento_fuera_rango
echo "octava_de_nota_fuera_de_rango $(head -1 files/octava_de_nota_fuera_de_rango_input.txt)"
./hacer_midi.sh octava_de_nota_fuera_de_rango
echo "tempo_negativo $(head -1 files/tempo_negativo_input.txt)"
./hacer_midi.sh tempo_negativo
echo "17_voces $(head -1 files/17_voces_input.txt)"
./hacer_midi.sh 17_voces
