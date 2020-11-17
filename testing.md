## Houseplant Heroes Testing

- [Primary README.md file](./README.md)
- [View Website](https://houseplant-heroes.herokuapp.com/)

## Table of Contents

1. [Validators](#validators)
2. [User Stories](#testing-user-stoies)
   - [First Time User Goals](#first-time-user-goals)
   - [Returning User Goals](#returning-user-goals)
   - [Frequent User Goals](#frequent-user-goals)
   - [Site Owner Goals](#site-ownner-goals)
3. [Manual Testing](#manual-testing)

   - [Devices & Browsers](#devices-tested-on)
   - [User Testing](#testing)
   - [Testing Features](#testing-interactive-elements)

4. [Bugs](#bugs)

### Validators

- HTML: [W3C Markup Validator](https://validator.w3.org/#validate_by_input)

  - The use of Jinja in the html results in a number of errors in each file, all have been reviewed and deemed acceptable.

- CSS: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

- JavaScript: [JSHint](https://jshint.com/)

- Python:
  - [PEP8](http://pep8online.com/)
  - [Gitpod](https://gitpod.io/)

### Testing User stories

#### First Time User Goals

1. As a First Time User, I want to easily understand the purpose of the website and the services it offers

   - The homepage heading clearly shows the website name, whilst the subheading provides information as to the purpose of the website "A community created guide to houseplant care."

   - The hero image clearly displays houseplants suggesting the nature of the website to the user.

   - The promo section of the homepage describes to user's the main functionalities of the site.

2) As a First Time User, I want to be able to navigate intuitively through the site

   - Upon entering the site, the navigation bar is positioned at the top of the page and unobstructed by any images. This makes it easy for users to locate and read.

   - The navigation bar is fixed to the top of the screen so the user is always able to navigate wherever they are in the site.

   - In accordance with UX expectancies the logo, in the right-hand corner, navigates users back to the homepage.

   - All navigation links provide feedback to the user with hover overs, this makes them easily identifiable as links.

   - Active pages are hightlighted in the navbar to indicate to the user what page they are on.

#### Returning User Goals

1.  As a Returning User, I want to browse plants

    - If the user is logged out, buttons directing the user are visible. One of which directs users to the Plants Page.

    - The promo section of the homepage also invites users to browse all plants.

2.  As a Returning User, I want to search for plants

    - The homepage has a conveniently place search bar to allow users to start searching with out the need for redirection.

    - The search bar has a modal tip to inform users of the available search terms.

    - The Plants page also has a search bar to allow users to search from there.

3.  As a Returning User, I want to know which plants are easiest/most difficult to care for

    - Both the Plants page and the, more detailed, plant profile displays the given maintenance level of a plant.

    - Users are able to search by maintenance level: Easy, medium or hard to provide them with options within their needs.

4.  As a Returning User, I want to find care instructions

    - The plants profile provides a detailed care guide for each plant. This can be foud via links from the Plants Page card.

5.  As a Returning User, I want to create my own posts

    - The promo content on the homepage explains that an account is required to add plants.

    - Once an account has been created:

      - User will immediately be directed to their profile which contains links to add a plant

      - "Add Plant" will appear in the navbar

#### Frequent User Goals

1. As a Frequent User, I want to see the plants that I have posted

   - The user Profile Page lists the plant posts by created by the session user.

2. As a Frequent User, I want to edit and delete my posts

   - Edit and delete buttons are included on the Plant's Profile page.
   - These buttons are only visible if the post has been created by the session user or the user is Admin.

3. I want to discuss the plants with others in the community

   - The Plant Profile Pages include a comments section to allow users to leave any thoughts or queries they may have.

4. As a Returning User, I want feedback on my posts

   - The comments section allows for feedback to be given on a plant post.

#### Site Owner Goals

1. As Admin, I want the ability to delete any posts deemed inappropriate or unnecessary
   - Is the session user is "admin" delete buttons are visible on every Plant Profile that allow admin to remove that post. This is also true of comment posts.

### Manual Testing

#### Devices & Browsers

- The Website was tested on Google Chrome, Firefox, Microsoft Edge and Safari browsers.

- The website was tested on a variety of devices including; Desktop, Laptop, iPad mini, iPhone 7, iPhone 8, iPhoneX, Nokia E30 and Galaxy S20.

- It was also viewed on all devices and orientations available in Chrome DevTools.

#### User Testing

- Friends and family members viewed the site and provided feedback on bugs and UX issues.

#### Testing Features

**Elements on Every Page Desktop**

- Navbar

  - Hovering over each link confirms that the hover effect works as intended.

  - Confirmed on click:
    - **Houseplant Hero logo** takes user to homepage.
    - **Home** takes user to homepage.
    - **Plants** takes user to all_plants page.
    - **Login** takes user to login page.
    - **Join** takes user to join page.
  - Logging in, confirm that the navbar no longer displays the Log In or Join links but now displays Profile, Add Plant and Log Out.

  - Confirmed on click:
    - **Profile** takes user to their profile page.
    - **Add Plant** takes user to the add_plant page.
    - **Logout** triggers function to remove session user, logging them out and reverting navbar to logged out configuration.

### Bugs

- on add plant the page may need a refresh for the new plant to appear
- defensive programming modal for comments
- alt image sometimes shows due to lazy load. Trade off for faster load time so could be changed depending on priorities.
- space
- join max length
