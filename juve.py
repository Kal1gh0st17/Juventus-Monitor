from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import urllib, winsound
import urllib.error
import urllib.request
import json, requests
import time

#

def telegram_bot_sendtext(bot_message):
    
    bot_token = '912915432:AAESgJBQlqSbo2aGeAh8Uko7n7UJehDexI4'
    bot_chatID = '173494066'
    send_text = 'https://api.telegram.org/bot' + '912915432:AAESgJBQlqSbo2aGeAh8Uko7n7UJehDexI4' + '/sendMessage?chat_id=' + '173494066' + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
while True:
    driver_path="C:/Windows/chromedriver_win32/chromedriver.exe" 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    prefs = {"credentials_enable_service": False , 
            "profile.password_manager_enabled" : False
            }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]);
    chrome_options.add_experimental_option('useAutomationExtension', False)
    #chrome_options.add_argument("--disable-infobars")
    
    browser = webdriver.Chrome(driver_path, options=chrome_options); 
    browser.get("https://pass.juventus.com/it/");
    browser.delete_all_cookies()
    browser.fullscreen_window()
    
    credentials={
    'eleguardini93@gmail.com' : 'password1987$$',
    'antoniocappiello@gmx.com' : 'Termosifone',
    }
    for user in credentials:
        access_button=browser.find_element_by_xpath("//a[@href='/login']").click();
        username = browser.find_element_by_id('username')
        username.send_keys(user)
        
        password = browser.find_element_by_id('password')
        password.send_keys(credentials[user])
        
        time.sleep(1)

        login_button = browser.find_element_by_class_name(u"dcm-login--btn").click()
        
        code = requests.get(browser.current_url)
        status = code.status_code

        if status != 200:
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)  
            message = telegram_bot_sendtext("Juventus need your help!!")
            browser.quit()
        else:
            time.sleep(2)
            user=browser.find_element_by_xpath('//*[@id="menuTarget"]/div[2]/div/ul/li[3]/a').click()
            time.sleep(2)
            logout=browser.find_element_by_xpath("/html/body/div/div[2]/div/section/div[2]/div/div/div/div[2]/form/button").click()
        
        time.sleep(5)

    time.sleep(310)
    browser.quit()
exit()








Router FastGate ip: 192.168.1.254/24 
Credenziali: 
usr: Administrator 
psw: 42a18b37c19
public 93.39.142.35
SSID: Giappoke
password: giappoke123 (cambiare ogni mese)

ip: tp-link piano superiore 192.168.1.50/24
ip lan: 192.168.0.x/24 --> per le stampanti delle comande 
mod accesspoint 
usr: admin
psw: admin 
SSID: TP-Link-piano_terra
psw:

ip: to-link piano sotto    192.168.0.x/24 
mod accesspoint
usr: admin
psw: admin
SSID: TP
psw:


stampante 192.168.1.66/24 statico connessa in wifi 
Nome rete: HP62B249.lan
amministrazione@
Kingoten!
silvia tamborra 
amministrazione@
xxxxxx (foglio scritto e stampato)
Account HP
Nome: Silvia
Cognome: Tamborra
e-mail: gestione@kingonet.it
password: kingo10!
numero di cellulare: 3384766311





