import requests 
import random
import time

form_link =  "https://docs.google.com/forms/d/e/1FAIpQLSfFCDhGgQNeNtk5joR5VE9pzym4v2BtYGjQ2XeVvAxEUmBz4Q/viewform"


name_data = "entry.663064494" #data fields
like_data = "entry.827354091"
no_spam_data = "entry.1028214941"

with open("names.txt", "r") as names:
  name_list = [name.strip("\n") for name in names] #list of all the names

spam_list = ["Ok", "Not ok"]

#===========================================================

x = 1

while True:
  name = random.choice(name_list) #randomizes data fields
  like = random.randint(1,11)
  no_spam = random.choice(spam_list)



  form_data = { #the data that we will send
  name_data: name,
  like_data: like,
  no_spam_data: no_spam
  }

  user_agent = {
    'Referer': "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfFCDhGgQNeNtk5joR5VE9pzym4v2BtYGjQ2XeVvAxEUmBz4Q/viewform",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
  }


  post = requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSfFCDhGgQNeNtk5joR5VE9pzym4v2BtYGjQ2XeVvAxEUmBz4Q/formResponse", data = form_data, headers = user_agent) #sending the request

  print(f"form spammed for the {x} time")
  x += 1
  time.sleep(random.randint(0,5)) #prevents u from getting caught and banned
