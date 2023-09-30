const favoriteBtn = document.querySelector('#favorite-button');
const baseCityBtn = document.querySelector('#base-city-button');

//track state of favorite and base city buttons; default is false
let isFavorite = false;
let isBaseCity = false;

/*
 * handle submit for favorite button
 */
function submitFavorite() {
  //toggle current state of favorite button
  isFavorite = !isFavorite;
  favoriteBtn.textContent = isFavorite ? 'Unfavorite' : 'Favorite';

  //get city from URL pathname
  const city= window.location.pathname;

  // Send a POST request to the /user/favorite route
  fetch('/favorites', {
    method: 'POST',
    data: { city: city }
  })
  .catch(error => {
    // Handle any network or other errors here
  });
}

/*
 * handle submit for base city button
 */
function submitBaseCity() {
   //toggle current state of base city button
  isBaseCity = !isBaseCity;

}


//click event listener for favorite button
favoriteBtn.addEventListener('click', submitFavorite);
//click event listneer for base city button
baseCityBtn.addEventListener('click', submitBaseCity);