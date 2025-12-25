"""
PDF OCR Text Extractor - Core Library
Extracts text from image-based (scanned) PDF files using Optical Character Recognition (OCR)

This is a library module. For general use, use pdf_to_markdown.py instead.
"""

import os
import sys
from pathlib import Path

try:
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image
except ImportError:
    print("Required packages not installed. Please install them first.")
    print("Run: pip install pdf2image pytesseract pillow")
    print("\nAlso install Tesseract OCR:")
    print("Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
    print("Mac: brew install tesseract")
    print("Linux: sudo apt-get install tesseract-ocr")
    sys.exit(1)


def extract_text_from_pdf(pdf_path, output_txt_path=None, dpi=300, output_format='txt'):
    """
    Extract text from image-based PDF using OCR
    
    Args:
        pdf_path: Path to the PDF file
        output_txt_path: Optional path to save extracted text (default: same name as PDF with .txt extension)
        dpi: Resolution for image conversion (higher = better quality but slower, default: 300)
        output_format: Output format - 'txt' or 'md' (default: 'txt')
    
    Returns:
        Extracted text as string
    """
    print(f"Processing PDF: {pdf_path}")
    
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Set output path if not provided
    if output_txt_path is None:
        if output_format == 'md':
            output_txt_path = str(Path(pdf_path).with_suffix('.md'))
        else:
            output_txt_path = str(Path(pdf_path).with_suffix('.txt'))
    
    # Convert PDF pages to images
    print("Converting PDF pages to images...")
    try:
        images = convert_from_path(pdf_path, dpi=dpi)
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        print("\nMake sure poppler is installed:")
        print("Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases")
        print("Mac: brew install poppler")
        print("Linux: sudo apt-get install poppler-utils")
        raise
    
    print(f"Found {len(images)} pages")
    
    # Extract text from each page using OCR
    all_text = []
    
    # Add markdown header if output format is md
    if output_format == 'md':
        pdf_name = Path(pdf_path).stem
        all_text.append(f"# {pdf_name}\n\n")
        all_text.append("---\n\n")
    
    for i, image in enumerate(images, 1):
        print(f"Processing page {i}/{len(images)}...")
        text = pytesseract.image_to_string(image, lang='eng')
        
        if output_format == 'md':
            all_text.append(f"## Page {i}\n\n")
        else:
            all_text.append(f"\n{'='*80}\n")
            all_text.append(f"PAGE {i}\n")
            all_text.append(f"{'='*80}\n\n")
        
        all_text.append(text)
        all_text.append("\n\n")
    
    # Combine all text
    full_text = "".join(all_text)
    
    # Save to file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"\nText extracted successfully!")
    print(f"Output saved to: {output_txt_path}")
    print(f"Total characters extracted: {len(full_text)}")
    
    return full_text


def batch_extract_from_folder(folder_path, output_folder=None):
    """
    Extract text from all PDF files in a folder
    
    Args:
        folder_path: Path to folder containing PDF files
        output_folder: Optional folder to save extracted text files
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if output_folder:
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = folder
    
    pdf_files = list(folder.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {folder_path}")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s)")
    
    for pdf_file in pdf_files:
        print(f"\n{'='*80}")
        output_file = output_path / f"{pdf_file.stem}.txt"
        try:
            extract_text_from_pdf(str(pdf_file), str(output_file))
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {e}")
            continue


def main():
    """Main function to run the OCR extractor"""
    print("="*80)
    print("PDF OCR Text Extractor")
    print("="*80)
    print()
    
    # Try to find Tesseract in common Windows locations
    import platform
    if platform.system() == 'Windows':
        common_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
            r'C:\Users\{}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'.format(os.getenv('USERNAME', '')),
        ]
        for path in common_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                print(f"Found Tesseract at: {path}")
                break
    
    # Check if Tesseract is installed
    try:
        version = pytesseract.get_tesseract_version()
        print(f"Tesseract version: {version}")
    except Exception:
        print("ERROR: Tesseract OCR is not installed or not in PATH")
        print("\nPlease install Tesseract OCR:")
        print("Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
        print("  - Install to: C:\\Program Files\\Tesseract-OCR")
        print("  - Or add Tesseract to PATH")
        print("Mac: brew install tesseract")
        print("Linux: sudo apt-get install tesseract-ocr")
        print("\nAfter installation, restart and try again.")
        return
    
    # Example usage
    if len(sys.argv) > 1:
        # Command line argument provided
        input_path = sys.argv[1]
        
        if os.path.isfile(input_path):
            # Single file
            extract_text_from_pdf(input_path)
        elif os.path.isdir(input_path):
            # Folder
            batch_extract_from_folder(input_path)
        else:
            print(f"Error: {input_path} is not a valid file or folder")
    else:
        # Interactive mode - process Accounting for Managers PDFs
        project_root = Path(__file__).parent.parent
        base_path = project_root / "sem1" / "Accounting for Managers"
        
        if base_path.exists():
            print(f"Processing PDFs in: {base_path}")
            print("\nAvailable PDF files:")
            pdf_files = list(base_path.glob("*.pdf"))
            for i, pdf in enumerate(pdf_files, 1):
                print(f"  {i}. {pdf.name}")
            
            print("\nProcessing all PDF files...")
            batch_extract_from_folder(str(base_path))
        else:
            print("Usage:")
            print("  python pdf_ocr_extractor.py <pdf_file_path>")
            print("  python pdf_ocr_extractor.py <folder_path>")
            print("\nExample:")
            print("  python pdf_ocr_extractor.py \"../sem1/Accounting for Managers/Accounting for Managers (1st Module Assessment).pdf\"")


if __name__ == "__main__":
    main()

