from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:/Users/jdhanjani/PycharmProjects/POMprojectDemo/tests/login.py")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("username")
