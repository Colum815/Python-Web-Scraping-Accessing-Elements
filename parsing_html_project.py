import re

from bs4 import BeautifulSoup

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
 19th Century,Folk Park,Thomas De Clare,Richard De Clare,O'Briens and MacNamaras"/>
  <meta name="author" content="Colum O Siochru" />
  <meta name="viewport" content="width = device-width, initial-scale=1" />
  <title>Bunratty Castle</title>
</head>

  <body>   <!--This is my main body that contains everything visual when the page is opened  -->


    <div class="main clearfix"> <!--This div contains the two column divs left and right -->
      <!--  -->
      <div class="main-container"> <!--This div contains left colums image and written content -->
        <div class="column-left">
          <h2>About the castle</h2>
          <a href="Images/Bunratty.jpg">
            <img src="Images/Bunratty.jpg" alt="Bunratty Castle."
          /></a>
         <aside>
       

            <p class="links">
              My favourite castle that I have visited is called Edinburagh
              Castle in Scotland. Built in 
              <a href="https://www.edinburghcastle.scot/" target="_blank"
                >11.03&</a
              >
              
            </p>
          </aside>
        </div>

      
        <div class="column-right hide-small"> <!--The hide-small class is for media query in CSS -->
          <h3>Plantation Families</h3>
     
        </div> 
        
       
      </div>
    </div>

    <footer> <!--Footer and Bottom Navigation -->
      <div class="main-container">
        <nav class="foot-nav four-links">
          <ul class="clearfix">
            <li><a href="index.html">Home</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="index.html">Terms and Conditions</a></li>
          </ul>
        </nav>
      </div>
    </footer>
  </body>
</html>



"""

""" 
CODE EXPLANATION:
I have copied in some html that I used on an old project for the purpose of accessing elements, extracting them and 
printing them to the console.

Beautiful Soup is imported to parse the HTML.

I have a class called ElementLocations dedicated to containing the locations of the element that I want to access. 
The reason for this class is that if the location changes on the website I only have to change the location 
in the variable in this class and not in any other function that interacts with it.

I have a class called RetrieveElements which contains all the functions and the constructor which contains the object of 
BeautifulSoup which I have named html_parser. Each function can now call on this to parse the html.

get_title: Access the contents of the title tag
The get_title function contains a variable which connects to the ElementLocations class and then using dot notation 
accesses the variable TITLE which contains the location of the tag. The variable in the constructor called html_parser 
is used to parse the html. I used the .string to print out only the content in the tag.

get_chosen_class: Access a particular class in a tag
The get_chosen_class function has a locator from the ElementLocations called CHOSEN_CLASS.
The variable in the constructor called html_parser is used to parse the html. The .attrs['class] accesses all the 
classes in the tag which are foot-nav and four-links.I only want to access the four_links class so I created a new list
which adds to the list once the class is not called foot-nav.

remove_symbol: 
Access the content of a link and fix the mistake. 
The content is meant to be the year 1103,but there 
is a dot and a symbol displayed by mistake.
This function removes the dot and symbol.

The remove_symbol function: The locator is accessed and the HTML is parsed as usual like in previous functions.
re is imported and a variable called matcher searches through the locator which is 11.03& to try and match 
the pattern to. I used a website called regexr to make a pattern for '11.03&'.I used brackets to create two groups 
group(0) is everything and group(1) is everything inside the brackets. This group(1) does not contain the symbol 
at the end. I had to use .replace() to replace the dot with an empty space. I have also achieved this by splitting
the content and removing the '&', I have left this commented at the end of the function.

"""


class ElementLocations:
    TITLE = 'head title'
    CHOSEN_CLASS = 'footer div nav'
    REMOVE_SYMBOL = 'aside p.links a'


class RetrieveElements:
    def __init__(self, page):
        self.html_parser = BeautifulSoup(page, 'html.parser')

    def get_title(self):
        locator = ElementLocations.TITLE
        content = self.html_parser.select_one(locator).string
        return content

    def get_chosen_class(self):
        locator = ElementLocations.CHOSEN_CLASS
        content = self.html_parser.select_one(locator).attrs['class']
        my_chosen_class = [c for c in content if c != 'foot-nav']
        return my_chosen_class[0]

    def remove_symbol(self):
        locator = ElementLocations.REMOVE_SYMBOL
        content = self.html_parser.select_one(locator).string
        pattern = '([0-9]+\.+[0-9]+)&'
        matcher = re.search(pattern, content)
        remove_comma = matcher.group(1).replace('.', '')
        return remove_comma
        # ----------EASIER OPTION FOR THIS FUNCTION--------
        # divide = content.split('.')
        # return f"{divide[0]}{divide[1].replace('&','')}"
        # -------------------------------------------------


"""
Three Objects are created from the RetrieveElements class and the HTML_CODE variable is passed to it.
Now that objects are created I can use these objects to access the functions in the class and store this process 
in a variable (Three Variables in total). Since I have returned the output in each function 
I must print the information out using print().
"""
title = RetrieveElements(HTML_CODE)
title_output = title.get_title()
print(title_output)

chosen_class = RetrieveElements(HTML_CODE)
chosen_class_output = chosen_class.get_chosen_class()
print(chosen_class_output)

remove_symbol = RetrieveElements(HTML_CODE)
remove = remove_symbol.remove_symbol()
print((remove))
