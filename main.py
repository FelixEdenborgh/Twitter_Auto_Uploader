import time

import MakeTwitterContent
import Upload




# settings
# ---------------------------------------------------------
# Steg 1: Öppna cmd och skriv in cd C:\Program Files (x86)\Google\Chrome\Application
# Steg 2: skriv in detta: chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Selenium\Chrome_Test_Profile



# Number of iterations to perform before taking a break
iterations_before_break = 3

# Time to sleep in seconds for the break
break_duration = 3 * 60 * 60  # 5 hours in seconds

numberOfUploads = 0
runeonetime = 0
while(True):
    for i in range(iterations_before_break):
        MakeTwitterContent.makeTxtFile("Talk about Current Events and News. the Message cant be longer then 250 characters")

        Upload.upload_Message_And_Image()
        runeonetime += 1
        numberOfUploads += 1

        print(f"Number of uploads on the selenium: {numberOfUploads}")
        time.sleep(5)

    print(f"Taking a break for {break_duration / 60 / 60} hours...")
    time.sleep(break_duration)