from unittest import TestCase
from collections import Deque
class JsonHtmlConverter:
    def __init__(self, json_string):
        self.json = json_string
        self.tokens = {'{':self.Element, '[':self.List, 'value':self.String, 'orderedlist':self.OrderedList}
        self.stack = Deque()
        self.res = "<body>"
    def parseOrderedList(self, s, depth):
        res = ""
        split_s = s.split(',')
        i = 0
        while i < len(split_s):
            parts = split_s.split(":")
            if split_s[i].startswith('{'):
                for j in range(i, len(split_s)):
                    if split_s[j].endswith('}'):
                        start = split_s[i][1:]
                        end = split_s[j][:len(split_s[j]) - 1]
                        sub_string = ",".join([start] + split_s[i+1:j] + [end])
                        res += self.parseListElement(sub_string, depth+1)
                        i = j + 1
                        break
                continue

            elif split_s[i].startswith('value'):
                res += " " * depth + parts[1] + '\n'
            elif split_s[i].startswith('orderedlist'):
                res += " " * depth + "<ol>" + '\n'
                res += self.parseOrderedList(parts[1][1:len(parts[1]) - 1], depth + 1)
                res += " " * depth + "<\ol>" + '\n'

        return res

    def parseListElement(self, s, depth):
        res = " " * depth + '<li>' + '\n'
        split_s = s.split(',')


    def parser(self, s, depth):
        split_s = s.split(',')
        for i in range(len(split_s)):
            parts = split_s.split(':')
            if split_s[i].startswith('{'):
                for j in range(i, len(split_s)):
                    if split_s[j].endswith('}'): # or use string.find
                        start = split_s[i][1:]
                        end = split_s[j][0:len(split_s[j]) - 1]
                        sub_string = ",".join([start]+split_s[i+1:j]+[end])
                        self.res += self.parser(sub_string, depth + 1)
            elif split_s[i].startswith('value'):
                self.res += " " * depth + parts[1] + '\n'
            elif split_s[i].startswith('orderedlist'):
                self.res += " " * depth + "<ol>" + '\n'
                self.res += self.parseOrderedList(parts[1][1:len(parts[1]) - 1], depth + 1) # strip ']','['
                self.res += " " * depth + "<\ol>" + '\n'
            if split_s.endswith('}'):
                self.res += "<\body>"

    def Element(self, s):
        pass

    def List(self, s):
        pass

    def String(self, s):
        pass

    def OrderedList(self, s):
        pass

class MyTest(TestCase):
    def __init__(self, name):
        super(MyTest, self).__init__(name)

    def test1(self):
        json_string = '{“value": 123, "orderedlist":[{"value”:12},{"value”:12}, "orderedlist":[{"value”:12},{"value”:12}]]}'
