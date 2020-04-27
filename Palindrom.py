
def palindrom_check(word):
        length = len(word)
        counter=-1
        for idx, letter in enumerate(word):
            middle_letter = len(word)//2
            if idx < middle_letter:
                if letter == word[counter]:
                    counter = counter-1
                else:
                    return False
            else:
                return True
    

print(palindrom_check("kajjak")) # powinno być True 
print(palindrom_check("potop"))  # Powinno być True
print(palindrom_check("kajak"))  # Powinno być True
print(palindrom_check("ribor"))  # Powinno być False

