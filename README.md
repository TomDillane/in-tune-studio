# In Tune Studio

In Tune Studio is a recording studio that can be booked by music artists on a day by day basis. 
The owner will be able to make updates to the room rates and details along with adding rooms.
Once a room is booked for a particular date, it cannot be booked  by another user. 
Users will be able to review their profiles and make updates.

## UX - User Experience

### User Stories

##### Anonymous User

+ Ability to quickly gather what the site is about
+ Ability to sign up to the site as a member
+ Ability to navigate around the site
+ Ability to view products
+ Ability to purchase products

##### Registered User

+ Ability to log in and out
+ Ability to update profile
+ Ability to view order history

##### Site Owner / Superuser

+ Ability to add new products
+ Ability to update and delete products

### Strategy Plane

+ The goal of the site is to provide an online presence for a recording studio where artists can purchase the time to use one of the studio rooms.
+ The studio owners can gather members and revenue from these sales.

### Scope Plane

+ Details on the services offered
+ Registration option for new users
+ Log in option for returning users
+ Superuser role for site owner to update products
+ On line shopping facility

### Structure Plane

#### Front End

+ The site will have a home page with a call out to use the studio
+ The site will have a booking page with room options
+ Anonymous and registered users can buy services
+ Anonymous users can register
+ Register and Login options will only be available to anonymous users
+ Log out option will only be available to signed in users
+ Site owner only will be able to add, update and delete products

##### Wireframes

+ [Home Wireframe](readme_images/home.png)
+ [Rooms Wireframe](readme_images/rooms.png)
+ [Room Booking Wireframe](readme_images/room-booking.png)
+ [Cart Wireframe](readme_images/cart.png)
+ [Checkout Wireframe](readme_images/checkout.png)
+ [Checkout Success Wireframe](readme_images/checkout-success.png)
+ [Login Wireframe](readme_images/login.png)
+ [Register Wireframe](readme_images/register.png)
+ [Profile Wireframe](readme_images/profile.png)
+ [Room Add Wireframe](readme_images/room-add.png)
+ [Room Edit Wireframe](readme_images/room-edit.png)
+ [Room Edit Detail Wireframe](readme_images/room-edit-detail.png)

#### Backend

##### Field detail

[Database Models](readme_images/database.png)

##### Relationships

[Database ER](readme_images/database-schema.png)

##### Products

+ This model handles the details of the rooms on offer including, price, image and other detail.
+ It is linked to the Order line item so that an order can draw on product details.

##### Order Line Item

+ This model takes care of the specific order line of product and in particular date to rerserve room.
+ It is linked to Product as mentioned above and Order itelf as part of the overall order.

##### Order

+ This model handles the entire order. It has details on the user and links to the Profile model where these details can be passed.

##### Profile

+ This model handles the user profile. It can be updated at time of checkout via order or directly.

### Skeleton Plane

The site will have the following structure:

+ Home page - Call out to use the studio
+ Room page - Details of the various rooms available to book
+ Room booking page - users can book a room for a particular date
+ Cart page - users can view cart and make updates by removing items
+ Checkout page - users can purchase their cart items
+ checkout success page - users get a confirmation on their purhase
+ Profile page - users can view and amend their personal details

##### Owner only 

+ Product Changes page - owner can add new rooms
+ Edit / Delete rooms - owner can amend room details or delete

### Skeleton Plane

The site typograthy is Otomanopee One and Russo. I chose these to give a bulky feel to the text as it is not intense in volume.
The colors are contrasting dark gray and off white with red hover. I chose this to keep the site simple and allow the home inage and room images to stand out.

## Features

### Current Features

+ Anonymous users can view rooms
+ Anonymous users can purchase rooms
+ Anonymous users can register 
+ Returning users can log in
+ Returning users can make updates to their profile
+ Returning users can view order history
+ Site owner can make updates to room details such as price
+ Site owner can remove rooms
+ Site owner can add new rooms to catalogue

### Feature Detail

##### Home

+ On arrival, the user is met with a home page with an image of a recording desk.
+ There is a call out to come and make a record with the studio.
+ The NAV bar is fixed to top and allows the user to view rooms, cart and account. 
+ At the top there is a link to home.
+ The color scheme is dark and light to allow the picture to stand out.

##### User functions
+ Anomyous users have the option to register or log in via account.
+ Logged in users have the option to view profile and update details.
+ Site owner has the option to go to product management.
+ Logged in users can sign out.
+ Usernames and emails must be unique.
+ Passwords must meet minimum requirements, e.g. multi character type and at least 8 characters.
+ On registration, users need to verify their email. 

##### Room / product

+ Anonymous and logged in users can go to rooms, select the prefered date and add to cart.
+ If the room and date exist in another order, the user will not be able to add it to their cart.
+ The date is via datepicker to avoid issue.
+ On progression, users can view cart and remove items if they wish.
+ Once happy, users proceed to checkout. For logged in users, any saved details will be prepopulated.
+ Also, in the case of logged in users, changes to details can be saved and applied to profile at this stage.
+ On completion of card details, users are presented with a page confirming the order and its details.

##### Product Managemnt - site owner

+ The site owner can make updates to products - edit / delete existing rooms and add new rooms. 
+ The links for these actions are not available to others, and in the case they bypass the url, there is logic
in the function to prevent all but the superuser from taking any action. 

### Future Features

+ Blog app to allow users to articulate their experiences in the studio.
+ Loyalty scheme where prices change for customers based on frequency of purchase.

## Security

+ The site uses Allauth primarily for user administraion.
+ For the forms, there is a CSRF token to ensure validity.
+ Login is required to access profile.
+ Product admin is unavailable to users other than the superuser fron the front end.
+ Product admin requires the user to be the super user even if front end bypassed.
+ The payment system is integrated with Stripe and uses a secret key and signing key for security.

*** Please note that I mistakenly put the Database URL in a commit. To counteract this and avoid any security issue with database access I created a new one that is not in any commit. ***

## Technologies Used

#### Framework, Tools and Libraries

+ Django
+ Bootstrap
+ Google Fonts
+ Balsamiq
+ Github
+ AWS S3
+ Heroku
+ Gitpod
+ Chrome Developer Tools
+ W3C Markup and CSS validators
+ PEP8 validator

#### Languages

+ HTML
+ CSS
+ JavaScript
+ Python 
+ Django templating

## Testing

[Testing Doc](TESTING.md)

## Deployment

#### Application Deployment

The application is deployed on Heroku. This was accomplished by the following:

+ Create a requirements.txt file and a Procfile
+ Track these two files by committing to GitHub
+ Go to Heroku and create a new application
+ Navigate to the app and deploy using "GitHub" and link to the relevant repository, in this case "TomDillane/in-tune-studio"
+ Go to settings in Heroku and select "Reveal Config Vars"
+ Populate the following fields:

[Heroku Config Vars](readme_images/config.vars.png)

+ AWS_ACCESS_KEY_ID - Access key for AWS S3
+ AWS_SECRET_ACCESS_KEY - Secret key for AWS S3
+ DATABASE_URL - Postgres DB URL
+ EMAIL_HOST_PASS - SMTP from gmail in this case
+ EMAIL_HOST_USER - host mail, using my own in this case
+ SECRET_KEY - secret key
+ STRIPE_PUBLIC_KEY - Stripe public key from account
+ STRIPE_SECRET_KEY - Stripe secret key from account
+ STRIPE_WH_SECRET - Stripe webhook secret
+ USE_AWS - set this to True

*** As mentioned above, please note that I mistakenly put the Database URL in a commit. To counteract this and avoid any security issue with database access I created a new one that is not in any commit. ***

#### Run Locally

To run locally, you need to install the following tools:

+ PIP
+ Python3
+ GitHub

- Go to GitHub and navigate to the main page of the repository (https://github.com/TomDillane/bulls_rugby_club)
- Click the "Code", drop down.
- Click the "Copy", icon next to the url.
- Install Github on your machine and launch the repository that you wish to use.
- Open Git Bash and navigate to where you want to put the clone.
- Type git clone https://github.com/TomDillane/in-tune-studio
- Press "Enter".
- In bash, enter "pip3 install requirements.txt"
- To run the app locally, enter "python3 manage.py runserver", in bash

## Credits

+ Photo by RODNAE Productions from Pexels for Home page.
+ Photo by Wallace Chuck from Pexels for room 1 products.
+ Photo by cottonbro from Pexels for room 2 products.
+ Photo by RODNAE Productions from Pexels for room 3 products.
+ Photo by Stas Knop from Pexels where no product image selected.

+ The project was influenced by Code Institute's Boutique Ado.
+ All content was written by Tom Dillane.

### Acknowledgements

I would like to thank my mentor and the tutors at code institute. In both cases, they pushed me to solve problems. 


