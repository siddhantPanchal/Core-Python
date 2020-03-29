import random as rd
import os


def String(matrix):
    text = ""

    for i in matrix:
        for j in i:
            text = text + " " + str(j)

    text = text[1:]
    return text

def encrypt(file):
    plainText = ""
    f = ""
    if not os.path.exists(".Encrypted"):
        os.system("mkdir .Encrypted")
    fileEnc = ".Encrypted\\"+file[:-4] + "Encrypted.txt"

    if os.path.exists(file):
        f = open(file, mode='r')
    else:
        print("your file does not exists \nExiting...... ")
        exit(0)

    plainText = [plainText+line for line in f.readlines()]
    f.close()
    # print(plainText)
    list1 = plainText
    matrix2 = []
    key = rd.randint(1,10)

    for i in list1:
        a = []
        for j in i:
            a.append(ord(j) + key)
            # print(type(ord(j)))
        matrix2.append(a)

    matrix2.append([key])
    # print(matrix2)
    if os.path.exists(fileEnc):
        f = open(fileEnc, mode='w')
    else:
        f = open(fileEnc, mode='a')

    f.write(String(matrix2))
    print("Writing encrypted file")
    f.close()
    print("File closed")
    return fileEnc
