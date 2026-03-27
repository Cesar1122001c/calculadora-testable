from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

def test_calculator_visible():
    """Pruebas con Firefox visible mostrando cada operación"""
    options = Options()
    # Aquí puedes descomentar para modo headless (sin ventana):
    # options.add_argument("--headless")
    
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    
    try:
        driver.get("file:///C:/Users/cesar/Desktop/calculadora-testable/web/index.html")
        driver.maximize_window()  # Maximizar la ventana
        
        print("\n" + "="*60)
        print("🧪 INICIANDO PRUEBAS DE CALCULADORA CON SELENIUM + FIREFOX")
        print("="*60 + "\n")
        
        # Test 1: Suma 2+3=5
        print("Test 1️⃣: Suma (2 + 3 = 5)")
        click_button(driver, '2')
        print("  ✓ Clickeado: 2")
        click_button(driver, '+')
        print("  ✓ Clickeado: +")
        click_button(driver, '3')
        print("  ✓ Clickeado: 3")
        click_button(driver, '=')
        print("  ✓ Clickeado: =")
        resultado = get_display(driver)
        assert '5' in resultado, f"Esperado 5, obtuve {resultado}"
        print(f"  ✅ Resultado: {resultado}\n")
        
        # Test 2: Resta 5-2=3
        print("Test 2️⃣: Resta (5 - 2 = 3)")
        click_button(driver, 'C')
        print("  ✓ Clickeado: C (Limpiar)")
        time.sleep(0.3)
        click_button(driver, '5')
        print("  ✓ Clickeado: 5")
        click_button(driver, '-')
        print("  ✓ Clickeado: -")
        click_button(driver, '2')
        print("  ✓ Clickeado: 2")
        click_button(driver, '=')
        print("  ✓ Clickeado: =")
        resultado = get_display(driver)
        assert '3' in resultado, f"Esperado 3, obtuve {resultado}"
        print(f"  ✅ Resultado: {resultado}\n")
        
        # Test 3: Multiplicación 3*4=12
        print("Test 3️⃣: Multiplicación (3 × 4 = 12)")
        click_button(driver, 'C')
        print("  ✓ Clickeado: C (Limpiar)")
        time.sleep(0.3)
        click_button(driver, '3')
        print("  ✓ Clickeado: 3")
        click_button(driver, '*')
        print("  ✓ Clickeado: *")
        click_button(driver, '4')
        print("  ✓ Clickeado: 4")
        click_button(driver, '=')
        print("  ✓ Clickeado: =")
        resultado = get_display(driver)
        assert '12' in resultado, f"Esperado 12, obtuve {resultado}"
        print(f"  ✅ Resultado: {resultado}\n")
        
        # Test 4: División 10/2=5
        print("Test 4️⃣: División (10 ÷ 2 = 5)")
        click_button(driver, 'C')
        print("  ✓ Clickeado: C (Limpiar)")
        time.sleep(0.3)
        click_button(driver, '1')
        print("  ✓ Clickeado: 1")
        click_button(driver, '0')
        print("  ✓ Clickeado: 0")
        click_button(driver, '/')
        print("  ✓ Clickeado: /")
        click_button(driver, '2')
        print("  ✓ Clickeado: 2")
        click_button(driver, '=')
        print("  ✓ Clickeado: =")
        resultado = get_display(driver)
        assert '5' in resultado, f"Esperado 5, obtuve {resultado}"
        print(f"  ✅ Resultado: {resultado}\n")
        
        print("="*60)
        print("✅ ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        print("="*60)
        
        # Mantener Firefox abierto 3 segundos para que veas el resultado
        time.sleep(3)
        
    except Exception as e:
        print(f"\n❌ ERROR en las pruebas: {e}")
        time.sleep(5)  # Mantener abierto para ver el error
        raise
    finally:
        driver.quit()  # Cerrar Firefox al finalizar

def click_button(driver, text):
    """Hacer clic en un botón por su texto"""
    button = driver.find_element(By.XPATH, f"//button[text()='{text}']")
    button.click()
    time.sleep(0.5)  # Pequeña pausa para ver visualmente

def get_display(driver):
    """Obtener el valor mostrado en la pantalla"""
    return driver.find_element(By.ID, "display").text

if __name__ == "__main__":
    test_calculator_visible()
