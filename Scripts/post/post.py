import pyautogui                                        

def press(string,pause):
    pyautogui.press(str(string))
    pyautogui.PAUSE = int(pause)
def write(string,pause):
    pyautogui.typewrite(str(string))
    pyautogui.PAUSE = int(pause)
def main():
    press('win',2.5)
    write('chrome',2)
    press('enter',2)
    write('facebook',1)
    pyautogui.press('up',presses=2)
    press('enter',4)
    r= None
    while r is None:
        r=pyautogui.locateCenterOnScreen('hhhhh.jpeg',grayscale=False, confidence = 0.95)
    X=r.x
    Y=r.y
    pyautogui.click(x=X, y=Y)
    pyautogui.PAUSE = 3
    write("Alhamdulillah, My first automated post with python.",4)
    R= None
    while R is None:
        R=pyautogui.locateCenterOnScreen('Post.jpeg',grayscale=False, confidence = 0.95)
    X=R.x
    Y=R.y
    # pyautogui.click(x=X, y=Y)
    # pyautogui.PAUSE = 3
    
if __name__ == '__main__':
    main()