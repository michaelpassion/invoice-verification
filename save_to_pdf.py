from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os
import logging
import string

logging.basicConfig(level=logging.DEBUG)

def create_chrome_options():
    chrome_options = Options()
    settings = {
        "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "isLandscapeEnabled": True,
    }
    prefs = {
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        'savefile.default_directory': os.getcwd()  # 下载文件保存的路径
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing') #静默打印，无需用户点击打印页面的确定按钮
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--enable-print-browser')
    return chrome_options


def save_webpage_to_pdf(url):
    chrome_options = create_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    
    if not url.startswith('http'):
        url = "file:///"+os.path.abspath(url)
    driver.get(url)
    driver.maximize_window()
    js = "document.title='"+'xxxxx'+"';window.print();"  # 保存文件的文件名是文章标题，使用js的window.print()调出打印窗口,避免使用ctrl+P
    driver.execute_script(js)

    driver.close() 

if __name__ == '__main__':
    save_webpage_to_pdf("demo.html")


