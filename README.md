# PDF OCR Converter

**Convert any image-based (scanned) PDF file to searchable markdown format using OCR technology.**

A powerful Python tool to convert image-based (scanned) PDF files into searchable markdown format using Optical Character Recognition (OCR) technology.

---

## 📖 Summary

This tool converts **scanned PDF files** (image-based documents) into **searchable markdown files** using Optical Character Recognition (OCR). Perfect for:
- Converting assignment PDFs to searchable text
- Extracting text from scanned documents
- Making PDFs searchable and editable
- Finding specific content in image-based PDFs

**Main Script:** `pdf_to_markdown.py` - Use this for all conversions!

---

## 🚀 Quick Start

### Clone the Repository

```bash
git clone https://github.com/RagingScout95/pdf-ocr-converter.git
cd pdf-ocr-converter
```

### Installation (3 Steps)

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install system dependencies:**
   - **Windows**: Run `install_ocr_dependencies.bat`
   - **Linux/Mac**: Run `install_ocr_dependencies.sh`

3. **Convert your PDF:**
   ```bash
   python pdf_to_markdown.py "path/to/your/document.pdf"
   ```

**Done!** Your markdown file is ready.

---

## 📋 Table of Contents
1. [What is This?](#what-is-this)
2. [Quick Start](#quick-start)
3. [How It Works](#how-it-works)
4. [Installation Guide](#installation-guide)
5. [Usage Guide](#usage-guide)
6. [Troubleshooting](#troubleshooting)
7. [Technical Details](#technical-details)

---

## 🎯 What is This?

This is a **PDF to Markdown Converter** that uses **Optical Character Recognition (OCR)** technology to extract text from **image-based PDF files** (scanned documents) and convert them into searchable markdown (.md) files.

### What Problem Does It Solve?

Many PDF files are actually **scanned images** - they look like text but are actually pictures. You can't:
- Copy text from them
- Search for specific words
- Use them in other applications

This tool solves that by:
- Converting PDF pages to images
- Using OCR to "read" the text from images
- Saving everything as a searchable markdown file

### When to Use This Tool

✅ **Use this tool when:**
- You have scanned PDF documents (image-based)
- You need to search for specific text in PDFs
- You want to convert PDFs to editable text format
- You have assignment PDFs that need to be searchable

❌ **Don't use this tool when:**
- Your PDF already has selectable text (use regular PDF readers)
- You need perfect formatting (OCR may have minor errors)
- The PDF quality is very poor (low resolution scans)

---

## 🔧 How It Works

### The Process (Step by Step)

```
PDF File (Scanned Images)
    ↓
[Step 1] Poppler converts each PDF page → Image files
    ↓
[Step 2] Tesseract OCR "reads" text from each image
    ↓
[Step 3] All extracted text is combined
    ↓
[Step 4] Text is formatted as Markdown
    ↓
Markdown File (.md) - Searchable and Editable!
```

### Detailed Explanation

1. **PDF to Image Conversion (Poppler)**
   - Takes each page of the PDF
   - Converts it to a high-resolution image (300 DPI by default)
   - Creates temporary image files in memory

2. **Text Extraction (Tesseract OCR)**
   - Analyzes each image pixel by pixel
   - Recognizes characters, words, and sentences
   - Extracts the text content
   - Handles different fonts, sizes, and layouts

3. **Markdown Formatting**
   - Organizes text by page numbers
   - Adds markdown headers and structure
   - Preserves basic formatting
   - Saves as `.md` file

### Technology Stack

- **Python** - Programming language
- **pdf2image** - Converts PDF pages to images
- **Poppler** - PDF rendering engine (system tool)
- **Tesseract OCR** - Text recognition engine (system tool)
- **pytesseract** - Python wrapper for Tesseract
- **Pillow (PIL)** - Image processing library

---

## 📦 Installation Guide

### Prerequisites

Before using this tool, you need to install:

1. **Python 3.7 or higher**
2. **Poppler** (PDF to image converter)
3. **Tesseract OCR** (Text recognition engine)

### Step 1: Install Python Packages

Open your terminal/command prompt and run:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pdf2image pytesseract pillow
```

**What this installs:**
- `pdf2image` - Converts PDF pages to images
- `pytesseract` - Python interface for Tesseract OCR
- `pillow` - Image processing library

### Step 2: Install Poppler (Windows)

**Option A: Automated Installation (Recommended)**
```bash
python install_dependencies.py
```

**Option B: Manual Installation**

1. **Download Poppler:**
   - Go to: https://github.com/oschwartz10612/poppler-windows/releases
   - Download the latest release (e.g., `Release-23.11.0-0.zip`)

2. **Extract Poppler:**
   - Extract the ZIP file
   - Move the extracted folder to: `C:\poppler`
   - The structure should be: `C:\poppler\Library\bin\pdftoppm.exe`

3. **Add to PATH (Optional but Recommended):**
   - Press `Win + X` → Select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", select "Path" → Click "Edit"
   - Click "New" → Add: `C:\poppler\Library\bin`
   - Click OK on all dialogs
   - **Restart your terminal/command prompt**

**Verify Installation:**
```bash
pdftoppm -v
```
If this shows version information, Poppler is installed correctly.

### Step 3: Install Tesseract OCR (Windows)

**Option A: Automated Installation (Recommended)**
```bash
python install_dependencies.py
```

**Option B: Manual Installation**

1. **Download Tesseract:**
   - Go to: https://github.com/UB-Mannheim/tesseract/wiki
   - Download the Windows installer (e.g., `tesseract-ocr-w64-setup-5.4.0.20240606.exe`)

2. **Install Tesseract:**
   - Run the installer
   - Install to: `C:\Program Files\Tesseract-OCR` (default location)
   - **IMPORTANT:** Check "Add to PATH" during installation
   - Complete the installation

3. **Restart** your terminal/command prompt after installation

**Verify Installation:**
```bash
tesseract --version
```
If this shows version information (e.g., `tesseract 5.4.0`), Tesseract is installed correctly.

### Step 4: Verify Everything Works

Run the installation script to check:
```bash
python install_dependencies.py
```

You should see:
- ✅ Python packages: [OK]
- ✅ Poppler: [INSTALLED] or [FOUND]
- ✅ Tesseract: [INSTALLED] or [FOUND]

---

## ⚡ Quick Start

### For First-Time Users

**Step 1: Install Everything**
```bash
python install_dependencies.py
```
This will automatically:
- Install Python packages
- Download and install Poppler
- Install Tesseract OCR

**Step 2: Convert Your First PDF**
```bash
python pdf_to_markdown.py "path/to/your/document.pdf"
```

**Step 3: Find Your Output**
The markdown file will be created in the same folder as the PDF (with `.md` extension).

---

## 🚀 Usage Guide

### Basic Usage

**Convert a PDF to Markdown:**
```bash
python pdf_to_markdown.py "path/to/your/document.pdf"
```

The output markdown file will be created in the same location as the PDF with a `.md` extension.

**Example:**
```bash
python pdf_to_markdown.py "documents/assignment.pdf"
```

This creates: `documents/assignment.md` in the same folder.

### Specify Custom Output Location

```bash
python pdf_to_markdown.py "input.pdf" "output.md"
```

**Example:**
```bash
python pdf_to_markdown.py "document.pdf" "../output/converted_document.md"
```

### Adjust Image Quality (DPI)

Higher DPI = Better quality but slower processing:
```bash
python pdf_to_markdown.py "document.pdf" --dpi 400
```

**DPI Recommendations:**
- `200` - Fast, lower quality (for simple documents)
- `300` - Balanced (default, recommended)
- `400-600` - High quality (for complex layouts, small text)

### Real-World Examples

**Example 1: Convert Document PDF**
```bash
python pdf_to_markdown.py "documents/report.pdf"
```

**Example 2: Convert with Custom Output**
```bash
python pdf_to_markdown.py "documents/document.pdf" "output/converted_document.md"
```

**Example 3: Convert Multiple PDFs (Using Batch Script)**
```bash
# For Windows PowerShell
Get-ChildItem "documents/*.pdf" | ForEach-Object {
    python pdf_to_markdown.py $_.FullName
}
```

---

## 🛠️ Troubleshooting

### Problem: "Poppler Error: Unable to get page count"

**Solution:**
1. Verify Poppler is installed:
   ```bash
   pdftoppm -v
   ```
2. If not found, install Poppler (see Installation Guide)
3. Make sure Poppler is in PATH or the script can find it at `C:\poppler\Library\bin`

**Quick Fix:**
- Run: `python install_dependencies.py` (it will download and install Poppler)

### Problem: "Tesseract Error: [WinError 2] The system cannot find the file specified"

**Solution:**
1. Verify Tesseract is installed:
   ```bash
   tesseract --version
   ```
2. If not found, install Tesseract (see Installation Guide)
3. Make sure Tesseract is in PATH or located at `C:\Program Files\Tesseract-OCR\tesseract.exe`

**Quick Fix:**
- Run: `python install_dependencies.py` (it will install Tesseract using winget)

### Problem: "ModuleNotFoundError: No module named 'pdf2image'"

**Solution:**
```bash
pip install pdf2image pytesseract pillow
```

### Problem: OCR Quality is Poor

**Solutions:**
1. **Increase DPI:**
   ```bash
   python pdf_to_markdown.py "document.pdf" --dpi 400
   ```

2. **Check PDF Quality:**
   - Original PDF should be at least 200 DPI
   - Text should be clear and not blurry
   - Avoid heavily compressed PDFs

3. **Pre-process PDF:**
   - Use PDF editing software to improve contrast
   - Remove noise/artifacts if possible

### Problem: Script Runs But Output is Empty

**Possible Causes:**
1. PDF is password protected
2. PDF has no actual content (blank pages)
3. OCR couldn't recognize the text (poor quality)

**Solution:**
- Check the PDF manually
- Try with a different PDF to verify the tool works
- Increase DPI if text is small

### Problem: "Permission Denied" Error

**Solution:**
- Make sure you have read access to the input PDF
- Make sure you have write access to the output directory
- Close the PDF file if it's open in another program

---

## 🔍 Technical Details

### How OCR Works

1. **Image Preprocessing:**
   - Converts color images to grayscale
   - Enhances contrast
   - Removes noise

2. **Text Detection:**
   - Identifies text regions in the image
   - Separates text from graphics/backgrounds

3. **Character Recognition:**
   - Analyzes each character shape
   - Matches patterns to known characters
   - Uses language models to improve accuracy

4. **Text Reconstruction:**
   - Combines characters into words
   - Identifies sentences and paragraphs
   - Preserves basic formatting

### Accuracy Factors

**High Accuracy When:**
- ✅ Clear, high-resolution scans (300+ DPI)
- ✅ Standard fonts (Arial, Times New Roman, etc.)
- ✅ Good contrast (black text on white background)
- ✅ Properly aligned text (not rotated)

**Lower Accuracy When:**
- ❌ Low resolution scans (< 150 DPI)
- ❌ Handwritten text
- ❌ Decorative/fancy fonts
- ❌ Poor contrast or faded text
- ❌ Rotated or skewed text
- ❌ Complex layouts with mixed content

### Performance

**Processing Speed:**
- **Small PDF (1-10 pages):** 10-30 seconds
- **Medium PDF (10-50 pages):** 1-5 minutes
- **Large PDF (50+ pages):** 5-15 minutes

**Factors Affecting Speed:**
- Number of pages
- DPI setting (higher = slower)
- Computer processing power
- PDF complexity

### File Sizes

**Typical Output Sizes:**
- 1 page PDF → ~5-20 KB markdown file
- 10 page PDF → ~50-200 KB markdown file
- 50 page PDF → ~250 KB - 1 MB markdown file

---

## 📁 Project Structure

```
pdf-ocr-converter/
├── pdf_to_markdown.py           # Main conversion script (USE THIS)
├── pdf_ocr_extractor.py         # Core OCR library
├── install_ocr_dependencies.bat # Windows dependency installer
├── install_ocr_dependencies.sh  # Linux/Mac dependency installer
├── requirements.txt              # Python packages
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
└── README_OCR_Setup.md           # Detailed setup instructions
```

---

## 💡 Tips & Best Practices

1. **Start with a Test PDF:**
   - Try with a small PDF first to verify everything works
   - Check the output quality before processing large files

2. **Organize Output:**
   - Keep original PDFs separate from converted markdown files
   - Create a dedicated folder for converted files if needed

3. **Quality vs Speed:**
   - Use DPI 300 for most documents (balanced)
   - Use DPI 400+ for important documents or small text
   - Use DPI 200 for quick previews

4. **Batch Processing:**
   - Process multiple PDFs in sequence
   - Don't run multiple conversions simultaneously (uses a lot of memory)

5. **Backup Originals:**
   - Always keep original PDF files
   - Markdown files are extracted text, not replacements

---

## 📝 Example Workflow

### Complete Example: Converting a PDF Document

```bash
# Step 1: Navigate to pdf-ocr-converter folder
cd pdf-ocr-converter

# Step 2: Convert PDF to Markdown
python pdf_to_markdown.py "documents/report.pdf"

# Step 3: Output will be created at:
# documents/report.md

# Step 4: Or specify custom output location
python pdf_to_markdown.py "documents/document.pdf" "output/converted_document.md"
```

### What You'll See:

```
================================================================================
PDF to Markdown Converter
================================================================================

Input PDF:  documents/report.pdf
Output MD:  output/report.md

Found Poppler at: C:\poppler\Library\bin
Poppler: OK
Found Tesseract at: C:\Program Files\Tesseract-OCR\tesseract.exe
Tesseract: OK (version 5.4.0.20240606)

--------------------------------------------------------------------------------
Starting conversion...
--------------------------------------------------------------------------------

Step 1: Converting PDF pages to images...
Found 41 pages

Step 2: Extracting text using OCR...
Processing page 41/41... [DONE]

Step 3: Saving to markdown file...

================================================================================
Conversion Complete!
================================================================================
Output saved to: output/report.md
Total pages processed: 41
Total characters extracted: 20,065
================================================================================
```

---

## 🆘 Getting Help

### Common Issues Checklist

- [ ] Python 3.7+ installed?
- [ ] Python packages installed? (`pip install -r requirements.txt`)
- [ ] Poppler installed and accessible?
- [ ] Tesseract installed and accessible?
- [ ] PDF file path is correct?
- [ ] Have read permission for PDF?
- [ ] Have write permission for output folder?

### Still Having Issues?

1. **Run the installer:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Check versions:**
   ```bash
   python --version
   pdftoppm -v
   tesseract --version
   ```

3. **Test with a simple PDF:**
   - Try with a 1-page PDF first
   - Verify the tool works before processing large files

---

## 📚 Additional Resources

- **Poppler Documentation:** https://poppler.freedesktop.org/
- **Tesseract OCR Documentation:** https://tesseract-ocr.github.io/
- **Python pdf2image:** https://github.com/Belval/pdf2image
- **pytesseract:** https://github.com/madmaze/pytesseract

---

## ✅ Quick Start Checklist

For someone completely new, follow these steps:

1. ✅ **Install Python** (if not already installed)
2. ✅ **Open terminal/command prompt**
3. ✅ **Navigate to pdf-ocr-converter folder:**
   ```bash
   cd pdf-ocr-converter
   ```
4. ✅ **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. ✅ **Wait for installation to complete**
6. ✅ **Test with a PDF:**
   ```bash
   python pdf_to_markdown.py "path/to/your/pdf.pdf"
   ```
7. ✅ **Check the output markdown file**

**That's it!** You're ready to convert PDFs to markdown.

---

*Last Updated: [Current Date]*
*Version: 1.0*
*Compatible with: Windows 10/11, Python 3.7+*

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Free to use** - Feel free to use, modify, and distribute this software.

## 📧 GitHub

**Open Source** - This project is available on GitHub.

GitHub Repository: https://github.com/RagingScout95/pdf-ocr-converter

For issues, contributions, or questions, please visit the repository.

---

**Made with ❤️ for converting PDFs to searchable text**
