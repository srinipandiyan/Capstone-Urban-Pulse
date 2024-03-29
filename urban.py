import requests

valid_cities = [
    "Aarhus, Denmark",
    "Adelaide, Australia",
    "Albuquerque, United States",
    "Almaty, Kazakhstan",
    "Amsterdam, Netherlands",
    "Anchorage, United States",
    "Andorra",
    "Ankara, Turkey",
    "Asheville, United States",
    "Asuncion, Paraguay",
    "Athens, Greece",
    "Atlanta, United States",
    "Auckland, New Zealand",
    "Austin, United States",
    "Baku, Azerbaijan",
    "Bali, Indonesia",
    "Baltimore, United States",
    "Bangkok, Thailand",
    "Barcelona, Spain",
    "Beijing, China",
    "Beirut, Lebanon",
    "Belfast, United Kingdom",
    "Belgrade, Serbia",
    "Belize City, Belize",
    "Bengaluru, India",
    "Bergen, Norway",
    "Berlin, Germany",
    "Bern, Switzerland",
    "Bilbao, Spain",
    "Birmingham, United Kingdom",
    "Birmingham AL, United States",
    "Bogota, Colombia",
    "Boise, United States",
    "Bologna, Italy",
    "Bordeaux, France",
    "Boston, United States",
    "Boulder, United States",
    "Bozeman, United States",
    "Bratislava, Slovakia",
    "Brighton, United Kingdom",
    "Brisbane, Australia",
    "Bristol, United Kingdom",
    "Brno, Czech Republic",
    "Brussels, Belgium",
    "Bucharest, Romania",
    "Budapest, Hungary",
    "Buenos Aires, Argentina",
    "Buffalo, United States",
    "Cairo, Egypt",
    "Calgary, Canada",
    "Cambridge, United States",
    "Cape Town, South Africa",
    "Caracas, Venezuela",
    "Cardiff, United Kingdom",
    "Casablanca, Morocco",
    "Charleston, United States",
    "Charlotte, United States",
    "Chattanooga, United States",
    "Chennai, India",
    "Chiang Mai, Thailand",
    "Chicago, United States",
    "Chisinau, Moldova",
    "Christchurch, New Zealand",
    "Cincinnati, United States",
    "Cleveland, United States",
    "Cluj-Napoca, Romania",
    "Cologne, Germany",
    "Colorado Springs, United States",
    "Columbus, United States",
    "Copenhagen, Denmark",
    "Cork, Ireland",
    "Curitiba, Brazil",
    "Dallas, United States",
    "Dar es Salaam, Tanzania",
    "Delhi, India",
    "Denver, United States",
    "Des Moines, United States",
    "Detroit, United States",
    "Doha, Qatar",
    "Dresden, Germany",
    "Dubai, United Arab Emirates",
    "Dublin, Ireland",
    "Dusseldorf, Germany",
    "Edinburgh, United Kingdom",
    "Edmonton, Canada",
    "Eindhoven, Netherlands",
    "Eugene, United States",
    "Florence, Italy",
    "Florianopolis, Brazil",
    "Fort Collins, United States",
    "Frankfurt, Germany",
    "Fukuoka, Japan",
    "Galway, Ireland",
    "Gdansk, Poland",
    "Geneva, Switzerland",
    "Gibraltar",
    "Glasgow, United Kingdom",
    "Gothenburg, Sweden",
    "Grenoble, France",
    "Guadalajara, Mexico",
    "Guatemala City, Guatemala",
    "Halifax, Canada",
    "Hamburg, Germany",
    "Hannover, Germany",
    "Havana, Cuba",
    "Helsinki, Finland",
    "Ho Chi Minh City, Vietnam",
    "Hong Kong",
    "Honolulu, United States",
    "Houston, United States",
    "Hyderabad, India",
    "Indianapolis, United States",
    "Innsbruck, Austria",
    "Istanbul, Turkey",
    "Jacksonville, United States",
    "Jakarta, Indonesia",
    "Johannesburg, South Africa",
    "Kansas City, United States",
    "Karlsruhe, Germany",
    "Kathmandu, Nepal",
    "Kiev, Ukraine",
    "Kingston, Jamaica",
    "Knoxville, United States",
    "Krakow, Poland",
    "Kuala Lumpur, Malaysia",
    "Kyoto, Japan",
    "Lagos, Nigeria",
    "La Paz, Bolivia",
    "Las Palmas de Gran Canaria, Spain",
    "Las Vegas, United States",
    "Lausanne, Switzerland",
    "Leeds, United Kingdom",
    "Leipzig, Germany",
    "Lille, France",
    "Lima, Peru",
    "Lisbon, Portugal",
    "Liverpool, United Kingdom",
    "Ljubljana, Slovenia",
    "London, United Kingdom",
    "Los Angeles, United States",
    "Louisville, United States",
    "Luxembourg",
    "Lviv, Ukraine",
    "Lyon, France",
    "Madison, United States",
    "Madrid, Spain",
    "Malaga, Spain",
    "Malmo, Sweden",
    "Managua, Nicaragua",
    "Manchester, United Kingdom",
    "Manila, Philippines",
    "Marseille, France",
    "Medellin, Colombia",
    "Melbourne, Australia",
    "Memphis, United States",
    "Mexico City, Mexico",
    "Miami, United States",
    "Milan, Italy",
    "Milwaukee, United States",
    "Minneapolis-Saint Paul, United States",
    "Minsk, Belarus",
    "Montevideo, Uruguay",
    "Montpellier, France",
    "Montreal, Canada",
    "Moscow, Russia",
    "Mumbai, India",
    "Munich, Germany",
    "Nairobi, Kenya",
    "Naples, Italy",
    "Nashville, United States",
    "New Orleans, United States",
    "New York, United States",
    "Nice, France",
    "Nicosia, Cyprus",
    "Norfolk, United States",
    "Norrkoping, Sweden",
    "Nuremberg, Germany",
    "Oklahoma City, United States",
    "Omaha, United States",
    "Orlando, United States",
    "Oslo, Norway",
    "Ottawa, Canada",
    "Oxford, United Kingdom",
    "Palo Alto, United States",
    "Panama City, Panama",
    "Paris, France",
    "Perth, Australia",
    "Philadelphia, United States",
    "Phoenix, United States",
    "Pittsburgh, United States",
    "Portland ME, United States",
    "Portland OR, United States",
    "Porto, Portugal",
    "Porto Alegre, Brazil",
    "Prague, Czech Republic",
    "Pretoria, South Africa",
    "Pristina, Kosovo",
    "Providence, United States",
    "Quebec City, Canada",
    "Quito, Ecuador",
    "Raleigh, United States",
    "Reykjavik, Iceland",
    "Riga, Latvia",
    "Rio de Janeiro, Brazil",
    "Riyadh, Saudi Arabia",
    "Rome, Italy",
    "Rotterdam, Netherlands",
    "Saint Petersburg, Russia",
    "Salt Lake City, United States",
    "Salvador, Brazil",
    "San Antonio, United States",
    "San Diego, United States",
    "San Francisco Bay Area, United States",
    "San Jose, Costa Rica",
    "San Juan, Puerto Rico",
    "San Salvador, El Salvador",
    "Santiago, Chile",
    "Santo Domingo, Dominican Republic",
    "Sao Paulo, Brazil",
    "Sarajevo, Bosnia and Herzegovina",
    "Seattle, United States",
    "Seoul, South Korea",
    "Seville, Spain",
    "Shanghai, China",
    "Sofia, Bulgaria",
    "Stavanger, Norway",
    "St Louis, United States",
    "Stockholm, Sweden",
    "Stuttgart, Germany",
    "Sydney, Australia",
    "Tallinn, Estonia",
    "Tampa Bay Area, United States",
    "Tbilisi, Georgia",
    "Tel Aviv, Israel",
    "Tenerife, Spain",
    "The Hague, Netherlands",
    "Thessaloniki, Greece",
    "Tijuana, Mexico",
    "Tokyo, Japan",
    "Toronto, Canada",
    "Toulouse, France",
    "Tucson, United States",
    "Tulsa, United States",
    "Turin, Italy",
    "Ulaanbaatar, Mongolia",
    "Valencia, Spain",
    "Valletta, Malta",
    "Vancouver, Canada",
    "Venice, Italy",
    "Vienna, Austria",
    "Vientiane, Laos",
    "Vilnius, Lithuania",
    "Warsaw, Poland",
    "Washington DC, United States",
    "Wellington, New Zealand",
    "Winnipeg, Canada",
    "Wroclaw, Poland",
    "Yerevan, Armenia",
    "Zagreb, Croatia",
    "Zurich, Switzerland"
  ]

valid_ua_ids = ['aarhus', 'adelaide', 'albuquerque', 'almaty', 'amsterdam', 'anchorage', 'andorra', 'ankara', 'asheville', 'asuncion', 
                'athens', 'atlanta', 'auckland', 'austin', 'baku', 'bali', 'baltimore', 'bangkok', 'barcelona', 'beijing', 'beirut', 
                'belfast', 'belgrade', 'belize-city', 'bengaluru', 'bergen', 'berlin', 'bern', 'bilbao', 'birmingham', 'birmingham-al', 
                'bogota', 'boise', 'bologna', 'bordeaux', 'boston', 'boulder', 'bozeman', 'bratislava', 'brighton', 'brisbane', 'bristol', 
                'brno', 'brussels', 'bucharest', 'budapest', 'buenos-aires', 'buffalo', 'cairo', 'calgary', 'cambridge', 'cape-town', 'caracas', 
                'cardiff', 'casablanca', 'charleston', 'charlotte', 'chattanooga', 'chennai', 'chiang-mai', 'chicago', 'chisinau', 'christchurch', 
                'cincinnati', 'cleveland', 'cluj-napoca', 'cologne', 'colorado-springs', 'columbus', 'copenhagen', 'cork', 'curitiba', 'dallas', 
                'dar-es-salaam', 'delhi', 'denver', 'des-moines', 'detroit', 'doha', 'dresden', 'dubai', 'dublin', 'dusseldorf', 'edinburgh', 
                'edmonton', 'eindhoven', 'eugene', 'florence', 'florianopolis', 'fort-collins', 'frankfurt', 'fukuoka', 'galway', 'gdansk', 'geneva', 
                'gibraltar', 'glasgow', 'gothenburg', 'grenoble', 'guadalajara', 'guatemala-city', 'halifax', 'hamburg', 'hannover', 'havana', 'helsinki', 
                'ho-chi-minh-city', 'hong-kong', 'honolulu', 'houston', 'hyderabad', 'indianapolis', 'innsbruck', 'istanbul', 'jacksonville', 'jakarta', 
                'johannesburg', 'kansas-city', 'karlsruhe', 'kathmandu', 'kiev', 'kingston', 'knoxville', 'krakow', 'kuala-lumpur', 'kyoto', 'lagos', 
                'la-paz', 'las-palmas-de-gran-canaria', 'las-vegas', 'lausanne', 'leeds', 'leipzig', 'lille', 'lima', 'lisbon', 'liverpool', 'ljubljana', 
                'london', 'los-angeles', 'louisville', 'luxembourg', 'lviv', 'lyon', 'madison', 'madrid', 'malaga', 'malmo', 'managua', 'manchester', 
                'manila', 'marseille', 'medellin', 'melbourne', 'memphis', 'mexico-city', 'miami', 'milan', 'milwaukee', 'minneapolis-saint-paul', 
                'minsk', 'montevideo', 'montpellier', 'montreal', 'moscow', 'mumbai', 'munich', 'nairobi', 'naples', 'nashville', 'new-orleans', 
                'new-york', 'nice', 'nicosia', 'norfolk', 'norrkoping', 'nuremberg', 'oklahoma-city', 'omaha', 'orlando', 'oslo', 'ottawa', 'oxford', 
                'palo-alto', 'panama-city', 'paris', 'perth', 'philadelphia', 'phoenix', 'pittsburgh', 'portland-me', 'portland-or', 'porto', 
                'porto-alegre', 'prague', 'pretoria', 'pristina', 'providence', 'quebec-city', 'quito', 'raleigh', 'reykjavik', 'riga', 'rio-de-janeiro', 
                'riyadh', 'rome', 'rotterdam', 'saint-petersburg', 'salt-lake-city', 'salvador', 'san-antonio', 'san-diego', 'san-francisco-bay-area', 
                'san-jose', 'san-juan', 'san-salvador', 'santiago', 'santo-domingo', 'sao-paulo', 'sarajevo', 'seattle', 'seoul', 'seville', 'shanghai', 
                'sofia', 'stavanger', 'st-louis', 'stockholm', 'stuttgart', 'sydney', 'tallinn', 'tampa-bay-area', 'tbilisi', 'tel-aviv', 'tenerife', 
                'the-hague', 'thessaloniki', 'tijuana', 'tokyo', 'toronto', 'toulouse', 'tucson', 'tulsa', 'turin', 'ulaanbaatar', 'valencia', 'valletta', 
                'vancouver', 'venice', 'vienna', 'vientiane', 'vilnius', 'warsaw', 'washington-dc', 'wellington', 'winnipeg', 'wroclaw', 'yerevan', 
                'zagreb', 'zurich']

def get_ua_id(city):
    """
    Given city from autocomplete suggestion, convert city name to API callable urban area id (ua_id).
    ua_id will have all chars in lowercase, country and punctuation removed, and spaces replaced with hypens (-).

    parameters:
        city (str): the user readable city name and location, for example: "San Francisco Bay Area, United States"

    returns:
        returns ua_id (str)
    """

    #split the city str by comma, retain the city name, replace any spaces with a hypen, and lowercase all chars.
    city_name = city.split(',')
    ua_id = city_name[0].strip().replace(' ', '-').lower()
    return ua_id

def get_city_scores(ua_id):
    """
    Given ua_id, call city scores from Teleport API for urban areas.
    
    parameters: 
        ua_id (str): the urban area id of a city, for example: "san-francisco-bay-area".
            arg must given in lowercase with any spaces replaced with hypens (-).
        
    returns:
       if request == 200, returns a JSON dict object from the API.
            else, returns NONE.
    """
    #API URL route for urban area scores
    url = f"https://api.teleport.org/api/urban_areas/slug%3A{ua_id}/scores/"
    #GET request
    response = requests.get(url)
    
    #verify request was successful with status code 200
    if response.status_code == 200:
        #return parsed json response
        return response.json()
        
    else:
        #handle case where the request was unsuccessful
        print(f"GET request failed: status code {response.status_code}")
        return None
    
def get_city_photo(ua_id):
    """
    Given ua_id, get city image url from Teleport API for urban areas.
    
    parameters: 
        ua_id (str): the urban area id of a city, for example: "san-francisco-bay-area".
            arg must given in lowercase with any spaces replaced with hypens (-).
        
    returns:
       if request == 200, returns a str from the API.
            else, returns NONE.
    """

    #API URL route for urban area photo
    url = f"https://api.teleport.org/api/urban_areas/slug%3A{ua_id}/images/"
    #GET request
    response = requests.get(url)
    
    #verify request was successful with status code 200
    if response.status_code == 200:
        #parse json response
        data = response.json()
        #access and return the web image URL from response
        image_url = data['photos'][0]['image']['web']
        return image_url
        
    else:
        #handle case where the request was unsuccessful
        print(f"GET request failed: status code {response.status_code}")
        return None
    
def get_city_details(ua_id):
    """
    Given ua_id, get city details from Teleport API for urban area.
    
    parameters: 
        ua_id (str): the urban area id of a city, for example: "san-francisco-bay-area".
            arg must given in lowercase with any spaces replaced with hypens (-).
        
    returns:
       if request == 200, returns a JSON dict object from the API.
            else, returns NONE.
    """

    #API URL route for urban area details
    url = f"https://api.teleport.org/api/urban_areas/slug%3A{ua_id}/details/"
    #GET request
    response = requests.get(url)

    #verify request was successful with status code 200
    if response.status_code == 200:
        #return parsed json response
        return response.json()
        
    else:
        #handle case where the request was unsuccessful
        print(f"GET request failed: status code {response.status_code}")
        return None
        
def get_city_salaries(ua_id):
    """
    Given ua_id, call city salaries from Teleport API for occupations in urban areas.
    
    parameters: 
        ua_id (str): the urban area id of a city, for example: "san-francisco-bay-area".
            arg must given in lowercase with any spaces replaced with hypens (-).
        
    returns:
       if request == 200, returns a JSON dict object from the API.
            else, returns NONE.
    """

    #API URL route for urban area occupational salaries
    url = f"https://api.teleport.org/api/urban_areas/slug%3A{ua_id}/salaries/"
    #GET request
    response = requests.get(url)
    
    #verify request was successful with status code 200
    if response.status_code == 200:
        #return parsed json response
        return response.json()
        
    else:
        #handle case where the request was unsuccessful
        print(f"GET request failed: status code {response.status_code}")
        return None