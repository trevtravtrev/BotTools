# toggles for features you want to run
vnc = True
amazon = False

# amazon affiliate password (assumes website already has cookie stored for your username, manually sign in once if not)
amazon_password = "pass"

# list of pi names to open. MUST exact match dictionary keys in vnc_accounts.linked_pis
pis_to_open = ['pi 0', 'pi 1', 'pi 2', 'pi 3', 'pi 4', 'pi 5', 'pi 6', 'pi 7']

"""
vnc_accounts (list of dictionaries)
 - username = vnc account username (string)
 - password = vnc account password (string)
 - linked_pis = {pi_name: image_filepath} (dictionary of strings)
        - pi_name: name of pi in vnc server
        - image_filepath: filepath for .png image of pi name as it appears in vnc viewer (for use with pyautogui)
"""
vnc_accounts = [
    {'username': 'user1',
     'password': 'pass1',
     'linked_pis': {
         'pi 0': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi0.png',
         'pi 1': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi1.png',
         'pi 2': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi2.png',
         'pi 3': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi3.png',
     }},
    {'username': 'user2',
     'password': 'pass2',
     'linked_pis': {
         'Gaming PC': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\gamingpc.png',
         'pi 4': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi4.png',
         'pi 5': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi5.png',
         'pi 6': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi6.png',
         'pi 7': r'C:\Users\trevo\Documents\GitHub\BotTools\monitor\assets\pi7.png'
     }}
]
