import pyautogui
import tkinter as tk
import pyperclip
import config
from time import sleep
from random import randint, choice


def locate_all_on_screen_and_click(image, wait=0.05, confidence=0.9):
    # get starting mouse position (when you click a button in the gui)
    mouse_x, mouse_y = pyautogui.position()
    locations = list(pyautogui.locateAllOnScreen(image, confidence=confidence))
    if locations:
        for location in locations:
            pyautogui.moveTo(location)
            pyautogui.click()
            sleep(wait)
        # return mouse to starting mouse position
        pyautogui.moveTo(mouse_x, mouse_y)
        return True
    if not locations:
        # return mouse to starting mouse position
        pyautogui.moveTo(mouse_x, mouse_y)
        return False


# def get_notifications():
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\notification.png')
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\notification2.png',
#                                    confidence=0.95)
#
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\all_bold.png')
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\all.png')
#     sleep(5)
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\mentions_bold.png')
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\mentions.png')


# def get_messages():
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\message.png')


# def get_home():
#     homes = locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\home.png')
#     # if all home buttons have already been clicked, click home buttons again to scroll to top of timelines
#     if not homes:
#         locate_all_on_screen_and_click(r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\home2.png', confidence=0.95)

# def get_mentions_screen():
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\notification.png')
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\mentions.png')


# def get_terminals():
#     locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\terminal.png',
#                                    confidence=0.97)

def get_refresh_mentions():
    locate_all_on_screen_and_click(
        image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\refresh_mentions.png')


def get_refresh_messages():
    locate_all_on_screen_and_click(
        image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\refresh_messages.png')


def get_mark_all_as_read():
    locate_all_on_screen_and_click(
        image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\mark_all_as_read.png', confidence=0.85)


def get_refresh():
    locate_all_on_screen_and_click(
        image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\refresh.png')


def get_exit():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\OneDrive\Documents\GitHub\BotTools\monitor\assets\exit.png')


def get_next_pi():
    get_mark_all_as_read()
    get_exit()


def get_notifications():
    get_refresh_mentions()
    get_refresh_messages()


def copy_reply_text(type):
    tweet_reply = ["dm'd you", "messaged you", "DM'd you", "Messaged you", "Sent a dm", "sent a dm", "Sent a message",
                   "sent a message"]
    locked_tweet_reply = ["your dm's are locked so I can't dm you", "your messages are locked so I can't message you",
                          "your dm's are locked so I can't message you", "your messages are locked so I can't dm you",
                          "your messages are private so I can't dm you", "your dm's are private so I can't message you",
                          "your messages are private so I can't message you", "your dm's are private so I can't dm you",
                          "Your dm's are locked so I can't dm you", "Your messages are locked so I can't message you",
                          "Your dm's are locked so I can't message you", "Your messages are locked so I can't dm you",
                          "Your messages are private so I can't dm you", "Your dm's are private so I can't message you",
                          "Your messages are private so I can't message you", "Your dm's are private so I can't dm you"]
    punctuation = "!"
    thanks = ["Thank you", "thank you", "Thank you so much", "thank you so much", "tysm", "Tysm", "Omg thank you",
              "omg thank you", "You just made my entire year", "you just made my entire year", "You are so kind",
              "you are so kind"]
    smilies = [':-)', ':)', ':))', ':D', ':-]', ':]', ':^)', ':-))', '']

    if type == "dm":
        return pyperclip.copy(
            f'{choice(thanks)}{randint(1, 10) * punctuation} {choice(smilies)}')
    elif type == "tweet":
        return pyperclip.copy(
            f'{choice(tweet_reply)}{randint(1, 10) * punctuation} {choice(thanks)}{randint(1, 10) * punctuation} {choice(smilies)}')
    elif type == "locked_tweet":
        return pyperclip.copy(
            f'{choice(locked_tweet_reply)}{randint(1, 10) * punctuation} {choice(thanks)}{randint(1, 10) * punctuation} {choice(smilies)}')


def get_crypto_buttons():
    crypto_addresses = {}
    for key, value in config.addresses.items():
        crypto_addresses[key] = lambda value=value: pyperclip.copy(value)
    return crypto_addresses


def center_window(window, width, height):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def run_gui():
    options = {
        "Next Pi": get_next_pi,
        "Notifications": get_notifications,
        "Mentions": get_refresh_mentions,
        "Mark All DM's Read": get_mark_all_as_read,
        "Refresh": get_refresh,
        "Exit Pi": get_exit,
        "Locked Tweet Reply": lambda: copy_reply_text(type="locked_tweet"),
        "Tweet Reply": lambda: copy_reply_text(type="tweet"),
        "DM Reply": lambda: copy_reply_text(type="dm")
    }
    options.update(get_crypto_buttons())
    buttons = {}
    window_width = 265
    window_height = 1008
    button_width = 18
    button_height = 3
    window = tk.Tk()
    center_window(window, width=window_width, height=window_height)
    window.title("Twitter Toolkit")
    window.geometry(f'{window_width}x{window_height}')

    for index, option in enumerate(options.keys()):
        if 0 <= index < 2:
            buttons[option] = tk.Button(window, text=option, height=button_height, width=button_width,
                                        command=options.get(option), bg='#FAD7A0').grid(columnspan=2, row=index,
                                                                                        column=0, sticky='nesw')
        elif 1 < index < 6:
            buttons[option] = tk.Button(window, text=option, height=button_height, width=button_width,
                                        command=options.get(option), bg='#CCD1D1').grid(columnspan=2, row=index,
                                                                                        column=0, sticky='nesw')

        elif 5 < index < 9:
            buttons[option] = tk.Button(window, text=option, height=button_height, width=button_width,
                                        command=options.get(option), bg='#5499C7').grid(columnspan=2, row=index,
                                                                                        column=0, sticky='nesw')
        else:
            if index % 2 == 0:
                buttons[option] = tk.Button(window, text=option, height=button_height, width=button_width,
                                            command=options.get(option), bg='#ABEBC6').grid(row=index - 1, column=1)
            else:
                buttons[option] = tk.Button(window, text=option, height=button_height, width=button_width,
                                            command=options.get(option), bg='#ABEBC6').grid(row=index, column=0)

    # open app on top of all other windows
    window.attributes('-topmost', True)
    window.update()

    window.mainloop()


if __name__ == '__main__':
    run_gui()
