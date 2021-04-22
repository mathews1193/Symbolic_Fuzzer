def carsList (*cars):
    i = input("Enter the number of cars in list (max = 10)")
    i = int(i)

    if i > 10:
        print("Error list size is greater than 10!")
        print("Terminating function")
    else:
        name = input("Enter car name")
        cars.append(name)

