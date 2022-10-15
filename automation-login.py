import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

Accounts = [('testertamvan000@gmail.com','Qwerty%'),
            ('testertamvan@gmail.com','Qwerty%0'),
            ('testertamvan000','kwerti123'),
            ('','Qwerty%0'),
            ('testertamvan000@gmail.com','')
]

@pytest.fixture
def setup():
    browser = webdriver.Chrome()
    browser.get("https://id.blooket.com/login")
    browser.implicitly_wait(10)
    browser.minimize_window()
    yield browser
    browser.close()


def test_login_success(setup):
    setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[4]/input').send_keys('testertamvan000@gmail.com')
    setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[5]/input').send_keys('Qwerty%0')
    setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/input').click()

    name = setup.find_element(By.XPATH,'/html/body/div/div/div/div[8]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]').text
    assert name == 'shidqiadiatma'

@pytest.mark.parametrize('uemail,upassword', Accounts)
def test_login_unsuccess(setup, uemail, upassword):
    setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[4]/input').send_keys(uemail)
    setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[5]/input').send_keys(upassword)
    setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/input').click()

    alert = setup.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[6]/div').is_displayed()
    assert alert == True

