player1 = input("Spelare 1: Sten, sax, eller påse?").lower().strip()
print("\n" * 100)
player2 = input("Spelare 2: Sten, sax, eller påse?").lower().strip()

if ((player1 == "sax" and player2 == "påse")
        or (player1 == "sten" and player2 == "sax")
        or (player1 == "påse" and player2 == "sten")):
    print("Spelare 1 vinner")
elif ((player2 == "sax" and player1 == "påse")
        or (player2 == "sten" and player1 == "sax")
        or (player2 == "påse" and player1 == "sten")):
    print("Spelare 2 vinner")
else:
    print("Oavgjort")
