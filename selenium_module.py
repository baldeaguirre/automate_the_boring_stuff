from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
elem.click()

elems = browser.find_elements_by_css_selector('p')

browser = webdriver.Firefox()
browser.get('https://wikipedia.org')

searchElem = browser.find_element_by_css_selector('#searchInput')
searchElem.send_keys('Python')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_elements_by_css_selector('.main > div:nth-child(1) > blockquote:nth-child(5)')

for value in elem:
    print(value.text)

elem = browser.find_elements_by_css_selector('html')

for value in elem:
    print(value.text)