class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def toWord(s: str):
            words = []
            current = ""

            for ch in s:
                if ch == ' ':
                    words.append(current)
                    current = ""
                else:
                    current += ch

            words.append(current)
            return words

        words = toWord(s)

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in p_to_w:
                if p_to_w[p] != w:
                    return False
            else:
                p_to_w[p] = w

            if w in w_to_p:
                if w_to_p[w] != p:
                    return False
            else:
                w_to_p[w] = p

        return True
