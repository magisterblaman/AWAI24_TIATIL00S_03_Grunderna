school = input("Vilken skola går du på? ")

if school == "lbs":
    print("Har du en stabil mental hälsa? ")
    mental_health = input().strip()
    if mental_health == "ja":
        print("Byt skola")
    else:
        print("Alexandra sitter på övervåningen")
elif school == "pb":
    pass
elif school == "ed":
    pass
else:
    print("Du har en konstig skola")