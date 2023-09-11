# Setup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import DeleteFilesFromFolder

import random

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
bot = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe",chrome_options=opt)


print(bot.title)

time.sleep(15)
bot.get("https://twitter.com/home")
time.sleep(15)

def getFirstTxtFile():
    folder_path = "C:\\Users\\FelixEdenborgh\\Documents\\PythonPrograms\\AutoTwitterXContenctCreator\\TweetMessage"
    files = [file for file in os.listdir(folder_path) if file.lower().endswith('.txt')]

    if not files:
        return None

    first_txt_file = files[0]
    first_txt_file_path = os.path.join(folder_path, first_txt_file)

    return first_txt_file_path

def get_random_image_from_folder():
    folder_path = "C:\\Users\\FelixEdenborgh\\Documents\\PythonPrograms\\AutoTwitterXContenctCreator\\Images"
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    if not image_files:
        return None  # No image files found in the folder

    random_image_file = random.choice(image_files)
    random_image_path = os.path.join(folder_path, random_image_file)

    return random_image_path



def upload_Message_And_Image():
    print("New upload started")
    time.sleep(3)
    bot.get("https://twitter.com/home")
    time.sleep(15)

    txt_file_path = getFirstTxtFile()
    image_file_path = get_random_image_from_folder()

    time.sleep(5)
    #Tweet Message
    try:
        try:
            if txt_file_path:
                with open(txt_file_path, 'r') as txt_file:
                    txt_content = txt_file.read()
                    addMessage = bot.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')  # Your element locator
                    addMessage.send_keys(txt_content)
        except:
            print("Cant find Make new tweet message bord by xpath")

        try:
            if txt_file_path:
                with open(txt_file_path, 'r') as txt_file:
                    txt_content = txt_file.read()
                    addMessage = bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')  # Your element locator
                    addMessage.send_keys(txt_content)
        except:
            print("Cant find Make new tweet message bord by Full xpath")

        try:
            if txt_file_path:
                with open(txt_file_path, 'r') as txt_file:
                    txt_content = txt_file.read()
                    addMessage = bot.find_element(By.CSS_SELECTOR, '/#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')  # Your element locator
                    addMessage.send_keys(txt_content)
        except:
            print("Cant find Make new tweet message bord by Selector")
    except:
        print("Cant add any Messages to the Tweet")
    """
    time.sleep(5)
    # Tweet Add image
    try:
        try:
            upload_image_xpath = "//input[@data-testid='SearchBox_Search_Input']"
            bot.find_element_by_xpath(upload_image_xpath).send_keys(image_file_path)
        except:
            print("Cant find Make new tweet image bord by xpath")

        try:
            element = bot.find_element_by_xpath("//input[@type='file']")

            bot.execute_script("arguments[0].style.display = 'block';", element)

            element.send_keys(image_file_path)
        except:
            print("javascript not found")

        try:
            addMessage = bot.find_element(By.ID, 'fileInput')
            addMessage.send_keys(image_file_path)
        except:
            print("Cant find image by id")
        try:
            addMessage = bot.find_element(By.CSS_SELECTOR, "br[data-text='true']")
            addMessage.send_keys(image_file_path)
        except:
            print("Cant find image by selector")
    except:
        print("Cant add any Messages to the Tweet") 
        """
    try:
        try:
            submitButton = bot.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
            submitButton.click()
            return
        except:
            print("Cant Click submitButton with xpath")

        try:
            submitButton = bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
            submitButton.click()
            return
        except:
            print("Cant Click submitButton with Full xpath")

        try:
            submitButton = bot.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-14lw9ot.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr')
            submitButton.click()
            return
        except:
            print("Cant Click submitButton with Selector")
    except:
        print("Some error with Post button")


















































