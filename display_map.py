from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

def display(all_places):
    while True:
        try:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_argument(f'user-agent={user_agent}')
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(executable_path="C:/Users/Dell/Downloads/chromedriver.exe", options=options)
            driver.implicitly_wait(10)

            driver.get('https://www.google.com/maps/dir///@18.8154265,76.7747674,7z')
            # driver.maximize_window()
            # driver.minimize_window()

            option_drive = driver.find_element("xpath",'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button/img')
            option_drive.click()

            # all_places = ['Fun N Food Village Nagpur', 'Pench National Park', 'Official-Dwarka Water Park Nagpur', 'Ramdham nagpur', 'River Wood Resort, Unnamed Road, Chicholi', 'Khekranala nagpur', 'CAC Adventure Camp Ramtek', 'Meghdhoot Agri And Adventure Park', 'Waki, Waghville Elite Aqua Park', 'Tadoba-Andhari National Park']

            first = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')
            first.send_keys(all_places[0] + Keys.ENTER)

            second = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')
            second.send_keys(all_places[1] + Keys.ENTER)

            add_destination = driver.find_element("xpath", '//*[@id="omnibox-directions"]/div/div[3]/button/div[2]/span')

            for i in range(2, 10):
                add_destination.click()
                third = driver.find_element("xpath", f'//*[@id="sb_ifc5{i}"]/input')
                third.send_keys(all_places[i] + Keys.ENTER)

            sleep(4)
            colapse = driver.find_element("xpath", '//*[@id="QA0Szd"]/div/div/div[2]/button/img')
            colapse.click()
            sleep(4)
            break

        except:
            pass
    #filename = f"static/image_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    #Image.save(filename)
    driver.save_screenshot("ss.png")
    url = driver.current_url
    url_string = str(url)
    #print(f'your url: {url_string}')

    driver.quit()
    return url_string