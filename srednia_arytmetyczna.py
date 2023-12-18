numbers = []
print("wyliczanie srednie arytmetycznej, podaj liczby aby wyliczyc, jeśli chcesz zakonczyc wpisz koniec")
x = int(input("wprowadz liczbe: "))
suma = 0

while x != "koniec":
        numbers.append(int(x))
        x = (input("wprowadz liczbe: "))
        continue
        if x == "koniec":
            break
print(numbers)

for i in numbers:
      suma = suma + i
print(suma)

srednia_arytmetyczna = suma / len(numbers)

print(f"Srednia arytmecznyna z podanych liczb to: {srednia_arytmetyczna}")

