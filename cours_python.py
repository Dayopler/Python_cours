import sys

def write(mon_fichier):
    f = open(mon_fichier , "w")
    f.write("RICKY MON SAUVEUR <3")
    f.close()

def read(mon_fichier):
    f = open(mon_fichier , "r")
    print(f.read())
    f.close()


if __name__ == "__main__":
    # execute only if run as a script
    mon_fichier = input(sys.argv[0])
    write(mon_fichier)
    read(mon_fichier)
    

    print("This is the name of the script :", sys.argv[0])
    print("Number of arguments :", len(sys.argv))
    print("The arguments ar", str(sys.argv))
