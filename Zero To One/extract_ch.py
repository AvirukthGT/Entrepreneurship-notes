import PyPDF2
import sys
sys.stdout.reconfigure(encoding='utf-8')

reader = PyPDF2.PdfReader('Zero-to-one.pdf')

# Chapter 5: pages 44-55 (index 43-54)
for i in range(43, 56):
    text = reader.pages[i].extract_text()
    print(f"=== PAGE {i+1} ===")
    print(text)
    print()
