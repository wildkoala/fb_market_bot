# FLIP SOURCING
from selenium import webdriver 
from time import sleep 
  
# INTERACTION WITH FB MARKETPLACE

# go to facebook market place
driver = webdriver.Chrome() 
driver.get('https://www.facebook.com/marketplace') 
print ("Opened facebook marketplace") 
sleep(1) 

# get user login info
usr=input('Enter Email Id:\n> ')  
pwd=input('Enter Password:\n> ') 

# put in email address
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 

# put in password
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 

# click login button
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("Logged In") 

# read first fb marketplace listing
	# Get the name of it
	# Get the price
	
# search ebay for it - pretty sure there's an api for this too
# findCompletedItems is the name of the call on Ebay's API
# i can make 5,00 calls to ebay per day. That should be more than enough.
'''
https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems
   &SERVICE-VERSION=1.0.0
   &SECURITY-APPNAME=YourAppID
   &RESPONSE-DATA-FORMAT=XML
   &REST-PAYLOAD
   &keywords=commodore%20vic-20
'''

# sanbox endpoint: https://svcs.sandbox.ebay.com/services/search/FindingService/v1

	# Give the name
	# Check the listings that have sold in the past month.
	# Calculate the average price of these


# check if the listing is 20% lower than the average
	# of the last 5 of them sold on ebay (shipping + cost)
# send me a text saying that we've got a potential flip:
	# include the name of the item
	# price they are asking
	# average price on ebay
# send a message to the seller offering them the Ebay average * .75

# I can make this thing more aggressive by sending a message
# To every listing offering them the 75% of ebay price no matter what they listed it for.



# INTERACTION WITH EBAY	
# go to ebay
# login to Ebay
# search for the item keyword
	# take the past 5 listings that have a condition of NOT "Parts Only"
	# Get the price it sold for
	# Get the cost of shipping


# SENDING MESSAGES TO ME
# setup a gmail account for this
# login to gmail
# send myself an email 
	# the title is the listed item
	# Then include the a message with what the item is
	# What it has been selling for on average on ebay
	# What it's being offered for on fb marketplace
	# Send the amount difference and percent margin in "()"
	# How many minutes away they are
	# Display the ebay listings that it averaged at the bottom
	
===========================================================================

# MAKING A SALE
# Login to ebay
# Post the item for 90% of the average sale price
# Put up the listing

# STORING RESULTS
# Get the price that I bought it for on fb marketplace
# Get the price it sold for on Ebay
# Write results to a file
	# Go to the next available line
	# write in the name of item, bought for, sold for, margin, etc.
	
	

