import time
import pymongo
import requests
# from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
# import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = client["dictionary_database"]
# mycol = mydb["words"]
# # print(client.list_database_names())
# url = "https://www.google.com/search?q=ant meaning in bengali google translate"
# response = requests.get(url)
# response.encoding = 'utf-8'
# # doc = html5lib.parse(response.text)
# # with open("output.html") as fp:
# soup = BeautifulSoup(response.content, features="lxml")
# # soup = html5lib.parse(doc)
# # meanings = soup.find_all("span", {"class": "SvKTZc"})
# # meanings = soup.find_all("span", class_="hrcAhc")
# # meanings = soup.find_all("span", attrs={"class": "hrcAhc"})
# # meanings = soup.select(".MUxGbd u31kKd gsrt lyLwlc")
# meanings = soup.find_all(id="lrtl-translation-text")
# # meanings = soup.select("[class~=hrcAhc4]")
# print(meanings[0].get_text())
# f = open("output.html", "w", encoding="utf-8")
# print(soup.prettify(), file=f)

def main():

    # f = open(r"D:\PythonProject\dictionary_project\data\a30.txt", "r")

    start = time.time()
    print("sample test case started")
    driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver')
    #driver=webdriver.firefox()  
    #driver=webdriver.ie()  
    #maximize the window size  
    driver.maximize_window()
    #navigate to the url
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("python")  
    time.sleep(3)
    #click on the Google search button  
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
    time.sleep(3)
    #close the browser  
    driver.close()
    print("sample test case successfully completed")
    # readlines = f.readlines()
    # for line in readlines:
    #     print(line, end="")
    
    # for x in mycol.find():
    #     print(x)

    # print(f.readlines())
    end = time.time()
    print(f"\nTime taken: {(end-start)} sec.")
    # f.close()

    # import time

    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service

    # service = Service('/path/to/chromedriver')
    # service.start()
    # driver = webdriver.Remote(service.service_url)
    # driver.get('http://www.google.com/');
    # time.sleep(5) # Let the user actually see something!
    # driver.quit()

if(__name__ == "__main__"):
    main()