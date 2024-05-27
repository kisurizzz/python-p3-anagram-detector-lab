# your code goes here!
# class Anagram:
#     def __init__(self, word):
#         self.word = word

#     def match(self,list_of_words)
#         anagrams = []
#         for match in list_of_words:
#             if self.
       
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = [word for word in word_list if self.is_anagram(word)]
        return anagrams

    def is_anagram(self, other_word):
        # Check if the given word is an anagram of the base word
        other_word = other_word.lower()
        return sorted(other_word) == sorted(self.word)