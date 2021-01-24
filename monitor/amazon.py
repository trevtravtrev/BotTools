import webbrowser
from time import sleep

import utils


def open_website(website, delay=1):
    webbrowser.open(website)
    print(f'{website} opened.')
    sleep(delay)


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
