from flask import Blueprint, render_template, request
from ..services import OCRService

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    return render_template('index.html')

@pages_bp.route('/parse-image', methods=['POST'])
def parse_image():
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400
    file = request.files['file']
    if file.filename == '':
        return {'error': 'No selected file'}, 400
    # For testing, just return the filename
    return {'filename': file.filename}, 200