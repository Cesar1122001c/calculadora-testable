from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
import time
import sys

def test_calculator_window():
    """Ejecutar pruebas en Firefox con ventana VISIBLE"""
    
    # Configurar opciones de Firefox
    options = Options()
    # NO usar headless - queremos ver la ventana
    options.set_preference("dom.webdriver.enabled", True)
    options.set_preference("useAutomationExtension", False)
    
    print("\n" + "="*70)
    print("🔥 INICIANDO FIREFOX CON SELENIUM")
    print("="*70)
    print("\n⏳ Abriendo Firefox en 2 segundos...")
    time.sleep(2)
    
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    
    try:
        print("✅ Firefox abierto correctamente\n")
        
        # Cargar la calculadora
        calculadora_path = "file:///C:/Users/cesar/Desktop/calculadora-testable/web/index.html"
        print(f"📂 Cargando calculadora desde:")
        print(f"   {calculadora_path}\n")
        
        driver.get(calculadora_path)
        driver.maximize_window()
        
        print("\n" + "="*70)
        print("🧪 EJECUTANDO PRUEBAS EN TIEMPO REAL")
        print("="*70 + "\n")
        
        time.sleep(1)
        
        # Test 1: Suma
        print("✏️  Test 1: SUMA (2 + 3 = 5)")
        print("─" * 50)
        
        print("  ► Haciendo clic en: 2")
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: +")
        driver.find_element(By.XPATH, "//button[text()='+']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 3")
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: =")
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(0.8)
        
        resultado = driver.find_element(By.ID, "display").text
        print(f"  ✅ Resultado: {resultado}\n")
        assert '5' in resultado
        
        time.sleep(1)
        
        # Test 2: Resta
        print("✏️  Test 2: RESTA (5 - 2 = 3)")
        print("─" * 50)
        
        print("  ► Haciendo clic en: C (Limpiar)")
        driver.find_element(By.XPATH, "//button[text()='C']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 5")
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: -")
        driver.find_element(By.XPATH, "//button[text()='-']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 2")
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: =")
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(0.8)
        
        resultado = driver.find_element(By.ID, "display").text
        print(f"  ✅ Resultado: {resultado}\n")
        assert '3' in resultado
        
        time.sleep(1)
        
        # Test 3: Multiplicación
        print("✏️  Test 3: MULTIPLICACIÓN (3 × 4 = 12)")
        print("─" * 50)
        
        print("  ► Haciendo clic en: C (Limpiar)")
        driver.find_element(By.XPATH, "//button[text()='C']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 3")
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: *")
        driver.find_element(By.XPATH, "//button[text()='*']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 4")
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: =")
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(0.8)
        
        resultado = driver.find_element(By.ID, "display").text
        print(f"  ✅ Resultado: {resultado}\n")
        assert '12' in resultado
        
        time.sleep(1)
        
        # Test 4: División
        print("✏️  Test 4: DIVISIÓN (10 ÷ 2 = 5)")
        print("─" * 50)
        
        print("  ► Haciendo clic en: C (Limpiar)")
        driver.find_element(By.XPATH, "//button[text()='C']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 1")
        driver.find_element(By.XPATH, "//button[text()='1']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 0")
        driver.find_element(By.XPATH, "//button[text()='0']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: /")
        driver.find_element(By.XPATH, "//button[text()='/']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: 2")
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        time.sleep(0.8)
        
        print("  ► Haciendo clic en: =")
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(0.8)
        
        resultado = driver.find_element(By.ID, "display").text
        print(f"  ✅ Resultado: {resultado}\n")
        assert '5' in resultado
        
        # Resultado final
        print("\n" + "="*70)
        print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        print("="*70)
        
        # Resumen de pruebas
        print("\n" + "="*70)
        print("📊 RESUMEN DE PRUEBAS EJECUTADAS")
        print("="*70)
        print("\n✅ Prueba 1: SUMA")
        print("   Operación: 2 + 3 = 5")
        print("   Resultado: ✓ PASADA\n")
        
        print("✅ Prueba 2: RESTA")
        print("   Operación: 5 - 2 = 3")
        print("   Resultado: ✓ PASADA\n")
        
        print("✅ Prueba 3: MULTIPLICACIÓN")
        print("   Operación: 3 × 4 = 12")
        print("   Resultado: ✓ PASADA\n")
        
        print("✅ Prueba 4: DIVISIÓN")
        print("   Operación: 10 ÷ 2 = 5")
        print("   Resultado: ✓ PASADA\n")
        
        print("="*70)
        print("📈 ESTADÍSTICAS")
        print("="*70)
        print(f"Total de pruebas: 4")
        print(f"Pruebas pasadas: 4 ✅")
        print(f"Pruebas fallidas: 0 ❌")
        print(f"Tasa de éxito: 100%")
        print("\n" + "="*70)
        print("✋ FIREFOX PERMANECERÁ ABIERTO")
        print("="*70)
        print("\n📝 Puedes:")
        print("   • Ver la calculadora en Firefox")
        print("   • Probar manualmente otras operaciones")
        print("   • Cerrar Firefox cuando termines")
        print("\n⏳ Presiona Ctrl+C en la consola para cerrar, o cierra Firefox manualmente...\n")
        
        # Mantener abierto indefinidamente
        while True:
            time.sleep(1)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\n⏳ Firefox se cerrará en 10 segundos...")
        time.sleep(10)
        raise
    finally:
        driver.quit()
        print("\n✅ Firefox cerrado correctamente\n")

if __name__ == "__main__":
    test_calculator_window()
