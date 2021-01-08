from time import sleep

from camera.grab_frame import grab_frame
from config import MANUALLY_CLOSED_GATE, CLOSE_GATE_DELAY
from gate_control.toggle import open_gate, close_gate
from platenumbers.models import PlateNumber
from recognition.recognize_plate import recognize_plate

DELAY_BETWEEN_FRAMES = 1


def start_recognizing():
    while True:
        plate_seen = None
        while plate_seen is None:
            frame = grab_frame()
            recognized_plate = recognize_plate(frame)
            if recognized_plate != "":
                plate_seen = recognized_plate
            else:
                sleep(1)
        if is_plate_in_db(plate_seen):
            open_gate()
            print(f"Gate opened for {plate_seen}")
            if MANUALLY_CLOSED_GATE:
                sleep(CLOSE_GATE_DELAY)
                close_gate()


def is_plate_in_db(plate_number):
    found = bool(PlateNumber.objects.get(plate_number=plate_number))
    print(found)  # TODO: Search
    return found
