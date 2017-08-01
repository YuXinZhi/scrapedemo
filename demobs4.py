from bs4 import BeautifulSoup
import lxml
import requests
url = 'http://snsingwq.com/'
login_url = ''

def snslogin():
    #构建一个Session对象，可以保存cookie
    session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}

    #首先获取登录页面，找到需要POST的数据（rand），同时会记录当前网页的Cookie
    html = session.get(url=url,headers=headers).text
    #print(html)

    #调用lxml解析库
    bs = BeautifulSoup(html,'lxml')

    #获取验证码
    content = bs.find(attrs={'class':'rand_font'})
    rand = content.string

    data = {
        'sulname': '******',
        'sulpass': '******',
        'rand': rand,
        'B1.x': '0',
        'B1.y': '0'
    }

    response = session.post('http://snsingwq.com/login.jsp',data=data,headers=headers)
    print(response.text)

'''
    page_number = '1'
    page_url = 'http://snsingwq.com/programinfo_list_view.jsp?fileName=&programId=0&vcpId=&programTheme=2&castIdInfo=0&contryArea=&programState=2&movieType=&startTime=&endTime=&orderField=fileName&asc=1&pages='+page_number.

    response = session.get(page_url)
    print(response.text)
'''

if __name__ == '__main__':
        snslogin()