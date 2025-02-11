from selenium import webdriver
import time

from src.pages.LoginPage import LoginPage
from src.pages.StudentDashboard import SkillgunStuDashboard
from src.pages.GohomeNewPlacement import GoHomePD


driver=webdriver.Chrome()
def test_login():
    driver.get('https://skillgun.com')
    time.sleep(10)
    l=LoginPage(driver)
    l.enter_mobile('#your-phonenumber')
    time.sleep(5)
    l.enter_email('your-email@gmail.com')
    l.enter_pw('#your-password')
    l.click_cb()
    time.sleep(10)
    l.click_login()
    time.sleep(5)
    assert 'Student' in driver.current_url
def test_NewPlacemntDrive():
    dashboard=SkillgunStuDashboard(driver)
    dashboard.click_new_placementDrive()
    time.sleep(5)
    assert 'NewPlacementDrive' in driver.current_url
def test_GohomeFrmNewPD():
    dashB=GoHomePD(driver)
    dashB.Click_GohomePlacement()
    time.sleep(5)
    assert 'Home' in driver.current_url
def test_Interview_Schedule():
    dashboard=SkillgunStuDashboard(driver)
    dashboard.click_interview_schedules()
    time.sleep(5)
    assert 'Interviews' in driver.current_url


