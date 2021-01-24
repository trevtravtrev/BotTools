import pyautogui

from time import sleep


def click_button(button_image, delay=1, confidence=.6, double_click=False):
    """
    :param button_image: image name string (must be stored in same directory as code)
    :param delay: delay in seconds after button is clicked
    :param confidence: int from 0 to 1 for machine learning confidence parameter
    :param double_click: bool to enable double click
    :return: n/a
    """
    location = pyautogui.locateCenterOnScreen(button_image, confidence=confidence)
    if location:
        pyautogui.moveTo(location)
        if double_click:
            pyautogui.click(clicks=2)
        else:
            pyautogui.click()
        sleep(delay)
    else:
        raise Exception(f'{button_image} image not found on screen.')
