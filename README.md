This repository contains all the files regarding Backend Task1 (Python-Flask) of HPDF.

Prerequisites:

    • Python3 and Flask should be installed on your computer.

Note:

    In case any of the above is not installed on your computer, you may use the following links:
    • Download Python3 from https://www.python.org/downloads/
    • Flask installation guide: http://flask.pocoo.org/docs/0.12/installation/

Steps: 

        1. Download the task1.py and templates folder.
        2. Paste the task1.py and templates folder in the same folder.
        3. Run the task.py in the virtual environment.
        4. Follow the further instructions according to the tasks designated:

Note:                

     http://localhost:8080/ is just an example, use the default ports on your local machine which 
     can be seen once you run task1.py in the virtual environment.

Sub-task 1:
	
        Task: A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit with your own first name).
        
        Steps for execution:
          •  Enter http://localhost:8080/ in the search bar of your browser.


Sub-task 2:

        Task: Add a route, for e.g. http://localhost:8080/authors, which:
              1. fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
              2. fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
              3. Respond with only a list of authors and the count of their posts (a newline for each author).

        Steps for execution:
          • Enter http://localhost:8080/authors in the search bar of your browser.
          • The list of authors and the count of their posts will be displayed on the rendered HTML page.
		

Sub-task 3: 

        Task: Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

        Steps for execution:
          • Enter http://localhost:8080/setcookie in the search bar of your browser.
          • After entering the above URL, you will be redirected to the task1-3.html which is situated in the templates folder. 
          • The rendered html page will show that cookie is set, further, if you wish to read the cookie, you may “Click here to readt he cookie”.

Sub-task 4: 

        Task: Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

        Steps for execution:
          • Enter http://localhost:8080/setcookie in the search bar of your browser.
          • After entering the above URL, you will be redirected to the task1-3.html which is situated in the templates folder. 
          • The rendered html page will show that cookie is set. Click on “Click here to read the cookie.”.
          • After clicking on “Click here to read the cookie.”, you will be redirected to http://localhost:8080/getcookies, where you    will see the cookie.


Sub-task 5: 

        Task: Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed).

	Steps for execution:
          • Enter http://localhost:8080/robots.txt in the search bar of your browser.
          • The rendered HTML page will deny access.


Sub-task 6: 

        Task: Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.

	Steps for execution:
          • Enter http://localhost:8080/html in the search bar of your browser.
          • The rendered HTML page will contain a poem.


Sub-task 7: 

        Task: A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout. 

	Steps for execution:
          • Enter http://localhost:8080/input in the search bar of your browser.
          • Once the page loads, enter your name and click submit.
          • After clicking on submit, you will be directed to http://localhost:8080/outputwhich displays “Your name is displayed on the Terminal.”
          • Check your Terminal like cmd in which you started the virtual environment and executed the task1.py, the name you entered   will be displayed there.







	


