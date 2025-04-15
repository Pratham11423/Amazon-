# Jai Shree Ram
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

# Search bar
driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Samsung S25 Ultra" + Keys.ENTER)
time.sleep(15)

# Scroll Down
driver.execute_script("window.scrollTo(0,800 )")
driver.implicitly_wait(4)
time.sleep(4)

# Add to Cart
driver.find_element(By.XPATH,'//*[@id="a-autoid-2-announce"]').click()
time.sleep(8)

# Go to cart
driver.find_element(By.XPATH,'//*[@id="ewc-compact-actions-container"]/div/div[2]/span/span/a').click()
time.sleep(8)

# Proceed to buy
driver.find_element(By.XPATH,'//*[@id="sc-buy-box-ptc-button"]/span/input').click()
time.sleep(8)

# scroll down
driver.execute_script("window.scrollTo(0,500 )")
driver.implicitly_wait(4)
time.sleep(4)

# click on Net Banking
driver.find_element(By.CLASS_NAME,'a-button-dropdown').click()
time.sleep(3)

# Click on Bank name
driver.find_element(By.XPATH,'//*[@id="pp-jgn5w1-119_5"]').click()
time.sleep(4)

# Click on Use this payment
driver.find_element(By.XPATH,'//*[@id="checkout-primary-continue-button-id"]/span/input').click()
time.sleep(8)

# Click on pay now
driver.find_element(By.XPATH,'//*[@id="placeOrder"]').click()
time.sleep(30)