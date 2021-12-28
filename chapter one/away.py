"""One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false

naive approach:
{p: 1, [a: 1], l: 1, e: 1}
{p: 1, l: 1, e: 1}

len {a:1} == 1

{p:1, a:1, l:1, e:1}
{b: 1, a:1, k:1, e:1}

len {p: 1, l:1} == 2    

base: 
if s0 == s1 return true
if abs(len(s0) - len(s1)) return false

constraints:
all must be lowered

pale -> ple

pale -> bake
replace p -> b
do nothing

difference_count = 0
ple -> pale

[0] p -> [0] p
nothing
[1] l -> [1] a
replace, difference_count++
[2] e -> [2] l
replace, difference_count++

difference_count > 1?
return False

algorithm:
    1. lower all the characters
    2. iterate each character over the minimum string

"""

def one_away(s0, s1):
    difference = abs(len(s0) - len(s1))
    
    if s0 == s1:
        return True
    
    if difference > 1:
        return False
    
    if len(s0) > len(s1):
        s0, s1, = s1, s0


    for idx, c in enumerate(s0):
        if c != s1[idx]:
            if difference < 1:
                difference += 1
            else:
                s0 = s0[idx:] + s1[idx] + s0[:idx]
                difference += 1
        
        if difference > 1:
            return False

    return True
    
print(one_away('ple', 'paer'))