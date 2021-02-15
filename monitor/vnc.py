import subprocess
import pyautogui
from time import sleep

import utils
import config


class Account:
    def __init__(self, username, password, linked_pis):
        self.username = username
        self.password = password
        self.linked_pis = linked_pis  # dictionary {pi_name: image_filepath} linked to account
        self.pis_to_open = []  # list of pis linked to account to open when program runs (keys for linked_pis dict,
        # set in config.pis_to_open)

        self._get_pis_to_open()

    def sign_in(self):
        while True:
            signin_clicked = utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\signin.png', confidence=.6)
            if signin_clicked:
                pyautogui.write(self.username)
                pyautogui.press('tab')
                pyautogui.write(self.password)
                pyautogui.press('enter')
                print(f'Signed into {self.username}')
                return True

    def open_pis(self):
        for pi in self.pis_to_open:
            pi_opened = False
            while not pi_opened:
                open_vnc()
                pi_opened = utils.click_button(self.linked_pis.get(pi), confidence=.95, clicks=2, open_vnc=True, loop=False)
            print(f'{pi} opened.')

    def _get_pis_to_open(self):
        for pi in config.pis_to_open:
            if pi in self.linked_pis.keys():
                self.pis_to_open.append(pi)


def open_vnc(delay=0):
    subprocess.Popen('vncviewer.exe', shell=True, cwd='C:\Program Files\RealVNC\VNC Viewer')
    sleep(delay)


def close_vnc():
    open_vnc()
    sleep(.2)
    pyautogui.hotkey('alt', 'f4')
    print('VNC closed.')


def authentication_status():
    signed_out = pyautogui.locateOnScreen(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\signin.png')
    if signed_out:
        print("VNC is signed out.")
        return False
    else:
        print("VNC is signed in.")
        return True


def sign_out():
    while True:
        open_vnc()
        checkmark_clicked = utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\checkmark.png', open_vnc=True)
        if checkmark_clicked:
            signout_clicked = utils.click_button(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\signout.png', open_vnc=True)
            if signout_clicked:
                pyautogui.press('enter')
                print("Signed out of VNC.")
                return True


def create_account_objects():
    """
    :return: list of account objects
    """
    accounts = []
    for account in config.vnc_accounts:
        accounts.append(Account(account.get('username'), account.get('password'), account.get('linked_pis')))
    return accounts
