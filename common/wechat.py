import requests

appid = 'wx0f0c0a0a0a0a0a0a'
secrets ='23123123123123123123123123123123'
# 根据code获取openid
class WeChat():
    def __init__(self):
        self.appid = appid
        self.secrets = secrets

    def get_openid(self, code):
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s' % (self.appid, self.secrets, code)
        res = requests.get(url)
        return res.json()['openid']
