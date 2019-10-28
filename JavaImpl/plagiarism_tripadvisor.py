import re
from collections import defaultdict

class Texter:
    def plagiarism_detect(self, dictionary, s1, s2):
        # assume dictionary is list of string list
        # every row is synonyms
        # I assume no numbers in the dictionary or numbers are not considered
        # initialize the dict
        d = defaultdict()
        for i in range(len(dictionary)):
             for j in range(len(dictionary[i])):
                 d[dictionary[i][j]] = i
        
                    
        # do you care about upper / lower case?
        s1 = s1.lower()
        s2 = s2.lower()

        # split the strings, form list
        # I assume no numbers in the dictionary or numbers are not considered
        sl1 = re.findall(r"[\w']+", s1) # by space and signs
        sl2 = re.findall(r"[\w']+", s2) # do you care about "'" in "it's" ?
