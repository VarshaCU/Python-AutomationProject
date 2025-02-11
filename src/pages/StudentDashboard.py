from seleniumpagefactory import PageFactory


class SkillgunStuDashboard(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
        'newplacement':('id','ContentPlaceHolder1_ahrefnewdrive'),
        'interviews':('id','ContentPlaceHolder1_ahrefInterview')
    }
    def click_new_placementDrive(self):
        self.newplacement.click()
    def click_interview_schedules(self):
        self.interviews.click()

