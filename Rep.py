#coding:utf-8
import urllib
import re




'''
爬取贴吧图片并保存到d盘

创建新的分支dev
'''
def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()

def getJPGs(html):
    #图片正则表达式
    jpgReg = re.compile(r'img.+?src="(.+?\.jpg)" width')
    #解析出jpg的列表
    jpgs = re.findall(jpgReg,html)
    return jpgs

def downloadJPG(imgUrls,fileName):
    urllib.urlretrieve(imgUrls,fileName)

def batchDownloadJPGs(imgurls, path='D:/zdl'):
    count = 1
    for url in imgurls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print('正在下载第'+str(count)+'张')
        count = count + 1

def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

def main():
    url= 'http：//tieba.baidu.com/p/2256306796'
    download(url)

if __name__ == '__main__':
    main()
    #测试
    ####
    


