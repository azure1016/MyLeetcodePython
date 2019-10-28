
class MyConverter:
    def __init__(self):
        self.unit_indent = 4

    def indent(self, depth):
        return self.unit_indent * depth * " "

    def parseObject(self, s, depth, wrap_start = '<body>', wrap_end = '<\\body>'):
        res = self.indent(depth) + wrap_start + '\n'
        start = s.find('value')
        end = s.find('orderedlist')
        if end == -1:
            end = len(s) + 2

        res += self.indent(depth + 1) + s[start+8: end-3] + '\n'
        ol_start = s.find('orderedlist')
        if ol_start != -1:
            res += self.parseList(s[ol_start + 15: len(s) - 2], depth + 1) # no [, ]
        res += self.indent(depth) + wrap_end + '\n'
        return res

    def parseList(self, s, depth): # receive a string starts without '['
        start, end = 0, -1
        res = self.indent(depth) + '<ol>' + '\n'
        while start != -1 and start < len(s):
            s = s[start:]
            start = s.find('{')
            if start != -1:
                end = s.find('}') + 1
                ol = s.find('orderedlist')
                if ol != -1 and ol < end:
                    end = len(s)
                res += self.parseObject(s[start:end], depth + 1, wrap_start = '<li>', wrap_end = '<\li>')
            start = end

        res += self.indent(depth) + '<\ol>' + '\n'
        return res

# class MyTest(TestCase):
#     def __init__(self, name):
#         super(MyTest, self).__init__(name)
#
#     def test1(self):
#         json = '{"value": 123, "orderedlist": [{"value": 12}, {"value": 12, "orderedlist": [{"value": 12}, {"value": 12}]}]}'
#         parser = MyConverter()
#         res = parser.parseObject(json, 0)
#         print(res[0:len(res-1)])


# test = MyTest('test1')
# test.test1()

json = '{"value": 123, "orderedlist": [{"value": 12}, {"value": 13, "orderedlist": [{"value": 14}, {"value": 15}]}]}'
parser = MyConverter()
res = parser.parseObject(json, 0)
print(res[0:len(res)-1])