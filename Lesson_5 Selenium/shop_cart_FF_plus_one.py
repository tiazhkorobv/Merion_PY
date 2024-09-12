from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver

# chrome_options = Options()
# # chrome_options.add_experimental_option("detach", True)
#browser2 = webdriver.Chrome()
browser2 = webdriver.Firefox()
browser2.implicitly_wait(4)
browser2.get('https://www.labirint.ru/')
token_my = {
    'name':'cookie_policy',#именно 'name', а не как в таблице - по-русски или с б.буквы
    'value':'1'#именно 'value', а не как в таблице - по-русски или с большой буквы
}
browser2.add_cookie(token_my)
browser2.maximize_window()
waiter = WebDriverWait(browser2,30)
waiter.until(EC.element_to_be_clickable((By.ID,'search-field'))).send_keys('python',Keys.RETURN)
waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".product-card.need-watch.watched.gtm-watched"))).click()
waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-buy"))).click()


browser2.get('https://www.labirint.ru/')
initial_qty = browser2.find_element(By.CSS_SELECTOR,".b-header-b-personal-e-icon-count-m-cart").text
print(f'QTY is {initial_qty}.')
print(initial_qty == '1')

# Wait for the search field and search for 'python'
waiter.until(EC.element_to_be_clickable((By.ID, 'search-field'))).send_keys('python', Keys.RETURN)

# Wait for the <div> that contains the "ОФОРМИТЬ" button
main_div = waiter.until(EC.presence_of_element_located((By.XPATH, "//div[.//a[contains(text(), 'ОФОРМИТЬ')]]")))

# Scroll only enough to ensure the element is in view but not overshoot
browser2.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", main_div)

# Now find the product link inside this <div> using the class 'product-card__name'
product_link = main_div.find_element(By.XPATH, ".//a[contains(@class, 'product-card__name')]")

# Click the product link to navigate to the item's details page
product_link.click()

# Wait for the item page to load (you can add some action here or check if a particular element is present)
# waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".plusone"))).click()
# browser2.implicitly_wait(30)
# qty = browser2.find_element(By.CSS_SELECTOR,".b-header-b-personal-e-icon-count-m-cart").text

# Wait for the 'plusone' button and click to increase the quantity
waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".plusone"))).click()

# Explicitly wait for the cart quantity to be updated (e.g., from 1 to 2)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart"), str(int(initial_qty) + 1)))

# Get the updated cart quantity
updated_qty = browser2.find_element(By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart").text
print(f'Updated QTY is {updated_qty}.')  # This should now reflect the correct quantity after adding another item

# Close the browser
# browser2.quit()

# . (Dot):
#    In XPath, the dot (.) represents the current node. It refers to the element itself and its text content.
#    So, . retrieves the text of the current element, including any nested text nodes (i.e., the text inside its child elements).
#  contains():
#    The contains() function is used to check whether a string (or node) contains a specific substring.
#    The syntax is contains(target, substring), where:
#         target is the element or attribute to search within.
#         substring is the text you're looking for.

print(updated_qty == '2')
# browser2.quit()


