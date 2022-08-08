# Fish Crypto Trader V2
- Don't want to think about what cryptocurrency to buy next? Don't worry, let a fish decide your financial future!
- Disclaimer: The fish nor it's creator are not financial experts or advisors. The fish is merely for entertainment purposes. Always invest at your own risk.
- About: the fish will move in random directions (left, right, down, up, in, out, and the diagonals) on a set speed. There will be two random cryptocurrencies pulled from the coingecko api and displayed on the two sides. Which ever side the fish is on, the cryptocurrecncy will acculumate points based on seconds. Which ever side accumulates the set time duration first will be declared the winner. 
- This project was inspired by Michael Reeves's "I Gave My Goldfish $50,000 to Trade Stocks" YouTube video: https://www.youtube.com/watch?v=USKD3vPD6ZA
## Prequisites:
```
pip install pygame
pip install requests
```
## Script Commands (default speed: 5, default time duration: 100):
```
python ./crypto_fish_v2.py
```

## Optional Operators:
```
-s [SPEED VALUE OF FISH (INTEGER or FLOAT)]
-t [TIME DURATION (SECONDS)]
```

## Example (speed: 5, time duration: 100):
```
python ./crypto_fish_v2.py -s 5 -t 100 
```
