import pytesseract

from recognition.consts import PAGE_SEGMENTATION_MODE_PARAMETER, PSM_TREAT_IMAGE_AS_SINGLE_WORD, ENGLISH_TESSERACT_LANG, \
    LANGUAGE_PARAMETER, PSM_CHAR_WHITELIST, ENGLISH_ALPHABET, DIGITS_LIST

# Tesseract Config
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Image To String Configuration
IMAGE_TO_STRING_CONFIG = f'{PAGE_SEGMENTATION_MODE_PARAMETER} {PSM_TREAT_IMAGE_AS_SINGLE_WORD} ' \
                         f'{LANGUAGE_PARAMETER} {ENGLISH_TESSERACT_LANG} ' \
                         f'-c {PSM_CHAR_WHITELIST}={ENGLISH_ALPHABET}{DIGITS_LIST}'
# Debug Mode opens the images with cv2
DEBUG_MODE = True
