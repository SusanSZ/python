import requests
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import urllib.request
import time

def list_hotel(pg):
    r = requests.get(url='http://hotels.ctrip.com/hotel/hangzhou17/p%d' % pg)
    soup = BeautifulSoup(r.text,"lxml")
    body=soup.body
    f1=body.form
    div=f1.find_all('div',id='base_bd')[0].find_all('div',id='J_mainBox')[0].find_all('div')[0].find_all('div',id='hotel_list')[0]
    urlset=set()
    for item in div.find_all('a'):
        urlset.add('http://hotels.ctrip.com'+item['href'])
    hotel_list=filter(lambda x:re.match(r"http://hotels\.ctrip\.com/hotel/(\d+)\.html\?isFull=F$",x) is not None,urlset)
    hotel_id=[]
    for x in hotel_list:
        m=re.match(r"http://hotels\.ctrip\.com/hotel/(\d*)",x)
        hotel_id.append(m.groups()[0])
    return hotel_id
    #for x in hotel_list:
     #   print(x)
#print(item.prettify())

def hotel_info(id):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    url="http://hotels.ctrip.com/hotel/dianping/%s.html" % id
    driver.get(url)
    time.sleep(5)
    name=driver.find_element_by_xpath("//div[@itemtype='//schema.org/Hotel']").text
    price_list=driver.find_elements_by_xpath("//span[@class='base_price']")
    pricelst=[]
    for i in price_list:
        pricetxt=i.text[1:]
        price=0
        try:
            price=int(pricetxt)
        except:
            pass
        if price:
            pricelst.append(price)
    aver_price=sum(i for i in pricelst)//len(pricelst)
    star=driver.find_element_by_xpath("//span[@class='n']").get_attribute("innerHTML")
    adress=driver.find_element_by_xpath("//div[@class='adress']").text.replace(',','，')
    #comments=[]
    #for i in range(1,150,2):
    #   url1="http://hotels.ctrip.com//hotel/dianping/435383_p%dt0.html" % i
    #   driver.get(url)
    #   time.sleep(5)
    #   cmts=driver.find_elements_by_xpath("//div[@class='J_commentDetail']")
    #   for i in cmts:
    #       comment=i.text
    #       comments.append(comment)
    print(name.encode('gb2312'),','.encode('gb2312'),aver_price.encode('gb2312'),','.encode('gb2312'),star.encode('gb2312'),',',',',',',adress.encode('gb2312'))
    #div1=f1.find_all('div',id='base_bd')[0].find_all('div',class_='main_detail_wrapper ')[0]
    #div2=div1.find_all('div',itemtype='//schema.org/Hotel')[0]
    #name=div2.h2.get_text()
    #price_list=soup.find_all('span',class_='base_price')
    #for i in price_list:
    #    print(i.prettify())
    #div2=div1.find_all()
    driver.quit()

def cmtpgs(id):
    #comments=[]
    for i in range(1,150,2):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        url="http://hotels.ctrip.com//hotel/dianping/%s_p%dt0.html" % (id,i)
        driver.get(url)
        time.sleep(5)
        cmtss=driver.find_elements_by_xpath("//div[@class='J_commentDetail show comment_txt_detail']")
        for x in cmtss:
            driver.execute_script("""
var i;
var p=document.getElementsByClassName('J_commentDetail show comment_txt_detail')
console.log(p.length);
for(i=0;i<p.length;i++){
        if(p[i]) p[i].className = 'J_commentDetail';
        if(p[i]) p[i].setAttribute('class','J_commentDetail');
}""")
        cmts=driver.find_elements_by_xpath("//div[@class='J_commentDetail']")
      #  print(len(cmts))
        psnstars=driver.find_elements_by_xpath("//div[@class='comment_main']//span[@class='score']//span[@class='n']")
        j=0
        for i in range(len(cmts)):
            psnstar=psnstars[j].text
            j+=1
            while psnstar=="":
                psnstar=psnstars[j].text
                j+=1
            comment=cmts[i].text
            comment=comment.replace(',','，')
            #comments.append(comment)
            print(',',',',psnstar.encode('gb2312'),',',comment.encode('gb2312'))
        driver.quit()
    #print(comments)

print('酒店名称,平均价格,总评分,评分，评论,地址'.encode('gb2312'))
for pg in range(1,20,2):
    hotel_list=list_hotel(pg)
    for item in hotel_list:
        hotel_info(item)
        cmtpgs(item)
        
        """break
    break"""