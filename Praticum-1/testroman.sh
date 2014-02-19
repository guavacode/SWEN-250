#!/bin/bash

echo "Test One Lowercase Letter - a"
echo "a" |  python3 Roman.py
echo "Output should be: n"
echo

echo "Test One Lowercase Letter - n"
echo "n" |  python3 Roman.py
echo "Output should be: a"
echo

echo "Test original sample - SE Rocks!"
echo "SE Rocks!" | python3 Roman.py
echo "Output should be: FR Ebpxf!"
echo

#Add others here:

#This part of the script tests standardly used punctuation mixed in with regular words and phrases. Phrase being testes seems to have the characteristics of a standard phrase.
echo "Test a variety of common non-alphabetic characters - Hello sir! This is a test of standard punctuation, in Roman.py; this should work: well."
echo "Hello sir! This is a test of standard punctuation, in Roman.py; this should work: well." | python3 Roman.py
echo "Output should be: Uryyb fve! Guvf vf n grfg bs fgnaqneq chapghngvba, va Ebzna.cl; guvf fubhyq jbex: jryy."
echo

#This part of the script tests numbers and letters mixed together in a single word-like-object. Letters from the first and second half of the alphabet are used.
echo "Test numbers with a few letters mixed in - 1a2A3x4X"
echo "1a2A3x4X" | python3 Roman.py
echo "Output should be: 1n2N3k4K"
