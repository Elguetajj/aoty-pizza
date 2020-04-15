import json
from datetime import datetime
from heaper import Heaper
from quicksorter import Quicksorter

class Albums:

    def __init__(self):
        self.__json = None
        self.__recent_albums = []
        self.__logged_albums = []
        self.getJson()
        self.filterAlbums()

    def getJson(self):
        with open('albums.json', 'r') as recent_tracks:
            self.__json = json.load(recent_tracks)

    def filterAlbums(self):
        albums:set = set()
        for item in self.__json['items']:
            album_name = item["track"]["album"]["name"]
            if album_name not in albums:
                albums.add(album_name)
                self.__recent_albums.append(item["track"]["album"])

    @property
    def recent_albums(self):
        return self.__recent_albums

    def getById(self,id):
        for album in self.__recent_albums:
            if album["id"] == id:
                return album

    def logAlbum(self, album_data:dict):
        album_data['timestamp'] = datetime.now()
        album_data['timestamp_string'] = str(datetime.now())


        print(album_data)
        self.__logged_albums.append(album_data)

    @property
    def logged_albums(self):
        return self.__logged_albums

    def sort_ascending(self):
        Heaper.heapSort(self.__logged_albums)
    
    def sort_descending(self):
        Quicksorter.quick_sort(self.__logged_albums,0,len(self.__logged_albums)-1)







