def getSector(number):
    sector = ''
    if number >= 0 and number < 11.25:
        sector  = 'N'
    elif number >= 11.25 and number < 33.75:
        sector = 'NNE'
    elif number >= 33.75 and number < 56.25:
        sector = 'NE'
    elif number >= 56.25 and number < 78.75:
        sector = 'ENE'
    elif number >= 78.75 and number < 101.25:
        sector = 'E'
    elif number >= 101.25 and number < 123.75:
        sector = 'ESE'
    elif number >= 123.75 and number < 146.5:
        sector = 'SE'
    elif number >= 146.5 and number < 168.75:
        sector = 'SSE'
    elif number >= 168.75 and number < 191.25:
        sector = 'S'
    elif number >= 191.25 and number < 213.75:
        sector = 'SSW'
    elif number >= 213.75 and number < 236.25:
        sector = 'SW'
    elif number >= 236.25 and number < 258.75:
        sector = 'WSW'
    elif number >= 258.75 and number < 281.25:
        sector = 'W'
    elif number >= 281.25 and number < 303.75:
        sector = 'WNW'
    elif number >= 303.75 and number < 326.25:
        sector = 'NW'
    elif number >= 326.25 and number < 348.75:
        sector = 'NNW'
    elif number >= 348.75 and number <= 360:
        sector = 'N'
    else:
        sector = 'error'
    return sector

def getSectorNUM(number):
    sector = 0
    if number >= 0 and number < 11.25:
        sector  = 1
    elif number >= 11.25 and number < 33.75:
        sector = 2
    elif number >= 33.75 and number < 56.25:
        sector = 3
    elif number >= 56.25 and number < 78.75:
        sector = 4
    elif number >= 78.75 and number < 101.25:
        sector = 5
    elif number >= 101.25 and number < 123.75:
        sector = 6
    elif number >= 123.75 and number < 146.5:
        sector = 7
    elif number >= 146.5 and number < 168.75:
        sector = 8
    elif number >= 168.75 and number < 191.25:
        sector = 9
    elif number >= 191.25 and number < 213.75:
        sector = 10
    elif number >= 213.75 and number < 236.25:
        sector = 11
    elif number >= 236.25 and number < 258.75:
        sector = 12
    elif number >= 258.75 and number < 281.25:
        sector = 13
    elif number >= 281.25 and number < 303.75:
        sector = 14
    elif number >= 303.75 and number < 326.25:
        sector = 15
    elif number >= 326.25 and number < 348.75:
        sector = 16
    elif number >= 348.75 and number <= 360:
        sector = 1
    else:
        sector = 0
    return sector
