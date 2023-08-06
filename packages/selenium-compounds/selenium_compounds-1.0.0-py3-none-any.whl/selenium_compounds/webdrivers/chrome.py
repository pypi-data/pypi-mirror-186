import os
from datetime import datetime
# import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
    
    Documentation for command switches found at: http://peter.sh/experiments/chromium-command-line-switches/

"""


from tempfile import mkdtemp

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

EXECUTABLE_PATH = '/opt/chromedriver'
DIR_LOCAL = '.'
DIR_PREFIX = os.environ.get("DIR_PREFIX", DIR_LOCAL)

def get_driver():
    if DIR_PREFIX == DIR_LOCAL:
        return get_driver_local()
    else:
        return get_driver_remote()

def get_driver_local():
    
    print('Launching Chrome')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver = webdriver.Chrome(executable_path=r"C:\Users\mukthar\CDLZendesk\cdl\Resources\chromedriver.exe")
    # to maximize the browser window
    driver.maximize_window()
    print('Returning driver')
    return driver
    
    # print('Launching Chrome')
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--single-process')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument(f'--window-size=1280,1024')
    # binary_path = './headless-chromium'
    # options.binary_location = binary_path
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager(path=binary_path).install()), chrome_options=options)
    
    # to maximize the browser window
    driver.maximize_window()
    
    print('Returning driver')
    return driver

def get_driver_remote():
    
    print('Launching Remote Chrome')
    options = webdriver.ChromeOptions()

    # headless: Opens Chrome in headless mode
    options.add_argument('--headless')
    
    # Sets the initial window size. Provided as string in the format "800,600".
    options.add_argument(f"--window-size=1280,1024")
    
    # Runs the renderer and plugins in the same process as the browser 
    options.add_argument("--single-process")
    
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }

    driver = webdriver.Remote(
        "http://localhost:4444",
        options=options,
        desired_capabilities=d
    )
    
    driver.implicitly_wait(30)
    return driver

def launch_chrome():
    return get_driver()


# launch chrome driver
# def launchChrome():
#     print('Launching Chrome')
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     #driver = webdriver.Chrome(executable_path=r"C:\Users\mukthar\CDLZendesk\cdl\Resources\chromedriver.exe")
#     # to maximize the browser window
#     driver.maximize_window()
#     print('Returning driver')
#     return driver


#exit chrome drvier
def exit_chrome(driver):
    print('Exit driver')
    driver.quit()

# def before_feature(context, feature):
#     desired_cap = setup_desired_cap(CONFIG[INDEX])
#     context.browser = webdriver.Remote(
#         desired_capabilities=desired_cap,
#         command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
#     )
#
#
# def after_feature(context, feature):
#     context.browser.quit()
#
# def setup_desired_cap(desired_cap):
#     """
#     sets the capability according to LT
#     :param desired_cap:
#     :return:
#     """
#     return desired_cap
