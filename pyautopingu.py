import pyautogui
import time


def main():
    win = False
    numRuns = 0
    print("Running bot...")
    while(win is False):
        numRuns += 1
        win = runGame()
    print("Bot has finished in", numRuns, "runs")


def runGame():
    ltime = time.strftime("%b%d%Y%H%M%S")
    ftime = time.strftime("%H:%M:%S")
    OK_LOC = pyautogui.locateOnScreen("ok.png")
    pyautogui.click(OK_LOC[0], OK_LOC[1], button="left")
    pyautogui.click(OK_LOC[0], OK_LOC[1], button="left")

    time.sleep(1.624)
    pyautogui.click(OK_LOC[0], OK_LOC[1], button="left")

    OK_LOC = None
    num = 0

    while(OK_LOC is None):
        if num == 0:
            print("Looking for 'OK' button")
            num += 1
        OK_LOC = pyautogui.locateOnScreen("ok.png")

    WIN_LOC = pyautogui.locateOnScreen("win.png")
    WIN_LOC2 = pyautogui.locateOnScreen("win2.png")
    WIN_LOC3 = pyautogui.locateOnScreen("win3.png")
    WIN_TEN = pyautogui.locateOnScreen("ten.png")

    print("Do we have a winner?")

    if(WIN_LOC is not None or WIN_LOC2 is not None or WIN_LOC3 is not None):
        if(WIN_TEN is not None):
            print("Score is 10,000, not high enough")
        else:
            print("Score is higher than 10,000")
            print("Bot finished at", ftime)
            return True

    print("I guess not..")
    print("Taking a screenshot")
    print()
    pyautogui.screenshot(
        ltime + ".png", region=(OK_LOC[0] - 155, OK_LOC[1], 100, 50))

    return False

main()
