import sys
import time
import itertools

class anagram_solver():
    def __init__(self, filepath):
        self.buckets = [None] * 100
        dictionary = []
        # read and sort all the words in the dictionary
        with open(filepath) as file:
            for line in file:
                word = line.strip('\n').lower()
                dictionary.append(word)

        # divide words by length into buckets,
        # and generate all the anagrams for each word
        for word in sorted(dictionary):
            l = len(word)
            anagrams = self.generate(word)
            if not self.buckets[l]:
                self.buckets[l] = [(word, anagrams)]
            else:
                bucket = self.buckets[l]
                bucket.append((word, anagrams))

    def contains(self, word):
        l = len(word)
        bucket = self.buckets[l]
        # if there are no words with target length,
        # we will output "-" immediately
        if not bucket:
            return "-"
        
        # check whether the word is in each key words' anagrams list,
        # if so, append the key word to answer list
        ans = []
        for key, anagrams in bucket:
            if word in anagrams:
                ans.append(key)

        if len(ans) == 0:
            return "-"
        
        # No need to sort the ouput list because the iteration is
        # operated on a sorted list of words which is done in the
        # offline part.
        res = " ".join(ans)
        return res

    def generate(self, word):
        anagrams = set(["".join(perm) for perm in itertools.permutations(word)])
        return anagrams

filepath = sys.argv[-1]
solver = anagram_solver(filepath)
while 1:
    time.sleep(0.01)
    for line in sys.stdin:
        word = line.strip('\n').lower()
        if not word:
            sys.exit()
        print(solver.contains(word))
