from random import*
import os
u_pwd = input("Contraseña: ")
pwd = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',]

pw = ""

while(pw != u_pwd):
    pw=""
    for l in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Craking Password.. Please Wait")
        os.system("cls")

print("Your Password Is: ", pw)
