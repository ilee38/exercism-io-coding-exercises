class PhoneNumber:
    def __init__(self, number):
        if len(number) < 10:
            raise ValueError("Invalid number")
        self.number = self.get_number(number)
        self.area_code = self.get_area_code(self.number)


    def get_number(self, number):
        num_str = [None]*10
        country_code = []
        digit_count = 9
        for i in range(len(number)-1, -1, -1):
            if number[i].isdigit() and digit_count >= 0:
                if digit_count == 3 or digit_count == 0:
                    if int(number[i]) > 1:
                        num_str[digit_count] = number[i]
                    else:
                        raise ValueError("Invalid number")
                else:
                    num_str[digit_count] = number[i]
                digit_count -= 1
            elif number[i].isdigit():
                country_code.append(number[i])
        if len(country_code) == 0:
            return ''.join(num_str)
        elif len(country_code) == 1 and country_code[0] == '1':
            return ''.join(num_str)
        else:
            raise ValueError("Invalid number")


    def get_area_code(self, number):
        return number[0:3]


    def pretty(self):
        return '({}) {}-{}'.format(self.area_code, self.number[3:6], self.number[6:])