while True:

    while True:
        time = input("Gib eine Uhrzeit ein getrennt von ':' beispiel: 11:23:56: ")

        try:
            num = []
            string = ""
            a, b, c = time.split(":")
            num.append(a.replace(":", ""))
            num.append(b.replace(":", ""))
            num.append(c)
            break
        
        except ValueError:
            try:
                num = []
                string = ""
                a, b = time.split(":")
                num.append(a.replace(":", ""))
                num.append(b)
                break
            
            except ValueError:
                try:
                    num = []
                    string = ""
                    num.append(time)
                    break
                
                except:
                    print("Error!")
                    exit(0)
    
    while True:
        m = int(input("In welchem Zahlensystem möchtest du die Uhrzeit haben? Zahl größer als 1 und kleiner als 11: "))

        if m <= 1 or m >= 11: 
            print("Hey! Ich hab größer als 1 und kleiner als 11 gesagt!")
        
        else:
            try:
                for zahl in num:
                    zahl = int(zahl)
                    h0 = zahl % m # rest
                    h01 = zahl // m # abs
                    h1 = h01 % m # rest
                    h11 = h01 // m # abs
                    h2 = h11 % m # rest
                    h21 = h11 // m # abs
                    h3 = h21 % m # rest
                    string = string + f" \033[92m{h3}{h2}{h1}{h0}\033[0m "
                
                print(string)
                break

            except:
                print("Tja, wenn du das ließt hast du etwas falsch gemacht :/ \nStarte einfach das Programm nochmal neu dann geht es bestimmt wieder")