import time
from selenium import webdriver
import getpass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

# ---------------------------------INPUT FEILDS----------------------- 
# print("Select Your Option ?")
# select_type = int(input("1. Only Messages \n2. Only Messages And Images \nEnter :"))

# msg = input("Enter Messages : ") 
# phone_list = [""] #Enter Your Own Nuber List

# --------------------------ADVANCED SETTINGS--------------------------
options = Options()
options.add_argument(f"--user-data-dir=C:/Users/{getpass.getuser()}/AppData/Local/Google/Chrome/User Data/Default")
options.add_argument("--profile-directory=Default")
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu/')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
options.add_argument('--hide-scrollbars')
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)
options.add_experimental_option("debuggerAddress", "localhost:54037")


# ------------------------START HERE ------------------------------
#Start Here
browser = webdriver.Chrome(options=options)
# val = select_type
val =1
count = int(input())
# -----------------------------ONLY MESSAGES------------------------------
def paste_content(driver, el, content):
    driver.execute_script(
      f'''
    const text = `{content}`;
    const dataTransfer = new DataTransfer();
    dataTransfer.setData('text', text);
    const event = new ClipboardEvent('paste', {{
    clipboardData: dataTransfer,
    bubbles: true
    }});
    arguments[0].dispatchEvent(event)
    ''',el)
if val == 1 or val == 0:
    print("Running......")
    browser.get('https://web.whatsapp.com/')
    time.sleep(10)
    for i in range(count):
        browser.find_element(By.XPATH,"//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]").click()
        time.sleep(1)
        text = browser.find_element(By.XPATH,"//*[@id=\'main\']/footer/div[1]/div/span[2]/div/div[2]/div[1]")
        text.send_keys("i will fuck you")
        msg = '🍷🍻🍺🍷🍸🍾🥃🥃🍺'
        paste_content(browser, text, msg)
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id=\'main\']/footer/div[1]/div/span[2]/div/div[2]/div[2]").click()
    print("Finish Task... \n")
    browser.quit()     