import pytesseract
from PIL import Image

from services.image_processing import preprocess_image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image_path):
    """
    Preprocess the image and extract text using Tesseract OCR.
    """

    processed_image = preprocess_image(image_path)

    text = pytesseract.image_to_string(processed_image)

    return text