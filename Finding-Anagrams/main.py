# Check if two words are anagrams 
# Example:


def find_anagrams(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

# print(find_anagrams("hello", "check"))
# #  --> False
# print(find_anagrams("below", "elbow")) 
# # --> True
