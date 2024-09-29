def chi_square(data, expected):
    # data = []
    # expected = []
    chi_square = 0

    # length = int(input("How long is the data set? "))
    # for i in range(length):
    #     u_input = float(input(f"Number {i+1}: "))
    #     data.append(u_input)
    # print("EXPECTED VALUE")
    # for i in range(length):
    #     u_input = float(input(f"Number {i+1}: "))
    #     expected.append(u_input)

    for i in range(len(data)):
        if expected[i] != 0:
            chi_square += ((data[i]-expected[i])**2)/expected[i]

    return(chi_square)