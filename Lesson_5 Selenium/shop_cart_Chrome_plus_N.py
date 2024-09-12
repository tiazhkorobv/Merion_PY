from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser2 = webdriver.Chrome(options=chrome_options)
browser2.get('https://www.labirint.ru/')
browser2.implicitly_wait(20)

token_my = {
    'name':'cookie_policy',#именно 'name', а не как в таблице - по-русски или с б.буквы
    'value':'1'#именно 'value', а не как в таблице - по-русски или с большой буквы
}
browser2.add_cookie(token_my)
browser2.maximize_window()
waiter = WebDriverWait(browser2,30)

# Search for 'python' on the Labirint site
waiter.until(EC.element_to_be_clickable((By.ID, 'search-field'))).send_keys('python', Keys.RETURN)

# Click on the first product in the search results
waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-card.need-watch.watched.gtm-watched"))).click()

# Click on the 'Buy' button
waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-buy"))).click()

# Return to the main page
browser2.get('https://www.labirint.ru/')

# Get the initial quantity in the cart
initial_qty_element = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart")))
initial_qty = int(initial_qty_element.text)  # Convert initial quantity to integer
print(f'Initial QTY is {initial_qty}.')

# Define the quantity to increase by
quantity_to_increase = 3  # Example: Increase by 3 items

# Perform a new search for 'python'
waiter.until(EC.element_to_be_clickable((By.ID, 'search-field'))).send_keys('python', Keys.RETURN)

# Wait for the <div> that contains the "ОФОРМИТЬ" button
main_div = waiter.until(EC.presence_of_element_located((By.XPATH, "//div[.//a[contains(text(), 'ОФОРМИТЬ')]]")))

# Scroll to ensure the element is in view
browser2.execute_script("arguments[0].scrollIntoView();", main_div)#скролл для хрома канает и без аргументов

# Find the product link inside this <div> using the class 'product-card__name'
product_link = main_div.find_element(By.XPATH, ".//a[contains(@class, 'product-card__name')]")
sleep(10)
# Click the product link to navigate to the item's details page
product_link.click()
sleep(10)
# Wait for the 'plusone' button and click to increase the quantity
plusone_button = waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".plusone")))

# Click the 'plusone' button the specified number of times
for _ in range(quantity_to_increase):
    plusone_button.click()

# Calculate the expected cart quantity after the increase
expected_qty = initial_qty + quantity_to_increase
print(f'Expected QTY after increase is {expected_qty}.')

# Explicitly wait for the cart quantity to be updated
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart"), str(expected_qty)))

# Get the updated cart quantity
updated_qty_element = browser2.find_element(By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart")
updated_qty = updated_qty_element.text
print(f'Updated QTY is {updated_qty}.')  # This should now reflect the correct quantity after adding items

# Close the browser
browser2.quit()
