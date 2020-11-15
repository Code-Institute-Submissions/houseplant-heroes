# Houseplant Heroes

## Milestone Project 3: Data Centric Development - Code Institute

![Home Responsive](./static/images/readme_images/responsive/home-responsive.png)
[Houseplant Heroes](https://houseplant-heroes.herokuapp.com/) was created as a response to the growing popularity of houseplants which, whilst aesthetically pleasing can often be difficult to maintain! The website allows users to access information on houseplant care as well as contribute their own insights and experiences.

## Table of Contents

1. <details><summary>UX</summary>

   - [User Stories](#user-stories)
     - [First Time User Goals](#first-time-user-goals)
     - [Returning User Goals](#returning-user-goals)
     - [Frequent User Goals](#frequent-user-goals)
     - [Site Owner Goals](#site-ownner-goals)
   - [Design](#design)
     - [Colour Scheme](#colour-scheme)
     - [Typography](#typography)
     - [Imagery](#imagery)
     - [Icons](#icons)
     - [Layout](#layout)
     - [Wireframes](#wireframes)
     </details>

# UX

## User Stories

### First Time User Goals

1. As a First Time User, I want to easily understand the purpose of the website and the services it offers
2. As a First Time User, I want to be able to navigate intuitively through the site

### Returning User Goals

1. As a Returning User, I want to browse plants
2. As a Returning User, I want to search for plants
3. As a Returning User, I want to know which plants are easiest/most difficult to care for
4. As a Returning User, I want ask questions about the plants
5. As a Returning User, I want to find care instructions
6. As a Returning User, I want to create my own posts

### Frequent User Goals

1. As a Frequent User, I want to see the plants that I have posted
2. As a Frequent User, I want to edit and delete my posts
3. I want to discuss the plants with others in the community
4. As a Returning User, I want feedback on my posts

### Site Owner Goals

1. As Admin, I want the ability to edit/delete any posts deemed inappropriate or unnecessary

## Design

The overall design of the website is clean and simplistic, this allows the plants themselves to be the main focus.

### Colour Scheme

![Colour Scheme](./static/images/readme_images/colour-scheme.png)

- The colours were chosen to compliment the hero image used on every page of the site. The muted tones are unobtrusive so as not to detract from the natural colours provided by the plant images.

- The add and edit plant form input uses the Materialize CSS default, on click, colours. They provide users with visually recognisable validation feedback:

Green for go
![Colour Scheme](./static/images/readme_images/form-green.png)

Red for stop
![Colour Scheme](./static/images/readme_images/form-red.png)

### Typography

- The Poppins font is used on all pages with Sans Serif as the back-up font due to it's clean presentation, the letters were also spaced apart by 2px to increase this effect.

- A range of font sizes and weights were used to denote importance.

- The white text used on the the hero image includes a text shadow to ensure readability.

### Imagery

**Hero Image**
![Hero Image](./static/images/hero-img.png)

- The hero image is used on each page of the site to create consistency and promote lasting brand image.
- The image was chosen as it emphsizes the natural aesthetic of house plants. It also isn't overly busy so as to obtrude upon the overlayed content.
- A liner gradient of (rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), is used to ensure content is visable on top.
- The hero image is resized on each page depending on the size of hero image content but is always recognisable as the same image.
- This image is coded as a background-image in css and set to background-size: cover; this making the image responsive.

**Carousel**
![Carousel](./static/images/readme_images/carousel.png)

- A [Slick](https://kenwheeler.github.io/slick/) Carousel is used to display the most recently added posts on the homepage.
- The carousel image links to the plant post for easy navigation for users.
- The carousel also state who the plant was posted by. The username was included to encourage users to post their own plants to be displayed on the front page.

### Icons

Icons are used throughout the site to provide the user with visual cues and create a more interesting aesthetic.

![Plant Profile Icons](./static/images/readme_images/plant-profile-icons.png)

- The use of icons in the plant profile page are particulary imporant as there may be quite a lot of information for the user to digest. The icons allow the user to easily scan the page for the information they are looking for. They also break up the information to make it more managable for the user.

![Arrow Icon](./static/images/readme_images/arrow-img.png)
![Chevron Icon](./static/images/readme_images/chevron-img.png)

- Arrow and Chevron icons are used throughout, with hover, to indicate directional links.

- A [Plant Pot](https://icons8.com/icon/106115/potted-plant) icon from [Icons8] is used for the site favicon to distinguish the website from other tabs sites for the user. The icon is also used in the footer for consistency.

- Social media icons are clearly positioned within the footer in accordance with user expectations. Dead links are used as the social media pages to exist at present.

### Layout

- [Materialize CSS Grid](https://materializecss.com/grid.html) was used to created the layout and make it responsive. The layout is simplistic, with no overcrowding of objects. This ensures users are able to clearly see and access the information they are looking for. Use of clean lines adds to this effect.

- A [Masonry](https://masonry.desandro.com/) grid was used to tidy up the layout of the cards in all_plants.html and profile.html. This was imporant as users are permitted to add images of varying dimensions, without masonry there could be large white spaces between each card.

### Styling

- [Materialize CSS](https://materializecss.com/) was used in conjunction with custom spacing and colours to provide much of the styling for the site. This includes all **buttons**, **forms**, **cards** and **nav bars**.

- [Materialize CSS Cards](https://materializecss.com/card.html) cards were utilized on all_plants.html and profile.html to display the lists of plants. They contained a condensed amount of information to allow the user to decide whether they wanted to proceed to the full care guide for the plant, for which a link is provided.

### Wireframes

- [Homepage](./static/images/readme_images/wireframes/wireframe-home.png)

- [Plants](./static/images/readme_images/wireframes/wireframe-all-plants.png)

- [Plant Profile](./static/images/readme_images/wireframes/wireframe-plant-profile.png)

- [Login](./static/images/readme_images/wireframes/wireframe-login.png)

- [Join](./static/images/readme_images/wireframes/wireframe-join.png)

- [User Profile](./static/images/readme_images/wireframes/wireframe-profile.png)

- [Add Plant](./static/images/readme_images/wireframes/wireframe-add-plant.png)

- [Edit Plant](./static/images/readme_images/wireframes/wireframe-edit-plant.png)

# Features

## Existing Features

### Elements on every page

- Navbar

  - The navigation bar has the Houseplants Hero title in the top left corner for clarity

  - The navigation links are on the top right hand corner.

  - For vistors who are not logged in, the links are:
    1. Home
    2. Plants
    3. Login
    4. Join
  - For users who are logged in, the links are:

    1. Home
    2. Plants
    3. Profile
    4. Add plant
    5. Log out

  - Python checks whether a user is logged in or not with `if 'user' in session`, this data is padded to Jinja to display the correct navbar for the user.

  - For mobile, the navbar collapses in to a burger icon with side navigation on the left of the screen.

  - Active classes are added to active page to show the user what page they are currently on.

  - The nav bar is fixed to the top of the screen to allow for accesible navigation regardless are where the user is on the page. This simplisity in the design of the nav bar ensure that it is not too obtrusive for the user.

- Hero Image

  - See [Imagery](#imagery).

- Flash Messages

  - Flash messages are used to provide feedback to the user for certain actions, e.g. when a posted is updated
  - The messages are layed over the hero-image and come before the heading so they are, generally, at eye height for the user.

- Heading

  - Each page has a heading position towards the center of the hero image. This reassures the user where they are on the site.

- Subheading

  - Each page has subheading to expand upon the purpose of the page.

- Footer
  - The footer contains:
    - Logo
    - Copywrite nformation
    - Social media links
    - In the future, contact information can be added

### Homepage

![Home Responsive](./static/images/readme_images/responsive/home-responsive-2.png)

As the first thing the user sees, the homepage was designed to be clear and informative.

**Search Bar**

- The search bar is conveniently placed for user to start using the website straight away.
- A tool-tip explains to the user the search terms that can be used.
- In line with user expectations, users can either hit the enter key or press the search button to enter search term. This takes them to the plants page.

**Redirect Buttons**

- If the user is not logged in they will have button links for, "Plants", "Login" and "Join" pages. These (as well as the homepage) are all the pages that can be accessed when a user is not logged in. This feauture is particulary targetted at first time visitors as it clearly presents them with all actions.

**Promo Content**

- This section is for promotional purposes, providing the user with immediate information of the features of the site. The majority of which cannot be accessed without an account. This encourages user to create an account in order to have full access to these features.

- Links are provided for convenient access.

**Recently Added Carousel**

- See [Imagery](#imagery).

### Plants Page

![Plants Responsive](./static/images/readme_images/responsive/all-plants-responsive.png)

**If users have arrived at the Plants page via the search bar on the home page:**

- If no matches have been found, a flash message will be displayed to user "No results. Please try again or browse all plants below." With all plants displayed below.

- If a match has been found, the user will be presented with their search results.

**Search Bar**

- See Search Bar in [Homepage](#Homepage)

**Search Bar Reset Button**

- Resetting the search results displays all plant posts in the database, eliminating the need for the user to refresh or go back.

**Cards**

- See [Layout](#layout) and [Styling](#styling)

### Plant Profile Page

![Join Responsive](./static/images/readme_images/responsive/plant-profile-responsive.png)
User's arrive on this page following a link from either the All Plants Page or User Profile Page card lists.

**Hero Image Content**

- Contains content to assure the user they are on the plant they expected

- The plant nickname is used as the page header at it is generally the most recognisable name.

- The plant botanical name is used as the subheading

- The plant description provides a little more informationon the plant, it is capped at 400 characters to ensure there is no overflow.

**Plant Info**
This section contains more detailed information on the plant.

- To the left or top of section(depending on screen size):

  - The plant image, which uses Materialize CSS's [responsive image](https://materializecss.com/media-css.html) class to ensure responsivity.
  - Shows who the plant is posted by.
  - Shows whether the plant is air purfiying.
  - Shows when the plant was last updated. This initially, will show the date and time the plant was added. If the plant is edited, it will update accordingly. This was included to allow users to see whether any updates have been made since their last viewing.

- Care instructions:

  - Shows all details obtained from the add plant form.
  - Materialize layouts and icons were used to break up the information.

**Edit/Delete**

- Edit/Delete buttons are only visible if the session user matches the "posted_by" of the specific plant, or is admin.
  ![edit delete icons](./static/images/readme_images/edit-delete.png)

- Clicking the edit button takes users to the [Edit Plant Page](#edit-plant-page).

- Clicking delete triggers a defensive modal:
  ![delete modal](./static/images/readme_images/delete-modal.png)
  1.  If yes, delete:
      - the plant post is removed from the database and the modal is closed.
  2.  If no, keep:
      - the modal is closed immediately, cancelling the action and the plant post remains in the database.

**Comments**
The comments section allows users to leave comments about specific plants. The aim is to increase user engagement and stimulate conversation. 

- All comments show username and date/time posted

- Comments are displayed, oldest to newest. This decision was based on [this post](https://ux.stackexchange.com/questions/38002/display-comments-order-best-practice) from Ux Stack Exchange in which it is conclued that reverse chronological order is more condusive to natural conversation.  

- If no user is logged in they will see:
  ![comments logged out](./static/images/readme_images/comment-logged-out.png)

  - The user must be logged in to comment as it shows who the comment is posted by to increase and accountability and allow for more developed conversation. 
  - Comments are visibile to all visitors as the provide futher information and encourage vistitors to make an account. 

- 

### Login Page

![Login responsive](./static/images/readme_images/responsive/login-responsive.png)

**Form**

- The login page features a simple form for user to enter their username and password.

- Python checks whether the password and passwords match what is held in the database.

- If both are correct:

  - user is directed to their profile page.

- If either are incorrect:
  - flash message is displayed "Incorrect username and/or password please try again.". It is not specified which is incorrect to increase security.

**Redirect Links**

- A link for the join page is provided "New? Join here ->" in case the user has found themself in the wrong place and needs redirecting.

### Join

![Join Responsive](./static/images/readme_images/responsive/join-responsive.png)

**Form**

- Similarly to the login page, a simple form is used for the user to enter a desired username and password.

- Users are asked to confirm password, (checked by Python). If the passwords don't match a flash message is displayed, "Passwords don't match, please try again"

- Tooltips are used to tell users what is required for a valid username and password.

- If user input does not meet requirements:

  - input field will be underlined in red
  - on submit, they will not be permitted to proceed.

- If the chosen username already exits in the database (checked by Python):

  - flash message will appear, "Username already in user, please try another".

- If user input meets all requirements:
  - input field will be underlined in green
  - on submit, user will be directed to their newly created profile page.

**Redirect Links**

- A link for the login page is provided "Already have an account? Login ->" in case the user has found themself in the wrong place and needs redirecting.

### User Profile Page

<i>Unable to provide responsive image due to necessity for session cookie</i>

**User's Plants list**

- The main purpose of the user profile page is to allow the user to see a list of the plants that they have posted. Users have the ability to edit and delete their own posts and this gives them easy access to do so.
- If the user has no plants to show they will see:

### Add Plant Page

### Edit Plant Page

## Features Left to Implement

- Pagination
- autofill search
- favourite
- water
- reply to comment
- page denied
- backend validation
- contact page
- reset password
- admin dashboard
- add postsed by?

## Technologies Used

### Languages

### Frameworks, Libraries & Programs Used

1. [Matarilize CSS](https://materializecss.com/)

   - Materlize CSS was used for styling, components and creating responivity on a range of devices

2. [Font Awesome:](https://fontawesome.com/)

   - Font Awesome icons were used throughout

3. [Git](https://git-scm.com/)

   - The Gitpod terminal from Git was used to commit to Git and Push to GitHub

4. [GitHub:](https://github.com/)

   - GitHub was used to store the code after being pushed from Git

5. [Google Fonts:](https://fonts.google.com/)

   - Google fonts was used to import the ‘Poppins’ font into the style.css

6. [jQuery:](https://jquery.com/)

   - jQuery was used in conjunction with Materlize CSS for interactive components

7. [Masonry](https://masonry.desandro.com/)

   - Masonry was used to create the cascading grid layout library when plant lists were used

8. [MongoDB:](https://www.mongodb.com/)

   - MongoDB was used to store and access all generated documents

9. https://imagesloaded.desandro.com/

10. [Slick Carousel](https://kenwheeler.github.io/slick/)

## Testing

### Validators

## -

### Testing User stories

#### First Time User Goals

1. As a First Time User, I want to easily understand the purpose of the website and the services it offers

   - The homepage heading clearly shows the website name, whilst the subheading provides information as to the purpose of the website "A community created guide to houseplant care."
   - The hero image clearly displays houseplants suggesting the nature of the website to the user

2. As a First Time User, I want to be able to navigate intuitively through the site

   - Upon entering the site, the navigation bar is positioned at the top of the page and unobstructed by any images. This makes it easy for users to locate and read
   - The navigation bar is stuck to the top of the screen so the user is always able to navigate wherever they are in the site
   - In accordance with UX expectancies the logo, in the right-hand corner, navigates users back to the homepage
   - All navigation links provide feedback to the user with hover overs, this makes them easily identifiable as links

#### Returning User Goals

1. As a Returning User, I want to browse plants

   -

2. As a Returning User, I want to search for plants

   - The homepage has a conveniently place search bar to allow users to start searching with out the need for redirection
   - The search bar has a modal tip to inform users of the available search terms
   - The Plants page also has a search bar to allow users to search from there

3. As a Returning User, I want to know which plants are easiest/most difficult to care for

   - Both the Plants page and the, more detailed, plant profile displays the given maintenance level of a plant
   - Users are able to search by maintenance level: Easy, medium or hard to provide them with options within their needs

4. As a Returning User, I want to find care instructions

   - A detailed care guide can be found by...

5. As a Returning User, I want to create my own posts

#### Frequent User Goals

1. As a Frequent User, I want to see the plants that I have posted

   -

2. As a Frequent User, I want to edit and delete my posts

   -

3. I want to discuss the plants with others in the community

4. As a Returning User, I want feedback on my posts

#### Site Owner Goals

1. ## As Admin, I want the ability to delete any posts deemed inappropriate or unnecessary

### Testing Interactive Elements

### Further Testing

### bugs

- on add plant the page may need a refresh for the new plant to appear
- defensive programming modal
- alt image sometimes shows due to lazy load. Trade off for faster load time so could be changed depending on priorities.

## Deployment

## Credits

https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown

https://kenwheeler.github.io/slick/

### Code

### Content

### Media

- https://tinypng.com/
- background img w3schools https://www.w3schools.com/howto/howto_css_hero_image.asp
- https://realfavicongenerator.net/
