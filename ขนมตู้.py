"""ขนมตู้"""
def main():
    """ขนมตู้"""
    mon = int(input())
    wat = int(input())
    sn1 = int(input())
    sn2 = int(input())
    sn3 = int(input())
    if mon >= wat:
        save = save (sn1*20)
        if (mon-wat)%3 == 0:
            total = sn1*10
            print("Now you have", ((mon-wat)%3)-total, "left.")
            print("Here’s your order!")
            print("Water:", wat, "baht")
        elif (mon-wat)%3 == 1:
            total = sn1*15
            print("Now you have", ((mon-wat)%3)-total, "left.")
            print("Here’s your order!")
            print("Water:", wat, "baht")
        elif (mon-wat)%3 == 2:
            total = sn1*20
            print("Now you have", ((mon-wat)%3)-total, "left.")
            print("Here’s your order!")
            print("Water:", wat, "baht")
            if (((mon-wat)%3)-total)%3:
                print("Now you have", mon-wat, "left.")
                print("Here’s your order!")
            elif (mon-wat)%3%3 == 1:
                print("Now you have", mon-wat, "left.")
                print("Here’s your order!")
            if (mon-wat)%3%3 == 2:
                print("Now you have", mon-wat, "left.")
                print("Here’s your order!")
    elif mon >= wat:
        print("Now you have", mon-wat, "left.")
        print("You don’t have enough money!")
