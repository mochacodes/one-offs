from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
        anagram_map = defaultdict(list)
        for word in strs:
            print(f"word: {word}")
            sorted_word = ''.join(sorted(word))
            print(f"sorted: {sorted_word}")
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())


print(groupAnagrams(strs))