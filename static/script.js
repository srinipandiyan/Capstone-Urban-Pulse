const input = document.querySelector('#cities');
const suggestions = document.querySelector('.suggestions ul');
const submitButton = document.querySelector('#submit-button');

const cities = [
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
    "St. Louis, United States",
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
    "Washington D.C., United States",
    "Wellington, New Zealand",
    "Winnipeg, Canada",
    "Wroclaw, Poland",
    "Yerevan, Armenia",
    "Zagreb, Croatia",
    "Zurich, Switzerland"
  ]

 /*
 * match characters in str to characters in elements of cities array
 * @param {string} results - filter cities array for chars in search query str
 */
function search(str) {
	const results = [];
	//filter cities array for str and append to results if true; else append an empty ''
	cities.filter(val => val.toLowerCase().includes(str) ? results.push(val) : null);
	//return results array
	return results
}

//event handler that returns search bar inputs matched to cities array
function searchHandler(e) {
	//store and extract lowercase keyup values as a string
	const inputVal = e.target.value.toLowerCase();
	//store and match user input to urban area
	const results = search(inputVal);
	//show matching fruit in dropdown menu else reset suggestions if no user input
	inputVal ? showSuggestions(results) : suggestions.innerText = "";
}

/*
 * show results as part of dropdown suggestions
 * @param {string array} results - suggestion array based on user input
 */
function showSuggestions(results) {
	// innerText default will clear suggestions
	suggestions.innerText = "";
	//userinput to display suggestions upon user keyup events
	if (results.length > 0){
		//displays abbreviated results--up to first five elements
		for (let i = 0; i < results.length && i < 5; i++){
			//created new list item element
			const newLi = document.createElement("li");
			//innerText of <li> set to index item in results array
			newLi.innerText = results[i];
			//list item element appended to suggestions
			suggestions.appendChild(newLi);
		}
	}
}

//toggle suggestion highlights using mouseover and mouseout event listeners
function toggleHighlight(e){
	const targetClass = e.target.classList;
	const eventType = e.type;
	//hovering over <li> adds highlights class
	if (eventType === 'mouseover') {
        targetClass.add('highlight');
	//hovering away from <li> removes highlight class
    } else if (eventType === 'mouseout') {
        targetClass.remove('highlight');
    }
}

function useSuggestion(e) {
	//click to access city suggestion value
	cityVal = e.target.innerText;
	//value attribute of search bar is assigned city value
	input.value = cityVal;
	//reset suggestions
	suggestions.innerText = "";
}

//function to handle form submission
function handleSubmit() {
    const selectedCity = input.value;

    fetch(`/search/${selectedCity}`)
        .then(response => {
            if (response.ok) {
                //the response status is OK (200).
                window.location.href = `/search/${selectedCity}`;
            } else {
                //handle other response statuses (404).
                console.log("Request failed with status: " + response.status);
            }
        })
        //may need to edit out
        .catch(error => {
            //handle network errors here, if needed.
            console.error("Network error:", error);
        });
}

//function to handle form submission via enter keyup
function handleEnter(event) {
    if (event.key === 'Enter'){
        handleSubmit();
    };
}

//keyup event listener for search bar inputs
input.addEventListener('keyup', searchHandler);

//enter keyup event listener for search bar
//input.addEventListener('keyup', handleEnter);

//mouseover event listener for highlighting suggestions
suggestions.addEventListener('mouseover', toggleHighlight);
//mouseout event listener for unhighlighting suggestions
suggestions.addEventListener('mouseout', toggleHighlight);
//click event listener for city suggestions
suggestions.addEventListener('click', useSuggestion);
//click event for autcomplete suggestions
suggestions.addEventListener('click', handleSubmit);

//click event listener for the submit button
//submitButton.addEventListener('click', handleSubmit);