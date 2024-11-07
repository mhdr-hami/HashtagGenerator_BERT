from bertopic import BERTopic


def funcion_model(theTweet, model_url, k):
    global model
    # Loading the last saved models.
    # with open(model_url, 'r') as file:
        # data = file.read()
        # lines = list(data.split(sep='\n'))
    # model = BERTopic.load(lines[0])

    # sentenceListTheTweet = list(theTweet.split("."))
    sentenceListTheTweet = []
    sentenceListTheTweet.append(theTweet)
    listOfAllHashtags = []
    usedHashtags = []

    for sentence in sentenceListTheTweet:

        representative_docs = []

        most_similar_topic, similarity = model.find_topics(sentence, top_n = 1)

        representative_docs.append(model.get_representative_docs(most_similar_topic))
        # Insering each sentence of the tweet to representative docs to extract hashtags from.
        if sentence not in representative_docs:
            representative_docs += sentenceListTheTweet

        # Extracting hashtags from theTweet and similar tweets to that in model 1.
        for doc in representative_docs:
            if isinstance(doc, str):
                listOfAllHashtags.append([item for item in hashtag_generator(sentence, doc, 3)])

                # Extracting used hashtags which are close to theTweet.
                # partsOfDoc = list(doc.split(" "))

                # for part in partsOfDoc:
                    # if part != '':
                        # if part[0] == '#':
                            # usedHashtags.append(part)
            else:
                # print(doc)
                pass
        
    finalHashtags = []
    for listItems in listOfAllHashtags:
        finalHashtags += sorted(listItems, reverse=True)

    finalHashtags = sorted(finalHashtags, reverse=True)[:k]

    return finalHashtags
    
