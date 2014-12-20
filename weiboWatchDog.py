#coding=utf8
from weibo import APIClient
from time import sleep
import urllib2, urllib, cookielib, json, sys, random


APP_KEY = ''
APP_SECRET = ''
CALLBACK_URL = ''
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
USER_ID = ''
PASSWORD = ''
UID = ''
DICTIONARY = 'dictionary.txt'
WEIBO_COUNT = 20
#COMMENT = "好好学习，别刷微博"


#wzp 1237207140
#gya 1806978950

file_handler = open(DICTIONARY, 'r')
file_content = file_handler.readlines()
file_length = len(file_content)

def getCode(user_id, passwd):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    postdata = {
        "action": "login",
        "client_id": APP_KEY,
        "redirect_uri":CALLBACK_URL,
        "userId": user_id,
        "passwd": passwd,
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Referer":referer_url,
        "Connection":"keep-alive"
    }
    req = urllib2.Request(
        url = AUTH_URL,
        data = urllib.urlencode(postdata),
        headers = headers
    )
    resp = urllib2.urlopen(req)
    return resp.geturl()[-32:]

def prepare():
    code = getCode(USER_ID, PASSWORD)
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    response = client.request_access_token(code)
    access_token = response.access_token
    expires_in = response.expires_in
    client.set_access_token(access_token, expires_in)
    return client

def randomString():
    i = random.randint(1,10)
    arr = []
    global file_content, file_length
    for i in range(1,i):
        offset = random.randint(0, file_length-1)
        val = file_content[offset].strip()               
        arr.append(val)
    return ''.join(arr)

def catch(randomComment):    
    try:
        client = prepare()
        result2 = client.statuses.home_timeline.get(count=WEIBO_COUNT)
        results = result2['statuses']
        for result in results:
            weibo_id = result['id']            
            user_id = str(result['user']['id'])
            user_name = result['user']['screen_name']
            print user_name
            if(not cmp(user_id, "1806978950")):
                result = client.comments.create.post(comment=randomComment, id=weibo_id)
    except APIError:
        print 'Repetitive comment'
    except:
        print 'Unknown exception'
    finally:
        print 'return'
        return
        
def timing():
    while True:
        random_comment = randomString()
        catch(random_comment)        
        print 'going to sleep'
        sleep(30)
        print 'wake up'

if __name__ == '__main__':    
    timing()
