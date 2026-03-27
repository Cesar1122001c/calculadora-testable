@echo off
echo ========================================
echo Instalando dependencias para Selenium
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no está instalado o no está en PATH
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Marca "Add Python to PATH" durante la instalación
    pause
    exit /b 1
)

REM Instalar Selenium
echo Instalando Selenium...
pip install selenium

REM Instalar webdriver-manager (auto-descarga drivers)
echo Instalando webdriver-manager...
pip install webdriver-manager

echo.
echo ========================================
echo ✅ Instalación completada
echo ========================================
echo.
echo Para ejecutar las pruebas:
echo   python test_calculator.py
echo.
