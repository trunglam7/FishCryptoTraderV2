import random as rnd
from enum import Enum
import pygame
import time
import requests as req
import math
import sys


#fish enviroment setup
tank_height = 550
tank_length = 1000
time_duration = 100

#fish location [x direction, y direction]
fish_loc = [tank_length / 2, tank_height / 2]

#fish speed
speed = 5

#fish diameter
radius = 10

#setting up colors
TANK_COLOR = (0, 224, 227)
FISH_COLOR = (255, 166, 0)
FONT_COLOR = (0, 0, 0)

#setting up API and coin list
response = req.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false')
response_json = response.json()
coinList = []
for coins in response_json:
    coinList.append(coins['id'])

#choose two random crypto tokens
leftString, rightString = rnd.sample(coinList, 2)
leftString = leftString.upper()
rightString = rightString.upper()

#enumerate directions
class Directions(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    IN = 5
    OUT = 6
    UPLEFT = 7
    UPRIGHT = 8
    DOWNLEFT = 9
    DOWNRIGHT = 0

#function to update fish location
def getFishLocation(dir):
    if dir == Directions.UP.value:
        if fish_loc[1] > radius:
            fish_loc[1] -= speed
        else:
            fish_loc[1] == radius

    elif dir == Directions.DOWN.value:
        if fish_loc[1] < tank_height - radius:
            fish_loc[1] += speed
        else:
            fish_loc[1] == tank_height - radius

    elif dir == Directions.LEFT.value:
        if fish_loc[0] > radius:
            fish_loc[0] -= speed
        else:
            fish_loc[0] == radius
        
    elif dir == Directions.RIGHT.value:
        if fish_loc[0] < tank_length - radius:
            fish_loc[0] += speed
        else:
            fish_loc[0] == tank_length - radius

    elif dir == Directions.UPLEFT.value:
        if fish_loc[0] > radius:
            fish_loc[0] -= speed * .7
        else:
            fish_loc[0] == radius
        if fish_loc[1] > radius:
            fish_loc[1] -= speed * .7
        else:
            fish_loc[1] == radius

    elif dir == Directions.UPRIGHT.value:
        if fish_loc[0] < tank_length - radius:
            fish_loc[0] += speed * .7
        else:
            fish_loc[0] == tank_length - radius
        if fish_loc[1] > radius:
            fish_loc[1] -= speed * .7
        else:
            fish_loc[1] == radius

    elif dir == Directions.DOWNLEFT.value:
        if fish_loc[0] > radius:
            fish_loc[0] -= speed * .7
        else:
            fish_loc[0] == radius
        if fish_loc[1] < tank_height - radius:
            fish_loc[1] += speed * .7
        else:
            fish_loc[1] == tank_height - radius

    elif dir == Directions.DOWNRIGHT.value:
        if fish_loc[0] < tank_length - radius:
            fish_loc[0] += speed * .7
        else:
            fish_loc[0] == tank_length - radius
        if fish_loc[1] < tank_height - radius:
            fish_loc[1] += speed * .7
        else:
            fish_loc[1] == tank_height - radius
        
            
    else:
        pass
        
    return fish_loc

def startFish():  

    #setting up pygame environment
    pygame.init()
    screen = pygame.display.set_mode([tank_length, tank_height])
    clock = pygame.time.Clock()
    font = pygame.font.Font('AlfaSlabOne-Regular.ttf', 32)
    running = True

    #counters to score
    leftCounter = 0
    rightCounter = 0
    leftCount = 0
    rightCount = 0
    
    #setting up font text and colors and positioning
    leftText = font.render(leftString, True, (0, 0, 0), None)
    rightText = font.render(rightString, True, (0, 0, 0), None)

    leftCountText = font.render(str(leftCount), True, (0, 0, 0), None)
    rightCountText = font.render(str(rightCount), True, (0, 0, 0), None)

    leftTextRect = leftText.get_rect()
    leftTextRect.center = (tank_length / 4, tank_height / 16)

    rightTextRect = rightText.get_rect()
    rightTextRect.center = (3 * tank_length / 4, tank_height / 16)

    leftCounterRect = leftCountText.get_rect()
    leftCounterRect.center = (tank_length / 4, tank_height / 8)

    rightCounterRect = rightCountText.get_rect()
    rightCounterRect.center = (3* tank_length / 4, tank_height / 8)

    #running the simulation
    while running:
        
        for event in pygame.event.get():
            #if exit button is pressed
            if event.type == pygame.QUIT:
                running = False
        
        #set framerate
        clock.tick(60)
        
        #set background color
        screen.fill(TANK_COLOR)

        #setting color to black
        leftText = font.render(leftString, True, (0, 0, 0), None)
        rightText = font.render(rightString, True, (0, 0, 0), None)
        leftCountText = font.render(str(leftCount), True, (0, 0, 0), None)
        rightCountText = font.render(str(rightCount), True, (0, 0, 0), None)

        #get the direction and update movement
        dir = rnd.randint(0, 9)
        pygame.draw.circle(screen, FISH_COLOR, getFishLocation(dir), radius)

        #update font colors to green if fish is on a certain side and time elapsed
        if fish_loc[0] < tank_length / 2:
            leftCounter += 1 / 60
            leftCount = math.trunc(leftCounter)

        else:
            rightCounter += 1 / 60
            rightCount = math.trunc(rightCounter)

        if leftCount >= time_duration or rightCount >= time_duration:
            if leftCount >= time_duration:
                leftText = font.render(leftString, True, (0, 255, 0), None)
                leftCount = time_duration
                rightCount = 0
            if rightCount >= time_duration:
                rightText = font.render(rightString, True, (0, 255, 0), None)
                rightCount = time_duration
                leftCount = 0
    
        #update text color
        screen.blit(leftText, leftTextRect)
        screen.blit(rightText, rightTextRect)
        screen.blit(leftCountText, leftCounterRect)
        screen.blit(rightCountText, rightCounterRect)

        #update the simulation
        pygame.display.update()

if __name__ == "__main__":
    argumentList = sys.argv[1:]
    print('Welcome to your Personal Crypto Trading Goldfish!')
    if len(argumentList) == 0:
        print('[DEFAULT] Speed:', speed)
        print('[DEFAULT] Time Duration:', time_duration)    
        startFish()
    else:
        for i in range(len(argumentList)):
            if argumentList[i] == '-s':
                speed = int(argumentList[i + 1])
            if argumentList[i] == '-t':
                time_duration = int(argumentList[i + 1])
        print('Speed:', speed)
        print('Time Duration:', time_duration)    
        startFish()