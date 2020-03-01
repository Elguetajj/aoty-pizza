# Aoty pizza 💿🍕
This project aims to create music rating web app that will be connected to either the spotify or lastfm api. This application will allow users to rate, review, add as entries to a diary any album found on the api. 

## Overview

### Problem
1.	**No app exists to orderly keep track of albums:** whereas films have letterboxd, anime has myanimelist, and literature has goodreads music does not have a comprehensive app that allows users to keep track of the albums they review.
2.	**Other apps don’t have complete rating and reviewing systems 💯:** lastfm allows users to track the music they listen to, but they can only rate albums as favorite or not. It also does not support user generated reviews for albums. 
3.	**There are many non-supported formats 📻:** apps that automatically track the music their users listen to by linking their accounts to their spotify or apple music history don’t support manual entries. If users listen to physical formats or use other non-supported music apps such as Bandcamp, they cannot track this music.   

### Goals

1.	Creating an app that allows tracking non-supported formats
2.	Take advantage of pertinent data structures to gain performance and save up space


### Out of Scope:
1.	**Outstanding UI design:** for the scope of this project minimal UI is required. The main focus will be functionality.
2.	Deploying the app and getting certificates

## Context

### Use Cases 
1.	Users want to:
*	Tracking, rating, and reviewing albums
*	**Making lists:** making lists, and specially a list of music they plan on listening to is essential to users.
*   **Seeing user generated reviews and ratings:** generally, music criticism is left to the big magazines and some influential influencers. Democratizing music criticism can make up for more relevant and relatable points of view. 


## Proposal

### Technologies 👨‍💻: 
The app will consist of a frontend made in JavaScript and a Back-End made in Python 🐍. As the project advances a Redis implementation for caching and storing certain data might be implemented. 

### User Experience
1.	**Album view 💿:** an album specific view which contains the artwork five star buttons for rating, a heart button for additional rating, a text box for writing reviews and pertinent info about the album such as name, track list, artists, producers and a brief synopsis of the album. 
2.	**List view 📃:** a view for user created lists which show all of the albums chosen in a user specified order, each displayed with their artwork, name, artist name, and the rating given by the user. 
3.	**Home/profile view 🏠:** shows the history of the user and all of their playlists
4.	**Search 🔎:** a search page that allows to search for albums, artists, songs or lists

