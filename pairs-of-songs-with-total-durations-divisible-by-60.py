# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
from math import comb

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        arr = [(x % 60) for x in time]
        myDict = Counter(arr)
        
        if (myDict[0] >= 2):
            result += comb(myDict[0],2)
        if (myDict[30] >= 2):
            result += comb(myDict[30],2)
        
        del myDict[0]
        del myDict[30]
        
        for key in myDict:
            if (60 - key) in myDict:
                result+= myDict[key] * myDict[60 - key]
                myDict[key] = 0
                myDict[60 - key] = 0
        
        return result
