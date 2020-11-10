# Houseplant Heroes

## Milestone Project 3: Data Centric Development - Code Institute

[Houseplant Heroes](https://houseplant-heroes.herokuapp.com/) was created as a response to the growing popularity of houseplants which, whilst aesthetically pleasing can often be difficult to maintain! The website allows users to access information on houseplant care as well as contribute their own insights and experiences.

## Table of Contents

1. [UX](#UX)
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

#### Colour Scheme

![Colour Scheme](./static/images/readme_images/colour-scheme.png)

- The colours were chosen to compliment the hero image used on every page of the site. The muted tones are unobtrusive so as not to detract from the natural colours provided by the plant images.

- The add and edit plant form input uses the Materialize CSS default, on click, colours. They provide users with visually recognisable validation feedback:

Green for go
![Colour Scheme](./static/images/readme_images/form-green.png)

Red for stop
![Colour Scheme](./static/images/readme_images/form-red.png)

#### Typography

- The Poppins font is used on all pages with Sans Serif as the back-up font due to it's clean presentation, the letters were also spaced apart by 2px to increase this effect.

- A range of font sizes and weights were used to denote importance.

- The white text used on the the hero image includes a text shadow to ensure readability.

#### Imagery

Hero Image

![Hero Image](./static/images/hero-img.png)

- The hero image is used on each page of the site to create consistency and promote lasting brand image. A liner gradient of (rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), is used to ensure content is visable on top.
- The hero image is resized on each page depending on the size of hero image content but is always recognisable as the same image.

Carousel

![Carousel](./static/images/readme_images/carousel.png)

- A [Materialize CSS Carousel](https://materializecss.com/carousel.html) is used to display the most recently added posts on the homepage.
- The carousel images state who the plant was posted by. The username was included to encourage users to post their own plants to be displayed on the front page.

#### Icons

#### Layout

-

### Wireframes

-

## Features

### Existing Features

- The website is responsive on a range of devices

- Users are able to create, read, update and delete
- All documents are stored in a [MongoDB]

## Comments

- the ability to edit a comment was deleted to...

### Features Left to Implement

- Pagination
- autofill search
- favourite
- water
- reply to comment

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

7. [Masonry]https://masonry.desandro.com/

   - Masonry was used to create the cascading grid layout library when plant lists were used

8. [MongoDB:](https://www.mongodb.com/)

   - MongoDB was used to store and access all generated documents

9. https://imagesloaded.desandro.com/

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

5. ## As a Returning User, I want to create my own posts

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
- carousel cuts off images

## Deployment

## Credits

https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown

### Code

### Content

### Media

- https://tinypng.com/
- background img w3schools https://www.w3schools.com/howto/howto_css_hero_image.asp
- https://realfavicongenerator.net/
