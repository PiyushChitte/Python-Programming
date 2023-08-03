import os

def Delete_File(FileName):

    if(os.path.exists(FileName)):
       os.remove(FileName)
       print("File is deleted successfully")
    else:
        print("There is no such file")
        return

def main():
    print("Entre the file name to create")
    Name = input()

    Delete_File(Name)

if __name__ == "__main__":
    main()