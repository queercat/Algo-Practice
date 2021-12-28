"""
Example: A ransom note can be formed by cutting words out of a magazine to form a new
sentence. How would you figure out if a ransom note (represented as a string) can be formed
from a given magazine (string)? 
"""

"""algorithm
1. iterate over each word in the magazine
    a. if the word exists in the string remove it
    b. if the string is empty return true
2. return false
"""

def can_ransom(ransom_note: str, magazine: str) -> bool:
    ransom_arr = ransom_note.split(" ")
    magazine_arr = magazine.split(" ")

    for word in magazine_arr:
        if word in ransom_arr:
            ransom_arr.remove(word)
        
        if ransom_arr == []:
            return True

    return False


ransom = "give us all your money"
magazine = "the world's money supply wants to give us all a run for our money, you're not gonna believe whats on the next page... your mom"

print(can_ransom(ransom, magazine))