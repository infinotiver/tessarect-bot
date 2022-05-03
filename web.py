#Dashboard under testing , Solve unauthorized for discord api error

from http import server
from threading import Thread
from shutil import ExecError
from django.shortcuts import render
from flask import *
import flask
from oauth import Oauth
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient

load_dotenv()

# Creating and Configuring the app
app = Flask(__name__)
app.config['SECRET_KEY'] = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"


# Intilize Database
db_url = os.environ['tst']
cluster = MongoClient(db_url)
database = cluster["Jarvis"]
welcome_collection = database["welcome"]
leave_collection = database["leave"]
basedb = database['flaskapp']



# Server
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/oauth/discord')
def oauth():
    # Authorization 
    code = request.args.get("code")
    token = Oauth.get_access_token(code)
    session['token'] = token
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect("https://discord.com/api/oauth2/authorize?client_id=916630347746250782&redirect_uri=https%3A%2F%2Ftessarect.prakarsh17.senarc.org%2F&response_type=code&scope=identify")

    user_data = Oauth.get_user_json(session.get('token'))
    user_guilds_data  = Oauth.get_user_guild(session.get('token'))
    bot_guilds = Oauth.get_bot_guilds()
    mutual_bot_guilds = Oauth.get_mutual_guilds(user_guilds_data, bot_guilds)
    return render_template('dashboard.html', guilds=mutual_bot_guilds, userdata=user_data)

@app.route('/guild/guild_id=<guild_id>')
def guild(guild_id: int):
    user_data = Oauth.get_user_json(session.get('token'))
    guild_info = Oauth.get_guild_data(guild_id, session.get('token'))
    channels = Oauth.get_channel_from_guild(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    return render_template('guilds.html', guild=guild_info, userdata=user_data, channel=channels)

@app.route("/forward/<guild_id>", methods=['POST'])
def move(guild_id:int):
    try:
        user_data = Oauth.get_user_json(session.get('token'))
        guild_info = Oauth.get_guild_data(guild_id, session.get('token'))
        channels = Oauth.get_channel_from_guild(guild_id)

        return render_template('update.html', guild=guild_info)
        
    except Exception as e:
        print(e)
    



def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()