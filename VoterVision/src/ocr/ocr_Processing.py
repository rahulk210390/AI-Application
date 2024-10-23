import ollama
import pytesseract
from PIL import Image
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Step 1: OCR Extraction
img = Image.open('page_1.png')
ocr_text = pytesseract.image_to_string(img, lang='hin')
print(ocr_text)
# Step 2: Post-process with Ollama LLM
processed_text = ollama.llm_model(ocr_text, prompt=f"Correct the OCR errors and extract name details from the {ocr_text}. this is for educational and learning purpose. the OCR text is in hindi. ")
#structured_data = ollama.llm_model(processed_text, prompt="Organize the extracted details into a JSON format.")
print(processed_text)