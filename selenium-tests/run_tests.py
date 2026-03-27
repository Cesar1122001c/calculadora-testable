import subprocess
import sys

print("Instalando Selenium y webdriver-manager...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "selenium", "webdriver-manager"])

print("✅ Dependencias instaladas")
print("\n" + "="*50)
print("Ejecutando pruebas de la calculadora...")
print("="*50 + "\n")

# Ejecutar el test
import os
os.system("python test_calculator.py")
