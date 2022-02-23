from selenium.webdriver.common.by import By
class LocatorLogin(object):
    email=(By.ID,'email')
    password=(By.ID,'password')
    loginButton = (By.ID, 'loginButton')
class first(object):
    dismiss=(By.XPATH,"//*[@id='mat-dialog-0']/app-welcome-banner/div/div[2]/button[2]/span[1]/span")
class last(object):
    quit1 = (By.ID, "navbarAccount")
    quit2 = (By.ID, "navbarLogoutButton")
class LocatorRegiter(object):
    pass
class LocatorBasket(object):
    pass