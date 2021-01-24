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
        utils.click_button(r'assets\signin.png')
        pyautogui.write(self.username)
        pyautogui.press('tab')
        pyautogui.write(self.password)
        pyautogui.press('enter')
        print(f'Signed into {self.username}')
        sleep(7)

    def open_pis(self):
        for pi in self.pis_to_open:
            utils.click_button(self.linked_pis.get(pi), delay=5.5, confidence=.95, double_click=True)
            print(f'{pi} opened.')
            open_vnc()

    def _get_pis_to_open(self):
        for pi in config.pis_to_open:
            if pi in self.linked_pis.keys():
                self.pis_to_open.append(pi)


def open_vnc(delay=1):
    subprocess.Popen('vncviewer.exe', shell=True, cwd='C:\Program Files\RealVNC\VNC Viewer')
    sleep(delay)


def close_vnc():
    open_vnc()
    pyautogui.hotkey('alt', 'f4')
    print('VNC closed.')


def authentication_status():
    signed_out = pyautogui.locateOnScreen(r'assets\signin.png')
    if signed_out:
        print("VNC is signed out.")
        return False
    else:
        print("VNC is signed in.")
        return True


def sign_out():
    utils.click_button(r'assets\checkmark.png', delay=.5)
    utils.click_button(r'assets\signout.png')
    pyautogui.press('enter')
    print("Signed out of VNC.")


def create_account_objects():
    """
    :return: list of account objects
    """
    accounts = []
    for account in config.vnc_accounts:
        accounts.append(Account(account.get('username'), account.get('password'), account.get('linked_pis')))
    return accounts
