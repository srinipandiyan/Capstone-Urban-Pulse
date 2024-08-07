# Urban Pulse - Capstone

## Overview
[Urban Pulse](https://urbanpulse.onrender.com) is a web application designed to assist users in making informed decisions regarding traveling, moving, or relocating to urban areas across the world. We aim to provide valuable metrics for ease-of-comparison among cities, such as cost-of-living, education, safety, and more. The target demographic includes students, potential home-buyers, and professionals seeking to relocate. 

To run locally, create and activate a virtual environment & install the requirements.txt file, run the urban_pulse.sql file with Postgres, and launch the server with the following commands: 
```shell
 $ python3 -m venv venv && source venv/bin/activate
 $ pip install -r requirements.txt
 $ psql urban_pulse.sql
 $ flask run
```

To launch tests, run the following commands:
```shell
$ python -m unittest test_city_model.py
$ python -m unittest test_user_model.py
```
## Features
Here are the key features implemented by Urban Pulse:
- **City Pulse**: Users can search our databases for cities and view a city reference page.
- **Comparison Report**: Users can set a base city and have a comparison report added to the city pulse.
- **User Profile**: Users' preferences, such as favorites, are saved for future reference in their profile.
- **Photo View**: Users can visually explore favorite cities through photo-immersion (because a photo is worth a 1000 words).
- **Teleport API Integration**: Urban area scores and data are fetched using Teleport's API.
- **Dynamic UI**: JavaScript and Bootstrap create an interactive user interface.

## Technology Stack
Urban Pulse deploys the following technologies:
- **Frontend**: JavaScript, HTML, CSS, jQuery, and Bootstrap.
- **Backend**: Python, Flask with Jinja for routing and HTML rendering, Flask-WTForms for form creation, and Gunicorn as the production-ready HTTP server.
- **Database**: SQLAlchemy with PostgreSQL to store user and city data.

## Standard User Flow
Here's a step-by-step walkthrough of the standard user flow for Urban Pulse:
1. **Homepage**: Users land on the homepage and are prompted to sign-up or login.
2. **Search**: Users are redirected to a search bar and can query urban areas in our databases.
3. **City Pulse Report**: After selecting a city, users are presented with a city pulse report containing a city summary and scores for 15+ metrics in a comparison report.
   - Favorite OR Set Base City: Users can add/remove a city to favorites or set it as the base city.
4. **User Profile**: Users can view and update their profile, including user credentials, favorites, and base city.
   - Photo View: Users can view photos of their favorite cities.

## API Integration
Urban Pulse relies on [Teleport's API](https://developers.teleport.org/api/) to fetch urban area metrics. 
**NOTE: Presently, Urban Pulse is looking for a new API as the previous API is no longer available!**

## Photos from Application
Here are photos displaying Urban Pulse's user interface

 Search Page displaying autocomplete functionality
 <img width="1440" alt="Search Page with autocomplete of Urban Pulse" src="https://github.com/srinipandiyan/Capstone-Urban-Pulse/assets/125408728/2cc201cb-1165-4b91-aa63-a2fb7769ed0e">
 
 Comparison Page of Two Cities with dynamically fetched and rendered metrics
 <img width="1440" alt="City Comparison of San Francisco and Aarhus" src="https://github.com/srinipandiyan/Capstone-Urban-Pulse/assets/125408728/6f7aacb1-778f-4a36-a098-c69354e601a1">
 
 Solo City Stats Page
 <img width="1440" alt="SF Bay Area-Solo stats " src="https://github.com/srinipandiyan/Capstone-Urban-Pulse/assets/125408728/e418e3f8-0752-4241-b810-208ab331813b">

 User Profile Page of Favorites and Base City
 <img width="1440" alt="Profile View of Favorites and Base City" src="https://github.com/srinipandiyan/Capstone-Urban-Pulse/assets/125408728/a4d639cc-5551-447c-ac02-a960f3371a5c">

## Additional Notes
Future enhancements could include integrating local news articles using a news API for selected cities in the comparison report. A stretch goal is to implement a city recommendation algorithm based on user preferences using content-based filtering.

Feel free to explore the codebase and contribute to the project. Suggestions, bug reports, or feature requests are welcome anytime!

I hope you find Urban Pulse a valuable and user-friendly tool for exploring different global locales. If you have any questions or feedback, please don't hesitate to reach out.
