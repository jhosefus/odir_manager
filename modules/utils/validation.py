from config import VALID_EXTENSIONS

def validate_image_path(path):
    return path.lower().endswith(VALID_EXTENSIONS)