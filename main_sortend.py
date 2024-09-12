import random
'''
1 for stone com , you
-1 for paper you,com
0 for sesor you,com
'''
computer = random.choice([-1,0,1])
youstr = input("enter your choice: ")
youdict= {"stone":1,"paper":-1,"sesor":0}
reversedict= {1:"stone",-1:"paper",0:"sesor"}

you = youdict[youstr]

print(f"you chosse : {reversedict[you]}\ncomputer chosse : {reversedict[computer]}")

if(computer == you):
    print("draw!")

else:    
    '''
    if(computer == 1 and you == 1):   #0
        print("draw! ")

    elif(computer == 1 and you == -1 ): #2
        print("you win! ")

    elif(computer == 1 and you == 0): #1
        print("you losse! ")

    elif(computer == -1 and you == -1):  #0
        print("draw! ")

    elif(computer == -1 and you == 1 ): #-2
        print("you losse! ")

    elif(computer == -1 and you == 0): #-1
        print("you win! ")

    elif(computer == 0 and you == 0):   #0
        print("draw! ")

    elif(computer == 0 and you == 1 ): #-1
        print("you win! ")

    elif(computer == 0 and you == -1): #1
        print("you losse! ")
    '''
    if((computer - you)== 2 or (computer-you)==-1):
        print("you win")
    else:
        print("you lose")

    