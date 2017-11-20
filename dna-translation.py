# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:04:20 2017

@author: Prince Adeyemi
"""
    # check the length of the sequence is divisible by 3:
    # loop through the sequence
    # extract codon
    # save result in a var
    # tested with real dna strands downloaded from ncbi
    # data from https://www.ncbi.nlm.nih.gov/search/?term=NM_207618.2
    
def translate_dna(seq):
    """ DNA Translator translates a string containing
    nucleotide sequence into a string containing the corresponding
    sequence of amino acids.  Nuclotides are translated in triplet
    using the table dictionary; each amino acid is encoded in a string
    of length 3 . Tested with real dna strands downloaded from ncbi
    # data from https://www.ncbi.nlm.nih.gov/search/?term=NM_207618.2"""
    
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',    
    }

    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]
            
    return protein
