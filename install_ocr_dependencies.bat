@echo off
echo ========================================
echo PDF OCR Extractor - Dependency Installer
echo ========================================
echo.

echo Installing Python packages...
pip install pdf2image pytesseract pillow

echo.
echo ========================================
echo IMPORTANT: Manual Installation Required
echo ========================================
echo.
echo 1. Install Tesseract OCR:
echo    Download from: https://github.com/UB-Mannheim/tesseract/wiki
echo    Install to default location: C:\Program Files\Tesseract-OCR
echo.
echo 2. Install Poppler:
echo    Download from: https://github.com/oschwartz10612/poppler-windows/releases
echo    Extract and add bin folder to PATH
echo    OR place in: C:\poppler\bin
echo.
echo 3. After installation, you may need to set paths in the Python script
echo.
pause

