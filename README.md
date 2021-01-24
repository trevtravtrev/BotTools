# BotTools    
 Tools for monitoring all of my different bots running on many raspberry pis.    
    

## **Monitor**  
#### **What it does:**  
 - VNC viewer: automates opening any number of remote device windows from any number of VNC accounts (since VNC limits 5 linked remote devices per account)  
 - Amazon affiliate: opens all of today's and yesterday's earning statistics for monitoring    
#### **To use:**    
 - Settings in config.py (toggles for features you want to run, vnc authentication details/linked pis to each account, specific linked pis you want to open)    
 - Run monitor.py  
#### **Features:**    
 - Opens any number of linked remote device windows simultaneously from any number of VNC accounts (signing out of a VNC account does not close its open remote devices windows)    
 - Automates sign in/sign out for any number of vnc accounts/linked remote devices    
 - Automates click procedures/hotkeys to open all linked remote devices you specify (in config.py) for every VNC account (also set in config.py)    
 - Opens 3 instances of amazon affiliate dashboard webpages    
   - instance 1: automates selecting today's commissions view    
   - instance 2: automates selecting today's bounties view    
   - instance 3: automates selecting yesterday's earnings overview