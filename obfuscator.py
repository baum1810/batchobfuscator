import random
from os import system
def main():
    system("cls")
    counter = 0
    counter2 = 0
    file = input("file\n> ")
    with open(f"{file}") as fileobj:
        try:
            file, lel = file.split('.')
        except:
            pass
        f = open(f"{file}obfusc.bat", "a")
        f.write("::obfuscated by https://github.com/baum1810")
        f.close()
        for line in fileobj:
           for ch in line:
                if not counter == 1:
                    if "\n" in ch:
                        f = open(f"{file}obfusc.bat", "a")
                        f.write(f"\n")
                        f.close()
                    elif "%" in ch:

                        f = open(f"{file}obfusc.bat", "a")
                        f.write(f"%")
                        f.close()
                        counter = 1
                    else:
                         n = random.randint(1,10)
                         randomi = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(n))
                         f = open(f"{file}obfusc.bat", "a")
                         f.write(f"{ch}%{randomi}%")
                         f.close()
                else:


                    if "%" in ch:
                        f = open(f"{file}obfusc.bat", "a")
                        f.write("%")
                        f.close()
                        counter = 0
                    elif "\n" in ch:
                        f = open(f"{file}obfusc.bat", "a")
                        f.write(f"\n")
                        f.close()
                    else:
                        f = open(f"{file}obfusc.bat", "a")
                        f.write(ch)
                        f.close()
    main()
main()
