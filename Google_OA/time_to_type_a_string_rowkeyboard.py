from collections import defaultdict, Counter
class Keyboard:
    def typing(self, keyboard, text):
        kb = defaultdict()
        for i, ch in enumerate(keyboard):
            kb[ch] = i
        time = 0
        last_pos = 0
        for i, ch in enumerate(text):
             time += abs(kb[ch] - last_pos)
             last_pos = kb[ch]
        return time

    def time_taken(self, keyboard, text):
        """
        Strategy: map letter to key index. for each char in text, lookup char in map and get abs val diff
        to curr position, add to res. update curr position.
        """
        res, curr = 0, 0
        map = {char: i for i, char in enumerate(keyboard)}
        for char in text:
            diff = abs(map[char] - curr)
            res += diff
            curr = map[char]
        return res

    def test1(self):
        keyboard = "abcdefghijklmnopqrstuvwxy"
        text = 'cba'
        time = self.typing(keyboard, text)
        print(time)

    def test2(self):
        keyboard = "abcdefghijklmnopqrstuvwxy "
        text = 'i love you'
        time1 = self.typing(keyboard, text)
        time2 = self.time_taken(keyboard, text)
        print(time1 == time2)


sol = Keyboard()
sol.test2()

