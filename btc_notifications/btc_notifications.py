import requests
import time


BTC_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/bitcoin_price_emergency/with/key/eVhhWNGPuKX5G1z77llTDPCr5yTxsMmF-pcDUUgXuPn'
BTC_PRICE_UPPER_LIMIT = 10000
BTC_PRICE_LOWER_LIMIT = 5000


def get_latest_btc_price():
    response = requests.get(BTC_API_URL)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])


def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)


def main():
    while True:
        price = get_latest_btc_price()
        # Sends an emergency notification
        if price < BTC_PRICE_LOWER_LIMIT or price > BTC_PRICE_UPPER_LIMIT:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Checking every 10 minutes
        time.sleep(10 * 60)


if __name__ == '__main__':
    main()