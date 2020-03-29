import os


def toList(list1):
    list2 = []
    list3 = []

    for i in list1:
        list2 = i.split(" ")

    for i in list2:
        list3.append(int(i))

    return list2


def getKey(list1):
    return list1.pop(len(list1) - 1)


def isExisting(encryptedFileName):
    if os.path.exists(".Encrypted"):
        if os.path.exists(encryptedFileName):
            return True
    return False


def decrypt(filename):
    encrypted = ""
    encryptedFileName = ".Encrypted\\"+filename[:-4] + "Encrypted.txt"
    plainText = ""
    int_list = []

    if not isExisting(encryptedFileName):
        print("Encrypted file is not found \n make sure you have encrypt " + filename + " first")
        exit(0)

    f = open(encryptedFileName,mode='r')

    encryptedText = toList([encrypted + line for line in f.readlines()])
    f.close()
    key = int(getKey(encryptedText))

    for i in encryptedText:
        int_list.append(int(i) - key)

    for i in int_list:
        plainText = plainText + str(chr(i))

    if not os.path.exists(".Decrypted"):
        os.system("mkdir .Decrypted")

    filename = ".Decrypted\\" + filename
    if not os.path.exists(filename):
        f = open(filename, mode='a')
    else:
        f = open(filename,mode='w')

    f.write(plainText)
    print("Writing Decrypted file...")
    f.close()
    print("File is closed")
