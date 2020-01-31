# TwitterTopicModeling

> A tool that implement the Latent Dirichlet Allocation for Twitter Tweets.

##Quicks Start Guide
-	 Download and install python 3
-	 Download and install pip 3
-	 Get a twitter consumer key and access token by creating a developer account at twitter. Set the two pairs under your environmental variables. It should be named like `tweepy_consumer_key`, `tweepy_consumer_key_secret`, `tweepy_access_token`and `tweepy_access_token_secret`
-	 Install all dependencies by `pip install -r requirements.txt`
-	 Get Tweets
	-	Navigate to `TwitterModelingPython` and run the `TwitterAPI.py` script by the command `python3 TwitterAPI.py`. It will collect a single tweet every 2 seconds and save it into tweets.csv
-	Train the model and make analysis
	-	Navigate to `TwitterModelingPython` and run the `LDAModel.py` script by the command `python3 LDAModel.py`. This will create the model and save it into `lda_model.sav`. For future prediction you can load this model with `pickle`.