from bertopic import BERTopic
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

models_history_url = "./HASHTopic_models_histoy.txt"


#Loading the last saved models.
with open(models_history_url, 'r') as file:
    data = file.read()
    lines = list(data.split(sep='\n'))
model_1 = BERTopic.load(lines[0])
model_2 = BERTopic.load(lines[1])
print("Logger: Models loaded.")


# Entering the starting information.
fineTune_cmd = input("Do you want to fine-tune the model on a new dataset and save it? [y/n]: ")


if fineTune_cmd == "y":

    # Reading dataset path.
    print("Dataset should be a .csv file, and tweets have to be in \"text\" column.")
    data_url = input("Enter the dataset path: ")

    # Read the dataset from the URL.
    data = pd.read_csv(data_url)
    print("Logger: Dataset read. Shaped :", data.shape , sep=" ")


    save_cmd = "n"
    while save_cmd != "y":

        # Fit and transform new dataset on each model
        topics_1, probs_1 = model_1.fit_transform(data.text)
        topics_2, probs_2 = model_2.fit_transform(data.text)
        ## nothing to do with these outputs??

        # Retrieving the topics info for new dataset.
        freq_1 = model_1.get_topic_info()
        print("Number of topics in model_1 (more specific one): {}".format(len(freq)))
        print(freq_1.head())
        ## printing new outputs to understand the quality. tc and td. ??

        freq_2 = model_2.get_topic_info()
        print("Number of topics in model_2 (more general one): {}".format(len(freq)))
        print(freq_2.head())
        ## printing new outputs to understand the quality. tc and td. ??

        # Ask for saving the model.
        save_cmd = input("""Do you want to save this fine-tuning or want to run again? [y/n] 
        (Due to the stochastic nature of UMAP, the results from BERTopic might differ even if you run the same code multiple times.)""")
        if save_cmd == "y":
            # Current date time in local system.
            datetime = datetime.now()
            name1 = "/content/drive/MyDrive/myModels/New model_1 saved {}".format(datetime)
            name2 = "/content/drive/MyDrive/myModels/New model_2 saved {}".format(datetime)
            model_1.save(name1)
            model_2.save(name2)

            # Write the new model's info in history file.
            f = open(models_history_url, "w")
            f.write(name1)
            f.write(name2)
            f.close()


# Enter the tweet that hashtags will be generated for.
theTweet = input("Enter the tweet: ")
sentenceListTheTweet = list(theTweet.split("."))
sentenceListTheTweet.append(theTweet)
listOfAllHashtags = []
listOfAllHashtags2 = []
usedHashtags = []


# Select most 3 similar topics to theTweet and each sentence in that, for each model.
avg_tweets_similarity_score_1 = 0
avg_tweets_similarity_score_2 = 0
avg_hashtags_similarity_score_1 = 0

for sentence in sentenceListTheTweet:

    representative_docs_1 = []

    most_similar_topic_1, similarity_1 = model_1.find_topics(sentence, top_n = 1)
    avg_tweets_similarity_score_1 += similarity_1

    representative_docs_1.append(model_1.get_representative_docs(most_similar_topic_1))
    # Insering each sentence of the tweet to representative docs to extract hashtags from.
    if sentence not in representative_docs_1:
        representative_docs_1 += sentenceListTheTweet
    
    # Extracting hashtags from theTweet and similar tweets to that in model 1.
    for doc in representative_docs_1:
        listOfAllHashtags.append([item for item in hashtag_generator(sentence, doc, 3)])

        # Extracting used hashtags which are close to theTweet.
        partsOfDoc = list(doc.split(" "))
        
        for part in partsOfDoc:
            if part != '':
                if part[0] == '#':
                    usedHashtags.append(part)



    representative_docs_2 = []
    
    most_similar_topic_2, similarity_2 = model_2.find_topics(sentence, top_n = 1)
    avg_tweets_similarity_score_2 += similarity_2

    representative_docs_2.append(model_2.get_representative_docs(most_similar_topic_2))
    # Insering each sentence of the tweet to representative docs to extract hashtags from.
    if sentence not in representative_docs_2:
        representative_docs_2 += sentenceListTheTweet 

    # Extracting hashtags from theTweet and similar tweets to that in model 2.
    for doc in representative_docs_2:
        listOfAllHashtags2.append([item for item in hashtag_generator(sentence, doc, 3)])   

        # Extracting used hashtags which are close to theTweet.
        partsOfDoc = list(doc.split(" "))
        
        for part in partsOfDoc:
            if part != '':
                if part[0] == '#':
                    usedHashtags.append(part)


# Logging the completion of hashtag generation.
print("Logger: Hashtags generated.")


# Logging the average of similarities for each model.
avg_tweets_similarity_score_1 /= len(sentenceListTheTweet)
print("Logger: Average similarity score of founded close tweets for model_1 outputs is: ", 
      avg_tweets_similarity_score_1, sep="")
avg_tweets_similarity_score_2 /= len(sentenceListTheTweet)
print("Logger: Average similarity score of founded close tweets for model_2 outputs is: ", 
      avg_tweets_similarity_score_2, sep="")


# Extracting top 3 hashtags of each part of tweet, model 1.
finalHashtags = []
for listItems in listOfAllHashtags:
    finalHashtags += sorted(listItems, reverse=True)[:3]

finalHashtags = sorted(finalHashtags, reverse=True)[:3]
print("Closest hashtags generated for your tweet in model 1 are: ", finalHashtags)


# Extracting top 3 hashtags of each part of tweet, model 2.
finalHashtags2 = []
for listItems in listOfAllHashtags2:
    finalHashtags2 += sorted(listItems, reverse=True)[:3]

finalHashtags2 = sorted(finalHashtags2, reverse=True)[:3]
print("Closest hashtags generated for your tweet in model 2 are: ", finalHashtags2)


# Printing the used hashtags in older tweets which are close to theTWEET.
print("Closest hashtags were used before: ", usedHashtags)

## CHECK IF THE NUMBER OF HASHTAGS IS OKEY. 27 HASHTAGS FOR 2 SENTENCE TWEET IN FINALS.
## AS A SOLUTION, OUTOUT THE TOP 10 OF THE FINALHASHTAGS.
## output = sorted(finalHashtags, reverse=True)[:10]
## output2 = sorted(finalHashtags2, reverse=True)[:10]
## print("Closest hashtags generated for your tweet in model 1 are: ", output)
## print("Closest hashtags generated for your tweet in model 2 are: ", output)
