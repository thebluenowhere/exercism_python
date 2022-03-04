def leap_year(year):
    is_leap = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: 
                pass
            else:
                is_leap = False
    else: 
        is_leap = False
    return is_leap
