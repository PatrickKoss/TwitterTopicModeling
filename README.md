# Twitter Topic Modeling

Twitter Topic Modeling is a Python-based tool that leverages the power of Latent Dirichlet Allocation (LDA) to analyze and categorize Twitter tweets. This tool is designed to collect tweets and analyze them to identify the underlying topics. It's a great resource for researchers, data scientists, and anyone interested in natural language processing and topic modeling.

## Quick Start Guide

1. **Setup Python Environment**: Download and install Python 3 and pip 3 on your system.

2. **Twitter Developer Account**: Create a developer account on Twitter to get a consumer key and access token. Set these keys as your environment variables. They should be named as follows:
    - `tweepy_consumer_key`
    - `tweepy_consumer_key_secret`
    - `tweepy_access_token`
    - `tweepy_access_token_secret`

3. **Install Dependencies**: Install all necessary dependencies by running `pip install -r requirements.txt` in your terminal.

4. **Collect Tweets**: Navigate to the `TwitterModelingPython` directory and run the `TwitterAPI.py` script with the command `python3 TwitterAPI.py`. This script collects a single tweet every 2 seconds and saves it into a `tweets.csv` file.

5. **Train the Model and Analyze**: In the `TwitterModelingPython` directory, run the `LDAModel.py` script with the command `python3 LDAModel.py`. This will create the model and save it as `lda_model.sav`. You can load this model for future predictions using pickle.

## License

This project is licensed under the Apache-2.0 License.

## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

Please make sure to give a star ⭐️ if you like this project!
