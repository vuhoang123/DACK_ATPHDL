from Encrypt import *
from Device_File import *
import hashlib
import os


def EncryptFile():
    while True:
        print("\n\n1: Encrypt file")
        print("2: Decrypt file")
        print("-1: Exit")
        print("\tChoose function: ", end="")
        cn = int(input())

        if cn == -1:
            break

        if cn == 1:
            filename = input("Enter file name: ")
            key = input("Enter key: ")
            k = hashlib.sha256(key.encode('utf-8')).digest()
            print(f"Key hashed: {k}")
            file_encrypt(filename, k)
        elif cn == 2:
            filename = input("Enter file name: ")
            key = input("Enter key: ")
            k = hashlib.sha256(key.encode('utf-8'))
            print(f"Key hashed: {k}")
            file_decrypt(filename, k)
        else:
            print("You did not choose a function!")
            print("Exiting program")


def Devide_Join_file():
    while True:
        print("\n\n1: Divide file")
        print("2: Join file")
        print("-1: Exit")
        print("\tChoose function: ", end="")
        cn = int(input())

        if cn == -1:
            break

        if cn == 1:
            filename = input("Enter file name: ")
            num_file = int(input("Enter number of files to divide into: "))
            divided(filename, num_file)
        elif cn == 2:
            filename = input("Enter file name: ")
            num_file = int(input("Enter number of files to join: "))
            join(filename, num_file)
        else:
            print("You did not choose a function!")
            print("Exiting program")


while True:
    print("\n\n1: Encrypt/Decrypt file")
    print("2: Divide/Join file")
    print("-1: Exit")
    print("\tChoose function: ", end="")
    cn = int(input())

    if cn == -1:
        break

    if cn == 1:
        EncryptFile()
    elif cn == 2:
        Devide_Join_file()
    else:
        print("You did not choose a function!")
        print("Exiting program")
