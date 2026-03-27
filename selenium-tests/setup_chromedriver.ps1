# Script para descargar ChromeDriver
# Obtener versión de Chrome
$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$chromeVersion = (Get-Item $chromePath).VersionInfo.ProductVersion

Write-Host "Versión de Chrome: $chromeVersion"
Write-Host ""
Write-Host "======================================"
Write-Host "Para descargar ChromeDriver:"
Write-Host "======================================"
Write-Host "1. Ve a: https://chromedriver.chromium.org/downloads"
Write-Host "2. Descarga la versión: $chromeVersion"
Write-Host "3. Extrae el archivo chromedriver.exe"
Write-Host "4. Pega el archivo en esta carpeta:"
Write-Host "   $(Get-Location)\chromedriver.exe"
Write-Host ""
Write-Host "O descarga automáticamente desde:"
Write-Host "https://edgedl.me/chromium-release/chromedriver/$chromeVersion/win64-x64/chromedriver.zip"
