class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self,text1:str,text2:str="")->str:
        self.text1=text1
        return(self.text1.upper())

    def format_text2(self,*args:str)->str:
        return sum(args)



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
