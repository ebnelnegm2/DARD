import requests, urllib3, random, re, time , pyfiglet, sys
from cfonts import render, say
CYAN = "\033[36m"
RED = "\033[91m"
RED2 = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE2 = "\033[34m"
BLUE = "\033[94m"
PURPLE = "\033[1;95m"
YELLOW = "\033[1;33m"
RESET_COLOR = "\033[0m"

logo = render("EBN", colors=["white", "blue"],
 align="center")    
print(logo)
logo = render("ELNEGM", colors=["white", "blue"], align="center")    
print(logo)
print(PURPLE + "" + PURPLE + f"""
• TELEGRAM => https://t.me/ebn_elnegm
""" + PURPLE+ " ")
print(f"{CYAN}" * 50)
urllib3.disable_warnings()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0025)

print()
lol = str("=" * 65)
jalan(f"{RED}  {lol}")

coin = input(f' {BLUE2}[?]{GREEN} COIN {PURPLE}->{YELLOW} ')
token = '6827216230:AAGvEgjnoea7tUkabnz_9R36tpQxZa3sWdU'
ch='LTCPRICE1'
params = {
    'fsym': coin,
    'tsyms': 'USDT',
}
while True:
    price = requests.get('https://min-api.cryptocompare.com/data/price', params=params)
    PRICE=price.json()['USDT']
    print(PRICE)
    msg=f"PRICE↝| {PRICE}$ "
    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=@{ch}&text={msg}"
    requests.get(tlg).json()
