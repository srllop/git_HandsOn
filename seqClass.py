#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    
args = parser.parse_args()

if re.search('^[ACGTU]+$', args.seq): # Chech characters are nucleotides
    if re.search('T', args.seq) and not re.search('U', args.seq) : # Chec for presence of "T"
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq): #Chech for presence of "U"
        print ('The sequence is RNA')
    elif re.search('U', args.seq) and re.search('T', args.seq):
        print ('The sequence is not dna nor RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif: # Chech if there's a motif argument
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq): #Motif found in seq
    print("FOUND!!!! :D ")
  else:
    print("NOT FOUND :( ")
