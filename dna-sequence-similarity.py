 def dna_sequence_similarity(seq1,seq2):
     """Returns similarity between two sequences"""
     similar = sum(x==y for (x,y) in zip(seq1, seq2))/float(len(seq1))
     return similar
