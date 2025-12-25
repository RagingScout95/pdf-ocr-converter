# PDF OCR Text Extractor - Setup Instructions

This tool extracts text from image-based (scanned) PDF files using Optical Character Recognition (OCR).

## Prerequisites

### 1. Install Python Packages

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pdf2image pytesseract pillow
```

### 2. Install Tesseract OCR

#### Windows:
1. Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install it (default location: `C:\Program Files\Tesseract-OCR`)
3. Add to PATH or set in code:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

#### Mac:
```bash
brew install tesseract
```

#### Linux:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### 3. Install Poppler (Required for PDF to Image conversion)

#### Windows:
1. Download from: https://github.com/oschwartz10612/poppler-windows/releases
2. Extract and add `bin` folder to PATH
   - Or place in: `C:\poppler\bin`
   - Add to PATH: `C:\poppler\bin`

#### Mac:
```bash
brew install poppler
```

#### Linux:
```bash
sudo apt-get install poppler-utils
```

## Usage

### Method 1: Command Line

Process a single PDF:
```bash
python pdf_ocr_extractor.py "sem1/Accounting for Managers/Accounting for Managers (1st Module Assessment).pdf"
```

Process all PDFs in a folder:
```bash
python pdf_ocr_extractor.py "sem1/Accounting for Managers"
```

### Method 2: Python Script

```python
from pdf_ocr_extractor import extract_text_from_pdf

# Extract text from a PDF
text = extract_text_from_pdf(
    "sem1/Accounting for Managers/Accounting for Managers (1st Module Assessment).pdf",
    output_txt_path="output.txt"
)

print(text)
```

### Method 3: Batch Processing

```python
from pdf_ocr_extractor import batch_extract_from_folder

# Extract text from all PDFs in a folder
batch_extract_from_folder(
    "sem1/Accounting for Managers",
    output_folder="extracted_texts"
)
```

## Output

The script will:
1. Convert each PDF page to an image
2. Extract text using OCR
3. Save extracted text to a `.txt` file (same name as PDF)
4. Display progress and statistics

## Notes

- **Quality**: Higher DPI (default 300) gives better OCR accuracy but is slower
- **Language**: Currently set to English ('eng'). For other languages, modify the `lang` parameter
- **Speed**: Processing time depends on PDF size and number of pages
- **Accuracy**: OCR accuracy depends on scan quality, font clarity, and image resolution

## Troubleshooting

### "Tesseract not found"
- Make sure Tesseract is installed
- Add Tesseract to your system PATH
- Or set the path manually in the code

### "Poppler not found"
- Install Poppler and add to PATH
- Or specify the path in code:
  ```python
  from pdf2image import convert_from_path
  images = convert_from_path(pdf_path, poppler_path=r"C:\poppler\bin")
  ```

### "Permission denied"
- Make sure you have read access to the PDF file
- Make sure you have write access to the output directory

## Example Output

```
Processing PDF: Accounting for Managers (1st Module Assessment).pdf
Converting PDF pages to images...
Found 31 pages
Processing page 1/31...
Processing page 2/31...
...
Text extracted successfully!
Output saved to: Accounting for Managers (1st Module Assessment).txt
Total characters extracted: 45230
```

