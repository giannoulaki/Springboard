from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
import os
import sys
import requests
import logging
import random
import json
import uuid

parameters = sys.argv[1:]

# Kill process if it fails, because it keeps on running if driver.quit() is not run
# for pid in $(ps -ef | grep "chromium" | awk '{print $2}'); do kill -9 $pid; done


"""
    Search google photos and download them

"""
### logging outout for after code runs
logging.basicConfig(filename='myapp.log', level=logging.INFO)
agent_version = '%.2f' % (random.randint(20, 100) + random.randint(1, 100)/float(100))

### Create a header for the get request when downloding the images
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 8\.0; Windows NT 5\.1; SV1)  Chrome/%s.2924.87 Safari/537.36' % agent_version
}

# opsys = 'linux'
#if os=='windows'
#    chrome_path = r"chromedriver.exe"
#    driver = webdriver.Chrome(executable_path=chrome_path)
#    wait = WebDriverWait(driver, 100)
#else:

### We are oppening a browser but not visible
display = Display(visible=0, size=(800, 800))
display.start()

# read the txt file with the search parameters
# print('--Read query')
# params = open(r"/home/chrysoula/google_photos/params.txt", "r")
# parameters = params.read().split(',')
print('- The search parameters are: ', ','.join(parameters))

### Google url for image searches
basic_url = 'https://www.google.gr/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjT-Kj668vbAhUD_iwKHSlVAKwQ_AUICigB&biw=1280&bih=615'
parameters = ['sun']
### For every search term...
for param in parameters:
    print('-'*20)
    print('-- Searching google for parameter: ', param)
    print('-'*20)
    ### include search term in google url
    url = basic_url.format(str(param))
    print('--- Google url: ', url)
    
    print('-- initiate driver')
    ### Run chromedriver for selenium to start the scraping process
    # https://stackoverflow.com/questions/22476112/using-chromedriver-with-selenium-python-ubuntu
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    print('-- waiting')
    ### Give time for selenium to start
    wait = WebDriverWait(driver, 100)
    
    ### Perform get request for the google url
    driver.get(str(url))
    try:
        # sometimes google opens a bot page first
        # wait until class name 'med'. It waits up to 100 seconds
        wait.until(
            lambda driver: driver.find_elements(By.CLASS_NAME, 'med'))
    except:
        continue

    time.sleep(2)

    ### Scroll down to reveal more pictures
    for scroll in range(10):
        driver.execute_script("window.scrollBy(0,1000000)")
        time.sleep(0.2)
    time.sleep(0.5)

    # list to store the image urls after scrapping the google results
    img_urls = []

    # find all photos
    ### This is where in the html from google we can find the images
    images = driver.find_elements_by_xpath("//div[@class='rg_meta notranslate']")
    print('---- Number of pictures found: ', len(images))
    for image in images:
        ### get image information from every html code chunk. the information i am retrieving is the image url
        img_url = json.loads(image.get_attribute("innerHTML"))["ou"]
        ### Create an id for the image url we retrieved, this is the name i am going to give to the image
        img_id = str(uuid.uuid4())
        ### store image url and image name in a dictionary
        img_dict = {'img_url':img_url, 'img_id':img_id}
        ### append the above information for every loop i.e. for every image
        img_urls.append(img_dict)
    
    ### Close selenium
    ### We only use selenium to trieve the information from google image search. once we have the 
    ### image urls we just do a simple get request. No need fro selenium driver.
    driver.quit()
        
    # create dir if it does not exist
    ### For every search term create the respective path file in order to store the image after
    if not os.path.exists('/home/chrysoula/google_photos/pictures/' + param):
        print('---- creating directory: /home/chrysoula/google_photos/pictures' +'/'+ param)
        os.makedirs('/home/chrysoula/google_photos/pictures' +'/'+ param)

    print('---- Downloading pictures')
    # download the pictures
    ### for every image url we download the image
    for dl, img in enumerate(img_urls):
        print('----- Download ', dl, ' of ', len(img_urls))
        try:
            ### Perform a get request for the image, wait 10 seconds for a responce
            response = requests.get(img['img_url'], headers=headers, timeout=10)
            time.sleep(0.1)
            if response.status_code == 200:
                ### if we get 200 response from get request store the image in the path i crated
                with open(r'/home/chrysoula/google_photos/pictures/'+ param + '/' + str(img['img_id'])+ '.jpg', 'wb') as f:
                    f.write(response.content)
        except:
            ### if we dont get a 200 response go to the next image
            print('---- Could not download image: ' + img['img_url'])
            pass

print('End of process')