from __future__ import annotations

try:
    from .. import Http
    from .. import Lg
    from .. import Random
    from .. import Hash
    from .. import Json
    from ..Http import useragents 
except:
    import sys 
    sys.path.append("..")
    import Http
    import Lg
    import Random
    import Hash
    import Json
    from Http import useragents 

import pygtrans

class Baidu():
    def __init__(self, appid:str, secretkey:str) -> None:
        self.appid = appid 
        self.secretkey = secretkey 
        self.apiurl = "http://api.fanyi.baidu.com/api/trans/vip/translate"
        self.to = "zh"
        self.From = "auto"

    def SetLang(self, To:str="zh", From:str="auto") -> Baidu:
        self.ffrom = From 
        self.to = To 
        return self 
    
    def Translate(self, text:str) -> dict:
        if "\n" in text:
            raise Exception("不允许换行符哦")

        salt = str(Random.Int(32768, 65536))
        preSign = self.appid + text + salt + self.secretkey
        sign = Hash.Md5sum(preSign)
        params = {
            "q":     text,
            "from":  self.ffrom,
            "to":    self.to,
            "appid": self.appid,
            "salt":  salt,
            "sign":  sign,
        }
        resp = Http.Get(self.apiurl, params)
        if resp.StatusCode != 200:
            raise Exception(f"翻译出错, 状态码: {resp.StatusCode}, 返回内容: {resp.Content}")
        
        rj = Json.Loads(resp.Content)

        return rj 

class Google():
    def __init__(self, httpProxy:str=None) -> None:
        self.httpProxy = httpProxy
        self.to = "zh-CN"
        self.From = "auto"

    def SetLang(self, To:str="zh-CN", From:str="auto") -> Google:
        self.From = From 
        self.to = To 
        return self 
    
    def Translate(self, text:str, format:str="html") -> str:
        """
        It translates the text from one language to another.
        
        :param text: The text to be translated
        :type text: str
        :param format: The format of the text to be translated, defaults to html. 可选html或者text
        :type format: str (optional)
        """
        client = pygtrans.Translate(
            target=self.to,
            source=self.From,
            fmt='html',
            user_agent=Random.Choice(useragents)['user_agent'],
            domain='com', # cn或者com
            proxies={"http": self.httpProxy},
        )
        return client.translate(text).translatedText

class NLLB():
    # version: '3'
    # services:
    #   nllb-arm64-facebook-nllb-200-distilled-600m:
    #     image: darren2046/nllb-arm64-facebook-nllb-200-distilled-600m
    #     container_name: nllb-arm64-facebook-nllb-200-distilled-600m-192.168.168.77
    #     restart: always
    #     ports:
    #       - 6060:6060

    def __init__(self, server:str) -> None:
        self.server = server 
        self.From = "eng_Latr"
        self.To = "zho_Hans"

        if not self.server.startswith("http://") and not self.server.startswith("https://"):
            self.server = "https://" + self.server + "/translate"
    
    def SetLang(self, To:str="zho_Hans", From:str="eng_Latr"):
        self.To = To 
        self.From = From
    
    def Translate(self, text:str) -> str:
        res = Http.PostForm(self.server, {
            "src_lang": self.From,
            "tgt_lang": self.To, 
            "source": text
        }, Timeout=60)
        # Lg.Trace(res.Content)

        res = Json.Loads(res.Content)
        
        return res["translation"][0]

if __name__ == "__main__":
    # appid, secretkey = open("baidu.ident").read().strip().split(',')
    # b = Baidu(appid, secretkey).SetLang("zh", "auto")
    # text = b.Translate("This is a test")
    # Lg.Trace(text)

    # g = Google("http://192.168.1.186:8899").SetLang("zh-CN")
    # text = g.Translate("This is a test")
    # Lg.Trace(text)

    n = NLLB("example.com")
    text = n.Translate("No Language Left Behind")
    Lg.Trace(text)