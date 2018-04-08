import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is Certain'
    elif answerNumber == 2:
        return 'It is undecidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again Later'
    elif answerNumber == 6:
        return 'Concentrate And Ask Again'
    elif answerNumber == 7:
        return 'My reply is No' 
    elif answerNumber == 8:
        return 'Outlook is No Bueno'
    elif answerNumber == 9:
        return 'Very Doubt, Do Not Even Try'
    else:
        return 'Oh Hell No!!!'

r = random.randint(1,15)
fortune = getAnswer(r)
print(fortune)
