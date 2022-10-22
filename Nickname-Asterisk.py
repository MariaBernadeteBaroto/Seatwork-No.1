#Program that will print my nickname into asterisk character only

name="ADETH"

letter_A = [[" " for i in range(7)] for j in range(5)]
letter_D = [[" " for i in range(7)] for j in range(5)]
letter_E = [[" " for i in range(7)] for j in range(5)]
letter_T = [[" " for i in range(7)] for j in range(5)]
letter_H = [[" " for i in range(7)] for j in range(5)]

#Code for letter A

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==2) and col>0 and col<4):
            letter_A[row][col]="#"

#Code for letter D

for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            letter_D[row][col]="#"      



#Code for letter E

for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
            letter_E[row][col]="#"  

#Code for letter T

for row in range(7):
    for col in range(5):
        if col==2 or (row==0 and col!=2):
            letter_T[row][col]="#" 

#Code for letter H

for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
            letter_H[row][col]="#" 



