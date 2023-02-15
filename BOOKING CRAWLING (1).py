#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import glob

def load_soup_object(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup


# In[11]:


def get_attribute(hotel_data, attrs):
    attribute_call = hotel_data.find(attrs=attrs)
    if attribute_call is not None:
        return attribute_call.get_text()
    else:
        return None





def scrap_town_country(town, state, country):
    pages = list()
    
    print(f"scraping {town} {country}")
    name = list()
    city = list()
    rating = list()
    rev_num = list()
    price = list()
    room_kind = list()
    pool = list()
    free_cancle = list()
    air_con = list()
    balcony = list()
    parking = list()
    view = list()
    disabledAccess=list()
    distance2center = list()
    free_style_description = list()
    staf_rat=list()
    wifi=list()
    distance2beach=list()
    food=list()
    gym=list()
    spa=list()
    propertyType=list()
    
    town_str = '+'.join(town.split())
    state_str = '+'.join(state.split()) if state is not None else ""  # for USA
    country_str = '+'.join(country.split())
    url = f"https://www.booking.com/searchresults.en-us.html?ss={town_str}{('%2C+ ' + state_str) if state is not None else ''}%2C+{country_str}" +           "&checkin=2023-03-01&checkout=2023-03-02&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204&order=price&offset=0"


    soup = load_soup_object(url)###open the url 
    num_hotels_so_far = 0
    done = False

    name2pages = {}

    i = 1

    
    while not done:
        url = url[:url.find("offset=")] + "offset=" + str(num_hotels_so_far)###loop to the next url
        print(url)
        loaded = False ###start with false value and become true if url load is good.
        while not loaded:
            try:
                soup = load_soup_object(url)
                loaded = True
            except requests.exceptions.SSLError:### if didnt work wait 0.1 sec before try again to avoid network errors.
                time.sleep(0.1)
        print(f"{i}th url loaded")###print the number of the URL

        testid = soup.findAll("div", attrs={"data-testid": "property-card"})###start the crwaling in the page
        num_hotels_in_this_page = len(testid)
        num_hotels_so_far += num_hotels_in_this_page
        print(f"page {i}, {len(testid)} hotels in this page")###print how much hotels there are in this page
        num_hotels = 0
        
        for hotel in testid:
            name1 = get_attribute(hotel, {"data-testid": "title"})
            if name1 is None:
                continue
            if name1 not in name2pages:
                name2pages[name1] = [i]#dictionary where the keys are the hotel names and the values are lists of page numbers.
            else:
                name2pages[name1].append(i)
            name.append(name1)#use to store the names of all hotels processed so far.
            #The dictionary is used to keep track of which page each hotel was found on.

            hotel_url = hotel.find(attrs={"data-testid": "title-link"}, href=True).attrs["href"]
            #used to extract the value of its href attribute, which represents the URL.
            hotel_url = hotel_url[:hotel_url.find(".html") + 5]
            #change the value of hotel_url by removing any text that appears after ".html".
            
            print(name1)
            #
            loaded = False
            while not loaded:
                try:
                    hotel_soup = load_soup_object(hotel_url)###upload the hotel page URL
                    loaded = True
                except requests.exceptions.SSLError:
                    time.sleep(0.1)
            
#############################
            
            staf_rat1= hotel_soup.find("div", attrs={"class": "ee746850b6 b8eef6afe1"})
            if staf_rat1:
                staf_rat.append(staf_rat1.get_text())
            else:
                staf_rat.append("NAN")

            
            wifi1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_107"})
            if wifi1:
                wifi.append(wifi1.get_text())
            else:
                wifi.append("NAN")

            pool1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_301"})
            if pool1:
                pool.append(pool1.get_text())
            else:
                pool.append("NAN")
                
                
            food1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_3"})#Restaurant
            if food1:
                food.append(food1.get_text())
            else:
                food.append("NAN")
                
                
            gym1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_11"})
            if gym1:
                gym.append(gym1.get_text())
            else:
                gym.append("NAN")
                
                
            spa1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_54"})
            if spa1:
                spa.append(spa1.get_text())
            else:
                spa.append("NAN")
                
                
            propertyType1=hotel_soup.find("span", attrs={"data-testid": "property-type-badge"})
            if propertyType1:
                propertyType.append(propertyType1.get_text())
            else:
                propertyType.append("NAN")
                
            air_con1=hotel_soup.find("div", attrs={"data-testid": "ROOM_11"})
            if air_con1:
                air_con.append(air_con1.get_text())
            else:
                air_con.append("NAN")
                
            parking1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_2"})
            if parking1:
                parking.append(parking1.get_text())
            else:
                parking.append("NAN") 
                
                
            disabledAccess1=hotel_soup.find("div", attrs={"data-testid": "PROPERTY_25"})
            if disabledAccess1:
                disabledAccess.append(disabledAccess1.get_text())
            else:
                disabledAccess.append("NAN") 
                
                
            view1=hotel_soup.find("div", attrs={"data-testid": "ROOM_81"})
            if view1:
                view.append(view1.get_text())
            else:
                view.append("NAN") 
                
                
                
            balcony1=hotel_soup.find("div", attrs={"data-testid": "ROOM_17"})
            if balcony1:
                balcony.append(balcony1.get_text())
            else:
                balcony.append("NAN")  
            
##############################

            city1 = get_attribute(hotel, {"data-testid": "address"})
            city.append(city1)

            rating1 = get_attribute(hotel, {"class": "b5cd09854e d10a6220b4"})
            rating.append(rating1)

            room_kind1 = get_attribute(hotel, {"class": "df597226dd"})
            room_kind.append(room_kind1)

            price1 = get_attribute(hotel, {"data-testid": "price-and-discounted-price"})
            price.append(price1)


            rev_num1 = get_attribute(hotel, {"class": "d8eab2cf7f c90c0a70d3 db63693c62"})
            rev_num.append(rev_num1)

            free_cancle1 = get_attribute(hotel, {"class": "d506630cf3"})
            if free_cancle1:
                free_cancle.append("Free Cancle")
            else:
                free_cancle.append("NAN")

            
            distance2center1 = get_attribute(hotel, {"data-testid": "distance"})
            distance2center.append(distance2center1)
            
            distance2beach1 = get_attribute(hotel, {"class": "acb0d5ead1"})
            if (distance2beach1=="Beachfront"):
                distance2beach.append("0")
            else:
                distance2beach.append(distance2beach1)
            
            #################################################################
            num_hotels += 1
           # if num_hotels == 3:
           #     done = True
            #    break

        print(num_hotels_so_far)
        if num_hotels_in_this_page < 25:
            done = True
        i += 1
        #if i==2:
            #done = True
    #end_time = time.time()
    #elapsed_time = end_time - start_time
    
    df = pd.DataFrame({"Property Name": name,
                       "City": city,
                       "Price": price,
                       "Property Type":propertyType,
                       "Rating": rating, 
                       "Review Number": rev_num,
                       "Room Kind": room_kind,
                       "Staff Rating":staf_rat, 
                       "Free Cancle": free_cancle,
                       "View":view,
                       "Balcony":balcony,
                       "Pool":pool,
                       "Parking":parking,
                       "Restaurant":food,
                       "GYM":gym,
                       "Air Condition":air_con,
                       "Disabled Access":disabledAccess,
                       "Distance To Center": distance2center,
                       "Distance To Beach":distance2beach,
                       "WiFi":wifi,
                        "SPA":spa})
 
    #df_unique_rows = df.drop_duplicates()#removes any duplicate rows
    #duplicated_boolean = df.duplicated(keep=False)
    #duplicated_rows = df[duplicated_boolean]
    #duplicated_hotel_names_boolean = df_unique_rows.duplicated(subset=["Property Name"], keep=False)
    #duplicated_hotel_names = df_unique_rows[duplicated_hotel_names_boolean]
    #hotel_names_that_appear_more_than_once = {name: pages for name, pages in name2pages.items() if len(pages) > 1}

    df.to_csv(f'{town}_{country}.csv')

scrap_town_country("new york", None, "usa")
scrap_town_country("Houston", None, "usa")
scrap_town_country("Los Angeles", None, "usa")
scrap_town_country("Orlando", None, "usa")
scrap_town_country("San Antonio", None, "usa")
scrap_town_country("Atlanta", None, "usa")
#scrap_town_country("New Orleans", None, "usa")
#scrap_town_country("San Diego", None, "usa")
#scrap_town_country("Austin", None, "usa")
#scrap_town_country("Miami", None, "usa")
#scrap_town_country("Las Vegas", None, "usa")
#scrap_town_country("Chicago", None, "usa")


New_York = pd.read_csv("new york_usa.csv")
Houston = pd.read_csv("Houston_usa.csv")
Los_Angeles = pd.read_csv("Los Angeles_usa.csv")
Orlando = pd.read_csv("Orlando_usa.csv")
San_Antonio = pd.read_csv("San Antonio_usa.csv")
Atlanta = pd.read_csv("Atlanta_usa.csv")
#New_Orleans = pd.read_csv("New Orleans_usa.csv")
#SanDiego = pd.read_csv("San Diego_usa.csv")
#Austin = pd.read_csv("Austin_usa.csv")
#Miami = pd.read_csv("Miami_usa.csv")
#Las_Vegas = pd.read_csv("Las Vegas_usa.csv")
#Chicago = pd.read_csv("Chicago_usa.csv")


all = pd.concat((New_York, Houston, Los_Angeles,Orlando,San_Antonio,Atlanta))
#,New_Orleans,SanDiego,Austin,Miami,Las_Vegas,Chicago
x=0


# In[12]:


all


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




