uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }
cara = "-" * 40

texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

pocet_textu = len(texts)
titlecase = 0
uppercase = 0
lowercase = 0 
numeric = 0
suma_cisel = 0
delky = {}

jmeno = input(str("username: "))
heslo = input(str("password: "))

if jmeno in uzivatele and uzivatele[jmeno] == heslo:
    print(cara)
    print(f"Welcome to the app, {jmeno}.")
    print(f"We have {pocet_textu} texts to be analyzed.")
    print(cara)

    cislo_textu = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")
    print(cara)

    if not cislo_textu.isdigit():
        print("Invalid choice, terminating the program.")
        quit()
    elif int(cislo_textu) < 1 or int(cislo_textu) > int(pocet_textu):
        print("Invalid choice, terminating the program.")
        quit()
    else:
        vybrany_text = texts[int(cislo_textu) - 1]
        vsechna_slova = vybrany_text.split()
        print(f"There are {len(vsechna_slova)} words in the selected text.")

        for slova in vsechna_slova:
            slovo = slova.strip(".,!?-+*:;|\"'()")
            if slovo.istitle():
                titlecase +=1
            elif slovo.isupper():
                uppercase +=1
            elif slovo.islower():
                lowercase +=1
            elif slovo.isnumeric():
                numeric +=1
                suma_cisel += int(slovo)
            else:
                typ = "other"

            d = len(slovo)
            delky[d] = delky.get(d, 0) + 1

        print(f"There are {titlecase} titlecase words.")
        print(f"There are {uppercase} uppercase words.")
        print(f"There are {lowercase} lowercase words.")
        print(f"There are {numeric} numeric strings.")
        print(f"The sum of all the numbers {suma_cisel}.")
        print(cara) 

        print("LEN|       OCCURRENCES       |NR.")
        print(cara)
        for delka, pocet in sorted(delky.items()):
            print(f"{delka:>3}|{"*" * pocet:<24} | {pocet}")

elif jmeno in uzivatele and uzivatele[jmeno] != heslo:
    print("Incorrect password, terminating the program.")
else:
    print("Unregistered user, terminating the program.")