"""1.3 URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)"""

def urlify(char_array: list):
    for i, char in enumerate(char_array):
        if char == " ":
            char_array[i] = "%20"

s = "a swing and a miss"
s_arr = [char for char in s]

print(s_arr)
urlify(s_arr)
print(s_arr)