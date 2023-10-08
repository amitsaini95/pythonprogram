letter='''Dear <|NAME|>
Greetings from ABC house. I am Happy to tell you about your selection
you are selected
thanks and regards
<|DATE|>
'''
name=input("Enter the Name :")
date=input("Enter the Date :")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)