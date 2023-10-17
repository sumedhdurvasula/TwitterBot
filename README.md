# TwitterBot
I've created a Twitter bot that uses data and automation to help investors make informed decisions in the stock market. This bot levarages the yfinance library for stock data retrieval and tweepy to access the Twitter API. It sifts through the S&P 500 companies' real time performance data to find the stock that has increased the most everyday. Twitter's simplicity makes it a perfect spot to post this information. To ensure the bot operates reliably and consistently, I've deployed it on Google Cloud Run, taking advantage of its scalability and serverless architecture. Additionally, I've set up a scheduler to ensure that the bot runs at predefined intervals, keeping the Twitter feed updated with the latest stock insights.

The primary goal of this Twitter bot is to focus on identifying the sectors within the S&P 500 that are experiencing notable growth. This will hopefully empower investors with the knowledge and awareness needed to make more informed investment decisions.

# Check it out here:
 https://twitter.com/SANDP_500_Bot
