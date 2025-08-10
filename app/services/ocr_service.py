class OCRService:
    def __init__(self, api_key):
        self.ocr_provider = 'https://api.ocr.space/parse/image'
        self.api_key = api_key

    def extract_text(self, image_path):
        """
        Extract text from an image using the specified OCR provider.
        
        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        """
        return self.ocr_provider.recognize(image_path)
    