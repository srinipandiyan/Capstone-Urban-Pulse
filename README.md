# Urban Pulse - Capstone

## Overview
[Urban Pulse](https://urbanpulse.onrender.com) is a web application designed to assist users in making informed decisions regarding traveling, moving, or relocating to urban areas across the world. We aim to provide valuable metrics for ease-of-comparison among cities, such as cost-of-living, education, safety, and more. The target demographic includes students, potential home-buyers, and professionals seeking to relocate. To run locally, install the requirements, create a db, and use the following commands start a flask server: `$flask run`.

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
- **Frontend**: JavaScript, HTML, CSS, and Bootstrap.
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

## Additional Notes
Future enhancements could include integrating local news articles using a news API for selected cities in the comparison report. A stretch goal is to implement a city recommendation algorithm based on user preferences using content-based filtering.

Feel free to explore the codebase and contribute to the project. Suggestions, bug reports, or feature requests are welcome anytime!

I hope you find Urban Pulse a valuable and user-friendly tool for exploring different global locales. If you have any questions or feedback, please don't hesitate to reach out.
