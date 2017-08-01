import urllib
from urllib import request,parse
import http.cookiejar

url = 'http://www.renren.com/PLogin.do'
email = '***'
password = '***'

#通过CookieJar()构建一个cookieJar()对象，用来保存cookie的值
cookie = http.cookiejar.CookieJar()

#通过HTTPCookieProcessor()处理器类构造一个处理器对象，用来处理cookie
#参数就是构建的CookieJar()对象
cookie_handler = request.HTTPCookieProcessor(cookie)

#构建一个自定义的opener
opener = urllib.request.build_opener(cookie_handler)
#通过自定义opener的addheaders的参数，可以添加HTTP报头参数
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')]

#账号密码
data = {'email':email,'password':password}

#通过urlencode()编码转换
data = urllib.parse.urlencode(data).encode(encoding='UTF-8')

#第一次是post请求，发送登录需要的参数，获取cookie
request = urllib.request.Request(url,data = data)

#发送第一次的post请求，生成登录后的cookie（如果登录成功）
response = opener.open(request)

#print(response.read().decode(encoding='UTF-8'))

#第二次可以是get请求，这个请求将保存生成cookie一并发送到web服务器，服务器验证cookie通过
response1 = opener.open('http://www.renren.com/893258970/profile')

#获取登录后才能访问的页面信息
print(response1.read().decode(encoding='UTF-8'))