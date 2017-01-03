class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        curWordSet = set()
        result = []
        sLen = len(s)
        if sLen == 1:
            if s in wordDict:
                result.append(s)
                return result
            else:
                return result
        else:
            if self.checkChar(s, sLen, wordDict):
                cacheBuffer = {}
                return self.wordBreak2(s, sLen, 0, curWordSet, wordDict, "", cacheBuffer, result)
            else:
                return result
        
    def wordBreak2(self, inputStr, strLen, depth, curWordSet, wordDict, tmpRes, cacheBuffer, result):
        """
        :type inputStr: str
        :type strLen: int
        :type depth: int
        :type wordDict: Set[str]
        :type tmpWord: str
        :type tmpRes: str
        :type wordDict: Set[str]
        :rtype result: List[str]
        """
        if inputStr[depth:] in cacheBuffer:
            if depth == (strLen - 1):
                if not tmpRes:
                    result.append(cacheBuffer[inputStr[depth:]])
                else:
                    result.append(tmpRes[1:] + " " + cacheBuffer[inputStr[depth:]])
            else:
                return cacheBuffer[inputStr[depth:]]
        tmpWord = ""  
        for i in range(depth, strLen):
            tmpWord += inputStr[i]
            if tmpWord in curWordSet or tmpWord in wordDict:
                if i == (strLen - 1):
                    if not tmpRes:
                        result.append(tmpWord)
                    else:
                        result.append(tmpRes[1:] + " " + tmpWord)
                    break
                else:
                    curWordSet.add(tmpWord)
                    cacheBuffer[inputStr[0:i+1]] = (tmpRes + " " + tmpWord)
                    self.wordBreak2(inputStr, strLen, i+1, curWordSet, wordDict, tmpRes + " " + tmpWord, cacheBuffer, result)
                    del cacheBuffer[inputStr[0:i+1]]

        return result

    def checkChar(self, inputStr, strLen, wordDict):
        charSet = set()
        for word in wordDict:
            for i in range(len(word)):
                charSet.add(word[i])

        for i in range(strLen):
            if inputStr[i] in charSet:
                continue
            else:
                return False

        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.wordBreak("a", {"a"})
    print sol.wordBreak("apple", {"pear","apple","peach"})
    print sol.wordBreak("catsanddog", {"cat", "cats", "and", "sand", "dog"})
    # TODO: need debug when add cache
    print sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"})
    print sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", {"aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"})