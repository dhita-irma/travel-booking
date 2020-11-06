var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        const id = this.dataset.id
        const action = this.dataset.action
        const date = this.dataset.date
    
        console.log('listingID:', id, 'Action:', action)
        console.log(date)
        console.log('USER:', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in.')
        } else {
            updateUserOrder(id, action, date)
        }
    })
}

function updateUserOrder(id, action, date) {
    console.log('User is authenticated, updating cart..')

    const url = '/update_cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({'id': id, 'action': action, 'date': date})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    });
}
