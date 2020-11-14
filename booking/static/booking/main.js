function filterDestination(destination) {
    // Get the checkbox 
    var checkBox = document.getElementById(destination);

    // Get the output text
    var allCatalog = document.getElementById("allCatalog");
    var filteredCatalog = document.getElementById("filteredCatalog");

    // If checkbox is checked, display the output text
    if (checkBox.checked == true){
      allCatalog.style.display = "none";
      filteredCatalog.style.display = "flex";

      // Fetch filtered listings
      fetch(`/filter/${destination}`)
      .then(response => response.json())
      .then(listings => {
        
        // Print listings 
        console.log(listings);

        // Display listings
        if (listings.length == 0) {
          filteredCatalog.innerHTML = 'No result';
        } else {
          for (var i = 0; i < listings.length; i++) {
            console.log(listings[i]);
  
            const colDiv = document.createElement('div');
            colDiv.className = `col-lg-4 listing card-padding ${listings[i].location} ${listings[i].category}`;
  
            colDiv.innerHTML = `
              <div class="card h-100 listing-card">
                  <img class="card-img-top" src="${listings[i].image_url}" alt="">
                  <div class="card-body p-2">
                      <a href="{% url 'catalog_item' listing.id %}" class="stretched-link">
                          <h6 class="card-title">${listings[i].title}</h6>
                      </a>
                      <p class="card-subtitle"> <i class="fas fa-map-marker-alt"></i>  ${listings[i].location}</p>
                      <p class="card-text card-desc"></p>
                  </div>
                  <div class="card-footer p-2">
                      US$ ${listings[i].price}<span>/pax</span>
                  </div>
              </div>
            `
            filteredCatalog.appendChild(colDiv);
  
          } // for
        } // ifelse


      }); //.then

    } else {
      allCatalog.style.display = "flex";
      filteredCatalog.innerHTML= "";
      filteredCatalog.style.display = "none";
    }
}
