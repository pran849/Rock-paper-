import random
import time
print("Winning rules of the Rock Paper Scissors game as follows : \n"+"Rock V/S Paper -> Paper wins \n"+"Rock V/S Scissors -> Rock wins\n"+"Paper V/S Scissors -> Scissors wins \n")
def logic():
    while 1:
        print('Enter your choice :-'+'\n\t1.ROCK'+'\n\t2.PAPER'+'\n\t3.SCISSORS')
        choice=int(input('Enter user choice : '))
        while choice>3 or choice<1:
            choice=int(input('Enter valid user choice : '))
        if choice==1:
            print('User choice is....:\nROCK')
        elif choice==2:
            print('User choice is....:\nPAPER')
        elif choice==3:
            print('User choice is....:\nSCISSORS')
        print ("Now its computer's turn",end='')
        for i in range (1,5):
            print('.',end="")
            time.sleep(1)
        print('\nComputer choice is .....:')
        ch=("ROCK","PAPER","SCISSORS")
        choic=random.choice(ch)
        print(choic)
        if(choic=='SCISSORS' and choice==2)or(choic=='ROCK' and choice==3)or(choic=='PAPER' and choice==1):
            print('****Computer wins****')
        if(choic=='ROCK' and choice==2)or(choic=='PAPER' and choice==3)or(choic=='SCISSORS' and choice==1):
            print("****User wins****")
        if((choic=='ROCK'and choice==1)or(choic=='PAPER'and choice==2)or(choic=='SCISSORS'and choice==3)):
            print('****Match is tie****')
        print("!!!..*** Do you want to play ? ***..!!!")
        n=int(input('\n1.YES \n2.NO \n'))
        if n!=1 or n!=2 :
            while n<1 or n>2:
                n=int(input('Enter valid choice : '))
        if n==2 :
            break
            
logic()
