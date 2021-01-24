import vnc
import config


def main():
    if config.vnc:
        # create list of account objects from accounts provided in config.py
        accounts = vnc.create_account_objects()
        # open VNC and get to sign in screen
        vnc.open_vnc()
        authenticated = vnc.authentication_status()
        if authenticated:
            vnc.sign_out()
        # for each account provided in config.py, sign in, open pi windows, sign out
        for account in accounts:
            if account.pis_to_open:
                account.sign_in()
                account.open_pis()
                vnc.sign_out()
        # close main vnc window
        vnc.close_vnc()


if __name__ == '__main__':
    main()
