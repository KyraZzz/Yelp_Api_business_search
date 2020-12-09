import json

data = {"rest_info": [
    {'id': 'ij3rkfAPdHwpiW7Ue9EBYw',
     'alias': 'pint-shop-cambridge',
     'name': 'Pint Shop',
     'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/Qy7N_hwdm-rXT8tRr-HrBQ/o.jpg',
     'is_closed': False,
     'url': 'https://www.yelp.com/biz/pint-shop-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ',
     'review_count': 59,
     'categories': [{'alias': 'british', 'title': 'British'}],
     'rating': 4.5,
     'coordinates': {'latitude': 52.2041657823304, 'longitude': 0.118927448689301},
     'transactions': [],
     'price': '££',
     'location': {'address1': '10 Peas Hill', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3PN', 'country': 'GB', 'state': 'CAM', 'display_address': ['10 Peas Hill', 'Cambridge CB2 3PN', 'United Kingdom']},
     'phone': '+441223352293',
     'display_phone': '+44 1223 352293',
     'distance': 266.83721254144325},
    {'id': '-r_31_vEuq3hUUD4ZjnPxA', 'alias': 'noodles-plus-cambridge', 'name': 'Noodles Plus', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/XJYOUeXVmm_K6JB8IQeX-w/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/noodles-plus-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 14, 'categories': [{'alias': 'chinese', 'title': 'Chinese'}], 'rating': 5.0, 'coordinates': {'latitude': 52.201247, 'longitude': 0.13366}, 'transactions': [], 'price': '£', 'location': {'address1': '24a Mill Road', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB1 2AD', 'country': 'GB', 'state': 'CAM', 'display_address': ['24a Mill Road', 'Cambridge CB1 2AD', 'United Kingdom']}, 'phone': '+441223362185', 'display_phone': '+44 1223 362185', 'distance': 1326.1869602662482}, {'id': 'yzBYyndSQ3RI6Hci2F9pRQ', 'alias': 'the-ivy-cambridge-brasserie-cambridge', 'name': 'The Ivy Cambridge Brasserie', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/9daDsE_Aq-AtJnDDPruBSQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-ivy-cambridge-brasserie-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 12, 'categories': [{'alias': 'british', 'title': 'British'}], 'rating': 4.5, 'coordinates': {'latitude': 52.2069714284192, 'longitude': 0.118247921026355}, 'transactions': [], 'location': {'address1': '16 Trinity Street', 'address2': 'City Centre', 'address3': None, 'city': 'Cambridge', 'zip_code': 'CB2 1TB', 'country': 'GB', 'state': 'CAM', 'display_address': ['16 Trinity Street', 'City Centre', 'Cambridge CB2 1TB', 'United Kingdom']}, 'phone': '+441223344044', 'display_phone': '+44 1223 344044', 'distance': 376.2612450815203}, {'id': 'cow69pmBjch97sqbkQl6Cw', 'alias': 'fitzbillies-cambridge-3', 'name': 'Fitzbillies', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/Xb4M6ZY1X-9DKe5g0yWY5g/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/fitzbillies-cambridge-3?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 57, 'categories': [{'alias': 'cakeshop', 'title': 'Patisserie/Cake Shop'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}, {'alias': 'sandwiches', 'title': 'Sandwiches'}], 'rating': 4.0, 'coordinates': {'latitude': 52.202085, 'longitude': 0.118138}, 'transactions': [], 'price': '££', 'location': {'address1': '52 Trumpington Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 1RG', 'country': 'GB', 'state': 'CAM', 'display_address': ['52 Trumpington Street', 'Cambridge CB2 1RG', 'United Kingdom']}, 'phone': '+441223352500', 'display_phone': '+44 1223 352500', 'distance': 319.6715287401551}, {'id': 'OZI4rK9s0xTwg2PdTRgmcw', 'alias': 'aromi-cambridge-cambridge', 'name': 'Aromi - Cambridge', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/eS-F_RSo1UyOumExtszsGA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/aromi-cambridge-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 31, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'cafes', 'title': 'Cafes'}, {'alias': 'delis', 'title': 'Delis'}], 'rating': 4.0, 'coordinates': {'latitude': 52.2042405, 'longitude': 0.1187084}, 'transactions': [], 'price': '£', 'location': {'address1': "Bene't Street Eatery", 'address2': "1 Bene't Street", 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3QN', 'country': 'GB', 'state': 'CAM', 'display_address': ["Bene't Street Eatery", "1 Bene't Street", 'Cambridge CB2 3QN', 'United Kingdom']}, 'phone': '+441223300117', 'display_phone': '+44 1223 300117', 'distance': 252.06456860050903}, {'id': 'WyvzcS2ClQheiIYbT5Oxpg', 'alias': 'the-trailer-of-life-cambridge', 'name': 'The Trailer of Life', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/l_YSv4axiGSJPx6T2DH8vw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-trailer-of-life-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 13, 'categories': [
        {'alias': 'hotdogs', 'title': 'Fast Food'}], 'rating': 4.5, 'coordinates': {'latitude': 52.2056550386056, 'longitude': 0.1192065231522}, 'transactions': [], 'price': '£', 'location': {'address1': '16 Market Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3NR', 'country': 'GB', 'state': 'BDF', 'display_address': ['16 Market Street', 'Cambridge CB2 3NR', 'United Kingdom']}, 'phone': '', 'display_phone': '', 'distance': 326.79804691974}, {'id': 'tiRG1br_mSQuhDgzPMYKHA', 'alias': 'millworks-cambridge', 'name': 'MillWorks', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/_al1e9IFTisDtZRNTp9v1g/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/millworks-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 15, 'categories': [{'alias': 'brasseries', 'title': 'Brasseries'}, {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'}, {'alias': 'steak', 'title': 'Steakhouses'}], 'rating': 4.5, 'coordinates': {'latitude': 52.199129, 'longitude': 0.114091}, 'transactions': [], 'price': '££', 'location': {'address1': 'The Watermill', 'address2': 'Newnham Road', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB3 9EY', 'country': 'GB', 'state': 'CAM', 'display_address': ['The Watermill', 'Newnham Road', 'Cambridge CB3 9EY', 'United Kingdom']}, 'phone': '+441223367507', 'display_phone': '+44 1223 367507', 'distance': 570.5774619248702}, {'id': '24kqzLWHc_nHAQeeNeopbw', 'alias': 'bibimbap-house-cambridge', 'name': 'Bibimbap House', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/OC5JmMVBN7_7E1fMZoWa-Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/bibimbap-house-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 18, 'categories': [{'alias': 'korean', 'title': 'Korean'}], 'rating': 4.5, 'coordinates': {'latitude': 52.2004433, 'longitude': 0.1358265}, 'transactions': [], 'price': '££', 'location': {'address1': '60 Mill Road', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB1 2AS', 'country': 'GB', 'state': 'CAM', 'display_address': ['60 Mill Road', 'Cambridge CB1 2AS', 'United Kingdom']}, 'phone': '+441223506800', 'display_phone': '+44 1223 506800', 'distance': 1470.1921975831447}, {'id': 'hitRPtegs7muUk__7mq74w', 'alias': 'nandos-cambridge-2', 'name': "Nando's", 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/PQ2ZKXEXph4N3cEyDgb-Mg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/nandos-cambridge-2?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 22, 'categories': [{'alias': 'hotdogs', 'title': 'Fast Food'}, {'alias': 'chickenshop', 'title': 'Chicken Shop'}], 'rating': 4.0, 'coordinates': {'latitude': 52.2033034, 'longitude': 0.1235108}, 'transactions': [], 'price': '££', 'location': {'address1': '33-34 st Andrews st', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3AR', 'country': 'GB', 'state': 'CAM', 'display_address': ['33-34 st Andrews st', 'Cambridge CB2 3AR', 'United Kingdom']}, 'phone': '+441223327908', 'display_phone': '+44 1223 327908', 'distance': 588.1626798930199}, {'id': 'CHRzxe_cY815qWiySqWCOg', 'alias': 'ta-bouche-cambridge', 'name': 'Ta Bouche', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/mTvaplpcNNajh-TnmBSIwA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/ta-bouche-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 14, 'categories': [{'alias': 'cafes', 'title': 'Cafes'}, {'alias': 'cocktailbars', 'title': 'Cocktail Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 52.20638, 'longitude': 0.12}, 'transactions': [], 'price': '££', 'location': {'address1': '10-15 Market Passage', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3PF', 'country': 'GB', 'state': 'CAM', 'display_address': ['10-15 Market Passage', 'Cambridge CB2 3PF', 'United Kingdom']}, 'phone': '+441223462277', 'display_phone': '+44 1223 462277', 'distance': 420.48372039328467},
    {'id': 'jU_ysQv84B6T7HB3ddCfmA', 'alias': 'pho-cambridge-cambridge', 'name': 'Pho - Cambridge', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/9CaBK8gOQln3dQt0RrqtEg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/pho-cambridge-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 29, 'categories': [{'alias': 'vietnamese', 'title': 'Vietnamese'}], 'rating': 3.5, 'coordinates': {'latitude': 52.204302, 'longitude': 0.119361}, 'transactions': [], 'price': '£', 'location': {'address1': '1 Wheeler Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3QB', 'country': 'GB', 'state': 'CAM', 'display_address': ['1 Wheeler Street', 'Cambridge CB2 3QB', 'United Kingdom']}, 'phone': '+441223350436', 'display_phone': '+44 1223 350436', 'distance': 297.3315678744828}, {'id': '9PbTzf0CQoehUhLHWeOujg', 'alias': 'butch-annies-cambridge', 'name': 'Butch Annies', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/TyjoZCvGd-Ca1KjenFkEuA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/butch-annies-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 36, 'categories': [{'alias': 'burgers', 'title': 'Burgers'}], 'rating': 4.5, 'coordinates': {'latitude': 52.2058904269578, 'longitude': 0.119822429160075}, 'transactions': [], 'price': '££', 'location': {'address1': '24 Market Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3PA', 'country': 'GB', 'state': 'CAM', 'display_address': ['24 Market Street', 'Cambridge CB2 3PA', 'United Kingdom']}, 'phone': '+441223361792', 'display_phone': '+44 1223 361792', 'distance': 376.2045325338557}, {'id': 'iX8o07wSfvhe1laJhUzsFA', 'alias': 'the-cambridge-chop-house-cambridge', 'name': 'The Cambridge Chop House', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/X0f8eIRng6edsp4CATMZYA/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/the-cambridge-chop-house-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 48, 'categories': [{'alias': 'steak', 'title': 'Steakhouses'}, {'alias': 'british', 'title': 'British'}], 'rating': 4.0, 'coordinates': {'latitude': 52.204257, 'longitude': 0.117823}, 'transactions': [], 'price': '£££', 'location': {'address1': '1 Kings Parade', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 1SJ', 'country': 'GB', 'state': 'CAM', 'display_address': ['1 Kings Parade', 'Cambridge CB2 1SJ', 'United Kingdom']}, 'phone': '+441223359506', 'display_phone': '+44 1223 359506', 'distance': 191.1098330912806}, {'id': 'ZRPcZ6XPY2WqcPyUUVemWA', 'alias': 'gardenia-take-away-cambridge', 'name': 'Gardenia Take Away', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/BKygGG5k72tegc_qku8xzg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/gardenia-take-away-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 15, 'categories': [{'alias': 'hotdogs', 'title': 'Fast Food'}, {'alias': 'greek', 'title': 'Greek'}, {'alias': 'mediterranean', 'title': 'Mediterranean'}], 'rating': 4.0, 'coordinates': {'latitude': 52.2063973, 'longitude': 0.1185894}, 'transactions': [], 'price': '£', 'location': {'address1': '2 Rose Cresent', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3LL', 'country': 'GB', 'state': 'CAM', 'display_address': ['2 Rose Cresent', 'Cambridge CB2 3LL', 'United Kingdom']}, 'phone': '+441223356354', 'display_phone': '+44 1223 356354', 'distance': 342.5429283832533}, {'id': 'NwuypxAN5FW3sfa7BW-lZg', 'alias': 'little-seoul-cambridge', 'name': 'Little Seoul', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/ET710XvXBgRVIvhG5UoC0Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/little-seoul-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 24, 'categories': [{'alias': 'korean', 'title': 'Korean'}], 'rating': 4.0, 'coordinates': {'latitude': 52.1995392, 'longitude': 0.1268765}, 'transactions': [], 'price': '££', 'location': {'address1': '108 Regent Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 1DP', 'country': 'GB', 'state': 'CAM', 'display_address': ['108 Regent Street', 'Cambridge CB2 1DP', 'United Kingdom']}, 'phone': '+441223308681', 'display_phone': '+44 1223 308681', 'distance': 975.0074147551042}, {
        'id': 'dBaqUPOwO_BWlkIev99aqw', 'alias': 'bread-and-meat-cambridge', 'name': 'Bread and Meat', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/hf7brwYZeZR2BBuoPiUB3g/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/bread-and-meat-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 15, 'categories': [{'alias': 'sandwiches', 'title': 'Sandwiches'}, {'alias': 'coffee', 'title': 'Coffee & Tea'}, {'alias': 'beerbar', 'title': 'Beer Bar'}], 'rating': 4.5, 'coordinates': {'latitude': 52.2039068878316, 'longitude': 0.118007876572928}, 'transactions': [], 'price': '££', 'location': {'address1': '4 Benet Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3QN', 'country': 'GB', 'state': 'CAM', 'display_address': ['4 Benet Street', 'Cambridge CB2 3QN', 'United Kingdom']}, 'phone': '+447918083057', 'display_phone': '+44 7918 083057', 'distance': 207.2014585667535}, {'id': 'CTB_GboBV3GBf6M1iQOoDg', 'alias': 'honest-burgers-cambridge', 'name': 'Honest Burgers Cambridge', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/3zKPdECxWXcXUFiARbN8kg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/honest-burgers-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 12, 'categories': [{'alias': 'burgers', 'title': 'Burgers'}, {'alias': 'wine_bars', 'title': 'Wine Bars'}, {'alias': 'beerbar', 'title': 'Beer Bar'}], 'rating': 4.5, 'coordinates': {'latitude': 52.2045158407787, 'longitude': 0.119860880076885}, 'transactions': [], 'location': {'address1': '1-6 Corn Exchange Street', 'address2': '', 'address3': None, 'city': 'Cambridge', 'zip_code': 'CB2 3QF', 'country': 'GB', 'state': 'CAM', 'display_address': ['1-6 Corn Exchange Street', 'Cambridge CB2 3QF', 'United Kingdom']}, 'phone': '+441223788240', 'display_phone': '+44 1223 788240', 'distance': 331.8871785506059}, {'id': 'qa8nZjslEFeyukPu-85irQ', 'alias': 'indigo-coffee-house-cambridge', 'name': 'Indigo Coffee House', 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/g7Vol_hpROI4Xv2YQpAwVQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/indigo-coffee-house-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 29, 'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}, {'alias': 'cafes', 'title': 'Cafes'}], 'rating': 4.0, 'coordinates': {'latitude': 52.2044251, 'longitude': 0.117985}, 'transactions': [], 'price': '£', 'location': {'address1': "8 Saint Edward's Passage", 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 3PJ', 'country': 'GB', 'state': 'CAM', 'display_address': ["8 Saint Edward's Passage", 'Cambridge CB2 3PJ', 'United Kingdom']}, 'phone': '+441223368753', 'display_phone': '+44 1223 368753', 'distance': 204.34335156409782}, {'id': 'oCVVAlWnr4D6sIrAaz68YQ', 'alias': 'lagona-cambridge', 'name': 'Lagona', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/4hOS9sNtlXYMk1N4u2LMHg/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/lagona-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 4, 'categories': [{'alias': 'lebanese', 'title': 'Lebanese'}, {'alias': 'hookah_bars', 'title': 'Hookah Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 52.201380757579, 'longitude': 0.133896095314535}, 'transactions': [], 'price': '££', 'location': {'address1': '22 Mill Road', 'address2': '', 'address3': None, 'city': 'Cambridge', 'zip_code': 'CB1 2AD', 'country': 'GB', 'state': 'CAM', 'display_address': ['22 Mill Road', 'Cambridge CB1 2AD', 'United Kingdom']}, 'phone': '+441223364106', 'display_phone': '+44 1223 364106', 'distance': 1325.2363426848879}, {'id': '2_oCvVuz0kSVUDAYdTag9g', 'alias': 'seven-days-cambridge', 'name': 'Seven Days', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/Y3YRGjKvlB1Kr20pmI13Pw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/seven-days-cambridge?adjust_creative=OGK23kwrCXPpr-9mF5GfLQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=OGK23kwrCXPpr-9mF5GfLQ', 'review_count': 20, 'categories': [{'alias': 'chinese', 'title': 'Chinese'}], 'rating': 4.0, 'coordinates': {'latitude': 52.200184, 'longitude': 0.126366}, 'transactions': [], 'price': '££', 'location': {'address1': '66 Regent Street', 'address2': '', 'address3': '', 'city': 'Cambridge', 'zip_code': 'CB2 1DP', 'country': 'GB', 'state': 'CAM', 'display_address': ['66 Regent Street', 'Cambridge CB2 1DP', 'United Kingdom']}, 'phone': '+441223309559', 'display_phone': '+44 1223 309559', 'distance': 886.9672454266323}]}
# print(json.dumps(data, indent=4))
print(len(data["rest_info"]))

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

# with open('data.txt') as json_file:
#    data = json.load(json_file)