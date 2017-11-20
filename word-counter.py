def count_words(text):
   """ Count frequency of unique words from strings """
    text = text.lower()
    skips = [".",",",";",":","!","'",'"']
    
    for char in skips:
        text = text.replace(char, "")
    
    word_counts = {}
   
    for word in text.split(" "):
        #know word
       if word in word_counts:
        word_counts[word] += 1
        
       else: 
        #unknown word
        word_counts[word] = 1
        
    return word_counts
