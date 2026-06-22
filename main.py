jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}

if "Marek" in uzivatel and uzivatel["Marek"] == "1234":
    zprava = "Ahoj Marek, vítej v aplikaci! Pokračuj..."
else:
    zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"
print(f"Výstup: {zprava}")