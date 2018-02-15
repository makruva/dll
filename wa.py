from selenium import webdriver

chromedriver="E:\\project\python\chromedriver.exe"       
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os
import time
from selenium.webdriver.common.keys import Keys

os.environ["webdriver.chrome.driver"]=chromedriver  
driver=webdriver.Chrome(chromedriver)               
driver.get("http://web.whatsapp.com")
wait = ui.WebDriverWait(driver, 20)
results = wait.until(lambda driver:driver.find_element_by_css_selector("#input-chatlist-search"))
with open("E:\\kontak.txt") as daftar_kontak:
	for kontak in daftar_kontak:
		new_chat = driver.find_elements_by_css_selector("#side > header > div._20NlL > div > span > div:nth-child(2) > div > span")
		chat = new_chat[0]
		chat.click()
		driver.implicitly_wait(5)
		kontak = kontak.strip()
		search=driver.find_elements_by_css_selector("#input-chatlist-search")
		searchbox=search[0]
		searchbox.send_keys(kontak)
		driver.implicitly_wait(5) 
		selector_kontak = "span[title='"+kontak+"']"
		wait.until(lambda driver:driver.find_element_by_css_selector(selector_kontak))
		time.sleep(5)
		name=driver.find_element_by_css_selector(selector_kontak)
		print(selector_kontak)
		ActionChains(driver).move_to_element(name).click().perform()
		#name.click()
		text=driver.find_element_by_css_selector("#main > footer > div._3oju3 > div._2bXVy > div > div.pluggable-input-body.copyable-text.selectable-text")
		with open("E:\\wa.txt") as f:
			for line in f:
				text.send_keys(line.strip())
				text.send_keys(Keys.SHIFT,Keys.ENTER)
			text.send_keys(Keys.ENTER)
			time.sleep(5)
#driver.quit()
