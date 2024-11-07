from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def hashtag_generator (tweet:str, doc: str, top_n: int):
    n_gram_range = (1, 5)
    stop_words = "english"

    # Extract candidate words/phrases
    long_count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
    long_candidates = long_count.get_feature_names_out()
    candidates = []

    for item in long_candidates:
        
        listOfWords = list(item.split(" "))
        if len(listOfWords) == 1:
            random = ""
            random += listOfWords[0]
            candidates.append(random)
            # candidates.append(item)

        elif len(listOfWords) == 2:
            random = ""
            random += listOfWords[0] + " " + listOfWords[1]
            tmp_random = listOfWords[1] + " " + listOfWords[0]
            if not(tmp_random in candidates) and not(random in candidates):
                candidates.append(random)
                # candidates.append(item)

        elif len(listOfWords) == 3:
            random = ""
            random += listOfWords[0] + " " + listOfWords[2]
            tmp_random = listOfWords[2] + " " + listOfWords[0]
            if (tmp_random not in candidates) and (random not in candidates) and listOfWords[0] != listOfWords[2]:
                candidates.append(random)
            candidates.append(item)
        
        elif len(listOfWords) == 4:
            random = ""
            random += listOfWords[0] + " " + listOfWords[3]
            tmp_random = listOfWords[3] + " " + listOfWords[0]
            if (tmp_random not in candidates) and (random not in candidates) and listOfWords[0] != listOfWords[3]:
                candidates.append(random)

        elif len(listOfWords) == 5:
            random = ""
            random += listOfWords[0] + " " + listOfWords[4]
            tmp_random = listOfWords[4] + " " + listOfWords[0]
            if (tmp_random not in candidates) and (random not in candidates) and listOfWords[0] != listOfWords[4]:
                candidates.append(random)
        
    # hashtag_model = SentenceTransformer("all-MiniLM-L6-v2")
    hashtag_model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
    tweet_embedding = hashtag_model.encode([tweet])
    candidate_embeddings = hashtag_model.encode(candidates)
    
    distances = cosine_similarity(tweet_embedding, candidate_embeddings)

    keywords = sorted(zip(distances[0],candidates), reverse=True)[:top_n]
    # print(keywords)
    return keywords

