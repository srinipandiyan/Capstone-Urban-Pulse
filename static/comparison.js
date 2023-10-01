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

  if (isFavorite) {
    favoriteBtn.textContent = 'Unfavorite';
    favoriteBtn.classList.remove('btn-primary');
    favoriteBtn.classList.add('btn-outline-warning');
  } else {
    favoriteBtn.textContent = 'Favorite';
    favoriteBtn.classList.remove('btn-outline-warning');
    favoriteBtn.classList.add('btn-primary');
  }
  
  const city = window.location.pathname.substring(1);

  $.ajax({
    type: 'POST',
    url: '/favorites',
    data: JSON.stringify({ ua_id: city }),
    contentType: 'application/json',
  });
}

/*
 * handle submit for base city button
 */
function submitBaseCity() {
   //toggle current state of base city button
  isBaseCity = !isBaseCity;

  if (isBaseCity) {
    baseCityBtn.textContent = 'Remove Base City';
    baseCityBtn.classList.remove('btn-secondary');
    baseCityBtn.classList.add('btn-outline-danger');
  } else {
    baseCityBtn.textContent = 'Set As Base City';
    baseCityBtn.classList.remove('btn-outline-danger');
    baseCityBtn.classList.add('btn-secondary');
  }

  const city = window.location.pathname.substring(1);

  $.ajax({
    type: 'POST',
    url: '/basecity',
    data: JSON.stringify({ ua_id: city }),
    contentType: 'application/json',
  });
}


//click event listener for favorite button
favoriteBtn.addEventListener('click', submitFavorite);
//click event listneer for base city button
baseCityBtn.addEventListener('click', submitBaseCity);