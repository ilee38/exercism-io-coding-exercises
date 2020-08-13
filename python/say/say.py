
single = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',10:'ten',
11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

double = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}


def say(number):
   
    if number < 0 or number > 999000000000:
        raise ValueError('Number out of range')
    elif number == 0:
        return 'zero'

    K, M, B, hundreds, tens = '', '', '', '',''

    # check 1,000,000,000's
    if number >= 1000000000:
        B = say(number // 1000000000) + ' billion'
        number = number % 1000000000

    # check 1,000,000's
    if number >= 1000000:
        M = say(number // 1000000) + ' million'
        number = number % 1000000

    # check 1000's
    if number >= 1000:
        K = say(number // 1000) + ' thousand'
        number = number % 1000

    # check 100's
    if number >= 100:
        hundreds = say(number // 100) + ' hundred'
        number = number % 100

    # check 10's
    if  number < 20:	
        tens = single[number]
    elif number < 100:
        first = number // 10
        last = number % 10
        if(last > 0):
            tens = f'{double[first]}-{single[last]}'
        else:
            tens = f'{double[first]}'

    return(f'{B} {M} {K} {hundreds} {tens}'.strip())

