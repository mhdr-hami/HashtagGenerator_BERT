# Neural Hashtag Generator for Twitter

## Introduction

Twitter is one of the most popular platforms for sharing quick updates, news, opinions, and stories. With its short character limit, Twitter encourages people to get straight to the point, and hashtags make it even easier to connect tweets to larger conversations. By adding hashtags, users can instantly link their tweets to trending topics, making them easier to find and engage with. Hashtags also let anyone see what's trending globally or locally, while offering quick access to tweets on a specific topic.

One challenge, though, is that even if people are talking about the same topic, they often use different hashtags. For instance, during the "Tour de France" cycling race, some people might use `#tdf`, while others might prefer `#tourdefrance`, `#cycling`, or `#procycling`. This splits the conversation and makes it harder for people to find all the tweets on the topic. This project aims to solve that problem by developing a model that can suggest the best hashtags for any given tweet.

## Project Overview

Our model takes in a tweet and outputs a list of the top 10 relevant hashtags for it. Built using **BERTopic** and **Transformers** from **Hugging Face**, this model goes beyond just pulling words from the tweet itself. It "understands" the context and suggests hashtags that capture the tweet's main topic, even if those hashtags aren’t used in the tweet, or are used as separete words. 

### Why This Model is Useful:

- **Consistent Hashtag Use**: By suggesting the most relevant and popular hashtags, the model helps people use the same hashtags for similar topics, making it easier for users to find related tweets.
- **Better Discoverability**: This model can boost the reach of tweets by connecting them to the right hashtags, increasing the chances of being part of a trending topic.
- **Easier Topic Search**: Standardizing hashtags means users can find a comprehensive collection of tweets on a topic with just one search.

## How It Works

The big picture of idea and technologies used to develope this model:

- **Data Cleaning**: Since we're working with tweets, a crucial step is cleaning the data to remove elements like emojis, URLs, "RT" for retweets, "@" for mentions, and other extraneous characters.

- **Clustering Tweets in the Training Dataset**: We used sentence transformers to create tweet embeddings, then applied DBSCAN to cluster the tweets within this embedding space.

- **Topic Extraction for Input Tweet Using BERTopic**: With BERTopic, we developed a function that extracts the main topics discussed in a single tweet.

- **Identifying the Cluster of the Input Tweet**: We used sentence transformers again to embed the input tweet and identified the cluster that best matches its embedding.

- **Extracting Representative Tweets from the Cluster**: Leveraging DBSCAN, we developed a function to pull representative tweets from the cluster, aligning with the relevant topic.

- **Extracting Key Phrases from Representative and Input Tweets**: We used sklearn to identify key phrases from both representative tweets and the input tweet, creating a function to combine these phrases.

- **Returning the Top 10 Best Phrases**: Using cosine similarity, we selected the top hashtags from all candidates, producing the most suitable hashtags for the input tweet.

## Benefits

With this hashtag generator, Twitter users can feel confident that they’re using the best hashtags for their tweets. This doesn’t just help individual tweets reach a bigger audience; it also organizes Twitter’s vast amount of content more effectively, making it easier to find and follow trending discussions. This tool aims to make hashtagging easier, helping people connect to topics faster and boosting their chances of being part of a bigger conversation.
