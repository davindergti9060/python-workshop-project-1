Que. Web scraping project
INPUT:
#importing modules
# importing requests module , request for getting page content
from pip._vendor import requests
# importing Beautifulsoup module and it is responsible for passing of html code
# (can't find package so need to be installed from vs terminal pip install beautifulsoup4)
from bs4 import BeautifulSoup 
# importing pandas module
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-chandigarh//?page="
page_num_Max = 3
scraped_info_list = []

for page_num in range(1, page_num_Max):
    url = oyo_url + str(page_num)
    print("Get Request for:" + url)
    #get to get info from url
    req = requests.get(url)
    #getting content
    content =  req.content

    soup = BeautifulSoup (content, "html.parser")

    #identifying listingcard
    all_hotels = soup.find_all("div", {"class": "hotellCardListing"})
    
    #creating loop
    for hotel in all_hotels:
        hotel_dict = [] #dictionary to store all values of hotel(name, address, price, rating)
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text
        # exception handling try .... except block for rating if there is no rating
        try :
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            pass
        
        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})
        
        amenitiies_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenitiies_list.append(amenity.find("span", {"class": "d-body-smd-textEllipsis"}).text.strip())
        
        hotel_dict["amenities"] = ', '.join(amenitiies_list[:-1])
        
        scraped_info_list.append(hotel_dict)
        
    # print (hotel_name, hotel_address, hotel_price, hotel_rating, amenitiies_list)
    
    dataFrame = pandas.FataFrame(scraped_info_list) 
    dataFrame.to_csv("oyo.csv")
