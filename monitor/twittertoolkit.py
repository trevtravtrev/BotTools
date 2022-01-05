import pyautogui
import tkinter as tk
from time import sleep


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


def get_notifications():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\notification.png')
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\notification2.png',
                                   confidence=0.95)

    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\all_bold.png')
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\all.png')
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\mentions_bold.png')
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\mentions.png')


def get_messages():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\message.png')


# def get_home():
#     homes = locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\home.png')
#     # if all home buttons have already been clicked, click home buttons again to scroll to top of timelines
#     if not homes:
#         locate_all_on_screen_and_click(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\home2.png', confidence=0.95)

def get_default_screen():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\notification.png')
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\mentions.png')


def get_refresh():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\refresh.png')


def get_terminals():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\terminal.png',
                                   confidence=0.97)


def get_exit():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\exit.png')


def get_next_pi():
    get_default_screen()
    get_terminals()
    get_exit()


def center_window(window, width, height):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def run_gui():
    window_width = 250
    window_height = 223
    button_width = 35
    button_height = 3
    window = tk.Tk()
    center_window(window, width=window_width, height=window_height)
    window.title("Twitter Toolkit")
    window.geometry('250x223')
    buttons = {}
    options = {"Next Pi": get_next_pi,
               "Notifications": get_notifications,
               "Messages": get_messages,
               "Default": get_default_screen,
               "Refresh": get_refresh,
               "Terminals": get_terminals,
               "Exit Pi": get_exit}

    for index, option in enumerate(options.keys()):
        # setup first 3 buttons full row width each vertically
        if index <= 2:
            buttons[option] = tk.Button(window, text=option, height=button_height, width=button_width,
                                        command=options.get(option))
            buttons[option].pack()
        # setup bottom 3 buttons 1/3 width each side by side in 1 row
        else:
            buttons[option] = tk.Button(window, text=option, height=button_height, width=int(button_width / 4),
                                        command=options.get(option))
            buttons[option].pack(side=tk.LEFT)

    # open app on top of all other windows
    window.attributes('-topmost', True)
    window.update()

    window.mainloop()


if __name__ == '__main__':
    run_gui()
