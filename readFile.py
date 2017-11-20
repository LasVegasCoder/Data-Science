def readFile(file_path):
   """ Read file into strings, removed new line and carriage return then return the strings"""
    with open(file_path, 'r', 'utf-8') as current_file:
        texts = current_file.read()
        text  = texts.current_file.replace("\n","").replace("\r","")
        
    return text
