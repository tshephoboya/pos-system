from checkduplicates import has_been_added

products = {"a": 11.49,
            "b": 32.78,
            "c": 23.47,
            "d": 12.52,
            "e": 73.44,
            "f": 31.21,
            "g": 20.22,
            "h": 10.02,
            "i": 35.66,
            "j": 20.87,
            "k": 12.25,
            "l": 9.76,
            "m": 24.45,
            "n": 35.43,
            "o": 17.32,
            "p": 40.92,
            "q": 72.21,
            "r": 21.92,
            "s": 76.31,
            "t": 54.21,
            "u": 65.19}

products_entered = []

print("Enter TT for Total.")
while (True):
    command = input("Enter a product: ").lower()
    if command in products.keys():
        while (True):
            quantity = input("Enter product quantity > 0: ")
            try:
                quantity = int(quantity)
                break
            except ValueError as e:
                print("Enter valid number: ")
            if (has_been_added(products_entered, command) > 0):
                quantity += has_been_added(products_entered, command)
                print(quantity)
       
        products_entered.append([command, products[command] * quantity ])
    elif command == "tt":
        total = 0.0
        print("product", "Quantity", "Total", sep="  ")
        for count, i in enumerate(products_entered):
            print(i[0], i[1] // products[i[0]], "$"+str(round(i[1], 2)), sep="         ")
            total += i[1]

        total = round((total), 2)
        print("Total:     ", "$"+str(total ))
        break
