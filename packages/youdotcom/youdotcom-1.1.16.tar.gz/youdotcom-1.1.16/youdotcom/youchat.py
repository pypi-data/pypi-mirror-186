import asyncio
import json
import os
import platform
import re
import time
import urllib.parse
import subprocess
import chromedriver_autoinstaller
import cloudscraper
import markdownify
import undetected_chromedriver.v2 as uc
import urllib3
from pyvirtualdisplay import Display
from ratelimit import limits
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urllib3.disable_warnings()


class Chat:
    """
    An unofficial Python wrapper for YOU.com YOUCHAT
    """

    # def __init__(
    #     self,
    #     verbose: bool = False,
    #     window_size: tuple = (800, 600),
    #     driver: object = None,
    # ) -> None:

    #     self.__verbose = verbose
    #     self.__driver = driver
    @limits(calls=6, period=100)
    def send_message(message: str, context=None, context_form_file=None, debug=False, webdriver_path=None, headless=True, keep=False) -> dict:

        """
        Send a message to YouChat\n
        Parameters:
        - message: The message you want to send\n
        - driver: pass the driver form the Init variable\n
        Returns a `dict` with the following keys:
        - message: The response from YouChat\n
        - time: the time it took to complete your request
        """
        start = time.time()
        scraper = cloudscraper.create_scraper(
            browser={'browser': 'firefox','platform': 'windows','mobile': False},
            delay=10,
            debug=debug
        )
        CloudflareChallengeError = False
        typeof = ""
        if context_form_file:

            with open(context_form_file) as F:
                textjson = json.load(F)
                context = textjson["context"]

            message = str(message).replace(" ", "%20")
            totalcontext = "["
            for item in context:

                item = str(item)
                totalcontext += '{"question":"' + item + '","answer":" "},'
            totalcontext += "]"
            totalcontext = str(totalcontext).replace(" ", "%20")
            try:    
                response = scraper.get(f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&domain=youchat&chat={totalcontext}", stream=True)
            except cloudscraper.exceptions.CloudflareChallengeError:
                from youdotcom import Webdriver
                driver = Webdriver(webdriver_path=webdriver_path, hide=True, headless=headless,keep=keep).driver
                driver.get(f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&domain=youchat&chat={totalcontext}")
                
                CloudflareChallengeError = True
        if context and context_form_file == None:
            message = str(message).replace(" ", "%20")
            totalcontext = "["
            for item in context:

                totalcontext += '{"question":"' + item + '","answer":" "},'
            totalcontext += "]"
            totalcontext = str(totalcontext).replace(" ", "%20")
            try:
                response = scraper.get(f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&domain=youchat&chat={totalcontext}", stream=True)
            except cloudscraper.exceptions.CloudflareChallengeError:
                from youdotcom import Webdriver
                driver = Webdriver(webdriver_path=webdriver_path, hide=True, headless=headless,keep=keep).driver
                driver.get(f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&domain=youchat&chat={totalcontext}")
                
                CloudflareChallengeError = True
                
        if not context and not context_form_file:
            message = urllib.parse.quote(message)
            try:
                response = scraper.get(f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&domain=youchat&chat=[]", stream=True)
              
            except cloudscraper.exceptions.CloudflareChallengeError:
                from youdotcom import Webdriver
                driver = Webdriver(webdriver_path=webdriver_path, hide=True, headless=headless,keep=keep).driver
                driver.get(f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&mkt=&responseFilter=WebPages,Translations,TimeZone,Computation,RelatedSearches&domain=youchat&queryTraceId=96fc50c0-1beb-42a8-bc3f-2b33df0202bc&chat=%5B%5D")
                
                
                CloudflareChallengeError = True
            
        output = ""
        if CloudflareChallengeError == False:
            typeof = "api"
            print(typeof)
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    key, value = decoded_line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key == "data":
                        if value == "I'm Mr. Meeseeks. Look at me.":
                            break
                        data = json.loads(value)
                        if "youChatToken" in data:
                            output += data["youChatToken"]
        if CloudflareChallengeError == True:
            typeof = "webdriver"
            print(typeof)
            # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "pre"), 'youChatToken'))
            listofdriver = driver.page_source.split("\n")
            print(driver.page_source)
            for line in listofdriver:
                if line:
                    
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                   
                    if key == "data":
                        if value == "I'm Mr. Meeseeks. Look at me.":
                            break
                        # data = json.loads(value[1:])
                        if "youChatToken" in value:
                            output += value.replace('{"youChatToken": " ', "")
                            
                            
        out = re.sub(r'\[.+?\]\(.+?\)', '', output)
        # out = out[1:]
        msg = markdownify.markdownify(out)
        
        # subprocess.call(["taskkill", "/im", "chromedriver.exe"],shell=True)
        # subprocess.call(["pkill", "-f", "chromedriver"], shell=True)
        # subprocess.call(["killall", "-m", "chromedriver"], shell=True)
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        
        return {"message": msg, "time": str(timedate), "v2Captcha": str(CloudflareChallengeError), "type": str(typeof)}
