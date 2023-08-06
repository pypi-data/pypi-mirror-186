
def inpt(inp_type,text):
    return inp_type(input(text))
    
c = inpt(float,"test")
print(c)