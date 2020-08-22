from python_imagesearch.imagesearch import imagesearch,click_image
import time
import pyautogui
print("sleeping")
time.sleep(5)

def failsafeCheck():
    current_mouse_position = pyautogui.position()
    if current_mouse_position[0]< 250 and current_mouse_position[1]< 250 :
        print("Fail Safe triggered object not found on screen")
        if imagesearch('refresh_browser.png')!=[-1,-1]:
            print('Refreshing browser')
            click_image('refresh_browser.png',imagesearch('refresh_browser.png'),"left",0.0,offset=0)
            print("sleeping till the page loads")
            time.sleep(10)
        current_mouse_position = pyautogui.position()

        if current_mouse_position[0]< 250 and current_mouse_position[1]< 250 :
            print("exiting")
            exit()

def deleteComments():
    if imagesearch('drop_down_menu.png')!= [-1,-1]:
        click_image('drop_down_menu.png',imagesearch('drop_down_menu.png'),"left",0.0,offset=0)

        if imagesearch('delete_option.png')!= [-1,-1]:    
            click_image('delete_option.png',imagesearch('delete_option.png'),"left",0.0,offset=0)
   
    else:
        print("scrolling")
        pyautogui.scroll(-10)

def deletePosts():
    if imagesearch('drop_down_menu.png')!= [-1,-1]:
        click_image('drop_down_menu.png',imagesearch('drop_down_menu.png'),"left",0.0,offset=0)    
    
        if imagesearch('delete_option.png')!= [-1,-1]:    
            click_image('delete_option.png',imagesearch('delete_option.png'),"left",0.0,offset=0)
            
            time.sleep(1)

            if imagesearch('delete_button.png')!= [-1,-1]:    
                click_image('delete_button.png',imagesearch('delete_button.png'),"left",0.0,offset=0)
                time.sleep(1.8)
    
    else:
        print("scrolling")
        pyautogui.scroll(-10)

while True:
    failsafeCheck()

