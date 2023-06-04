import threading
import logging
import webserver
from realtime_recognition import start_recognizing
from recognition.consts import LOG_FILE_NAME


def main():
    webserver.start()


if __name__ == '__main__':
    logging.basicConfig(filename=LOG_FILE_NAME, encoding='utf-8', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    recognition = threading.Thread(target=start_recognizing)
    recognition.start()
    logging.debug("Started Capturing & Recognizing")
    webserver.start()
    logging.debug("Started Server")
