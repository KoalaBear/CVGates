import cv2
import imutils
import numpy
import pytesseract

from recognition.config import IMAGE_TO_STRING_CONFIG, DEBUG_MODE
from recognition.consts import NO_CONTOUR_DETECTED, EMPTY_STRING_READ


def recognize_plate(image: numpy.ndarray):
    """
    Recognizes a Plate number from a given Image ndarray[eg cv2's imread()]
    :param numpy.ndarray image: image: A Readen image
    :return string: Plate Number
    """
    if DEBUG_MODE:
        cv2.imshow("Frame", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to grey scale
    gray = cv2.bilateralFilter(gray, 11, 17, 17)  # Blur to reduce noise
    edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
    contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
    if screenCnt is None:
        cv2.destroyAllWindows()
        return NO_CONTOUR_DETECTED
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
    mask = numpy.zeros(gray.shape, numpy.uint8)
    cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    cv2.bitwise_and(image, image, mask=mask)
    x, y = numpy.where(mask == 255)
    topx, topy = (numpy.min(x), numpy.min(y))
    bottomx, bottomy = numpy.max(x), numpy.max(y)
    cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
    plate = pytesseract.image_to_string(cropped, IMAGE_TO_STRING_CONFIG).strip()
    if DEBUG_MODE:
        cv2.imshow("Frame", image)
        cv2.imshow('Cropped', cropped)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    if not plate:
        return EMPTY_STRING_READ
    return plate
