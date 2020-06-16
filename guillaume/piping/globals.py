import requests
from bs4 import BeautifulSoup
import time
import os.path
import logging
from os import path
from datetime import date
from tqdm import tqdm
from random import randint

url = "http://www.ardeche.gouv.fr/"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

import downloadRaa
import getPageRaa
import getLinkFromHomePage