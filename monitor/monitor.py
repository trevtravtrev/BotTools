from time import sleep

import vnc
import amazon
import config


def main():
    if config.vnc:
        # create list of account objects from accounts provided in config.py
        accounts = vnc.create_account_objects()
        # open VNC and get to sign in screen
        vnc.open_vnc(delay=.5)
        authenticated = vnc.authentication_status()
        if authenticated:
            vnc.sign_out()
        # for each account provided in config.py, sign in, open pi windows, sign out
        for account in accounts:
            if account.pis_to_open:
                account.sign_in()
                account.open_pis()
                sleep(.6*(len(account.linked_pis)))
                vnc.sign_out()
        # close main vnc window
        vnc.close_vnc()

    if config.amazon:
        # open today's amazon commission earnings (authenticates if not signed in)
        amazon.open_amazon_affiliate_webpage(
            'https://affiliate-program.amazon.com/home/reports?ac-ms-src=summaryforthismonth', delay=10)
        amazon.view_commissions()
        # open today's amazon bounty earnings (authenticates if not signed in)
        amazon.open_amazon_affiliate_webpage(
            'https://affiliate-program.amazon.com/home/reports?ac-ms-src=summaryforthismonth', delay=10)
        amazon.view_bounties()
        # open yesterday's amazon consolidated earnings (authenticates if not signed in)
        amazon.open_amazon_affiliate_webpage('https://affiliate-program.amazon.com/p/reports/global', delay=0)

    print("Successfully completed all tasks.")


if __name__ == '__main__':
    main()
