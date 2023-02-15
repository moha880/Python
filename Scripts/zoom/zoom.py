import os
import time
import datetime
import urllib.request
import pyautogui as py
from selenium import webdriver


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False


def picCoordinates(picture):
    r= None
    while r is None:
        r=py.locateCenterOnScreen(picture,grayscale=False,confidence=.7)
    return r.x,r.y


def join(meet_code,passcode):
    driver = webdriver.Chrome()
    driver.get('https://zoom.us/join')
    
    # --> storing meeting id and passcode, you may also take this as an input in your code from the user
    
    meet_code1 = meet_code[:3]
    meet_code2 = meet_code[3:6]
    meet_code3 = meet_code[6:]

    element_box=driver.find_element("xpath","//input[@id='join-confno']")
    time.sleep(1) 
    element_box.send_keys(meet_code1)
    time.sleep(0.5) 
    element_box.send_keys(meet_code2)
    time.sleep(0.5) 
    element_box.send_keys(meet_code3) 
    #waiting for 2 seconds to send the code
    time.sleep(2) 
    #finding the join button and clicking on it
    
    Btn = driver.find_element("xpath","//a[@id='btnSubmit']")
    Btn.click()
    
    X,Y =picCoordinates("openZoomMeetings.jpg")
    time.sleep(0.5) 
    py.click(clicks=2,x=X, y=Y)
    
    X,Y =picCoordinates("passcode.jpeg")
    py.click(clicks=2,x=X, y=Y)
    time.sleep(1) 

    py.typewrite(passcode,interval=0.25)

    X,Y =picCoordinates("joinMeeting.jpg")
    py.click(clicks=2,x=X, y=Y)
    
    if picCoordinates("mute.jpg"):
        py.hotkey('alt', 'a')

if __name__ == "__main__":
    print("********starting....********")
    time.sleep(5)

    meet_code="6224511075"
    passcode = "IMT-S6J9T2"
    x = datetime.datetime.now()
    days=["Monday","Tuesday","Wednesday","Thursday"]
    while True:
        if connect(): 
            print("connected...")
            time.sleep(5)

            if x.strftime("%A") in days:
                if int(x.strftime("%H"))>=20:
                    print("joining...")
                    join(meet_code,passcode)
                print("joined")
                time.sleep(5)
            break
        else:
            # input Wifi name
            print("start connecting...")
            time.sleep(2)
            name_of_router = "Mohammad"
            # connect to the given wifi network
            os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')


        
    
    
    
    