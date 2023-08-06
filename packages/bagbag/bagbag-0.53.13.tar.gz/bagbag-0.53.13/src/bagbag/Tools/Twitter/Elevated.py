import tweepy
import typing 

class twitterUser():
    def __init__(self) -> None:
        self.ID:int = None 
        self.Name:str = None 
        self.ScreenName:str = None 
        self.Location:str = None 
        self.RegisterTime:int = None 
        self.Description:str = None 
        self.URL:str = None
        
    def __repr__(self) -> str:
        return f"twitterUser(ID={self.ID} Name={self.Name} ScreenName={self.ScreenName} Location={self.Location} RegisterTime={self.RegisterTime} URL={self.URL} Description={self.Description})"

    def __str__(self) -> str:
        return f"twitterUser(ID={self.ID} Name={self.Name} ScreenName={self.ScreenName} Location={self.Location} RegisterTime={self.RegisterTime} URL={self.URL} Description={self.Description})"

class twitterTweet():
    def __init__(self) -> None:
        self.ID:int = None
        self.User:twitterUser = None 
        self.Time:int = None 
        self.Text:str = None 
        self.Language:str = None 
    
    def __repr__(self) -> str:
        return f"twitterTweet(ID={self.ID} Time={self.Time} Language={self.Language} Text={self.Text} User={self.User})"
    
    def __str__(self) -> str:
        return f"twitterTweet(ID={self.ID} Time={self.Time} Language={self.Language} Text={self.Text} User={self.User})"

class Elevated():
    def __init__(self, consumer_key:str, consumer_secret:str) -> None:
        auth = tweepy.OAuth2AppHandler(consumer_key, consumer_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True)
    
    def _wrapUser(self, author) -> twitterUser:
        u = twitterUser()
        u.ID = author.id
        u.Name = author.name
        u.ScreenName = author.screen_name
        u.Location = author.location
        u.Description = author.description
        u.URL = author.url
        u.RegisterTime = int(author.created_at.timestamp())

        return u
    
    def _wrapStatus(self, status) -> twitterTweet:
        u = self._wrapUser(status.author)

        t = twitterTweet()
        t.User = u 

        t.ID = status.id # https://twitter.com/saepudin1991/status/1613434061741260803
        t.Time = int(status.created_at.timestamp())

        if hasattr(status, 'retweeted_status'):
            # 由于如果是转推, 那么status.full_text会被截断到140个字符, 而完整的推文在status.retweeted_status.full_text
            # 所以拼接一下
            sidx = 0
            foundsidx = False 
            while True:
                if sidx > 140 or status.full_text[sidx:-1] == "":
                    break 

                if status.full_text[sidx:-1] in status.retweeted_status.full_text:
                    foundsidx = True 
                    break 

                sidx += 1
            if foundsidx:
                text = status.full_text[:sidx] + status.retweeted_status.full_text
            else:
                text = status.full_text
        # 如果不是转推
        else:
            text = status.full_text
        t.Text = text

        t.Language = status.lang

        return t
    
    def Search(self, keyword:str, days:int=7) -> typing.Iterable[twitterTweet]:
        for status in tweepy.Cursor(self.api.search_tweets, q=keyword, tweet_mode='extended').items():
            yield self._wrapStatus(status)
    
    def Timeline(self, screename:str) -> typing.Iterable[twitterTweet]:
        for status in tweepy.Cursor(self.api.user_timeline, screen_name=screename, tweet_mode='extended').items():
            yield self._wrapStatus(status)
    
    def Followers(self, screename:str) -> typing.Iterable[twitterUser]:
        for user in tweepy.Cursor(self.api.get_followers, screen_name=screename).items():
            yield self._wrapUser(user)

if __name__ == "__main__":
    import json 

    cfg = json.loads(open('twitter.ident').read())

    twitter = Twitter(cfg['consumer_key'], cfg['consumer_secret'])
    
    print("search")
    for i in twitter.Search("coinsbee"):
        print(i)
        break 

    print('timeline')
    for i in twitter.Timeline("asiwaju_wa"):
        print(i)
        break 
    
    print("followers")
    for i in twitter.Followers("asiwaju_wa"):
        print(i)
        break 