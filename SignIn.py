# Jai Shree Ram

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
driver = webdriver.Chrome()
# driver = webdriver.Chrome('C:\BSPLAut\chromedriver.exe')
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(4)
UserNumber = ""

# enter the number
driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys(UserNumber)
time.sleep(3)
# click on the button
driver.find_element(By.XPATH,'//*[@id="continue"]').click()
time.sleep(6)

# //*[@id="continue"]
# click for the OTP

driver.find_element(By.ID,'continue').click()
time.sleep(30)

