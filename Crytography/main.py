from Crytography import Encryption as e
from Crytography import Decryption as d

if __name__ == "__main__":

    file_name = ""

    while True:
        ch = int(input("\n0.Enter new file name to operate \n1.Encryption \n2.Decryption\n3.Exit\nEnter your choice : "))
        if ch == 0:
           file_name = input("Enter file name (along with .txt extension) : ")
        elif ch == 1:
            if file_name == "":
                file_name = input("Enter File name to Encrypt (along with .txt extension : ")
            encyptedFileName = e.encrypt(file_name)
            # print(encyptedFileName)
        elif ch == 2:
            if file_name == "":
                file_name = input("Enter File name to Encrypt (along with .txt extension : ")
            d.decrypt(file_name)
            pass
        elif ch == 3:
            exit(0)

        # sys("cls")