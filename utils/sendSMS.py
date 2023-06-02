import os
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send(chipCode):
    os.system(f"open 'sms://888222/;?&body={chipCode}'")
    keyboard.press(Key.enter)
    return True


