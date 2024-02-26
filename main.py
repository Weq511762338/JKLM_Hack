import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://jklm.fun/FGDF'



driver = webdriver.Chrome()
driver.get(url)



# html = requests.get(url)
# parsed = BeautifulSoup(html.content, 'html5lib')
# print(parsed.prettify())


# srccode = requests.get(url)
# # print(srccode.status_code)
# if srccode.status_code == 200:
#     page = srccode.content.decode()
#     print(page)
#     print(type(page))


# while True:
#     start = time.time()
    
#     srccode = requests.get(url)
#     print("time used: ", time.time()-start)
#     print(srccode)
