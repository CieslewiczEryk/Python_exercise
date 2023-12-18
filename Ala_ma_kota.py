print("Zadanie zliczania Ala ma kota \n")

zdanie = "Ala ma kota"
words = 1
letters = 0
hash_table = {}

for letter in zdanie:
    if letter == " ":
        words += 1

for letter in zdanie:
    if letter != " ":
        letters += 1        

for letter in zdanie:
    letter = letter.lower()
    if letter == " ":
        continue   
    elif letter in hash_table:
        hash_table[letter] += 1
    else:
        hash_table[letter] = 1 

print(f"słow w zadniu: {words}")
print(f"liter w zdaniu: {letters}")    
print(hash_table)    