UserN = input("Username: ")
Pass = input("Password: ")

if UserN == "Chakkarin" and Pass == str(1234):
    print("Welcome K.Chakkarin")
    print("What would do you want?")
    print("Juice 20 THB\n" "Cola 25 THB\n" "Coffee 40 THB")
    ItemSel = input(">> ")
    ItemQTY = int(input(">> "))
    if ItemSel == "Juice":
        print("Tatal: ",ItemQTY * 20," THB")
    elif ItemSel == "Cola":
        print("Tatal: ", ItemQTY * 25, " THB")
    elif ItemSel == "Coffee":
        print("Tatal: ", ItemQTY * 40, " THB")
    else:
        print("Please Try Again.")
else:
    print("Incorrect Password or Username")