# Capstone-City-Comparison-Tool

The City Comparison Tool is a practical and useful interface for users considering traveling, moving, or relocating to different US cities. The app will provide valuable metrics for ease-of-comparison among cities, such as quality of life, commutability, safety, among others. This kind of app can be highly beneficial for individuals looking to make informed decisions about their next destination. The target demographic includes students, potential home-buyers, and professionals seeking to move cities.

The City Comparison Tool will rely on Teleport’s computed aggregate scores for urban areas. At present, the API provides scores for the following categories: “housing, cost of living, startups, venture capital, travel connectivity, commute, business freedom, safety, healthcare, education, environmental quality, economy, taxation and internet access”. Teleport additionally provides native access to photos of urban areas within their API, which enhances functionality when implemented alongside city metrics.

The approach to building the City Comparison Tool will be as follows. The backend with Flask and Jinja will be used to build the routes and HTML that the user can navigate to. 
API data is displayed using Jinja and HTML and called using Flask GET requests. Potential API issues may include data inconsistencies or changes to the API structure over time. These should be tested for regularly using unit testing and GET requests should be updated if errors are thrown. From there, SQLAlchemy will be used to generate a PostgreSQL database containing user data, including saved home or favorite cities, as well as the most sensitive information: username and hashed password combinations. Finally, the front-end will be stylized and made dynamic with Bootstrap and JavaScript, respectively, to create the core of the user interface. 

The app will have critical functionality related to city search, metric selection, and comparison reports. The user flow will go hand-in-hand with functionality and appear as follows. The user lands on the homepage to a search bar and is allowed to select cities for comparison or select among pre-defined cities. The user is allowed to toggle on and off desired metrics before comparing cities. Once complete, the user will be shown a page with a comparison report of the various cities and metrics selected. Lastly, the user will have the option to form a profile and save preferences for future reference. 

The premise of the app largely contains features which utilize CRUD principles. As such, appropriate stretch goals could expand app features to be “more than CRUD”. One such feature would utilize News’ API to integrate web URLs of local news articles among selected cities for use in the comparison report. Another stretch feature would generate a small-scale city recommendation algorithm based on saved user preferences with content-based filtering.

API: https://developers.teleport.org/api/
