import sys, time
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(argv):
    browser=webdriver.Chrome()
    cookbook="https://www.blueapron.com/cookbook"
    browser.get(cookbook)
    time.sleep(2)
    
    body=browser.find_element_by_tag_name('body')
    print "ESCAPE"
    body.send_keys(Keys.ESCAPE)
    
    for _ in range(25):
        time.sleep(5)
        print "PAGE_DOWN"
        for _ in range(3):
            body.send_keys(Keys.PAGE_DOWN)
        
    html_source=browser.page_source
    
    soup=BeautifulSoup(html_source, "html.parser")

    header3=soup.find_all("h3")
    header6=soup.find_all("h6")
    i=0
    for el in header6:
        print header3[4+i].string +" "+header6[i].string
        i=i+1
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))