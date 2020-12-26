# tesseract - Page Segmentation Mode - Consts
PAGE_SEGMENTATION_MODE_PARAMETER = "--psm"
PSM_CHAR_WHITELIST = "tessedit_char_whitelist"
PSM_TREAT_IMAGE_AS_SINGLE_WORD = "8"
# tesseract - Language - Consts
LANGUAGE_PARAMETER = "-l"
ENGLISH_TESSERACT_LANG = "eng"  # Language values supported by tesseract [available on `tesseract --list-langs`]
# Presets for Whitelisting
DIGITS_LIST = '1234567890'
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ENGLISH_ALPHABET += ENGLISH_ALPHABET.upper()

# Errors
NO_CONTOUR_DETECTED = "No Contour detected"
EMPTY_STRING_READ = "Tesseract returned an empty string."
