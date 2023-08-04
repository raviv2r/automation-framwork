# call the selenium
# use the selenium coomands

# selenium code (python,java) > API HTTP Request > chromedriver /GekoDriver > chorme /firefox


from selenium import webdriver

# create a session
# send the coomand - nevigate to URl
# if you are using Selenium <4 , We use to the driver path
# If you are using the selenium > 4, driver path is not needed they will handle automaticliy
# 4.10


browser = webdriver.Chrome()
browser.get("https://lawpreptutorial.com/")