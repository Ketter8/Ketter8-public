"""Conert numbers from decimal to binary."""

number_as_string = input("Enter a decimal number:")
# number_as_string = input("Ask question here")

# input() gives us text, let's convert it to number
number = int(number_as_string)

# here we gather the result
result = ""

while number > 0:
    remainder = number % 2
    result = str(remainder) + result
    number = number // 2

print("Result in binary:", result)

___

10110111

summa on null

võtta viimane number
    Korruta läbi 2 astmel 0
    liida tulemus summale
    suurenda astendajat ühe võrra
    korda kuni lõppeb
___
decimalValue = 0
Power = 0
while len(result) > 0:
        lastDigit = int(result[-1])
        decimalValue += lastDigit * 2 ** power
        power += 1
        result = result[0:-1]
        
        Print("Kümnend väärtus on", decimalValue)