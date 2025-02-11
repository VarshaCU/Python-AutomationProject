import time

from seleniumpagefactory import PageFactory


class GoHomePD(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
        'goH':('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[2]/div/a')
    }
    def Click_GohomePlacement(self):
        self.goH.click()
