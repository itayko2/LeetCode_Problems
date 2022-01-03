https://leetcode.com/problems/design-twitter/
class Twitter:

    def __init__(self):
        self.twitterDict = dict()
        self.listOfTwitts = []
        self.recent = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.checkIfFirstTime(userId)
        self.listOfTwitts.insert(0,[tweetId,userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for twitt in self.listOfTwitts:
            if twitt[1] in self.twitterDict[userId]:
                if len(feed) == self.recent:
                    break
                    
                feed.append(twitt[0])

        return feed
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.checkIfFirstTime(followerId)
        self.twitterDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.twitterDict[followerId]:
            self.twitterDict[followerId].remove(followeeId)
    
    def checkIfFirstTime(self, userId: int) -> None:
        if userId not in self.twitterDict:
            self.twitterDict[userId] = {userId}
            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
