import random
import tweepy
import time

from tweepy.errors import TweepyException
from tweepy.models import Status

arquivo = input("Arquivo para ser aberto: ")
print('\n')

try:
    file1 = open(arquivo,'r',encoding='UTF-8')
except FileNotFoundError as f:
    print('Arquivo não econtrado. Verifique se você digitou o nome ou o caminho correto.')

lista1 = file1.read()
lista1 = lista1.split('\n')

frases_responder = []
frases_curtir = []
frases_naocurtir = []
respostas = []

for tweet in lista1:
    if 'r=' in tweet:
        frases_responder.append(tweet[2:])
    if 'c=' in tweet:
        frases_curtir.append(tweet[2:])
    if '/' in tweet:
        frases_naocurtir.append(tweet[1:])
    if '-' in tweet:
        respostas.append(tweet[1:])

frases = frases_responder + frases_curtir

for i in range(len(frases_naocurtir)):
    frases_naocurtir.append(frases_naocurtir[i].lower())
    frases_naocurtir.append(frases_naocurtir[i].upper())
    frases_naocurtir.append(frases_naocurtir[i].capitalize())

print('Todas as frases para interagir: ' + str(frases))
print('Frases para serem respondidas: ' + str(frases_responder))
print('Frases para serem curtidas: ' + str(frases_curtir))
print('Frases para não curtir: ' + str(frases_naocurtir))
print('Frases de respostas: ' + str(respostas))
print('\n')

if '-p' in str(respostas):
    respostas = str(respostas)[2:-2].replace('-p', '\n')
    print(respostas)

consumerkey = input('API Key: ')
consumerkey_secret = input('API Key Secret: ')

acesstoken = input('Acess Token: ')
acesstoken_secret = input('Acess Token Secret: ')

vairesponder = int(input("\nDeseja responder os tweets? (0)Não (1)Sim: "))
vaicurtir = int(input("Deseja curtir os tweets? (0)Não (1)Sim: "))

print("\nIntervalo de tempo inicial/final")
time_init = int(input("inicio (segundos): "))
time_final = int(input("fim (segundos): "))


auth = tweepy.OAuthHandler(consumerkey, consumerkey_secret)
auth.set_access_token(acesstoken, acesstoken_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

while True:
    rc = random.choice(frases)
    for tweet in tweepy.Cursor(api.search_tweets, rc).items(1):
        time.sleep(random.randint(time_init, time_final))
        try:
            cstatus = api.get_status(tweet.id, tweet_mode="extended")
            text = cstatus.full_text

            if rc in frases_responder and vairesponder != 0:
                print('\nFrase buscada responder: ' + str(rc))
                api.update_status('@' + tweet.user.screen_name + ' ' + random.choice(respostas), in_reply_to_status_id=tweet.id)
                print('\nTweet respondido de ' + tweet.user.screen_name + '\nTweet ID: ' + str(tweet.id) +
                '\nTweet date: ' + str(tweet.created_at.strftime('%d/%m/%Y')))

                if vairesponder != 0 and vaicurtir == 0:
                    rc = random.choice(frases_responder)
                    continue
                if vairesponder == 0 and vaicurtir != 0:
                    rc = random.choice(frases_curtir)
                    continue
                if vairesponder != 0 and vaicurtir != 0:
                    rc = random.choice(frases)
                    continue

            time.sleep(random.randint(time_init, time_final))
            
            if rc in frases_curtir and vaicurtir != 0:
                for naointeragir in text:
                    if not any(x in naointeragir for x in frases_naocurtir):
                        print('\nFrase buscada curtir: ' + str(rc))
                        tweet.favorite()
                        print('\nTweet curtido de: ' + tweet.user.screen_name + '\nTweet ID: ' + str(tweet.id) + 
                        '\nTweet date: ' + str(tweet.created_at.strftime('%d/%m/%Y')))
                        time.sleep(random.randint(time_init, time_final))

                if vairesponder != 0 and vaicurtir == 0:
                    rc = random.choice(frases_responder)
                    continue
                if vairesponder == 0 and vaicurtir != 0:
                    rc = random.choice(frases_curtir)
                    continue
                if vairesponder != 0 and vaicurtir != 0:
                    rc = random.choice(frases)
                    continue

        except tweepy.TweepyException as e:
            print(e)
        except tweepy.Forbidden as e:
            time.sleep(random.randint(time_init, time_final))
            rc = random.choice(frases)
            print(e)
        except tweepy.Unauthorized as f:
            print(f)
        except StopIteration:
            print('No more tweets')
            break