def find_places(nb,intr):
    places = []
    categories = {
        "Historical": ["Central Museum of Nagpur nagpur", "Divekar Puratan Vastu Sangrahalay nagpur", "Raman Science Centre & Planetarium, Raman Science Centre, Subhash Rd, Empress City, Nagpur", "Zonal Anthropological Museum nagpur",  "Deekshabhoomi nagpur", "Dragon Palace Temple Nagpur", "Suraburdi nagpur", "Ramtek Fort nagpur", "Sitabuldi Fort nagpur", "Narrow Gauge Rail Museum nagpur", "Gandhi Sagar Lake nagpur", "Ambagad Fort, FJ5W+CV2, Ambagad,tah.Tumsar,Dist.Bhandara", "Adasa nagpur"],
        "Religious": ["Shri Ganesh Temple Tekdi nagpur", "Sai Baba Mandir 437C+83G, Wardha Rd, Near Sai Mandir, Sawarkar Nagar, Vivekanand Nagar, Nagpur, Maharashtra 440015",  "Swaminarayan Temple nagpur", "St. Francis De Sales Cathedral nagpur", "Masjid Markaz nagpur", "Adasa Ganpati Temple nagpur", "Sri Poddareshwar Ram Mandir nagpur", "Hazrat Baba Tajuddin Dargah nagpur", "Telankhedi Hanuman Temple nagpur", "All Saint's Cathedral Church nagpur", "St. Thomas Church nagpur", "Ramtek Temple nagpur", "St. Anthony Church nagpur"],
        "Wildlife": ["Futala Lake nagpur", "Maharajbagh Zoo nagpur", "Gorewada Lake nagpur", "Seminary Hill nagpur", "Ambazari Lake nagpur", "Khindsi Lake nagpur", "Satpuda Botanical Garden, 524Q+WWM, Vayusena Nagar, Nagpur", "Karhandla Gate Umred Karhandla Wildlife Sanctuary, RCW2+676, Nagpur",  "Nagzira Wildlife Sanctuary nagpur", "Nawegaon Nagzira Tiger Reserve, X5G8+63F, Nishani"],
        "Adventure": ["Fun N Food Village Nagpur", "Pench Tiger Reserve Nagpur", "Official-Dwarka Water Park Nagpur", "Ramdham nagpur", "Waki Woods nagpur", "Khekranala nagpur", "CAC Adventure Camp Ramtek", "Meghdhoot Agri And Adventure Park", "Waki, Waghville Elite Aqua Park", "Tadoba-Andhari National Park"],
        "Shopping": ["VR Mall Nagpur", "Glocal Square Mall Nagpur", "Eternity Mall nagpur", "Itwri Market 5436+G3C, Teen Nal Chowk, Itwari, Nagpur, Maharashtra 440002", "Shree Shivam Shopping Complex nagpur", "Reliance Centro nagpur", "Apna Bazar nagpur", "Meena Bazar nagpur", "Sadar Bazaar nagpur", "Empress Mall nagpur", "Jaswant Tuli Mall nagpur"]
    }
    
    if(len(intr)==1):
        if(intr[0]==nb):
            #print("10 places of same intrest")
            places.append(categories[nb][:10])
        else:
            #print("7:3 Ratio")
            places.append(categories[nb][:3]+categories[intr[0]][:7])

    elif(len(intr)==2):
            if(intr[0]!=nb and intr[1]!=nb):
                 places.append(categories[intr[0]][:4]+categories[intr[1]][:3]+categories[nb][:3])
            elif(intr[0]==nb):
                 places.append(categories[intr[0]][:6]+categories[intr[1]][:4])
            elif(intr[1]==nb):
                 places.append(categories[intr[0]][:4]+categories[intr[1]][:6])

    return places

#tsp('Historical',['Shopping'])

    # nb = 'Place1'
    # intr = 'Place2' or 'Place2 and 3'