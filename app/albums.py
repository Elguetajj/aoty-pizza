import json
from heaper import Heaper
from quicksorter import Quicksorter
import time
import os.path

class Albums:

    def __init__(self):
        self.__json = None
        self.__recent_user_albums = []
        self.__recent_releases = []

        self.recent_user_albums_dict = {}
        self.recent_releases_dict = {}

        self.__logged_albums = []
        self.__logged_albums_json = {}
        self.__album_names = set()

    def setJson(self, json):
        self.__json = json
        self.filterAlbums()

    @property
    def recent_releases(self):
        return self.__recent_releases

    def load_albums(self, user_id:str):
        if os.path.exists(f"./albums/{user_id}.txt"):
            with open(file= f"./albums/{user_id}.txt") as albums_file:
                albums = json.load(albums_file)
                self.__logged_albums = albums["albums"]

    def get_recent_releases(self, releases_json):
        for item in releases_json["albums"]["items"]:
            album_name = item["name"]
            if album_name not in self.__album_names:
                self.__album_names.add(album_name)
                self.__recent_releases.append(item)
                idd = item["id"]
                self.recent_releases_dict[f"{idd}"]=item

    def filterAlbums(self):
        for item in self.__json['items']:
            album_name = item["track"]["album"]["name"]
            if album_name not in self.__album_names:
                self.__album_names.add(album_name)
                self.__recent_user_albums.append(item["track"]["album"])
                idd = item["track"]["album"]["id"]
                self.recent_user_albums_dict[f"{idd}"]=item["track"]["album"]

    @property
    def recent_user_albums(self):
        return self.__recent_user_albums

    def getById(self,idd):
        print(idd)
        if idd in self.recent_releases_dict:
            return self.recent_releases_dict[idd]
        elif idd in self.recent_user_albums_dict:
            return self.recent_user_albums_dict[idd]

        # for album in self.__recent_user_albums:
        #     if album["id"] == id:
        #         return album
        
    def logAlbum(self, album_data:dict, user_id:str):
        album_data["timestamp"] = int(time.time()) 
        self.__logged_albums.append(album_data)
        self.__logged_albums_json["albums"] = self.__logged_albums
        with open(file= f"./albums/{user_id}.txt",mode="w") as albums_file:
            json.dump(self.__logged_albums_json, albums_file) 



    @property
    def logged_albums(self):
        return self.__logged_albums

    def sort_ascending(self,key):
        Heaper.heapSort(self.__logged_albums,key)
    
    def sort_descending(self,key):
        Heaper.heapSort(self.__logged_albums,key,True)







