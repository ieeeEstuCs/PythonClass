def Calculator(first_number, operator, second_number):
    if "+" is operator:
        result = first_number + second_number

    elif "-" is operator:
        # if first_number > second_number:
        result = first_number - second_number

        # elif second_number > first_number:
        #     result = second_number - first_number
        # else:
        #     result = 0
    elif "*" is operator:
        result = first_number * second_number
    elif "/" is operator and second_number != 0:
        # &
        result = first_number / second_number
    else:
        print("Mistake calculate")
    print(first_number, operator, second_number, "=", result)


Calculator(1, "/", 2)
Calculator(-7, "*", 4)
Calculator(0, "/", 1)
Calculator(18, "/", 8)
