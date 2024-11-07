import pandas as pd
import numpy as np
hashtag_model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

def remove_hashtag(text):
    text = str(text)
    return text.replace('#', '')


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def evaluate(setOfTweets, model_url):
    global model
    # imagin K is the number of recommended hashtags. for each k, for each tweet, 
    # extract k hashtags, compute the precision and recall at k, 
    # their number is the measure for that k
    
    precisionAtK = []
    recallAtK = []
    f1AtK = []
    simAtk = []

    AVGprecision = 0
    AVGrecall = 0
    AVGsimilarity = 0
    AVGf1 = 0
    j = 0

    

    for K in range(5, 10):
        
        numberofTotal = 300
        numberofTotal2 = 300
        j += 1
        precision = 0
        recall = 0
        similarity = 0
        f1 = 0

        for i in range(300):
            if ((i+1)/300)*100 % 10 == 0:
                print('percentage: ',((i+1)/300)*100, sep="")

            tweet = setOfTweets.iloc[i]['text']
            tweet = str(tweet)

            # remove original hashtags and save them.
            origins = []
            words = list(tweet.split(" "))
            for word in words:
                word = str(word)

                if word == '':
                    pass

                elif word[0] == '#':
                    origins.append(word)

            if len(origins) != 0:

                tweet = remove_hashtag(tweet)

                # run the model for the tweet and extract K hashtags.
                predicts = [item[1] for item in funcion_model(tweet, model_url, K)]


                # compare these K hashtags with the original ones
                # and calculate the precision and recall.
                precision += len(intersection(origins, predicts))/len(predicts)
                recall += len(intersection(origins, predicts))/len(origins)
                f1 += (2*recall*precision) / (recall+precision+0.000001)

                tweet_embedding = hashtag_model.encode(origins)
                candidate_embeddings = hashtag_model.encode(predicts)

                try:
                    distances = cosine_similarity(tweet_embedding, candidate_embeddings)
                    similarity += np.mean(distances>0.35)
                except:
                    numberofTotal2 -= 1
                    print(origins)
                    print(predicts)
            else:
                numberofTotal -= 1


        precision /= numberofTotal
        precisionAtK.append(precision)
        AVGprecision += precision

        recall /= numberofTotal
        recallAtK.append(recall)
        AVGrecall += recall

        f1 /= numberofTotal
        f1AtK.append(f1)
        AVGf1 += f1


        similarity /= numberofTotal2
        simAtk.append(similarity)
        AVGsimilarity += similarity

        print(K)
        print('###############################')


    AVGprecision /= K
    AVGrecall /= K
    AVGf1 /= K
    AVGsimilarity /= j

    return AVGrecall, AVGprecision, AVGf1, AVGsimilarity, recallAtK, precisionAtK, f1AtK, simAtk


eval_dataset = pd.read_csv('./theTestHashtags.csv')
model_url = './model_url.txt'

AVGrecall, AVGprecision, AVGf1, AVGsimilarity, recallAtK, precisionAtK, f1AtK, simAtk = evaluate(eval_dataset, model_url)
print('avg recall: ', AVGrecall, sep="")
print('####')
print('avg precision: ', AVGprecision, sep="")
print('####')
print('avg f1: ', AVGf1, sep="")
print('####')
print('avg SIMILARITY: ', AVGsimilarity, sep="")
print('####')
print('recall@K list: ', recallAtK, sep="")
print('####')
print('precision@K list: ', precisionAtK, sep="")
print('####')
print('f1@K list: ', f1AtK, sep="")
print('SIMILARITY@K list: ', simAtk, sep="")
print('####')
