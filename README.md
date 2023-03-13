![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome jonathanwhitedev,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


# Python Jack BlackJack Game

View my live project here! [Santa's Big Christmas Quiz](https://jonathanwhitedev.github.io/santa-quiz/) 

Santa's Big Christmas Quiz is a interactive website based quiz that is readily available to provide fun Christmas themed quizes for all. Traditionally many office parties and family get togethers incorporate a quiz of some sort, and many have to make there own quiz from scratch, trawlliing the web to find questions and answers. This website aims to fill the gap for a lack of online quizes.

![Responsive Mockup](docs/screenshots/am-i-responsive.png)

The following responsive screensizes of my website can also be found here: (https://ui.dev/amiresponsive?url=https://jonathanwhitedev.github.io/voyager/index.html)

## User Stories and UX

- __As a visiting user, I would like Christmas themed quizes readily available.__

As part of the UX specification and planning phase it was noted that there is a lack of Chrismtas themed quizes on the web that are purely Chrismtas driven. The vast majority of those surveyed (100) agreed that there was no simple and fast solution to finding a christmas themed quiz online without spending a long time searching for one and very often eventually finding most sites were long winded, quizes generic and dated, or the questions were either too repetitive and easy. Santa's Big Christmas Quiz aims to fill the gap to being the best source for all christmas quiz content on the web.

- __As a visiting user, I would like free Christmas quizes.__

Over three quarters of those surveyed (100), also came to agreement there were not many quizes online that were free. Many required signing up, and/or applications that wanted money for generated quizes on apps through App Store or Google Play, of which many were very poorly rated. Santa's Big Christmas Quiz will remain free to all and readily available to all who seek it.

- __As a visiting user, I would like something easy to use.__

Another shortfall noted was that many quizes online were extremely spam orientated, with many adverts spilling into the quiz and detracting the user from reading them accurately. Even if some websites had little to no adverts, they were often jumbled and messy, or too full of distracting information that was not clean and easy to use. It was also observed that most users wanted a website that could be read on a mobile or tablet rather then a computer that had easy to read fonts no matter the display used. Almost all that were surveyed in the UX consulation stage agreed there was no one website that provided an easy to use quiz online.

- __As a visiting user, I would like to share my scores.__

Of half of the group surveyed, they agreed it would be useful to be able to share the scores via social media afterwards, a link is available to all who complete the quiz to post their scores and boast the best bragging rights at Christmas.


## Home Landing Page
The landing page provides a simple and clean layout with clear information on what the website offers. "Santa's Big Christmas Quiz" is displayed in large font with a cartoon Santa Claus displayed above. This is followed with a clickable button under the main heading texts of "begin" which sends the user through onto the next page and the start of the quiz. Subtle Christmas themed colours envoke the the memories and familiarity of the season. Lastly a footer of the social media links for Santa's Big Christmas Quiz is also provided on the landing page.

![Landing Page](docs/screenshots/home-page.png)

## Quiz Pages

The interactive quiz pages runs through 15 clear and easy to navigate random questions of 15 in total. There are 4 multiple choice options to chose for the questions and require clicking on the "Submit" button to get to the next question. Each page follows the last and has simple easy to read font.  

![Quiz Page](docs/screenshots/questions-page.png)

## Bad Santa! Result

"Bad Santa!" appears upon the end of the quiz if the user scores below half of the 15 questions correctly (0-7). A picture from the film "Bad Santa" accompanies the headed text with the score. A "Restart Quiz" button takes the user back to the homepage to begin the quiz again if they so choose. Another button "Check Answers" is provided for the user to check the correct answers. Lastly a footer of the social media links for "Share My Score" is also provided.

![Bad Santa Result](docs/screenshots/badsanta-result.png)

## Santa Baby! Result
"Santa Baby!" appears upon the end of the quiz if the user scores over half of the 15 questions correctly (8-14) But not all 15. A picture of Santa in sunglasses making okay hand gestures appears to accompany the headed text with the score. A "Restart Quiz" button takes the user back to the homepage to begin the quiz again if they so choose. Another button "Check Answers" is provided for the user to check the correct answers. Lastly a footer of the social media links for "Share My Score" is also provided.

![Santa Baby Result](docs/screenshots/santababy-result.png)

## You're A Winner! Result 
"You're A Winner!" appears upon the end of the quiz if the user scores all of the 15 questions correctly (15). A picture of a happy Santa with hands full of dollar bills appears to accompany the headed text with the score. A "Restart Quiz" button takes the user back to the homepage to begin the quiz again if they so choose. Another button "Check Answers" is provided for the user to check the correct answers. Lastly a footer of the social media links for "Share My Score" is also provided.

![You're A Winner Result](docs/screenshots/winner-result.png)

## Answer Page 
Clicking the "Check Answers" button as mentioned in the results pages, displays all the correct answers to the questions in the quiz. Another "Restart Quiz" button is provided.

![Answer Page](docs/screenshots/answers-page.png)

## Features 

Santa's Big Christmas Quiz includes the following;

### Existing Features

- __Images__

  - Featured on the landing page and scores pages.
  - A large cartoon Santa Claus appears on the landing page, confirming to the user they have landed on a website that is Christmas related.

  ![Santa Logo](docs/screenshots/santa-logo.png)

- __Variable Images and Texts__

  - Scores Pages each have a Santa Claus image and text depicting the mood of the score and of Santa, adding amusement to the user. These are:
  - "Bad Santa"

  ![Bad Santa](assets/images/bad-santa.jpeg)

  - "Santa Baby"

  ![Santa Baby](assets/images/good-santa.jpeg)

  - "You're A Winner" 

  ![Winner Santa](assets/images/winner-santa.webp)

- __Button__
  - A button is on every page and uses and stands out in a christmas red colour. This is site wide using the same styling and colour to reinforce that this is always a button.
 
  ![Button](docs/screenshots/buttons.png)

- __The Footer__ 

  - The footer section included in home and results pages gives links to the relevant social media sites for Santa's Big Christmas Quiz. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media where they can find out even more about Santa's Big Christmas Quiz and for sharing their scores.

  ![Footer](docs/screenshots/footer-social.png)

  - __Favicon Icon__ 

   - The Favicon Icon of Santa claus is displayed in the browser tab to confirm you are at the correct page for easier navigation when multiple tabs are open and adds usability and humour to the end user.

  ![Browser Icon](docs/screenshots/favicon-icon.png)

  - __Statistics Container__ 

  - This is a container in gold (#d7be69) displaying a rolling questions and correctly answered information to the user using javascript interaction.

  ![Statistics](docs/screenshots/statistics-container.png)

  - __Quiz Container__ 

  - This is a container in blue (#3b81d6c6) displaying the quiz questions and mutiple choice options to the user using javascript interaction.

  ![Questions](docs/screenshots/quiz-container.png)

- __Correct Answer Interaction__ 

  - When a user clicks an list item (question) that is correctly answered, an interaction appears highlighting to the user that the question is correct by filling the question item with a green colour temporarily before moving onto the next question.

  ![Correct](docs/screenshots/correct-answer.png) 

- __Incorrect Answer Interaction__ 

  - When a user clicks an list item (question) that is incorrectly answered, an interaction appears highlighting to the user that the question is incorrect by filling the question item with a red colour temporarily before moving onto the next question.

  ![Incorrect](docs/screenshots/wrong-answer.png)  


### Future features Left to Implement

- Future features will include a larger selection of questions. This is curently set to a bank of 15, but could be increaded to literally hundreds of populated multiple choice questions to keep the question bank varied and interesting for users that repeatedly visit.
- An about page section where by users can find out more from the creator and author of the website and get in touch.
- Questions that invlove even more interactivity, this can be done through animated questions, games related questions incorporating advanced JavaScript.
- A Childrens section of the quiz that would give Children under the age of 11 a chance to partake in the quiz in a fun and educational way with slightly easier questions and fun animations/images.


## Typography and Colour

- Typography was taken from Google Fonts using 1 base font, "Cormorant Garamond" and "Anton" for 1 text element for the score. I felt this complimented the Christmas theme well, was clean and clear to read and easily accessible. With colour schemes I chose to use 3 Christmas themed colours, Red, Gold and Blue. Being mainly primary colours these work very well together and make the style eye catching. These were applied using hex, red (#7c0017), gold (#d7be69) and blue (#3b81d6c6). Then Black (#000000) and White (#ffffff) were used for the typography for Questions and Buttons.

Google Fonts can be found here (https://fonts.google.com/)


## Wireframes
- I used Balsamiq for my wireframes and drew a rough design of what I wanted my website quiz to look like with accurate images and cartoons of Santa with relevant sizing. Due to limitations I wanted the wording to be bigger on the Opening text "Santa's Big Christmas Quiz" but with balsamiq it wasn't possible to make the main text big enough in the page, I made sure to carry this over into my website. You can see screenshots of these pages below.

Quiz Home Page
![Balsamic Home Page](docs/screenshots/Balsamic-screenshot-home.png)

Quiz Question Page
![Balsamic Question Page](docs/screenshots/Balsamic-screenshot-questions.png)

Result Page Bad Santa
![Balsamic Bad Santa Result](docs/screenshots/Balsamic-screenshot-badsanta.png)

Result Page Santa Baby
![Balsamic Santa Baby Result](docs/screenshots/Balsamic-screenshot-santababy.png)

Result Page You're A Winner
![Balsamic You're A Winner Result](docs/screenshots/Balsamic-screenshot-winnersanta.png)

Answer Page
![Balsamic Sign-Up](docs/screenshots/Balsamic-screenshot-answers.png)

## Technology
__Various technologies were used in the entire process of building this website as follows;__
- Balsamiq. This was used to make a rough template of the design of my website.
- GitHub. To build the repository for Voyager and lay the groundwork for its development and deployment of website.
- GitPod. Where the design came to life in the physical coding of the website building the files and folders and writing the code to commit back to GitHub. This beginning of this Readme file was written before coding took place and extra folders were added for HTML and Assets including CSS and media.
- HTML. The building block for all the code and written across 5 pages, index, about, spotlight, signup, welcome.
- CSS. The style of the website linked via stylesheets to the HTML code.
- JavaScript. Used for all the questions and variables of the quiz, including calculating the score through additions, changing the colour of the question "Green" for correctly answered and "Red" for incorrect answered questions. Additionally, functions were added to change the image and text depending on the Results score.
- Fontawesome. Used to take social media icons for the bottom of the results page.
- Google Fonts. All font styles were taken to add a more unique design.
- Google images. Images taken from searching for Santa cartoon images and of bad santa.
- W3 Validator. Used to ensure all HTML code was working with no errors.
- Jigsaw Validator. USed to ensure all CSS code met best practices and was working with no errors.
- Lightouse. Used to ensure testing of performance met expectations wit no severe errors or performance issues. 
- JS Hint. This was used to test the functionality of my javascript codes and functions and to ensure nothing was returning errors.

## Testing 

Overall, I am very happy with the testing outcomes with lighthouse, HTML, and CSS validation. Js Hint was an invaluable tool to help make sense of javascript when certain functions were not performing as expected and would give you guidance on how to fix or improve. I had a couple of intances where I had not properly assigned a function, so this as extremely handy as a reminder.
Jigsaw spotted anothe error I rectified where i was using "padding auto" on a button on line 210 of my CSS file which does nothing! This was swiftly removed as was causing validation issues.
I have tested this website on a macbook pro with a 32 inch external monitor, an Ipad Pro, and a Iphone 13 pro max. I have also used reponsive design in Google dev tools with other devices such as a Surface Duo, Samsung galaxy devices including the fold'.
The CSS code was written first and foremost for a smartphone to save on time and to also accept that many people now use hones as a preferred way to browse the web. The ability to be scaled up with media queries for bigger devices when required.I made one small media query to enhance playing the game on bigger devices past 750px width.

The website runs smoothly across all used devices with no glitches or errors.

### Performance Testing 

- Lighthouse (Chrome Dev Tools)
  - Some "Best Practices" issues were returned when passing through Lighthouse on google chrome dev tools [https://developer.chrome.com/docs/lighthouse/overview/] on both the index landing page and the quiz pages. However scores of over 97% were present throughout on Performance, Accessibility and SEO.
  - I addressed the issues with best practices by removing the font awesome cookies that was attached to the link and href of the index and quiz html pages. These were returning data that google lighthouse was scoring badly.
  - I addressed the issues further by adding "meta http-equiv="Permissions-Policy" content="interest-cohort=() on line 9 of index and quiz pages as previously lighthouse was reporting an issue with permissions policy. I found this added meta tag on google after searching for the problem. After adding this the errors went away.
  - With these updated changes the score was improved to 92% as you can see in the screenshots below: 

  Index Page
 ![Lighthouse Test](docs/screenshots/lighthouse-test-index.png)

  Quiz Page (Game Area)
 ![Lighthouse Test](docs/screenshots/lighthouse-test-js.png)

### JavaScript Testing 

- Js Hint
  - There were a few issues with JS hint i had to learn to encounter which are highlighted here:
  - I had forgotten in one instance to apply a function correctly on line 122 "initializeQuiz" this helped me realise i had forgotten to add an event listener, which was then swiftly added!
  - I kept getting a ES6 issue with using const variables in my code for the questions (19 errors!) i added /*jshint esversion: 6 */ on line 1 of the script.js and questions.js file after googling the issue whivh was only related to js hint. I left in place in the code as wasnt affecting the website.

  All JS code (Combined questions and functions pages)
 ![JS Hint Test](docs/screenshots/js-hint-testing.png)


### Validator Testing 

- HTML
  - No errors were returned when passing through the official ![W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjonathanwhitedev.github.io%2Fsanta-quiz%2F) on all pages of website as follows: 

 ![HTML](docs/screenshots/html-validation.png)
 

- CSS
  - No errors were found on completion when passing through the official ![(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjonathanwhitedev.github.io%2Fvoyager%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

  ![CSS](docs/screenshots/css-validation.png)
 

### Test Cases
__Index Page Testing:__
1. User hovers over on the Begin option on the landing index page. A curser pointer hand will be displayed. User should be redirected to Quiz start page first question when clicked upon. Working as expected every time.

 ![Begin Button](docs/screenshots/begin-button.png)
 ![Quiz Start](docs/screenshots/quiz-page-test.png)

 __Social Link Testing:__
 1. User hovers over any of the 3 social media links at bottom of page on Inde Landing page and also the Results pages of the end of the quiz. A curser pointer hand appears directly over the link.
 2. A pop up text also appears on hover that displays a message that the website will open on in a new tab. 
 3. When clicked upon any of the 3 links, it will open in a seperate new tab.
 4. All testing was completed, and all was working satisfactory.
 5. See Screenshots below of test outcomes.

 ![Social Link Test](docs/screenshots/footer-social.png)
 ![Social Link Test](docs/screenshots/social-media-links.png)

 __Quiz Button Testing:__
 1. User clicks on any answer button between (A-D) in the "Quiz" page, this was tested for fast accurate response to move to the next question.
 2. When user clicks on a correctly answered question the span of the button will change colour to 'Green' before moving to next question, this is working correctly only on the correct answers.
 3. When user clicks on a incorrectly answered question the span of the button will change colour to 'Red' before moving to next question, this is working correctly only on the incorrect answers.
 4. "Skip Question" button works to provide an easy way of skipping the question without answering it. This will prevent the user picking up any points and a total of none will be given if every question is subsequently skipped. This is working as expected.
 5. "Check Answers" button appears on the scorecard at the end of the quiz and works correctly, displaying all the correct answers for the questions in a new container.
 6. "Restart Quiz" also appears on scorecard and answer cards at the end of the quiz. These correctly move the user back to question 1 of the quiz.

![Button Test Colour Change Green](docs/screenshots/correct-answer-green.png)
![Button Test Colour Change Red](docs/screenshots/wrong-answer-red.png)

__Scoring System for Image and Text Scorecard Testing:__
 1. User plays the quiz of 15 questions and depending upon the results gets given a different image/text scorecard based on final calculation (3 Images/3 Texts total) All 3 of these outcomes have been tested extensively ranging from deliberately scoring every score between 1 -15 correctly with no issues found.
 2. If the player gets a score of 7 or less (<=7) BAD SANTA! appears with the image from the film bad santa.
 3. If the player gets a score of 14 or less (<=14) SANTA BABY! appears with the relavent image.
 4. If the player gets a maximum score of 15 (default score)) YOU'RE A WINNER! appears with the relavent image.

![BAD SANTA](docs/screenshots/badsanta-test.png)
![SANTA BABY](docs/screenshots/santababy-test.png)
![YOU'RE A WINNER](docs/screenshots/winner-test.png)

### Supported Browsers and Screen Sizes.
  - Testing was carried out on Google Chrome, Safari, and Mozilla Firefox. All rendered the content and was fast and reponsively across these browsers.
  - Testing was carried out on Macbook Pro M1, Ipad Pro, and Iphone 13 Pro Max models in personal collection. 
  - There is one media query stepping up sizes after hitting a minimum width of 750px. I designed this mostly as a mobile first application.

### Unfixed Bugs

There were no bugs present that were unfixed. There were some recommendations that there were some unused variables in JSHint however these are not being used as JavaScript functions but for styling purposes in CSS. 

## Deployment
  - The site was deployed to GitHub pages. The live link can be found here - https://github.com/jonathanwhitedev/santa-quiz

  __To deploy the project:__
   1. In the [GitHub repository](https://github.com/jonathanwhitedev/santa-quiz), Navigate to the settings tab (small red box in image below).
   2. Once in the settings, navigate to the pages tab on the left hand side.
   3. In the build and deployment section under Branch, select the "master" branch and click Save.
   4. Once the master branch has been selected, the page will be automatically refreshed and a display indicates the successful deployment and the link to the address as below (large red box).

   ![Deployment](docs/screenshots/repository-1.png)

__To open Gitpod and Voyager website preview:__
   1. In the [GitHub repository](https://github.com/jonathanwhitedev/santa-quiz), click the green Gitpod button. This will open GitPod.
   2. Once in GitPod, click the tab hamburger button in top left corner, navigate to Terminal and highlight and click "New Terminal".
   3. In the Terminal after gitpod/workspace/santa-quiz, type the following command "python3 -m http.server" and hit the enter key.
   4. Once entered correctly a pop up will appear in bottom left corner displaying a service port is available. Click "Open Browser" and the website preview will open in a brand new tab.
   5. All steps pictured below and highlighted in red boxes.

   ![Deployment](docs/screenshots/repository.png)
   ![Deployment](docs/screenshots/terminal-commands1.png)
   ![Deployment](docs/screenshots/terminal-command2.png)

### Extra Deployment Tasks
 __To run the website on a local screen:__
   1. Go to the [GitHub repository](https://github.com/jonathanwhitedev/santa-quiz).
   2. Once in there, click on the green Code button and Download ZIP.
   3. Extract the ZIP file on your local machine.
   4. Run the index.html file in a browser.
   5. All steps pictured below with red highlighted boxes.

   ![Deployment](docs/screenshots/local-website.png)

 __To clone the repo:__
   1. Go to the [GitHub repository](https://github.com/jonathanwhitedev/santa-quiz).
   2. Click on the green Code button and directly underneath as shown, copy the HTTPs link there.
   3. Open a GitBash terminal and navigate to the directory where you want to locate the clone.
   4. Type "git clone" and paste the copied HTTPs link, press the enter key to begin the clone process.

   ![Deployment](docs/screenshots/clone-repo.png)

## Credits 

I will firstly like to credit my fiancé, Toni, for this website and motivating me to get over the line and by taking on more domestic tasks! I was not in a particularly brilliant headspace with less then 2 weeks from finishing JS modules in the elearning to submission. I'd felt the strain of the learning and did not feel confident with handling javascript at all. She was very supportive and this quiz idea relating to christmas was hers. She had already made a question bank from the previous christmas for a company party backed up and saved in her work laptop. These answers were all verified and accurate and were extremely handy to use in this quiz! 

 I found a simple quiz project builder on google at https://simplestepscode.com/javascript-quiz-tutorial/ which helped find the basics of making this quiz and took my own spin on it with this finshed result. With thanks to them for their publication in helping me break it down step by step.

Lastly I would like to thank my mentor, Rohit, for helping impeccably as always with his wisdom and guidance which was very helpful and greatly appreciated indeed.

Content and media inspiration is as follows below;

### Content 

_ All of the ideas in relation to this quiz including format, image selection, colour schemes were all my own. However the following helped me get there:

- The social icons in the bottom of section of all pages were taken from [Font Awesome](https://fontawesome.com/)
- The webkit stroke function was found after heavy research in needing a solution to allow text to pop off the background to be unique and more readble against the background colours in the scorecards, this was found at (https://css-tricks.com/adding-stroke-to-web-text/) I then incorporated this into my css for my specific needs.

### Media

- All of the Images used on all pages were found on google images (http://google.co.uk/search) these were then resaved as different file names, as text was either in alternate language to english or had spaces and would fail testing or reading for other developers.

## Thank you for taking the time to view my README file, hope you enjoy the quiz! 

## Jonathan White