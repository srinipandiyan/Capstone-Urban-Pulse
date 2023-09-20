const input = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');

const fruit = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

/*
 *match characters in str to characters in elements of fruit array
 */
function search(str) {
	const results = [];
	//filter fruit array for str and append to results if true; else append an empty ''
	fruit.filter(val => val.toLowerCase().includes(str) ? results.push(val) : null);
	//return results array
	return results
}

//event handler that returns search bar inputs matched to fruit array
function searchHandler(e) {
	//store and extract lowercase keyup values as a string
	const inputVal = e.target.value.toLowerCase();
	//store and match user input to fruit
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
	//click to access fruit suggestion value
	fruitVal = e.target.innerText;
	//value attribute of search bar is assigned fruit value
	input.value = fruitVal;
	//reset suggestions
	suggestions.innerText = "";
}

//keyup event listener for search bar inputs
input.addEventListener('keyup', searchHandler);
//mouseover event listener for highlighting suggestions
suggestions.addEventListener('mouseover', toggleHighlight);
//mouseout event listener for unhighlighting suggestions
suggestions.addEventListener('mouseout', toggleHighlight);
//click event listener for fruit suggestions
suggestions.addEventListener('click', useSuggestion);
