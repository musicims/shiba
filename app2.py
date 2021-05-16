from datetime import datetime
import os
import tweepy
#from kucoin.client import Client
from binance.client import Client
from binance.enums import *
from binance.websockets import BinanceSocketManager
from binance.exceptions import BinanceAPIException, BinanceOrderException
from twisted.internet import reactor
from keys import *
from functions import *

#wss://fstream.binance.com/ws/dogeusdt

# twitter api auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

#init binance keys
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

#init binance client
client = Client(api_key, api_secret)

#init DOGE price
doge_price = {'DOGEUSDT': none, error:False}

#init orderId
#order_id = buy_order['orderId']

def doge_trade_history(msg):
    '''define how to process incoming WebSocket messages'''
    if msg['e'] != 'error':
        print(msg['b'])
        doge_price['close'] = msg['c']
        doge_price['bid'] = msg['b']
        doge_price['last'] = msg['a']
    else:
        doge_price['error'] = True

# init kucoin client
#client = Client(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase)

# init twitter api
api = tweepy.API(auth, wait_on_rate_limit=True)

# choose terms to watch
terms = ['doge', 'dogecoin', 'Doge', 'Dogecoin', 'DOGE']

# create twitter stream listener
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # check tweet for terms
        term_used = find_terms(terms, status.text)
        # place a market order if term in tweet
        if term_used == True
            #init and start WebSocket
            bsm = BinanceSocketManager(client)
            conn_key = bsm.start_symbol_ticker_socket('DOGEUSDT', doge_trade_history)
            bsm.start()
            # wait for stream to have data
            while not doge_price['DOGEUSDT']:
            sleep(0.1)
            # check to make sure WebSocket is working
            #while True:
                #if doge_price['error']
                # stop and restart socket
                    #bsm.stop_socket(conn_key)
                    #bsm.start()
                    #price['error'] = False
            # get available balance for futures account
            balance = client.furtures_account_balance
            # set percentage of market order wanted to be placed
            portion_balance = float(balance['free']) * 0.95
            # Find the Stop Loss
            stop_loss = (((doge_price['bid']) * .01) - doge_price['bid'])
            # place the market order
            try:
                buy_order = client.create_order(symbol='DOGEUSDT', side='BUY', type='MARKET', quantity=portion_balance)
                print('Order sucessfully placed' buy_order)
            except BinanceAPIException as e:
                # error handling
                print(e)
            except BinanceOrderException as e:
                # order error handling
                print(e)
            #send alert about the order    
            send_alert('fork-elon alert!', 'Elon tweeted about dogecoin at {0}! Bought' buy_order['executedQty'] .format(str(datetime.now())))
            # Have stop loss waiting listener and execution
            if order_id != 'error'
                while not doge_price['last'] <= stop_loss:
                    try:
                        sell_order = client.create_oco_order(symbol='DOGEUSDT', side='SELL', type='MARKET', quantity=buy_order['executedQty'], stopPrice=stop_loss, stopLimitPrice=stop_loss)
                    
                    except BinanceAPIException as e:
                    # error handling
                    print(e)
                    except BinanceOrderException as e:
                    # order error handling
                    print(e)
            else
                print('Stop loss Order was not sucesfully placed')
            # order = client.create_market_order('DOGE-BTC', Client.SIDE_BUY, size=100)
            
        else:
            send_alert('fork-elon alert!', 'Elon tweeted, but not about dogecoin at {0}.'.format(str(datetime.now())))



# define streaming function
def streamtweets():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(follow=['44196397'])

# run streaming function
streamtweets()
