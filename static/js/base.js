//Detect light and dark mode in browser and match nav bar 
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    document.addEventListener('DOMContentLoaded', function () {
        var navbar = document.querySelector('#nav-container');
        if (navbar) {
            //Remove dark theme classes
            navbar.classList.remove('navbar-dark', 'bg-dark'); 
            //Add light theme classes
            navbar.classList.add('navbar-light', 'bg-light'); 
        }
    });
}