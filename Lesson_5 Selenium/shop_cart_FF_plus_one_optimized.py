from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 1. Open Driver Function
def open_driver(browser="chrome"):
    """Initialize WebDriver for the specified browser.
    Supported browsers: 'chrome', 'firefox', 'edge'"""
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "ff":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser not supported. Choose 'chrome', 'firefox', or 'edge'.")
    driver.maximize_window()
    driver.implicitly_wait(4)
    waiter = WebDriverWait(driver, 30)
    return driver, waiter

# 2. Open Page and Add Cookies
def open_page(driver, url, cookies=None):
    """Open the specified page and optionally add cookies."""
    driver.get(url)
    if cookies:
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()  # Refresh to apply cookies

# 3. Search on Page and Go to Card Page
def search_on_page(waiter, search_query):
    """Perform a search on the page and navigate to the first product's card page."""
    # Wait for the search field and perform the search
    search_field = waiter.until(EC.element_to_be_clickable((By.ID, 'search-field')))
    search_field.send_keys(search_query, Keys.RETURN)

# Test Function 1: Add to Cart and Check Initial Quantity
def test_1(driver, waiter, url, cookies, search_query):
    open_page(driver, url, cookies)
    search_on_page(waiter, search_query)
    # Wait for the first product in the search results and click it
    first_product = waiter.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-card.need-watch.watched.gtm-watched")))
    first_product.find_element(By.CSS_SELECTOR, ".btn-tocart").click()
    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart"),'1'))
    initial_qty = driver.find_element(By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart").text
    return initial_qty

# Test Function 2: Navigate and Add to Cart from Product Page
def test_2(driver, waiter, url, search_query, initial_qty, btn_text):
    open_page(driver, url)
    search_on_page(waiter, search_query)
    # Wait for the <div> that contains the "ОФОРМИТЬ" button
    main_div = waiter.until(EC.presence_of_element_located((By.XPATH, f"//div[.//a[contains(text(), {btn_text})]]")))
    # Scroll to bring the div into view
    # driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", main_div)#FF
    driver.execute_script("arguments[0].scrollIntoView();", main_div)#Ch
    # Find the product link inside this <div>
    product_link = main_div.find_element(By.XPATH, ".//a[contains(@class, 'product-card__name')]")
    product_link.click()
    # Click the plusone button to increase the quantity
    one_more = waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".plusone")))
    one_more.click()
    # Wait for the cart quantity to update (e.g., from 1 to 2)
    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart"),
                                                  str(int(initial_qty) + 1)))
    # Get the updated cart quantity
    updated_qty = driver.find_element(By.CSS_SELECTOR, ".b-header-b-personal-e-icon-count-m-cart").text
    return updated_qty

def main():
    browser = 'chrome'  # Choose 'chrome', 'ff', or 'edge'
    url = "https://www.labirint.ru/"
    search_query = "python"
    btn_text = 'ОФОРМИТЬ'
    cookies = [{'name': 'cookie_policy','value': '1'}]
    driver, waiter = open_driver(browser)
    # Test 1: Add item to cart and verify initial quantity
    initial_qty = test_1(driver, waiter, url, cookies, search_query)
    print(f'Initial QTY is {initial_qty}')
    print(f'Passed: {initial_qty == '1'}')
    # Test 2: Increase quantity of the same item
    updated_qty = test_2(driver, waiter, url, search_query, initial_qty, btn_text)
    # Quantity Check in the Main Function
    print(f'Updated QTY is {updated_qty}')  # This should now reflect the correct quantity after adding another item
    print(f'Passed: {updated_qty == str(int(initial_qty) + 1)}')
    # Close the browser
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
