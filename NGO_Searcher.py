
# coding: utf-8

# In[121]:

#----------------------Get info from Twitter through Tweepy----------------------#
import tweepy

#Create variables for each key, secret, token.
consumer_key = 'hrABYWoeNcdDgyMYUPqlcITNi'
consumer_secret = '8KkiJEgeJySQ8ZFDA2ywHPx2cagifHqiXS7jxcsCWDtLPGV59K'
access_token = '838796084038230016-L8xC5JUjkDxUvfNJR4iZACE5QIKlXMG'
access_token_secret = 'jhQC3kWgc8SbkmlMnJ5965UDddeV61EbGbqcUnfzI3DuQ'

#Set up OAuth and integrate with API.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[122]:

#Search for users.
def get_user(keyword):
    ulist = []
    for i in range(3):
        ulist.append(api.search_users(keyword, 20 ,i))
    return ulist


# In[123]:

from flask import Flask, abort, request, render_template
from uuid import uuid4
import requests
import requests.auth
import urllib
import string
import random
import tweepy


# In[124]:

app = Flask(__name__)

# Search bar
@app.route('/', methods=['GET', 'POST'])
def homepage():
    text = '<a href="%s">Search for NGOs on Twitter</a>'
    return render_template("index.html")

@app.route("/search/", methods=['GET','POST'])
def search():
    location = request.form.get('location')
    user_list = get_user(str(location)+"+ non profit")
    return render_template('users.html', user_list=user_list,location = location)

if __name__ == '__main__':
    #from werkzeug.serving import run_simple
    #run_simple('localhost', 9000, app)
    app.run()


# In[ ]:
