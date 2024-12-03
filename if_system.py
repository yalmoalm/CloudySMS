# This function get the average wind gust and determines
# the appropriate clothing item for the day based on predefined conditions.
def ifs(avg_wind):

    if 0 <= avg_wind <= 10:
        return ('hoodie')

    elif 11 <= avg_wind <= 20:
        return ('Softshell')

    elif 21 <= avg_wind <= 30:
        return ('Thick coat')

    elif 31 <= avg_wind:
        return ('Thick coat + wool hat')
    else:
        raise ValueError("The value is incorrect.")







