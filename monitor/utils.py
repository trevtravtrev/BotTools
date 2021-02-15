import pyautogui
import vnc


def click_button(button_image, confidence=.8, clicks=1, open_vnc=False, loop=True):
    """
    :param button_image: image name string (must be stored in same directory as code)
    :param confidence: int from 0 to 1 for machine learning confidence parameter
    :param clicks: amount of clicks
    :param open_vnc: opens VNC directly before double click (fixed bug from vnc pi window opening overtop of vnc viewer)
    :param loop: infinitely tries to click button if True.
    :return: n/a
    """
    while True:
        location = pyautogui.locateCenterOnScreen(button_image, confidence=confidence)
        if location:
            if open_vnc:
                vnc.open_vnc()
            pyautogui.moveTo(location)
            pyautogui.click(clicks=clicks)
            return True
        else:
            if not loop:
                return False
