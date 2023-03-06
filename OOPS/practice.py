def is_leap(Year):
    if ((Year % 400 == 0) or
            (Year % 100 != 0) and
            (Year % 4 == 0)):
        return is_leap()

year = int(input())
is_leap(year)
