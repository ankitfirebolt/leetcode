class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users_followed = [userId] + list(self.following[userId])
        feed = []
        for u in users_followed:
            feed += self.tweets[u]
        return [x[1] for x in heapq.nlargest(10, feed, key = lambda k: k[0])]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)