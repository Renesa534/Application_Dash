# Application_Dash

Performing Sentiment Analysis of the tweets from the twitter. Live twitter tweets are extracted and stored in a database. User could get the sentiment patterns of a particular search 
term and the historical sentiment information concerning that term. Time series graphs, dataframe(collecting the recent tweets) & a sentiment pie chart, that provides the quantity of positive
& negative elements, is visualized in dash application using Plotly. All the process occurs dynamically, with the evolving database.

Related search terms are also updated accordingly, and recent trending terms of Twitter are also suggested for users, to gain insights about the latest feed.

Live_Twittersentiment_graph.py- Main application code, which extracts the data from twitter database, then plot the plotly graphs, tables & pie-charts in an interactive dashboard.
Twitter_Streaming- This code is running in the background, to update the SQLite database continuously with live Twitter tweets.
cache.py- For caching purposes
config.py- It contains a bunch of stop-words.
