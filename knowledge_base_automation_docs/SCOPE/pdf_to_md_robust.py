#!/usr/bin/env python3
"""
Robust PDF to Markdown converter with error handling.
Handles malformed pages, missing text, and parsing errors gracefully.

Usage:
    python pdf_to_md_robust.py <input.pdf> [output.md]

Example:
    python pdf_to_md_robust.py Keysight_6000X_Programming.pdf keysight_prog.md
"""

import pdfplumber
import re
import sys
import os
from pathlib import Path
from typing import Optional, List, Dict, Any

class PDFToMarkdownConverter:
    """Convert PDF to Markdown with error handling."""
    
    def __init__(self, pdf_path: str, verbose: bool = True):
        self.pdf_path = pdf_path
        self.verbose = verbose
        self.errors = []
        self.warnings = []
        self.total_pages = 0
        self.processed_pages = 0
        
    def log(self, msg: str, level: str = "INFO"):
        """Log message with level."""
        if self.verbose:
            print(f"[{level}] {msg}")
    
    def extract_text(self, page) -> str:
        """Safely extract text from page with error handling."""
        try:
            if page is None:
                self.warnings.append("None page object")
                return ""
            
            # Try direct text extraction
            text = page.extract_text()
            
            if text is None:
                self.log("Page has None text, trying fallback...", "WARN")
                # Fallback: extract from layout
                text = ""
                try:
                    layout = page.chars
                    if layout:
                        text = ''.join([char['text'] for char in layout if char.get('text')])
                except Exception as e:
                    self.warnings.append(f"Fallback extraction failed: {e}")
                    return ""
            
            return text.strip() if text else ""
        
        except AttributeError as e:
            self.errors.append(f"AttributeError during extraction: {e}")
            return ""
        except Exception as e:
            self.errors.append(f"Unexpected error during extraction: {e}")
            return ""
    
    def extract_tables(self, page) -> List[str]:
        """Safely extract tables from page."""
        tables = []
        try:
            if not hasattr(page, 'extract_tables'):
                return []
            
            page_tables = page.extract_tables()
            if page_tables:
                for table in page_tables:
                    if table:
                        # Convert table to markdown
                        md_table = self._table_to_markdown(table)
                        if md_table:
                            tables.append(md_table)
        except Exception as e:
            self.warnings.append(f"Table extraction error: {e}")
        
        return tables
    
    def _table_to_markdown(self, table: List[List[str]]) -> str:
        """Convert table to markdown format."""
        try:
            if not table or not table[0]:
                return ""
            
            lines = []
            
            # Header
            header = table[0]
            lines.append("| " + " | ".join(str(cell).strip() if cell else "" for cell in header) + " |")
            
            # Separator
            lines.append("|" + "|".join(["---" for _ in header]) + "|")
            
            # Rows
            for row in table[1:]:
                lines.append("| " + " | ".join(str(cell).strip() if cell else "" for cell in row) + " |")
            
            return "\n".join(lines)
        except Exception as e:
            self.warnings.append(f"Table markdown conversion error: {e}")
            return ""
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize extracted text."""
        if not text:
            return ""
        
        # Remove excessive whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        
        # Remove control characters
        text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\t')
        
        return text.strip()
    
    def convert_page(self, page_num: int, page) -> str:
        """Convert single page to markdown."""
        try:
            self.processed_pages += 1
            
            md_content = []
            
            # Extract text
            text = self.extract_text(page)
            
            if text:
                # Clean text
                text = self.clean_text(text)
                md_content.append(text)
            
            # Extract tables
            tables = self.extract_tables(page)
            if tables:
                md_content.append("\n".join(tables))
            
            # Add page break
            md_content.append(f"\n---\n**[Page {page_num}]**\n")
            
            return "\n".join(md_content)
        
        except Exception as e:
            self.errors.append(f"Page {page_num}: {e}")
            self.log(f"Failed to process page {page_num}: {e}", "ERROR")
            return f"\n[ERROR: Page {page_num} could not be extracted]\n"
    
    def convert(self, output_path: Optional[str] = None, 
                skip_pages: Optional[List[int]] = None,
                max_pages: Optional[int] = None) -> Optional[str]:
        """
        Convert PDF to Markdown.
        
        Args:
            output_path: Output markdown file path. If None, generates from input filename.
            skip_pages: List of page numbers to skip (1-indexed).
            max_pages: Maximum pages to process. If None, process all.
        
        Returns:
            Path to output markdown file, or None if failed.
        """
        
        skip_pages = skip_pages or []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                self.total_pages = len(pdf.pages)
                self.log(f"Processing {self.total_pages} pages...")
                
                md_lines = [
                    f"# PDF Extracted Markdown\n",
                    f"**Source:** {os.path.basename(self.pdf_path)}\n",
                    f"**Pages:** {self.total_pages}\n",
                    f"**Extraction Date:** {__import__('datetime').datetime.now().isoformat()}\n",
                    "---\n"
                ]
                
                for page_num, page in enumerate(pdf.pages, start=1):
                    # Check limits
                    if max_pages and page_num > max_pages:
                        self.log(f"Reached max_pages limit ({max_pages})")
                        break
                    
                    # Skip specified pages
                    if page_num in skip_pages:
                        self.log(f"Skipping page {page_num}")
                        continue
                    
                    # Progress
                    if page_num % 10 == 0 or page_num == 1:
                        print(f"  Page {page_num}/{self.total_pages}...", end='\r')
                    
                    # Convert page
                    page_md = self.convert_page(page_num, page)
                    md_lines.append(page_md)
                
                # Generate output path
                if output_path is None:
                    base = Path(self.pdf_path).stem
                    output_path = f"{base}.md"
                
                # Write output
                output_content = "\n".join(md_lines)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(output_content)
                
                self.log(f"✓ Conversion complete: {output_path}")
                self.log(f"  Pages processed: {self.processed_pages}/{self.total_pages}")
                
                if self.errors:
                    self.log(f"  Errors: {len(self.errors)}", "WARN")
                    for err in self.errors[:5]:
                        self.log(f"    - {err}", "WARN")
                
                if self.warnings:
                    self.log(f"  Warnings: {len(self.warnings)}", "WARN")
                
                return output_path
        
        except FileNotFoundError:
            self.log(f"PDF file not found: {self.pdf_path}", "ERROR")
            return None
        except pdfplumber.utils.PDFException as e:
            self.log(f"PDF parsing error: {e}", "ERROR")
            return None
        except Exception as e:
            self.log(f"Unexpected error: {e}", "ERROR")
            return None


def main():
    """CLI interface."""
    
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_md_robust.py <input.pdf> [output.md] [options]")
        print("\nOptions:")
        print("  --skip-pages N,M,O    Skip specified pages (comma-separated, 1-indexed)")
        print("  --max-pages N         Process only first N pages")
        print("  --quiet               Suppress verbose output")
        print("\nExample:")
        print("  python pdf_to_md_robust.py keysight.pdf keysight.md --max-pages 100")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Parse options
    skip_pages = []
    max_pages = None
    verbose = True
    
    for i in range(3, len(sys.argv)):
        arg = sys.argv[i]
        if arg == '--quiet':
            verbose = False
        elif arg == '--max-pages' and i + 1 < len(sys.argv):
            max_pages = int(sys.argv[i + 1])
        elif arg == '--skip-pages' and i + 1 < len(sys.argv):
            skip_pages = [int(x.strip()) for x in sys.argv[i + 1].split(',')]
    
    # Convert
    converter = PDFToMarkdownConverter(pdf_path, verbose=verbose)
    result = converter.convert(output_path, skip_pages=skip_pages, max_pages=max_pages)
    
    if result:
        print(f"\n✓ Success: {result}")
        sys.exit(0)
    else:
        print(f"\n✗ Conversion failed")
        sys.exit(1)


if __name__ == '__main__':
    main()
