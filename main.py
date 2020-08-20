import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import click_image
# wrapper for less typing
pyautogui.PAUSE=0.01

def click(context):
    pyautogui.click(context)


def locateOnScreen(image_path):
    return pyautogui.locateOnScreen(image_path, confidence=0.75)


def deleteTagsUsingReport():
    #haven't tested the new opencv method hence the sleep persists
    
    click_image('report_button.png',imagesearch('report_button.png'),"left",0,offset=1)
    time.sleep(1)

    
    click_image('annoying_option.png',imagesearch('annoying_option.png'),"left",0,offset=1)
    time.sleep(1)

    
    click_image('remove_tag_option`.png',imagesearch('remove_tag_option`.png'),"left",0,offset=1)
    time.sleep(1)

    
    click_image('remove_tag_button.png',imagesearch('remove_tag_button.png'),"left",0,offset=1)
    time.sleep(1)

    click_image('navbar_back_button.png',imagesearch('navbar_back_button.png'),"left",0,offset=1)
    time.sleep(1)


    click_image('chrome_refresh.png',imagesearch('chrome_refresh.png'),"left",0,offset=1)
    time.sleep(1)


while True:
    
    if imagesearch('dropdown_menu.png',precision=0.9) != [-1,-1]:
        click_image('dropdown_menu.png',imagesearch('dropdown_menu.png'),"left",0,offset=1)
        if imagesearch('delete_option.png'):
            click_image('delete_option.png',imagesearch('delete_option.png'),"left",0,offset=1)
        elif imagesearch('report_button.png'):
            deleteTagsUsingReport()

        elif imagesearch('unvote_button.png'):
            click_image('unvote_button.png',imagesearch('unvote_button.png'),"left",0,offset=1)
    elif imagesearch('load_more_option.png') != [-1,-1]:
        print("Refreshing")
        click_image('chrome_refresh.png',imagesearch('chrome_refresh.png'),"left",0,offset=1)
        time.sleep(1)   

    else:
        print("couldn't find more previous posts scrolling for more")
        pyautogui.scroll(100)
