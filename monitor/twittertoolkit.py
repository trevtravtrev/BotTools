import pyautogui
import tkinter as tk
from time import sleep


def locate_all_on_screen_and_click(image, wait=0.1, confidence=0.85):
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
    notifications = locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\notification.png')
    # if all notification buttons have already been clicked, click "see more tweets" to scroll to top of notifications
    if not notifications:
        locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\notification2.png')


def get_messages():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\message.png')


def get_home():
    homes = locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\home.png')
    # if all home buttons have already been clicked, click home buttons again to scroll to top of timelines
    if not homes:
        locate_all_on_screen_and_click(r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\home2.png', confidence=0.9)


def get_terminals():
    locate_all_on_screen_and_click(image=r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\terminal.png')


def center_window(window, width, height):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def run_gui():
    window = tk.Tk()
    center_window(window, width=250, height=223)
    window.title("Twitter Toolkit")
    window.geometry('250x223')
    buttons = {}
    options = {"Home": get_home,
               "Notifications": get_notifications,
               "Messages": get_messages,
               "Terminals": get_terminals}

    for option in options.keys():
        buttons[option] = tk.Button(window, text=option, height=3, width=250, command=options.get(option))
        buttons[option].pack()

    # open app on top of all other windows
    window.attributes('-topmost', True)
    window.update()

    window.mainloop()


if __name__ == '__main__':
    run_gui()
