import urllib.request
import re
def getVideo(page):
        input_web=input('请输入网址')
        req = urllib.request.Request("%s/%s" %page%input_web)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        html = urllib.request.urlopen(req).read()
        html = html.decode('UTF-8')
        reg = r'data-mp4="(.*?)"'
        for i in re.findall(reg,html):
            filename = i.split("/")[-1]#以‘/ ’为分割f符，保留最后一段，即MP4的文件名
            print ('正在下载%s视频' %filename)
            urllib.request.urlretrieve(i,"mp4/%s"%filename)
for  i in range (1,20):
    getVideo(i)
