seq_a = "TGGAGGCAATGGCGGCCAGCA"
seq_b = "GACTCCTCCTCCTCCTGCTCA"    
len_a = len(seq_a)    
len_b = len(seq_b)    
print("Length of Sequence A: " + str(len_a))    
print()    
print("Length of Sequence B: " + str(len_b))
print()

def sequence_compare(seq_a, seq_b):
        len1 = len(seq_a)
        len2 = len(seq_b)
        mismatches = []
        for pos in range (0, min(len1, len2)) :
              if seq_a[pos] != seq_b[pos]:
                  mismatches.append('|')
              else:
                  mismatches.append(' ')
        print (seq_a)
        print ("".join(mismatches))
        print (seq_b)
sequence_compare(seq_a,seq_b)

OUTPUT:
TGGAGGCAATGGCGGCCAGCA
||||||||| |||||||||
GACTCCTCCTCCTCCTGCTCA
