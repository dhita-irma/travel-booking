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

function submitFormData(){
    console.log('Payment button clicked.')
    const form = document.getElementById('contact-form')

    // console.log(form.id_phone_number.value)

    // Send contact info form 
    fetch('/process_order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            'title': form.id_title.value,
            'first_name': form.id_first_name.value,
            'last_name': form.id_last_name.value,
            'country': form.id_country.value,
            'phone_number': form.id_phone_number.value,
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    });
}