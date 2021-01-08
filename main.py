import threading

import webserver
from realtime_recognition import start_recognizing


def main():
    webserver.start()


if __name__ == '__main__':
    server = threading.Thread(target=webserver.start)
    server.start()
    print("Started Server")
    start_recognizing()
    print("Started Capturing & Recognizing")
