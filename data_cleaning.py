import pandas as pd
import re

def remove_urls(text):
    url_pattern = re.compile(r'https//\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_retweet(text):
    text = str(text)
    return text.replace('RT @', "")

def remove_nan(text):
    text = str(text)
    return text.replace('nan', "")

def remove_at(text):
    text = str(text)
    return text.replace('@', "")

def remove_dot(text):
    text = str(text)
    text = text.replace('.', "")
    text = text.replace(':', "")
    text = text.replace('"', "")
    text = text.replace(',', "")
    return text


def remove_emogy2(data):
    emoj = re.compile("["
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U00002600-\U000026FF"  # Miscellaneous Symbols
        u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols And Pictographs
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


def remove_emogy(text):
    text = str(text)
    text = text.replace('🇺', "")
    text = text.replace('🎯', "")
    text = text.replace('💕', "")
    text = text.replace('🚨', "")
    text = text.replace('💙', "")
    text = text.replace('🏆', "")
    text = text.replace('🤩', "")
    text = text.replace('🎉', "")
    text = text.replace('👋', "")
    text = text.replace('🎂', "")    
    text = text.replace('➡️', "")
    text = text.replace('⬇️', "")
    text = text.replace('⬇', "")
    text = text.replace('⬆', "")
    text = text.replace('🍑', "")
    text = text.replace('☑️', "")
    text = text.replace('✔️', "")
    text = text.replace('✓', "")
    text = text.replace('❤️', "")
    text = text.replace('🔁', "")
    text = text.replace('💥', "")    
    text = text.replace('🤔', "")
    text = text.replace('👉', "")
    text = text.replace('🤙🏾', "")
    text = text.replace('🤙', "")
    text = text.replace('💝', "")
    text = text.replace('💯', "")    
    text = text.replace('🎶', "")    
    text = text.replace('🌎', "")
    text = text.replace('🔑', "")    
    text = text.replace('✔', "")
    text = text.replace('🇸', "")
    text = text.replace('📹', "")
    text = text.replace('🗓️', "")
    text = text.replace('⚡', "")
    text = text.replace('🔴', "")
    text = text.replace('📺', "")
    text = text.replace('😱', "")
    text = text.replace('🎆', "")
    text = text.replace('😍', "")
    text = text.replace('🦅', "")
    text = text.replace('🙏🏻', "")
    text = text.replace('👇🏻', "")
    text = text.replace('😐', "")
    text = text.replace('😂', "")
    text = text.replace('👀', "")
    text = text.replace('🤨', "")
    text = text.replace('🔊', "")
    text = text.replace('🤣', "")
    text = text.replace('👊', "")
    text = text.replace('🎺', "")
    text = text.replace('✅', "")
    text = text.replace('🚀', "")
    text = text.replace('🗳️', "")
    text = text.replace('*', "")
    text = text.replace('🔥', "")

    return text

##################################################################

# BrackObama's tweets dataset
df = pd.DataFrame(data=['1'], columns=['text'])
data_url = './drive/MyDrive/finalDatasets/BarackObama.text'

lines = []
with open(data_url, 'r') as file:
    data = file.read()
    lines = list(data.split(sep='\n'))    

for line in lines:
    if line == "" or line == "\n" or line == '                 ':
        lines.remove(line)

for line in lines:
    df2 = {'text': line}
    df = df.append(df2, ignore_index = True)

df['text'] = df['text'].apply(remove_urls)
df.to_csv('BarackObama_PP.csv', index = False)

## PART2
data_url = './BarackObama_PP.csv'
df = pd.read_csv(data_url)

# df.iloc[0] = "1"
df['text'] = df['text'].apply(remove_retweet)
df['text'] = df['text'].apply(remove_nan)
df['text'] = df['text'].apply(remove_at)
df['text'] = df['text'].apply(remove_dot)
df['text'] = df['text'].apply(remove_emogy)

df_2 = df.iloc[:4230, :]
print(df_2.head())
print(df_2.shape)
df_2.to_csv('BarackObama_PP2.csv', index = False)

##################################################################

# FoxNews's tweets dataset

df = pd.DataFrame(data=['1'], columns=['text'])
data_url = './drive/MyDrive/finalDatasets/FoxNews.text'

lines = []
with open(data_url, 'r') as file:
    data = file.read()
    lines = list(data.split(sep='\n'))

for line in lines:
    if line == "" or line == "\n" or line == '                 ':
        lines.remove(line)

for line in lines:
    df2 = {'text': line}
    df = df.append(df2, ignore_index = True)

df['text'] = df['text'].apply(remove_urls)
df.to_csv('FoxNews_PP.csv', index = False)

## PART2
data_url = './FoxNews_PP.csv'
df = pd.read_csv(data_url)

# df.iloc[0] = "1"
df['text'] = df['text'].apply(remove_retweet)
df['text'] = df['text'].apply(remove_nan)
df['text'] = df['text'].apply(remove_at)
df['text'] = df['text'].apply(remove_dot)
df['text'] = df['text'].apply(remove_emogy)

df_2 = df.iloc[:4287, :]
print(df_2.head())
print(df_2.shape)
df_2.to_csv('FoxNews_PP2.csv', index = False)

##################################################################

# Trump's tweets dataset

data_url = './Trump.csv'
df = pd.read_csv(data_url)
df2 = pd.DataFrame(data=df['text'], columns=['text'])

df2['text'] = df2['text'].apply(remove_urls)
df2['text'] = df2['text'].apply(remove_retweet)
df2['text'] = df2['text'].apply(remove_nan)
df2['text'] = df2['text'].apply(remove_at)
df2['text'] = df2['text'].apply(remove_dot)
df2['text'] = df2['text'].apply(remove_emogy)
df2['text'] = df2['text'].apply(remove_emogy2)

df2.to_csv('Trump_PP.csv', index = False)

## PART2
data_url = './Trump_PP.csv'
df = pd.read_csv(data_url)

df_2 = df.iloc[:13000, :]
print(df_2.head())
print(df_2.shape)
df_2.to_csv('Trump_PP_SMALL.csv', index = False)
