function filterCatalog(keywords) {
    var filteredCatalog = document.getElementById("filteredCatalog");

    // Fetch filtered listings
    fetch(`/search?q=${keywords}`)
    .then(response => response.json())
    .then(listings => {
      
      // Print listings 
      console.log(listings);

      // Display listings
      if (listings.length == 0) {
        filteredCatalog.innerHTML = 'No result';
      } else {
        // Clear previous filtered catalog 
        filteredCatalog.innerHTML = "";
        
        for (var i = 0; i < listings.length; i++) {
          console.log(listings[i]);

          const colDiv = document.createElement('div');
          colDiv.className = `col-lg-4 col-md-6 mb-4 d-flex align-items-stretch`;

          colDiv.innerHTML = `
          <div class="listing-item card bg-white rounded">
              <img src="${listings[i].image_url}" class="img-fluid card-img-top">
              <div class="card-body px-4 pt-4 pb-1">
                  <h6> <a href="/catalog/${listings[i].id}" class="text-dark stretched-link">${listings[i].title}</a></h6>
              </div>
              <div class="card-footer">
                  <div class="d-flex align-items-center justify-content-between rounded-pill bg-light pl-2">
                      <p class="location lead mb-0"><i class="icon fas fa-map-marker-alt"></i><span> ${listings[i].location}</span></p>
                      <div class="badge badge-warning px-3 py-2 rounded-pill font-weight-normal font-weight-bold">$${listings[i].price}</div>
                  </div>
                    </div>
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