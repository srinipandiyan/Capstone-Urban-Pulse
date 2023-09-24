const input = document.querySelector('#cities');
const suggestions = document.querySelector('.suggestions ul');
const submitButton = document.querySelector('#submit-button');

const cities = [
    "Aarhus, Denmark",
    "Adelaide, Australia",
    "Albuquerque, United States",
    "Almaty",
    "Amsterdam",
    "Anchorage"]

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
                // The response status is OK (200).
                window.location.href = `/search/${selectedCity}`;
                console.log("Request was successful!");
            } else {
                // Handle other response statuses (e.g., 404 for "Not Found").
                console.log("Request failed with status: " + response.status);
            }
        })
        .catch(error => {
            // Handle network errors here, if needed.
            console.error("Network error:", error);
        });
}


//keyup event listener for search bar inputs
input.addEventListener('keyup', searchHandler);
//mouseover event listener for highlighting suggestions
suggestions.addEventListener('mouseover', toggleHighlight);
//mouseout event listener for unhighlighting suggestions
suggestions.addEventListener('mouseout', toggleHighlight);
//click event listener for city suggestions
suggestions.addEventListener('click', useSuggestion);
//click event listener for the submit button
submitButton.addEventListener('click', handleSubmit);
/*enter keyup event listener for search bar
input.addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        handleSubmit();
    }
});
*/
