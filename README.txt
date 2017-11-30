Read Me
---------------------------------------
Question 1: What is the running time of your program?
Answer:
    Offline part: suppose the dictionary contains N words and the average length of each word is M,
                  then the offline time complexity would be O(N * logN + N * M!). We will first use
                  O(N * logN) to sort our dictionary to lexicongraphical order, and then use O(M!)
                  time to generate anagrams for each word. In cour case, M is no larger than 100,
                  and N is no larger than 10,000.
    Online part:  suppose we have N words in dictionary, and the word passed in to check has length K,
                  then the amortized time we spent on checking is O(N/100), since the average amount of
                  words that have length K are N/100. In the worst case, the time complexity is O(N).
                  Notice this is irrelevant to the length of the word, K.

Question 2: How much memory does your program consume?
Answer:
    Again, suppose there are N words in the dictionary and the average length of each word is M.
    (Note that the actual space complexity is hard to compute because we generate all the anagrams
    for each word, the space took by this step would be factorial to the length. Here to simplify,
    we assume the average length is M and use it to compute the result)
    The space grabbed by the program would be O(N * M * (M!+1)), because there are N words, each will
    have M! anagrams plus itself, each takes M characters length.

Question 3: What if no sufficient memory?
Answer:
    What we can do in this case is to simplify the offline part and sacrifice the time complexity of
    the online part task. During the offline part, we can store only the words, again in buckets divided
    according to different word length. During the online part, we first find the bucket which contains
    word with exact the same length as the input word. Then generate all anagrams for the input word,
    which will take O(K!) if the length of the word is K. Then we compare the words in the bucket and
    the words generated from the input word. If there are overlapping, then the overlapped words are the
    answers we are looking for. This could decrease the time complexity of the offline part to O(N), where
    N is the length of the dictionary. However, at the same time, increase the time complexity of online
    part to O(N/100 * K!), where N is still the dictionary length and K is the length of our target word.