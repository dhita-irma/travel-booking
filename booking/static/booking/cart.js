var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        const id = this.dataset.id
        const action = this.dataset.action
        const date = this.dataset.date
        const itemId = this.dataset.item
    
        console.log('listingID:', id, 'Action:', action)
        console.log(date)
        console.log('USER:', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in.')
        } else {

            // Update order 
            updateUserOrder(id, action, date)

            .then(data => {
                // Update subtotal
                var subtotal = document.getElementById(`subtotal-${itemId}`)
                subtotal.innerHTML = `$${data.orderItem.subtotal}`

                // Update cart total
                var cartTotal = document.getElementById('cart-total')
                cartTotal.innerHTML = `$${data.cart_total}`
            })
        }
    })
}

function updateUserOrder(id, action, date) {
    console.log('User is authenticated, updating cart..')

    const url = '/update_cart/'

    return fetch(url, {
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
        return data
    });
}


function submitFormData(total){
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
            'total': total
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success', data);
        alert('Transaction completed');

        // Redirect user to homepage 
        window.location.href = "/"

    });
}