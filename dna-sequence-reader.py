def readSeq(seq_in):
    """ Reads sequences from input filename,
    removes new lines, and carriege returns
    return cleaned sequence to the caller"""
    
    with open(seq_in, "r") as f:
        seq = f.read();
        seq = seq.replace("\r", "")
        seq = seq.replace("\n", "")
        
        return seq
