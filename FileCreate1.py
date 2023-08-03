import os

def Createfile(FileName):

    if(os.path.exists(FileName)):
        print("File is already existing")
        return
    else:
        fd = open(FileName, "w")
        

def main():
    print("Entre the file name to create")
    Name = input()

    Createfile(Name)

if __name__ == "__main__":
    main()