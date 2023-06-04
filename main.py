import threading
import logging
import webserver
from realtime_recognition import start_recognizing


def main():
    webserver.start()


if __name__ == '__main__':
    recognition = threading.Thread(target=start_recognizing)
    recognition.start()
    logging.debug("Started Capturing & Recognizing")
    webserver.start()
    logging.debug("Started Server")
