from bs4 import BeautifulSoup
import requests
import time
from win10toast import ToastNotifier


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def btctousd(search):
    search=search.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q=bitcoin+price&rlz=1C1VDKB_enUS933US933&oq=bitcoin+price&aqs=chrome..69i57j0i433i512l5j0i131i433i512j69i60.2605j1j4&sourceid=chrome&ie=UTF-8',headers=headers)
    
    soup = BeautifulSoup(res.text,'html.parser')   
    
    usd = soup.select('.pclqee')[0].getText().strip()

    
    information = f"1 Bitcoin = ${usd} USD"
    toaster = ToastNotifier()
    toaster.show_toast("Bitcoin Price Tracker", f"{information}",
                                            duration=20,
                                            threaded=True)
    while toaster.notification_active(): time.sleep(0.005)
    
search = "bitcoin"
search=search+" price"
btctousd(search)