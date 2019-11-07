try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open('C:\wamp64\www\CDA\guillaume\ocr\c.png')))



ERROR: Command errored out with exit status 1:
     command: 'c:\users\gcerd\appdata\local\programs\python\python37\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\gcerd\\AppData\\Local\\Temp\\pip-install-q0x96i6t\\tesseract-ocr\\setup.py'"'"'; __file__='"'"'C:\\Users\\gcerd\\AppData\\Local\\Temp\\pip-install-q0x96i6t\\tesseract-ocr\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\gcerd\AppData\Local\Temp\pip-record-ixgk8h4z\install-record.txt' --single-version-externally-managed --compile
         cwd: C:\Users\gcerd\AppData\Local\Temp\pip-install-q0x96i6t\tesseract-ocr\
    Complete output (8 lines):
    running install
    running build
    running build_py
    file tesseract_ocr.py (for module tesseract_ocr) not found
    file tesseract_ocr.py (for module tesseract_ocr) not found
    running build_ext
    building 'tesseract_ocr' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'c:\users\gcerd\appdata\local\programs\python\python37\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\gcerd\\AppData\\Local\\Temp\\pip-install-q0x96i6t\\tesseract-ocr\\setup.py'"'"'; __file__='"'"'C:\\Users\\gcerd\\AppData\\Local\\Temp\\pip-install-q0x96i6t\\tesseract-ocr\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\gcerd\AppData\Local\Temp\pip-record-ixgk8h4z\install-record.txt' --single-version-externally-managed --compile Check the logs for full command output.