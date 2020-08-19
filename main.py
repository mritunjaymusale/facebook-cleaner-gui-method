import pyautogui
import time

# wrapper for less typing
def click(context):
    pyautogui.click(context)

def locateOnScreen(image_path):
    return pyautogui.locateOnScreen(image_path,confidence=0.75)



while True:

    if locateOnScreen('dropdown_menu.png'):
        dropdown = locateOnScreen('dropdown_menu.png')
        click(dropdown)
    else:
        print("Found no dropdowns checking for older posts")
        #TODO Use load_more.png for loading older posts


    if locateOnScreen('delete_option.png'):
        delete_option = locateOnScreen('delete_option.png')
        click(delete_option)
    if locateOnScreen('report_button.png'):

        #sleep is added because internal screenshot mechanism is slow
        report_option = locateOnScreen('report_button.png')
        click(report_option)
        time.sleep(1)
        annoying_option= locateOnScreen('annoying_option.png')
        click(annoying_option)
        time.sleep(1)

        remove_tag_option =locateOnScreen('remove_tag_option.png')
        click(remove_tag_option)
        time.sleep(1)

        remove_tag_button = locateOnScreen('remove_tag_button.png')
        click(remove_tag_button)
        time.sleep(1)

        navbar_back_button= locateOnScreen('navbar_back_button.png')
        click(navbar_back_button)
        time.sleep(1)

        refresh_webpage = locateOnScreen('chrome_refresh.png')
        click(refresh_webpage)
        time.sleep(1)

    if locateOnScreen('unvote_button.png'):
        unvote_button = locateOnScreen('unvote_button.png')
        click(unvote_button)