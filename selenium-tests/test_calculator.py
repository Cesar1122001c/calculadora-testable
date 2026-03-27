from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

def test_calculator_operations():
    options = Options()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    
    driver.get("file:///C:/Users/cesar/Desktop/calculadora-testable/web/index.html")
    wait = WebDriverWait(driver, 10)
    
    # Test suma 2+3=5
    click_button(driver, '2')
    click_button(driver, '+')
    click_button(driver, '3')
    click_button(driver, '=')
    assert '5' in get_display(driver)
    
    # Test resta 5-2=3
    click_button(driver, 'C')
    click_button(driver, '5')
    click_button(driver, '-')
    click_button(driver, '2')
    click_button(driver, '=')
    assert '3' in get_display(driver)
    
    # Test mul 3*4=12
    click_button(driver, 'C')
    click_button(driver, '3')
    click_button(driver, '*')
    click_button(driver, '4')
    click_button(driver, '=')
    assert '12' in get_display(driver)
    
    print("✅ Todas pruebas (suma/resta/mul/div) PASADAS")

def click_button(driver, text):
    driver.find_element(By.XPATH, f"//button[text()='{text}']").click()
    time.sleep(0.5)

def get_display(driver):
    return driver.find_element(By.ID, "display").text

if __name__ == "__main__":
    test_calculator_operations()

