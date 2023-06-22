from selenium import webdriver
import winsound
from selenium.webdriver.common.keys import Keys
from time import sleep

#source = input("enter the current location: ")

def src_to_dis(source, all_places):
    distance_matrix = [['no place', 'Central Museum of Nagpur nagpur', 'Divekar Puratan Vastu Sangrahalay nagpur', 'Raman Science Centre & Planetarium, Raman Science Centre, Subhash Rd, Empress City, Nagpur', 'Zonal Anthropological Museum nagpur', 'Deekshabhoomi nagpur', 'Dragon Palace Temple Nagpur', 'Suraburdi nagpur', 'Ramtek Fort nagpur', 'Sitabuldi Fort nagpur', 'Narrow Gauge Rail Museum nagpur', 'Gandhi Sagar Lake nagpur', 'Ambagad Fort, FJ5W+CV2, Ambagad,tah.Tumsar,Dist.Bhandara', 'Adasa nagpur', 'Shri Ganesh Temple Tekdi nagpur', 'Sai Baba Mandir 437C+83G, Wardha Rd, Near Sai Mandir, Sawarkar Nagar, Vivekanand Nagar, Nagpur, Maharashtra 440015', 'Swaminarayan Temple nagpur', 'St. Francis De Sales Cathedral nagpur', 'Masjid Markaz nagpur', 'Adasa Ganpati Temple nagpur', 'Sri Poddareshwar Ram Mandir nagpur', 'Hazrat Baba Tajuddin Dargah nagpur', 'Telankhedi Hanuman Temple nagpur', "All Saint's Cathedral Church nagpur", 'St. Thomas Church nagpur', 'Ramtek Temple nagpur', 'St. Anthony Church nagpur', 'Futala Lake nagpur', 'Maharajbagh Zoo nagpur', 'Gorewada Lake nagpur', 'Seminary Hill nagpur', 'Ambazari Lake nagpur', 'Khindsi Lake nagpur', 'Satpuda Botanical Garden, 524Q+WWM, Vayusena Nagar, Nagpur', 'Karhandla Gate Umred Karhandla Wildlife Sanctuary, RCW2+676, Nagpur', 'Nagzira Wildlife Sanctuary nagpur', 'Nawegaon Nagzira Tiger Reserve, X5G8+63F, Nishani', 'Fun N Food Village Nagpur', 'Pench Tiger Reserve Nagpur', 'Official-Dwarka Water Park Nagpur', 'Ramdham nagpur', 'Waki Woods nagpur', 'Khekranala nagpur', 'CAC Adventure Camp Ramtek', 'Meghdhoot Agri And Adventure Park', 'Waki, Waghville Elite Aqua Park', 'Tadoba-Andhari National Park', 'VR Mall Nagpur', 'Glocal Square Mall Nagpur', 'Eternity Mall nagpur', 'Itwri Market 5436+G3C, Teen Nal Chowk, Itwari, Nagpur, Maharashtra 440002', 'Shree Shivam Shopping Complex nagpur', 'Reliance Centro nagpur', 'Apna Bazar nagpur', 'Meena Bazar nagpur', 'Sadar Bazaar nagpur', 'Empress Mall nagpur', 'Jaswant Tuli Mall nagpur'],
    ['Dr Babasaheb Ambedkar International Airport', 8.7, 6.9, 10.1, 12.9, 6.4, 26.6, 20.9, 58.0, 9.5, 11.5, 10.0, 117.0, 47.1, 9.2, 4.2, 13.9, 10.0, 13.3, 47.0, 10.8, 10.2, 12.4, 9.7, 10.7, 58.0, 6.8, 12.6, 9.6, 16.1, 12.5, 8.2, 59.5, 14.8, 58.2, 11.7, 152.0, 40.1, 86.1, 43.1, 50.1, 41.3, 62.7, 58.4, 63.3, 45.7, 107.0, 8.4, 7.9, 7.7, 12.1, 8.0, 7.3, 8.0, 8.5, 8.5, 10.0, 13.1],
    ['532Q+W7 Nagpur, Maharashtra', 2.2, 8.4, 2.0, 6.3, 4.8, 19.4, 20.5, 50.9, 2.9, 4.3, 1.9, 110.0, 40.5, 1.1, 5.6, 7.9, 2.9, 6.7, 40.5, 3.6, 6.9, 5.8, 3.1, 4.0, 50.9, 5.0, 6.4, 3.1, 9.5, 5.9, 7.6, 52.4, 9.2, 55.3, 3.7, 145.0, 39.8, 79.0, 36.6, 42.9, 34.7, 56.1, 51.3, 56.1, 42.7, 104.0, 3.4, 2.1, 2.5, 4.1, 2.1, 3.7, 2.1, 1.9, 4.2, 1.8, 5.9]]


    if source == "Dr Babasaheb Ambedkar International Airport":
        sou_to_places = []
        for i in all_places:
            index_of_i = distance_matrix[0].index(i)
            sou_to_places.append(distance_matrix[1][index_of_i])
        print(sou_to_places)

    elif source == "Nagpur Railway Station":
        sou_to_places = []
        for i in all_places:
            index_of_i = distance_matrix[0].index(i)
            sou_to_places.append(distance_matrix[2][index_of_i])
        print(sou_to_places)

    else:
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

        option_drive = driver.find_element("xpath",'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button/img')
        option_drive.click()

        k = len(all_places)
        left_count = 0
        left_list = []
        server_crash_count = 0
        counter = 0
        sou_to_places = []


        for i in all_places:

            if source == i:
                sou_to_places.append(0)
                counter += 1
                print(f"{counter}] {source}, {i}, {0}")
                continue

            try:
                start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')
                start.send_keys(source)
                start.send_keys(Keys.ENTER)

                end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')
                end.send_keys(i)
                end.send_keys(Keys.ENTER)
                sleep(3)

                try:
                    distance = driver.find_element("xpath", '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div')
                    dist = distance.text

                    if dist[-3:] == " km":
                        dist = dist[: -3]

                        sou_to_places.append(float(dist))
                        counter += 1
                        print(f"{counter}] {source}, {i}, {float(dist)}")

                        start.clear()
                        end.clear()

                    elif dist[-2:] == " m":
                        dist = dist[: -2]
                        dist_in_km = (float(dist))/1000

                        sou_to_places.append(float(dist_in_km))
                        counter += 1
                        print(f"{counter}] {source}, {i}, {float(dist_in_km)}")

                        start.clear()
                        end.clear()

                    else:
                        left = []
                        left.append(source)
                        left.append(i)
                        left_list.append(left)

                        sou_to_places.append(((i).upper()))

                        left_count += 1
                        print(f"left this one: {left_count}] {source}, {i}, {dist}")

                        start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')

                        end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')

                        start.clear()
                        end.clear()

                except:
                    same_place = driver.find_element("xpath", '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/jsl')
                    sleep(3)

                    sou_to_places.append(0)
                    counter += 1
                    print(f"{counter}] {source}, {i}, {0}")

                    start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')

                    end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')

                    start.clear()
                    end.clear()

            except:
                try:
                    try:
                        server_crash_count += 1
                        print(f"server crash count: {server_crash_count}")

                        start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')
                        start.send_keys(source)
                        start.send_keys(Keys.ENTER)

                        end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')
                        end.send_keys(i)
                        end.send_keys(Keys.ENTER)
                        sleep(3)

                        distance = driver.find_element("xpath",'//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div')
                        dist = distance.text

                        if dist[-3:] == " km":
                            dist = dist[: -3]

                            sou_to_places.append(float(dist))
                            counter += 1
                            print(f"{counter}] {source}, {i}, {float(dist)}")

                            start.clear()
                            end.clear()

                        elif dist[-2:] == " m":
                            dist = dist[: -2]
                            dist_in_km = (float(dist)) / 1000

                            sou_to_places.append(float(dist_in_km))
                            counter += 1
                            print(f"{counter}] {source}, {i}, {float(dist_in_km)}")

                            start.clear()
                            end.clear()

                        else:
                            left = []
                            left.append(source)
                            left.append(i)
                            left_list.append(left)

                            sou_to_places.append(((i).upper()))
                            
                            left_count += 1
                            print(f"left this one: {left_count}] {source}, {i}, {dist}")

                            start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')

                            end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')

                            start.clear()
                            end.clear()
                    except:
                        same_place = driver.find_element("xpath", '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/jsl')
                        sleep(3)

                        sou_to_places.append(0)
                        counter += 1
                        print(f"{counter}] {source}, {i}, {0}")

                        start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')

                        end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')

                        start.clear()
                        end.clear()

                except:
                    winsound.Beep(810, 250)
                    left_count += 1

                    left = []
                    left.append(source)
                    left.append(i)
                    left_list.append(left)

                    dist_for_left = float(input(f'Enter distance between {source} & {i}: '))
                    sou_to_places.append(dist_for_left)

                    start = driver.find_element("xpath", '//*[@id="sb_ifc50"]/input')

                    end = driver.find_element("xpath", '//*[@id="sb_ifc51"]/input')

                    start.clear()
                    end.clear()




        print(f"server crash count {server_crash_count}:")

        print(f"left count: {left_count}")
        print(f'left list: {left_list}')

        print("left lest in vertical form: ")
        for i in left_list:
            print(i)


        print(f'success count: {counter}')
        print(f'our distance matrix list: {sou_to_places}')

        #print("our distance matrix in vertical form: ")
        #for i in sou_to_places:
        #    print(i)


        driver.quit()

    return sou_to_places