def uruu(year):

    result = None
    if year % 4 == 0:
        result = True

        if year % 100 ==0:
            result = False

            if year % 400 == 0:
                result = True

    else:
        result = False

    return result
