import sys, time
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(argv):
    browser=webdriver.Chrome()
    cookbook="https://www.blueapron.com/cookbook"
    browser.get(cookbook)
    time.sleep(5)
    
    body=browser.find_element_by_tag_name('body')
    body.click()
    
    for _ in range(3):
        print "PAGE_DOWN"
        #body.click()
        for _ in range(5):
            body.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        
    html_source=browser.page_source
    
    soup=BeautifulSoup(html_source)
    #print soup
    
    '''
    header3=browser.find_elements_by_tag_name('h3')
    for el in header3:
        print el.text
    header6=browser.find_elements_by_tag_name('h6')
    for el in header6:
        print el.text
    '''
    #webpage=urllib2.urlopen(cookbook)
    #soup=BeautifulSoup(webpage)
    header3=soup.find_all("h3")
    header6=soup.find_all("h6")
    i=0
    for el in header6:
        print header3[4+i].string +" "+header6[i].string
        i=i+1
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))