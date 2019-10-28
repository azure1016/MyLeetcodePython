# request for reusable design: preprocess html can be totally different. So it would be nice if a preprocess function is passed as a parameter of Preprocessor.preprocess()
# higher-level abstraction
# maybe use unit-test as well!

# ASSUMPTIONS:
'''
1. We care about order of words in a tuple: for example: [go,for,a] is not the same as [for, a, go].
2. No need to do depunctuation/lowercase for synonyms!
3. We don't care about numbers in text, but we still retain numbers.
4. "I'm", "you're" will be regarded as one word.
5. If some tuple in originalText appears more than once, count as once? What if I count the exact appearing times?
6. If multiple texts are detected against one originalText, then class Detector should be initialize with one the originalText, generating a hashset against it. If not, generate a hashset against the shorter text to save memory
'''

# DESIGN INITIALTIVES
'''
HOW TO DETECT TUPLES WITH SAME MEANING
1. using dictionary(hashtable) + set;
    constrained: this would work if memory storage allowed; when N is proportional to m or n, then time complexity can be much worse
    time complexity: O(N*(m+n)), linear when N << m+n 
    where m is proportional to the number of N-tuples in originalText, n is proportional to the number of N-tuples in suspectText.

    space complexity: O(min(m,n))
    where m is proportional to the number of N-tuples in originalText, n is proportional to the number of N-tuples in suspectText.

2. create 'signature' for tuples: namely the hash, then do counting
    use 'rolling hash' to generating hash for a N-tuples in averagely O(1) time, namely O(m) for all N-tuples in orginalText (do the same for suspectText).

    constrained/challenge: collision of hashing; design an efficient hashing function.

    time complexity: O(m+n).
    space complexity: O(m+n): in the worst case, all m + n tuples are different, so we need m+n keys to store the appearance.

'''

import re
from collections import defaultdict


class Detector:
    def __init__(self, synonym_dictionary, words_of_original, N):
        '''
        here's the parameter doc
        ues doc_string?
        '''
        self.synonyms = synonym_dictionary
        # only generate hashset for the text with smaller size
        self.original_tuples = self.generate_tuples(N, words_of_original)


    def digit_representation(self, list_of_words, start, N):
        # generate a tuple representing each word as a number
        tpl = []
        for i in range(start, start + N):
            word = list_of_words[i]
            if word not in self.synonyms:
                self.synonyms[word] = len(self.synonyms)
            tpl.append(self.synonyms[word])
        tpl = tuple(tpl)
        return tpl

    def generate_tuples(self, N, list_of_words):
        # generate N-tuples for a list of words, store in a set
        tuples = set()  # if assumption 5 is not allowed, then use a hash table, use 'key' field to record appearance
        for i in range(len(list_of_words) - N + 1):
            tuples.add(self.digit_representation(list_of_words, i, N))
        return tuples

    def plagiarism_report(self, words_of_suspect, N):
        suspect_num = 0
        for i in range(len(words_of_suspect) - N + 1):
            if self.digit_representation(words_of_suspect, i, N) in self.original_tuples:
                suspect_num += 1
        percent = suspect_num * 1000 / (len(words_of_suspect) - N + 1)
        if percent % 10 >= 5: return percent / 10 + 1
        else: return percent / 10


class Preprocessor:
    def __init__(self):
        pass

    def to_lowercase(self, text):
        # preprocess: lowercase all words in text
        return text.lower()

    def depunctuation(self, text):
        # eliminate punctuations
        return re.findall(r"[\w']+", text)  # words or "I'm" will be retained

    def generate_synonym_dictionary(self, synonym_text):
        list_of_synonyms = synonym_text.split("|")
        synonym_dictionary = defaultdict()
        for i, synonyms in enumerate(list_of_synonyms):
            for word in synonyms.split():  # split by space
                # synonyms have the same value in dictionary
                synonym_dictionary[word] = i
        return synonym_dictionary

    def preprocess(self, text):
        # do all the preprocessing in one pass to improve performance: including changing to lowercase/eliminate punctuations/etc.
        return re.findall(r"[\w']+", text.lower())


def solution(inputs, tupleSize):
    preprocessor = Preprocessor()
    if len(inputs) != 3: raise ValueError()
    list_original = preprocessor.preprocess(inputs[1])
    list_suspect = preprocessor.preprocess(inputs[2])
    synonym_dictionary = preprocessor.generate_synonym_dictionary(inputs[0])

    detector = Detector(synonym_dictionary, list_original, tupleSize)
    return detector.plagiarism_report(list_suspect, tupleSize)

inputs = ["run sprint jog | zig zag zoe | i you she he it they | yesterday today tomorrow", "I ran for a jog yesterday. I will do so again, probably totay!", "I go for a jog today, I will not do it again because I'm tired!"]
tupleSize = 3
res = solution(inputs, tupleSize)
print(res)




