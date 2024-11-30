from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Test case 1: Verify the home page loads correctly
def test_home_page():
    # Set up the Selenium WebDriver (make sure ChromeDriver is installed and in PATH)
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:5000/")  # Replace with your deployed app URL if necessary
        assert "Welcome to Sample Web App!" in driver.page_source
        print("Home page test passed!")
    except Exception as e:
        print("Home page test failed:", e)
    finally:
        driver.quit()

# Test case 2: Verify adding a visitor works
def test_add_visitor():
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:5000/")  # Replace with your deployed app URL if necessary
        
        # Access the add visitor page
        driver.get("http://localhost:5000/add-visitor/testuser")
        time.sleep(2)  # Wait for the page to process

        # Verify the response
        assert "Visitor testuser added!" in driver.page_source
        print("Add visitor test passed!")
    except Exception as e:
        print("Add visitor test failed:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_home_page()
    test_add_visitor()
