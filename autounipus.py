from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Gaming\chromedriver.exe')

username = 161002516
password = 161002516

driver.get(url="http://202.204.121.159/")

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("newlogintable_third_button").click()

my_script = open("core/myscript.js", encoding='utf-8').read()
addIn = "var keyScore = %s; \n" % (80 / 100)

my_script = addIn + my_script

driver.execute_script()