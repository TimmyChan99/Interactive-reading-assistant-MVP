import requests

class OCRService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.ocr_provider_url = 'https://api.ocr.space/parse/image'

    def extract_text(self, image_path):
        """
        Extract text from an image using the OCR API.
        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        """
        with open(image_path, 'rb') as image_file:
            response = requests.post(
                self.ocr_provider_url,
                files={'file': image_file},
                data={'apikey': self.api_key, 'language': 'eng'}
            )
        result = response.json()
        # Handle response and errors
        if result.get('IsErroredOnProcessing'):
            raise Exception(result.get('ErrorMessage', 'OCR processing error'))
        return result['ParsedResults'][0]['ParsedText']
