import webbrowser
import pyautogui
from time import sleep

import utils
import config


def open_amazon_affiliate_webpage(website, delay=1):
    _open_website(website, delay=delay)
    authenticated = _authentication_status()
    if not authenticated:
        _sign_in()


def view_commissions():
    try:
        utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\commissions.png')
    except:
        utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\commissions2.png')
    print("Commission view selected.")


def view_bounties():
    try:
        utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\bounties.png')
    except:
        utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\bounties2.png')
    print("Bounty view selected.")


def _open_website(website, delay=1):
    webbrowser.open(website)
    print(f'{website} opened.')
    sleep(delay)


def _authentication_status():
    signed_out = pyautogui.locateOnScreen(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\amazonsignin.png')
    if signed_out:
        print("Amazon is signed out.")
        return False
    else:
        print("Amazon is signed in.")
        return True


def _sign_in():
    pyautogui.write(config.amazon_password)
    pyautogui.press('enter')
    print(f'Signed into Amazon.')
    sleep(7)
