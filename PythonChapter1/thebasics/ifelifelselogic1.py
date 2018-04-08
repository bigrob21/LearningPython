print('What grade did you receive?')
grade = input()
if(int(grade) >= 90):
    print('Congrats you got an  A')
elif(int(grade) < 90 and int(grade) >= 80):
    print('Not bad, not bad, you got a B')
elif(int(grade) < 80 and int(grade) >= 70):
    print('passable you got a C, try harder next time!')
else:
    print('Good graceous you F\'n scrwed the pooch on this one....WTF')