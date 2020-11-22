function filterCatalog(keywords) {
    var filteredCatalog = document.getElementById("filteredCatalog");

    // Fetch filtered listings
    fetch(`search?q=${keywords}`)
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
                    <a href="/catalog/${listings[i].id}" class="stretched-link">
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
}


function Search(event) {
  const value = event.target.value;
  console.log(`Searching for "${value}"...`)
  
  const resultSection = document.getElementById('result');

  if (value.length >= 3) {

    // Show search result section
    resultSection.style.display = 'block';

    // fetch search result 
    fetch(`search?q=${value}`)
    .then(response => response.json())
    .then(listings => {
      console.log(listings)
      
      resultSection.innerHTML = "";

      // Display search results
      for (var i = 0; i < listings.length; i++) {
  
        const a = document.createElement('a');
        a.setAttribute('href', `/catalog/${listings[i].id}`);

        a.className = 'list-group-item list-group-item-action d-flex align-items-center';
        a.innerHTML = `
        <div class="image-parent">
          <img src="${listings[i].image_url}" class="img-fluid" alt="image">
        </div>
        <div class="pl-3">
          ${listings[i].title}
        </div>
        `
  
        resultSection.appendChild(a);
      }
    });
  } else {
    resultSection.innerHTML = "";
  }

}