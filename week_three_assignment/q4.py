def create_table():
    print("Celsius  |  Fahrenheit")


def append_to_table(cels, fahr):
    print(f'{cels}        |  {fahr}')


def convert_cels_to_fahr(cels):
    create_table()
    for i in range(cels + 1):
        append_to_table(i, (i * 9.0/5.0) + 32.0)


cels_range = 100
convert_cels_to_fahr(cels_range)
