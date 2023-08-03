# def group_anagrams(strs):
#     anagram_groups = {}
    
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagram_groups:
#             anagram_groups[sorted_word].append(word)
#         else:
#             anagram_groups[sorted_word] = [word]
    
#     return list(anagram_groups.values())

# # Testing the function
# input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
# anagram_groups = group_anagrams(input_strings)
# print(anagram_groups)


from collections import defaultdict

def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))  # Sort the letters of the word
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())

# Example usage
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_strs)
print(result)

