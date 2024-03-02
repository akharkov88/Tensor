import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os


class tensor(object):
    # Locators for Lambdatest Home Page
    start_url = 'https://sbis.ru/'
    contact = "//a[text()='Контакты']"
    img_tensor = "//img[@alt='Разработчик системы СБИС — компания «Тензор»']"
    p_detailed = '//p[text()="Сила в людях"]/..//a[text()="Подробнее"]'
    h2_contact = "//h2[text()='Контакты']/../..//div[2]/span/span"
    contacts_list = '//div[@id="contacts_list"]//div[@data-qa="item"]//i'
    kamchatskij = "//span[@title='Камчатский край']"
    download = "//a[text()='Скачать локальные версии']"
    download_plagin = "//div[text()='СБИС Плагин']/../../.."
    download_name = "//a[contains(text(), 'Скачать (Exe')]"
    p_work="//h2[text()='Работаем']/../..//img"
def test_script1():
    browser: WebDriver = webdriver.Chrome()
    browser.get(tensor.start_url)
    assert 'СБИС — экосистема для бизнеса: учет, управление и коммуникации' in browser.title

    browser.find_element(By.XPATH, tensor.contact).click()
    browser.find_element(By.XPATH, tensor.img_tensor).click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    browser.execute_script("arguments[0].focus();", browser.find_element(By.XPATH, tensor.p_detailed))
    browser.find_element(By.XPATH, tensor.p_detailed ).click()
    assert 'https://tensor.ru/about' in browser.current_url
    for val in browser.find_elements(By.XPATH, tensor.p_work):
        if 'comparison' in locals():
            assert comparison['height'] in val.get_attribute('height')
            assert comparison['width'] in val.get_attribute('width')
        else:
            comparison={'height':val.get_attribute('height'),'width':val.get_attribute('width')}
    browser.quit()

def test_script():
    browser: WebDriver = webdriver.Chrome()
    browser.get(tensor.start_url)
    assert 'СБИС — экосистема для бизнеса: учет, управление и коммуникации' in browser.title
    browser.find_element(By.XPATH, tensor.contact).click()
    assert browser.find_element(By.XPATH, tensor.h2_contact).get_attribute('innerHTML') in 'г. Москва'
    assert len(browser.find_elements(By.XPATH, tensor.contacts_list))!=0
    browser.find_element(By.XPATH, tensor.h2_contact).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, tensor.kamchatskij))).click()
    time.sleep(2)
    assert WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, tensor.h2_contact))).get_attribute('innerHTML') in 'Камчатский край'
    assert 'СБИС Контакты — Камчатский край' in browser.title
    assert '41-kamchatskij-kraj' in browser.current_url
    assert len(browser.find_elements(By.XPATH, tensor.contacts_list))!= 0
    browser.quit()
def test_script_():
    browser: WebDriver = webdriver.Chrome()
    browser.get(tensor.start_url)
    browser.execute_script("arguments[0].focus();", browser.find_element(By.XPATH, tensor.download))

    browser.find_element(By.XPATH, tensor.download).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, tensor.download_plagin)))
    time.sleep(2)
    browser.find_element(By.XPATH, tensor.download_plagin).click()

    path='/home/aleksey/Загрузки/sbisplugin-setup-web.exe'
    if os.path.exists(path):
        os.remove(path)
    myfile = requests.get(browser.find_element(By.XPATH, tensor.download_name).get_attribute('href'))
    open(path, 'wb').write(myfile.content)
    assert convert_bytes(os.stat(path).st_size) in str(browser.find_element(By.XPATH, tensor.download_name).get_attribute('innerHTML')).replace("Скачать (Exe ","")[:-2]
    browser.quit()

def convert_bytes(num):
    for x in ['bytes', 'KB', 'МБ', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.2f %s" % (num, x)
        num /= 1024.0



