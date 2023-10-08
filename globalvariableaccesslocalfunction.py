
def globalMethod():
    g="Good"
    def greeting():
        global m
        m="Morning"
    greeting()
    print(f"global method function variable {g}")
    print(f"Greeting function variable with global method {m}")
    

globalMethod()