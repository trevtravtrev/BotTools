vnc = True
amazon = True

# list of pi names to open. MUST exact match dictionary keys in vnc_accounts.linked_pis
pis_to_open = ['pluggrr', 'pi 5', 'pi 6', 'pi 7']

# vnc accounts (list of dictionaries)
# username = vnc account username (string)
# password = vnc account password (string)
# linked_pis = {pi_name: image_filepath} (dictionary of strings)
    # pi_name: name of pi in vnc server
    # image_filepath: filepath for .png image of pi name as it appears in vnc viewer (for use with pyautogui)
vnc_accounts = [{'username': 'user1',
                 'password': 'pass1',
                 'linked_pis': {
                     'Gaming PC': r'assets\gamingpc.png',
                     'pi 4': r'assets\pi4.png',
                     'pi 5': r'assets\pi5.png',
                     'pi 6': r'assets\pi6.png',
                     'pi 7': r'assets\pi7.png'
                 }
                 },
                {'username': 'user2',
                 'password': 'pass2',
                 'linked_pis': {
                     'deallrr': r'assets\deallrr.png',
                     'pi 1': r'assets\pi1.png',
                     'pi 2': r'assets\pi2.png',
                     'pi 3': r'assets\pi3.png',
                     'pluggrr': r'assets\pluggrr.png'
                 }
                 }]
