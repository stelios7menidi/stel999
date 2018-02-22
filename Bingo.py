#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Giannis
#
# Created:     17/02/2018
# Copyright:   (c) Giannis 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

for m in range(1,1001):

    for i in range(1,101):
     Li = [0,0,0,0,0]



    for i in range(1,101):
     for j in range (5):
         Li[j] = input("Select a number between 1-80: ")

         n = Li[j]

         while int(n)>80 or int(n)<=0 :
             print("The number you enter is >80 or <=0")
             Li[j] = input("Please try again.Select a number between 1-80: ")
             n= Li[j]



    arithmoi=0
    k=0
    while k==0  :
     import random
     value = random.randint(1,80)
     abingo= value



     for i in range(1,101):
      t=0
      for j in range(5):
         n=Li[j]
         if  value == int[n] :
            Li[j]=0



         if int[n]==0:
           t= t+1

     if t==5:
      k=1
      arithmoi=arithmoi+1

print("Ο μέσος όρος είναι",arithmoi/1000)
