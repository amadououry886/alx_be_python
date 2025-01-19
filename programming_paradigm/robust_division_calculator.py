def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)

    except ValueError:
        return "Erro please try to check your numbers again"

    try:

        result = numerator/denominator
        return f"The result of this division is : {result}"

    except ZeroDivisionError :
        return "can not divide by zero"

