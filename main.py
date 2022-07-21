from flask import Flask,redirect, url_for,render_template,request
import tweepy

# Authorization Keys
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" 
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
callback_uri='oob'

app=Flask(__name__)

def get_auth():
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    
    # Calling api
    api = tweepy.API(auth)

    # returns authorized object
    return api

def get_images_using_keyword(hashtag):
    api=get_auth()
    images=[]
    for tweets in tweepy.Cursor(api.search_tweets,q=hashtag,count=30).items(200):
        # print(tweets.entities)
        if 'media' in tweets.entities:
            k=tweets.entities['media'][0]['media_url']
            images.append(k)
    
    return images
    # for i in images:
        # print(i)

@app.route('/home')
def hello():
    return render_template('home.html',sent=images)

@app.route("/login",methods=["POST","GET"])
def login():
    if(request.method=="POST"):
        form_data=request.form["nm"]
        image_url=get_images_using_keyword(form_data)
        # k=set(k)
        return render_template('home.html',sent=image_url)
    else:
        return render_template("/login.html")


@app.route('/about')
def about():
    return render_template('/about.html')

if __name__== '__main__':
    app.run(debug=True) 



