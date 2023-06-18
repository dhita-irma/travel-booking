# TRAVORA - Travel Booking Website 
TRAVORA is an online travel booking website that provides attractions and activities for various destinations in Indonesia. User can browse activities in all destinations and they can also filter the catalog based on the location. After that, they can pick dates to make reservation, add it to the cart and and pay it via Paypal. 

## Features 
- User can login or register to create account 
- The homepage features a search bar to quickly search for activity or destination 
- There is also section for top destination and top things to do for a quick look on what's activities in the website 
- In the catalog page, user can review all of activities and filter it based on destination 
- In each listing page, there is a datepicker to choose before adding it to the cart 
- At the bottom of the page of each listing, there is a reccommendation of similar activities in the same destination
- All items that's been put in the cart can be reviewed in the Shopping Cart section, user can increase or decrese the quantity and see the subtotal and total change immediately 
- Use can then check out the items in the cart and they will be brought to booking details page to fill out their contact info 
- User can make payment via PayPal or Debit/Credit card 
- After transaction is completed, user can view their booking history 


## What's contained in each files 
#### views.py 
Contains functions and API to render page and generate JsonResponse as follow:
* index, catalog, catalog_destination, catalog_item, cart_view, checkout: render each page, respectively
* search: API that takes user query input and return JSON data of listings that match the queries. This API is used to implement dynamic search bar and dynamic filtering feature so that the page doesn't reload everytime user make query
* update_cart: API to add, remove, or delete item from the cart. The JsonResponse returns details of ordered item and cart total, this data will be used to dynamically change subtotal and cart total every time user add or decrease item quantity
* process_oder: API submit contact information and process payment

#### models.py
Contains models as follow:
* User
* Desination
* Category
* Listing: contains listing details and relational to destination and category. serialize() function returns the JSON representation of the listing
* Order: contains order details user who make the order, date_ordered, and complete (boolean value). Order complete value will be False, until user made the payment. 
* OrderItem: each item that is orderd, same item with different reservation_date is count as separate item 
* ContactInfo: used to store contact information for booking details 

#### JavaScript files 
Located in booking/static/booking/
* front.js: Handles the front end of behavior the website such as Date Picker and Navigation bar 
* main.js: JS code for checkbox filtering and dynamic search bar. In each action performed, this JS code fetch information from search API, returns the data, and display it back to the user without reloading the webpage
* cart.js: JS code to assign some buttons to update cart on click, and submiting the booking details form data when the payment button is clicked

## Justification of why this final project is distinct and more complex than previous projects
- This project has a dynamic search bar feature that has never been done in the previous project. Search bar is implemented using JavaScript to deliver instant result below the search bar that changes as the user type in the box 
- This project also has checkbox filtering feature that is implemented using JavaScript to fetch filtered activies using API, allowing the website to filter listings based on destination without ever refreshing the page, makes the filtering experience much faster 
- In each listing page, there is a reccomendation section at the bottom of the page, automatically showing activities in the same destination 
- Previous projects never has the feature of Cart and Payment via PayPal 
- When user increase and decrease item quanity in the Cart, the website handles it with JavaScript so that the subtotal and cart total can dynamically change instantly without reloading the page
- Using datepicker to choose the date of reservation is something new to do. In the Cart, same activity with different reservation date would be showed as separate item 
- There is also booking history, that keeps track of every item that has been successfully booked by user