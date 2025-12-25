"""
PDF to Markdown Converter using OCR
A general-purpose script to convert image-based (scanned) PDF files to markdown format.

Usage:
    python pdf_to_markdown.py <input_pdf_path> [output_md_path]
    
Examples:
    python pdf_to_markdown.py "../sem1/Accounting for Managers/Accounting for Managers (1st Module Assessment).pdf"
    python pdf_to_markdown.py "document.pdf" "output.md"
"""

import os
import sys
import argparse
from pathlib import Path

from pdf2image import convert_from_path
import pytesseract
import platform


def find_poppler():
    """Find Poppler installation in common locations"""
    poppler_paths = [
        r"C:\poppler\Library\bin",  # Most common after extraction
        r"C:\poppler\bin",
        r"C:\poppler-23.11.0\Library\bin",
        r"C:\poppler-23.08.0\Library\bin",
        r"C:\poppler-22.12.0\Library\bin",
        r"C:\Program Files\poppler\bin",
        r"C:\Program Files (x86)\poppler\bin",
        os.path.join(os.environ.get('LOCALAPPDATA', ''), 'poppler', 'bin'),
        os.path.join(os.environ.get('PROGRAMFILES', ''), 'poppler', 'bin'),
    ]
    
    for path in poppler_paths:
        if path and os.path.exists(path) and os.path.exists(os.path.join(path, "pdftoppm.exe")):
            return path
    
    # Check if in PATH
    import shutil
    if shutil.which('pdftoppm'):
        return None  # Will use system PATH
    
    return None


def find_tesseract():
    """Find Tesseract OCR installation in common locations"""
    if platform.system() == 'Windows':
        username = os.getenv('USERNAME', '')
        common_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
            rf'C:\Users\{username}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe',
            r'C:\Tesseract-OCR\tesseract.exe',
        ]
        for path in common_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                return path
        
        # Check if in PATH
        import shutil
        if shutil.which('tesseract'):
            return "system PATH"
    
    return None


def convert_pdf_to_markdown(pdf_path, output_md_path=None, dpi=300):
    """
    Convert an image-based PDF to markdown format using OCR
    
    Args:
        pdf_path: Path to the input PDF file
        output_md_path: Optional path for output markdown file (default: same name as PDF with .md extension)
        dpi: Resolution for image conversion (default: 300, higher = better quality but slower)
    
    Returns:
        Path to the created markdown file
    """
    print("="*80)
    print("PDF to Markdown Converter")
    print("="*80)
    print()
    
    # Validate input PDF
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if not pdf_path.suffix.lower() == '.pdf':
        raise ValueError(f"Input file must be a PDF: {pdf_path}")
    
    print(f"Input PDF:  {pdf_path}")
    
    # Set output path
    if output_md_path is None:
        output_md_path = pdf_path.with_suffix('.md')
    else:
        output_md_path = Path(output_md_path)
    
    # Create output directory if needed
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Output MD:  {output_md_path}")
    print()
    
    # Find and verify Poppler
    poppler_path = find_poppler()
    if poppler_path:
        print(f"Found Poppler at: {poppler_path}")
    else:
        print("Checking for Poppler in system PATH...")
    
    try:
        if poppler_path:
            test_images = convert_from_path(str(pdf_path), poppler_path=poppler_path, first_page=1, last_page=1)
        else:
            test_images = convert_from_path(str(pdf_path), first_page=1, last_page=1)
        print("Poppler: OK")
    except Exception as e:
        print(f"\n[ERROR] Poppler Error: {e}")
        print("\nPlease install Poppler:")
        print("1. Download from: https://github.com/oschwartz10612/poppler-windows/releases")
        print("2. Extract to: C:\\poppler")
        print("3. Add C:\\poppler\\Library\\bin to your system PATH")
        print("\nOr run: install_ocr_dependencies.bat (Windows) or install_ocr_dependencies.sh (Linux/Mac)")
        raise
    
    # Find and verify Tesseract
    tesseract_path = find_tesseract()
    if tesseract_path:
        print(f"Found Tesseract at: {tesseract_path}")
    else:
        print("Checking for Tesseract in system PATH...")
    
    try:
        version = pytesseract.get_tesseract_version()
        print(f"Tesseract: OK (version {version})")
    except Exception as e:
        print(f"\n[ERROR] Tesseract Error: {e}")
        print("\nPlease install Tesseract OCR:")
        print("1. Download from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("2. Install to: C:\\Program Files\\Tesseract-OCR")
        print("3. Add to PATH during installation")
        print("\nOr run: install_ocr_dependencies.bat (Windows) or install_ocr_dependencies.sh (Linux/Mac)")
        raise
    
    print()
    print("-"*80)
    print("Starting conversion...")
    print("-"*80)
    print()
    
    # Convert PDF pages to images
    print("Step 1: Converting PDF pages to images...")
    try:
        if poppler_path:
            images = convert_from_path(str(pdf_path), poppler_path=poppler_path, dpi=dpi)
        else:
            images = convert_from_path(str(pdf_path), dpi=dpi)
        print(f"Found {len(images)} pages")
    except Exception as e:
        print(f"[ERROR] Failed to convert PDF to images: {e}")
        raise
    
    # Extract text from each page using OCR
    print()
    print("Step 2: Extracting text using OCR...")
    all_text = []
    
    # Add markdown header
    pdf_name = pdf_path.stem
    all_text.append(f"# {pdf_name}\n\n")
    all_text.append("---\n\n")
    all_text.append(f"**Source PDF:** `{pdf_path}`\n\n")
    all_text.append(f"**Total Pages:** {len(images)}\n\n")
    all_text.append("---\n\n")
    
    # Process each page
    for i, image in enumerate(images, 1):
        print(f"Processing page {i}/{len(images)}...", end='\r')
        text = pytesseract.image_to_string(image, lang='eng')
        all_text.append(f"## Page {i}\n\n")
        all_text.append(text)
        all_text.append("\n\n---\n\n")
    
    print(f"Processing page {len(images)}/{len(images)}... [DONE]")
    
    # Combine all text
    full_text = "".join(all_text)
    
    # Save to markdown file
    print()
    print("Step 3: Saving to markdown file...")
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print()
    print("="*80)
    print("Conversion Complete!")
    print("="*80)
    print(f"Output saved to: {output_md_path}")
    print(f"Total pages processed: {len(images)}")
    print(f"Total characters extracted: {len(full_text):,}")
    print("="*80)
    
    return output_md_path


def main():
    """Main function with command-line argument parsing"""
    parser = argparse.ArgumentParser(
        description='Convert image-based PDF files to markdown format using OCR',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert PDF to markdown (output will be PDF name with .md extension)
  python pdf_to_markdown.py "document.pdf"
  
  # Convert PDF with custom output path
  python pdf_to_markdown.py "document.pdf" "output.md"
  
  # Convert PDF from relative path
  python pdf_to_markdown.py "../sem1/Accounting for Managers/Assessment.pdf"
        """
    )
    
    parser.add_argument(
        'input_pdf',
        help='Path to the input PDF file (image-based/scanned PDF)'
    )
    
    parser.add_argument(
        'output_md',
        nargs='?',
        default=None,
        help='Optional: Path for output markdown file (default: same name as PDF with .md extension)'
    )
    
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='DPI resolution for image conversion (default: 300, higher = better quality but slower)'
    )
    
    args = parser.parse_args()
    
    try:
        output_path = convert_pdf_to_markdown(
            pdf_path=args.input_pdf,
            output_md_path=args.output_md,
            dpi=args.dpi
        )
        return 0
    except Exception as e:
        print(f"\n[ERROR] Conversion failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

