import asyncio
import json
import os
import platform
import re
import time
import cloudscraper

import markdownify
import undetected_chromedriver as uc
import urllib3
from pyvirtualdisplay import Display
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

    def send_message(message: str) -> dict:

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
        scraper = cloudscraper.create_scraper()
        
        url = "https://you.com/api/youchatStreaming?question=" + str(message)
        loops = 0
        while loops < 10:
            try:
                msg = scraper.post(url).text
                break
            except:
                time.sleep(2)
                
                
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        return {"message": msg, "time": str(timedate)}
