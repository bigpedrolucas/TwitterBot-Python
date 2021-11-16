import tweepy
import time

from tweepy.errors import TweepyException
from tweepy.models import Status

arquivo = open('frases.txt','r',encoding='UTF-8')
lista = arquivo.read()
lista = lista.split('\n')


lista_frases = list(filter(lambda x: x[0].lower() != '-', lista))
lista_respostas = list(filter(lambda y: y[0].lower() in '-', lista))

consumerkey = 'YOUR CONSUMER KEY'
consumerkey_secret = 'YOUR SECRET CONSUMER KEY'

acesstoken = 'YOU ACESS TOKEN'
acesstoken_secret = 'YOUR SECRET ACESS TOKEN'

auth = tweepy.OAuthHandler(consumerkey, consumerkey_secret)
auth.set_access_token(acesstoken, acesstoken_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search = ['apostas','ortegatips']

numeroTweets = 4

# Respondendo tweets
for tweet in tweepy.Cursor(api.search_tweets, lista_frases).items(numeroTweets):
    try:
        print('Tweet respondido de ' + tweet.user.screen_name + '\nTweet ID: ' + str(tweet.id))
        api.update_status(lista_respostas[0][1:], in_reply_to_status_id=tweet.id)
        time.sleep(3)
    except tweepy.Forbidden as e:
        print(e)
    except StopIteration:
        print('No tweets anymore')
        break

#Curtindo tweets
for tweet in tweepy.Cursor(api.search_tweets, search).items(numeroTweets):
    try:
        print('Tweet curtido de: ' + tweet.user.screen_name + '\nTweet ID: ' + str(tweet.id))
        tweet.favorite()
        time.sleep(3)
    except tweepy.Forbidden as e:
        print(e)
    except StopIteration:
        print('No tweets anymore')
        break