var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        const listingID = this.dataset.id
        const action = this.dataset.action
        console.log('listingID:', listingID, 'Action:', action)
        console.log('USER:', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in.')
        } else {
            updateUserOrder(listingID, action)
        }
    })
}

function updateUserOrder(id, action) {
    console.log('User is authenticated, updating cart..')

    const url = '/update_cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({'id': id, 'action': action})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    });
}
