import logging
from time import sleep

from camera.grab_frame import grab_frame
from config import MANUALLY_CLOSED_GATE, CLOSE_GATE_DELAY, DELAY_BETWEEN_FRAMES
from gate_control.toggle import open_gate, close_gate
from platenumbers.models import PlateNumber
from recognition.consts import EMPTY_STRING_READ
from recognition.recognize_plate import recognize_plate


def start_recognizing():
    while True:
        plate_seen = None
        while plate_seen is None:
            frame = grab_frame()
            recognized_plate = recognize_plate(frame)
            if recognized_plate != EMPTY_STRING_READ:
                plate_seen = recognized_plate
            else:
                sleep(DELAY_BETWEEN_FRAMES)
        if is_plate_in_db(plate_seen):
            open_gate()
            logging.info(f"Gate opened for {plate_seen}")
            if MANUALLY_CLOSED_GATE:
                sleep(CLOSE_GATE_DELAY)
                close_gate()


def is_plate_in_db(plate_number):
    found = bool(PlateNumber.objects.get(plate_number=plate_number))
    logging.debug(f"{plate_number} found in DB")  # TODO: Search if Plate in DB
    return found
