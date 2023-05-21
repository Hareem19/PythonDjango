secret_number=19
tot=3
i=0
while(i<tot):
    i+=1
    Guess_Num=input("Guess the number:   ")
    if int(Guess_Num)==secret_number:
        print("you won...")
        break
    else:
        print("you lost...")
else:
    print("Better luck next time...")