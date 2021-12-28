"""1.4
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

"""scratchpad"""

def is_permutation_palindrome(s: str) -> bool:
    frequency = {}

    s.replace(" ", "")

    for char in s.lower():
        if char not in frequency:
            frequency[char] = 0

        frequency[char] += 1

    odd_count = 0
    for val in frequency.values():
        if (val % 2) == 1:
            odd_count += 1

        if odd_count > 1:
            return False
    
    return True