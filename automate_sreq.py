import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# linkedin post liker
#
# Add your post url (if any) to your posts here for others to like them : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
#
#
#
# To like other people's post:
# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb

# step 1 change this from : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
links = [
    "https://www.linkedin.com/posts/sidd-oo_100daysofcode-devsnestday21-devsnest6monthschallenge-activity-6789459261542973440-x7FX/",
    "https://www.linkedin.com/posts/ross-nelson-32493684_devsnest6monthschallenge-devsnestday21-slowandsteady-activity-6788661474186338304-Dx0z"
]
#step 2 : run code , check if you are logged in (if not, then login) then press 1 in console
#step 3 : the code shoud take care of the rest add your posts that you would want to get liked



options = webdriver.ChromeOptions()
#options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")
# delete this after every month

#while "1" != input("press 1 when signed in: "):
 #   pass
driver.get("https://www.linkedin.com/login?")
username = driver.find_element_by_id("username")
username.send_keys("Put your username/emailid here!")
password = driver.find_element_by_id("password")
print("signing in...")
password.send_keys("Put your password here!")
log_b = driver.find_element_by_xpath("//*[@type='submit']")
log_b.click()

driver.get("https://www.linkedin.com/mynetwork/")
print("making connections....")
sleep(10)
#driver.find_element_by_class_name("invitation-card__action-btn").click()

buttons= driver.find_elements_by_class_name("full-width")
for button in buttons:
    word = button.get_attribute("type")
    if word == "button":
        print("Clicking...")
        button.click()
        print("Clicked!!")
        sleep(2)

#driver.find_element_by_xpath("//*[@aria-label='button']").click()

#buttons = driver.find_element_by_class_name("invitation-card__action-btn")
#for button in buttons:
 #   word=button.get_attribute("aria-label")
  #  if word.split(" ")[0] == "Accept":
   #     print("Clicking....")
    #    button.click()        
     #   print("Clicked!!")
      #  sleep(1)

print("closing driver")

#for link in links:
 #   try:
  #      print("accessing link ", link)
   #     driver.get(link)
    #    sleep(2)
     #   el = driver.find_element_by_class_name("react-button__trigger")
      #  if "false" == el.get_attribute("aria-pressed"):
    #        print("liking")
     #       el.click()
      #      print("liked")
       #     sleep(1)
       # else:
        #    print("already processed link ", link)
    #except Exception as e:
     #   print("error processing link\nlink: ", link, "\nerror",  e)

driver.close()
