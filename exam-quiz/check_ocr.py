try:
    import easyocr
    print("easyocr available")
except ImportError:
    print("easyocr not available")

try:
    import paddleocr
    print("paddleocr available")
except ImportError:
    print("paddleocr not available")

try:
    import pytesseract
    print("pytesseract available")
except ImportError:
    print("pytesseract not available")
