from collections import OrderedDict


def arabictoroman(number):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    list = []
    for r in roman.keys():
        (factor, number) = divmod(number, r)
        list.append(roman[r]*factor)
        if number == 0:
            break
    return ''.join(list)


print(arabictoroman(900))

ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def arabictoroman_2(number):
    list = []
    for (arabic, roman) in ROMAN:
        (factor, number) = divmod(number, arabic)
        list.append(roman*factor)
        if number == 0:
            break
    return ''.join(list)


print(arabictoroman_2(900))


# make a list of tuples for the function to refer
# for every tuple in list find the factor and remainder
# number gets reduced everytime divmod is run successfully
# append to list the roman equivalent times the factor
# break when number equals zero
# improvement - ->can use ordereddict and yield
