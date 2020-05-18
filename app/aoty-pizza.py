from flask import Flask, render_template, url_for, request,redirect
import requests
import json
from albums import Albums
from datetime import datetime
from auth_token import AuthToken
import time


app = Flask(__name__)




token = AuthToken()


@app.route('/auth')
def auth():
    client_id = "26fd557b95a64a33ab3293032169caed"
    redirect_url = "http://localhost:5000/callback"
    scope = "user-read-recently-played user-read-private"
    return redirect(f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_url}&scope={scope}")

@app.route('/callback')
def callback():
    code = request.args.get('code')
    response = requests.post("https://accounts.spotify.com/api/token", data= {"grant_type": "authorization_code", "code": code, "redirect_uri": "http://localhost:5000/callback", "client_id":"26fd557b95a64a33ab3293032169caed", "client_secret":"e3f02f59f3464c529808ced058592312"}, headers= {"content-type":"application/x-www-form-urlencoded"})
    response = response.json()
    access_token = response['access_token']
    refresh_token = response['refresh_token']
    expires_in = int(response['expires_in'])
    token.overwrite_token(access_token,refresh_token,expires_in)
    print(f"timestamp{type(token.token_timestamp)}")
    print(f"token:{token.access_token}")
    print(f"refresh_token:{token.refresh_token}")
    print(f"expires_in:{token.expires_in}")
    
    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {token.access_token}"}
    r = requests.get(url= url, headers = headers)
    r = r.json()
    user_id = r["id"]
    user_albums.load_albums(user_id)
    print(user_albums.logged_albums)


    return render_template("callback.html")

@app.route('/refresh_token')
def refresh():
    # print("this should be the access token:"+token.access_token)
    now = datetime.now()
    timestamp = token.token_timestamp 
    now = int((now - timestamp).total_seconds())
    if token.access_token:
        if(now >= token.expires_in):
            response = requests.post("https://accounts.spotify.com/api/token", data= {"grant_type": "refresh_token", "refresh_token": token.refresh_token, "client_id":"26fd557b95a64a33ab3293032169caed", "client_secret":"e3f02f59f3464c529808ced058592312"}, headers= {"content-type":"application/x-www-form-urlencoded"})
            response = response.json()
            access_token = response['access_token']
            refresh_token = token.refresh_token
            expires_in = int(response['expires_in'])
            token.overwrite_token(access_token,refresh_token,expires_in)
        else:
            pass 
    return render_template("layout.html")



user_albums = Albums() 


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/dashboard')
def dashboard():
    key = request.args.get("key")
    if request.args.get("sort") == 'ascending':
        user_albums.sort_ascending(key)
        albums = user_albums.logged_albums

    elif request.args.get("sort") == "descending":
        user_albums.sort_descending(key)
        albums = user_albums.logged_albums

    else:
        albums = user_albums.logged_albums

    return render_template("dashboard.html", albums = albums ) 

@app.route('/albums')
def albumes():
    timestamp = int(time.time())
    url = f"https://api.spotify.com/v1/me/player/recently-played?type=track&limit=50&after={timestamp}"
    headers = {"Authorization": f"Bearer {token.access_token}"}
    r = requests.get(url=url, headers = headers)
    r = r.json()
    user_albums.setJson(r)
    url = f"https://api.spotify.com/v1/browse/new-releases?country=US&offset=0&limit=12"
    r = requests.get(url= url, headers= headers)
    r = r.json()
    user_albums.get_recent_releases(r)
    return render_template("albums.html", albums = user_albums.recent_user_albums_dict.values(), releases = user_albums.recent_releases_dict.values())

@app.route('/log')
def log():
    album = user_albums.getById(request.args.get('id'))
    return render_template("log.html", album = album)


@app.route('/log_entry', methods = ['POST'])
def log_entry():
    data = json.loads(request.data)
    print(data)
    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {token.access_token}"}
    r = requests.get(url= url, headers = headers)
    r = r.json()
    user_id = r["id"]
    user_albums.logAlbum(data, user_id)
    return render_template("layout.html")





    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0',debug=True)