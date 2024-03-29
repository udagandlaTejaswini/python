def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    if len(str1) != len(str2):
        return False
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  
    for count in char_count.values():
        if count != 0:
            return False

    return True
# Input
str1 = input().strip()
str2 = input().strip()
# Check anagram
print(are_anagrams(str1, str2))