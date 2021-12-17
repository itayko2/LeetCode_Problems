# https://leetcode.com/problems/design-an-ordered-stream/
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.size = n
        self.curr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        temp = self.curr
        while (self.curr < self.size) and (self.stream[self.curr] != None) :
            self.curr += 1
            
        return self.stream[temp:self.curr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
