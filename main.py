import threading

import webserver
from realtime_recognition import start_recognizing


def main():
    webserver.start()


if __name__ == '__main__':
    recognition = threading.Thread(target=start_recognizing)
    recognition.start()
    print("Started Capturing & Recognizing")
    webserver.start()
    print("Started Server")
