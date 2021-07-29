# Testing

## Code Validation

### HTML Validator

Only errors related to checkout success regarding stray td and div tag. Verified in file
that no strays. Suspect it is related to if statement on where user came from. 

### CSS Validator

No issues.

### JS Validator

Three warnings. Decision to accept.

### PEP8 Validator

No issues.

## Site Performance

I used Chrome Developer tools to test performance, namely Lighthouse.

### Performance

Overall performance was good. It dropped on the rooms page due to images. I will look to address this with more time.

### Accessibility

Accessibility scored well across pages.

### Best Practises

Best practises were adhered to and reflected in the score.

### SEO

Score not as high as previous items but acceptable for the business purpose. 

## Device Testing

The site was tested across multiple browsers and devices. No issues in content or performance.

## User Story Testing

#### All users

+ Expected to be able to browser recording rooms on offer
+ Actual result - rooms available with price detail
+ Expected to be able to register
+ Actual result - new users can register
+ Expected to be able to purchase room date without registration
+ Actual result - can purchase room date without registration
+ Expected to prevent double booking
+ Actual result - once room is booked for a date, it is unavailable to others
+ Expected to be able to remove room date booking from cart
+ Actual result - on clicking 'Remove', selected date was removed and cart total updated

##### Registered User

+ Expected ability to log in and out
+ Actual result - users can log in and sign out
+ Expected ability to update profile
+ Actual result - can update profile in 'My Profile', or during checkout with 'save changes' checked
+ Expected ability to view order history
+ Actual result - order history available in 'My Profile' for each user

##### Site Owner / Superuser

+ Expected ability to add new products
+ Actual result - can add new rooms which are available to book / rent
+ Expected default image if none uploaded
+ Actual result - default image attached where none uploaded
+ Expected ability to update room details
+ Actual result - can update all aspects of room details
+ Expected ability to delete rooms
+ Actual result - can delete any room 
+ Expected only superuser can edit / delete, even by manipulating link
+ Actual result - only superuser can edit / delete rooms

#### Sign up

+ Expected username fields to highlight to user where not unique username / email addresss
+ Actual result - users informed username / email already in use
+ Expected password to be min 8 characters, and validate where all numeric, too weak
+ Actual result - user cannot proceed until password standard met
+ Expected to be taken to login page on email confirmation
+ Actual result - user is taken to login page post email confirmation

#### Log in

+ Expected user to be taken to home page on login
+ Actual result - user was taken to home page

#### My Profile

+ Expected user to be able to access profile and make updates
+ Actual result - user can access their profile and update details

#### Rooms 

+ Expected user to be taken to room detail page on clicking "Rooms"
+ Actual result - user is taken to room option page
+ Expected user to be taken to booking form on room selection
+ Actual result - user is taken to booking form
+ Expected user to be able to select date and add to cart
+ Actual result - user could select room date and add to cart

#### Checkout

+ Expected user to be taken to cart summary on clicking cart icon
+ Actual result - User taken to cart summary
+ Expected user to be taken to checkout form on clicting 'Checkout'
+ Actual result - user taken to checkout form
+ Expected user to be taken to success page with summary of purchase
+ Actual result - user taken to success page and summary available
+ Expected on checking 'Save Info', user detail added to profile
+ Actual result - user profile updated with details

#### Overall Site Testing

+ All links open in a new tab
+ No reliance on browser back button
+ Messages display until user closes
+ The site is repsonsive across different devices including large screen, desktop, mobile and tablet
+ Each user type has been tested as above for ability to perform functions and restrictions



