class MyFile: 
    def __init__(self, name, mode, encode='utf-8'): 
        self.filename = name 
        self.mode = mode 
        self.encode = encode
 
    def __enter__(self): 
        self.file = open(self.name, self.mode, encoding=self.encode) 
        return self.file 
 
    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.file.close()