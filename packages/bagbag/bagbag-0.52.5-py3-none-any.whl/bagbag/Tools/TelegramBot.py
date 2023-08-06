from __future__ import annotations

import telebot # https://github.com/eternnoir/pyTelegramBotAPI

try:
    from .Ratelimit import RateLimit
except:
    from Ratelimit import RateLimit

class TelegramBot():
    def __init__(self, token:str, ratelimit:str="20/m"):
        """
        :param token: The token of your bot
        :type token: str
        :param ratelimit: The ratelimit for the bot. This is a string in the format of "x/y" where x is
        the number of messages and y is the time period. For example, "20/m" means 20 messages per
        minute, defaults to 20/m. There is no limit if set to None.
        :type ratelimit: str (optional)
        """
        self.token = token 
        self.tb = telebot.TeleBot(self.token)
        self.tags:list[str] = []
        if ratelimit != None:
            self.rl = RateLimit(ratelimit)
        else:
            self.rl = None 
    
    def rateLimit(func): # func是被包装的函数
        def ware(self, *args, **kwargs): # self是类的实例
            if self.rl != None:
                self.rl.Take()

            res = func(self, *args, **kwargs)
            
            return res

        return ware

    @rateLimit
    def GetMe(self) -> telebot.types.User:
        return self.tb.get_me()
    
    @rateLimit
    def SetChatID(self, chatid:int) -> TelegramBot:
        self.chatid = chatid
        return self
    
    @rateLimit
    def SendFile(self, path:str):
        self.tb.send_document(self.chatid, open(path, 'rb')) 

    @rateLimit
    def SendImage(self, path:str):
        self.tb.send_photo(self.chatid, open(path, 'rb'))

    @rateLimit
    def SendVideo(self, path:str):
        self.tb.send_video(self.chatid, open(path, 'rb')) 

    @rateLimit
    def SendAudio(self, path:str):
        self.tb.send_audio(self.chatid, open(path, 'rb')) 

    @rateLimit
    def SendLocation(self, latitude:float, longitude:float):
        self.tb.send_location(self.chatid, latitude, longitude)
    
    @rateLimit
    def SetTags(self, *tags:str) -> TelegramBot:
        self.tags = tags
        return self 

    @rateLimit
    def SendMsg(self, msg:str, *tags:str):
        """
        It sends a message to a chat, and if there are tags, it adds them to the end of the message
        
        :param msg: The message to be sent
        :type msg: str
        :param : chatid: the chat id of the chat you want to send the message to
        :type : str
        """
        if len(tags) != 0:
            tag = '\n\n' + ' '.join(['#' + t for t in tags])
        else:
            if len(self.tags) != 0:
                tag = '\n\n' + ' '.join(['#' + t for t in self.tags])
            else:
                tag = ""
        
        if len(msg) <= 4096 - len(tag):
            self.tb.send_message(self.chatid, msg.strip() + tag) 
        else:
            for m in telebot.util.smart_split(msg, 4096 - len(tag)):
                self.tb.send_message(self.chatid, m.strip() + tag) 


if __name__ == "__main__":
    token, chatid = open("TelegramBot.ident").read().strip().split("\n")
    t = TelegramBot(token).SetChatID(int(chatid))
    # t.SendMsg(open("Telegram.py").read(), "tag1", "tag2")
    t.SendMsg("test")
    # t.SendFile("URL.py")