feeling = input("Hur mår du? ")
school = input("Vilken skola går du på? ")

if feeling == "bra" and school == "pb":
    print("Du ljuger")
elif feeling == "jättebra":
    print("Hejhej pinocchio")
elif feeling == "dåligt" or feeling == "sämst":
    print("Låter rimligt")
else:
    print("Fel")