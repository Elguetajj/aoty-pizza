from flask import Flask, render_template, url_for, request,redirect
import requests
import json
from albums import Albums
from datetime import datetime

app = Flask(__name__)



#------------------------------------------------Beggining of work in progress -----------------------------------------------------------------------
code = ''
token = ''
expiration = 0
token_timestamp = None

@app.route('/auth')
def auth():
    client_id = "26fd557b95a64a33ab3293032169caed"
    redirect_url = "http://localhost:5000/callback"
    scope = "user-read-recently-played"
    return redirect(f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_url}&scope={scope}")

@app.route('/callback')
def callback():
    code = request.args.get('code')
    response = requests.post("https://accounts.spotify.com/api/token", data= {"grant_type": "authorization_code", "code": code, "redirect_uri": "http://localhost:5000/callback", "client_id":"26fd557b95a64a33ab3293032169caed", "client_secret":"e3f02f59f3464c529808ced058592312"}, headers= {"content-type":"application/x-www-form-urlencoded"})
    response = response.json()
    token_timestamp = datetime.now()
    token = response['access_token']
    code = response['refresh_token']
    expiration = int(response['expires_in'])

    print(f"token:{token}")
    print(f"refresh_token:{code}")
    print(f"expires_in:{expiration}")
    return render_template("home.html")

@app.route('/refresh_token')
def refresh():
    print(code)
    time_delta = (datetime.now()-token_timestamp).total_seconds
    if code is not '':
        if(time_delta >= expiration):
            response = requests.post("https://accounts.spotify.com/api/token", data= {"grant_type": "refresh_token", "refresh_token": code, "client_id":"26fd557b95a64a33ab3293032169caed", "client_secret":"e3f02f59f3464c529808ced058592312"}, headers= {"content-type":"application/x-www-form-urlencoded"})
        else:
            pass 
    return render_template("home.html")

#----------------------------------------------- End of Work in progress -----------------------------------------------------------------------------


user_albums = Albums() 


@app.route('/')
@app.route('/home')
@app.route('/dashboard')
def dashboard():
    if request.args.get("sort") == 'ascending':
        user_albums.sort_ascending()
        albums = user_albums.logged_albums

    elif request.args.get("sort") == "descending":
        user_albums.sort_descending()
        albums = user_albums.logged_albums

    else:
        albums = user_albums.logged_albums

    return render_template("dashboard.html", albums = albums ) 

@app.route('/albums')
def albumes():
    return render_template("albums.html", albums = user_albums.recent_albums)

@app.route('/log')
def log():
    album = user_albums.getById(request.args.get('id'))
    return render_template("log.html", album = album)


@app.route('/log_entry', methods = ['POST'])
def log_entry():
    data = json.loads(request.data)
    print(data)
    user_albums.logAlbum(data)
    return render_template("layout.html")





    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0')