import random
'''
1 for stone computer , user
-1 for paper user,computer
0 for sesor user,computer
'''
computer = random.choice([-1,0,1])
userstr = input("enter userr choice: ")
userdict= {"stone":1,"paper":-1,"sesor":0}
reversedict= {1:"stone",-1:"paper",0:"sesor"}

user = userdict[userstr]

print(f"user chosse : {reversedict[user]}\ncomputer chosse : {reversedict[computer]}")

if(computer == 1 and user == 1):
    print("draw! ")

elif(computer == 1 and user == -1 ):
    print("user win! ")

elif(computer == 1 and user == 0):
    print("user losse! ")

elif(computer == -1 and user == -1):
    print("draw! ")

elif(computer == -1 and user == 1 ):
    print("user losse! ")

elif(computer == -1 and user == 0):
    print("user win! ")

elif(computer == 0 and user == 0):
    print("draw! ")

elif(computer == 0 and user == 1 ):
    print("user win! ")

elif(computer == 0 and user == -1):
    print("user losse! ")

else:
    print("something went wrong! ")

# Main loop for multiple rounds
while True:
    play_round()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break