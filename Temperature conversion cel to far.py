# please use python > 3.5 with this code. thanks and happy calculating.



def get_input(prompt):
        temp = input(prompt)
        while True:
                try:
                        if str(temp) == '':
                            print('Field can not be empty, please enter a number to calculate.')
                            return get_input(prompt)
                        elif int(temp) < -273.15:
                            print('Invalid celsius temperature value, celsius '
                                  'value can not go below absolute zero temperature.')
                            return get_input(prompt)
                        return int(temp)
                except ValueError:
                        print("Please use numbers only to enter temperature value.")
                        return get_input(prompt)


def calc_temp(cel):
    a = round(float(cel) * float(9) / 5)
    f = a + 32
    return int(f)


def main_program():
    temp_in_celsius = get_input("Please input the temperature value in celsius you want to convert in fahrenheit:- ")
    print('You entered temperature value', temp_in_celsius,
          'degree celsius, it is equal to', calc_temp(temp_in_celsius),
          'degree fahrenheit.')
    return main_program()


main_program()
