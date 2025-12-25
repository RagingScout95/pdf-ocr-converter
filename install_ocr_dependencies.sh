#!/bin/bash

echo "========================================"
echo "PDF OCR Extractor - Dependency Installer"
echo "========================================"
echo ""

echo "Installing Python packages..."
pip install pdf2image pytesseract pillow

echo ""
echo "Installing Tesseract OCR..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac OS
    brew install tesseract
    brew install poppler
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr
    sudo apt-get install -y poppler-utils
else
    echo "Unknown OS. Please install Tesseract and Poppler manually."
fi

echo ""
echo "Installation complete!"
echo "You can now run: python pdf_ocr_extractor.py"

