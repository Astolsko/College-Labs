import numpy as np
import pandas as pd

df = pd.read_csv('spam.csv',encoding='ISO-8859-1')

df.head()

df.info()

df.isnull().sum()

df.drop(columns = ['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace = True)

df.rename(columns={'v1':'target','v2':'text'},inplace= True)
df.head()

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['target'] = encoder.fit_transform(df['target'])

df.isnull().sum()

df.duplicated().sum()

df.head()

df = df.drop_duplicates(keep = 'first')

df.duplicated().sum()

df.head()

df['target'].value_counts()

import matplotlib.pyplot as plt
plt.pie(df['target'].value_counts(),labels=['ham','spam'],autopct='%0.2f')
plt.show()

import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Manually create a tokenizer
tokenizer = PunktSentenceTokenizer()

text = "Hello, this is a test. How are you?"
sentences = tokenizer.tokenize(text)
print(sentences)

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

# Test word tokenization
text = "Hello, this is a test. How are you?"
words = word_tokenize(text)

print(words)

df['num_characters'] = df['text'].apply(len)

df.head()

df['num_words'] =df['text'].apply(lambda x:len(word_tokenize(x)))

df.head()

df['num_sentences'] = df['text'].apply(lambda x:len(nltk.sent_tokenize(x)))
df.head()

df[['num_characters','num_words','num_sentences']].describe()

#ham
df[df['target'] == 0][['num_characters','num_words','num_sentences']].describe()

#spam
df[df['target'] == 1][['num_characters','num_words','num_sentences']].describe()

import seaborn as sns
sns.histplot(df[df['target'] == 0]['num_characters'])
sns.histplot(df[df['target'] == 1]['num_characters'],color = 'red')

import seaborn as sns
sns.histplot(df[df['target'] == 0]['num_words'])
sns.histplot(df[df['target'] == 1]['num_words'],color = 'red')

sns.pairplot(df,hue='target')

sns.heatmap(df[['target','num_characters','num_words','num_sentences']].corr(),annot= True)
#there is high correlation between these columns so we will remove the columsn and
#now we will go onto data preprocessing

### data preprocessing
'''
lower case
tokenizations
removing special characters
removing stop words and puntuations
stemming
'''

#nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')

import string
string.punctuation

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
ps.stem('loving')

def transform_text(text):
    y = []
    text = text.lower()
    text = nltk.word_tokenize(text)
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

transform_text("Hi how are you Saahil")

df['transformed_text'] = df['text'].apply(transform_text)

df.head()

from wordcloud import WordCloud
wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')

spam_wc = wc.generate(df[df['target'] ==1]['transformed_text'].str.cat(sep=" "))

plt.imshow(spam_wc)

ham_wc = wc.generate(df[df['target'] ==0]['transformed_text'].str.cat(sep=" "))

plt.imshow(ham_wc)

spam_corpus = []
for msg in df[df['target'] ==1]['transformed_text'].tolist():
    for word in msg.split():
        spam_corpus.append(word)

len(spam_corpus)
from collections import Counter

counter_df = pd.DataFrame(Counter(spam_corpus).most_common(30), columns=['Word', 'Frequency'])

# Plot using seaborn
plt.figure(figsize=(10, 5))
sns.barplot(x='Word', y='Frequency', data=counter_df)
plt.xticks(rotation=90)  # Rotate labels vertically
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 30 Most Common Words in Spam Corpus")
plt.show()

ham_corpus = []
for msg in df[df['target'] ==0]['transformed_text'].tolist():
    for word in msg.split():
        ham_corpus.append(word)

len(ham_corpus)

counter_df = pd.DataFrame(Counter(ham_corpus).most_common(30), columns=['Word', 'Frequency'])

# Plot using seaborn
plt.figure(figsize=(10, 5))
sns.barplot(x='Word', y='Frequency', data=counter_df)
plt.xticks(rotation=90)  # Rotate labels vertically
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 30 Most Common Words in Spam Corpus")
plt.show()

"""Model Building"""

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = CountVectorizer()
tfidf = TfidfVectorizer()

X = tfidf.fit_transform(df['transformed_text']).toarray()
print(X)

y = df['target'].values

print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score

gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()

gnb.fit(X_train,y_train)
y_pred1 = gnb.predict(X_test)
print(accuracy_score(y_test,y_pred1))
print(confusion_matrix(y_test,y_pred1))
print(precision_score(y_test,y_pred1))

mnb.fit(X_train,y_train)
y_pred2 = mnb.predict(X_test)
print(accuracy_score(y_test,y_pred2))
print(confusion_matrix(y_test,y_pred2))
print(precision_score(y_test,y_pred2))

bnb.fit(X_train,y_train)
y_pred3 = bnb.predict(X_test)
print(accuracy_score(y_test,y_pred3))
print(confusion_matrix(y_test,y_pred3))
print(precision_score(y_test,y_pred3))


from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)