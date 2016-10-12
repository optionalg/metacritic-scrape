#!/usr/bin/env python3

from flask import Flask
import metacritic

app = Flask(__name__)

@app.route('/')
def hello():
    return(u'Hello World!')

@app.route('/games', methods=['GET'])
def get_games():
    return(','.join(metacritic.topps3games()))

@app.route('/games/<string:name>', methods=['GET'])
def get_game(name):
    #Get a copy of the array of games
    gamearray = metacritic.topps3games()
    #Loop throught the array searching for the given string
    for i in range(len(gamearray)):
        if '"title": "' + name + '"' in gamearray[i]:
            return(gamearray[i])
    #If nothing found, return 'not found'    
    return(u'Game not found')

if __name__ == '__main__':
    app.run()
