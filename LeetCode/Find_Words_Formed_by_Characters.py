class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = 0
        for word in words:
            good = True
            for l in word:
                if chars.count(l) < word.count(l): 
                    good = False
                    break 
            if good == True: c += len(word)
        return c 