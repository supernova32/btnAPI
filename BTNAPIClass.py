__author__ = 'pato'

import jsonrpclib, json

class BTNAPIClass:
    key = "f55626b2101fff21666cd230c600eea7"
    api = jsonrpclib.Server("http://api.btnapps.net")
    #api = jsonrpclib.Server("http://de1.freedomvpn.info/test.php")

    def searchByName(self, name, max):
        result = self.api.getTorrentsSearch(self.key, {'series': name} , max)
        print result

    def userInfo(self):
        result = self.api.userInfo(self.key)
        print result

    def browse(self):
        result = self.api.getTorrentsBrowse(self.key)
        print result

    def searchByTVDBId(self, id, max):
        result = self.api.getTorrentsSearch(self.key, {'tvdb': id}, max)
        print result

    def searchByTVRageID(self, id, max):
        result = self.api.getTorrentsSearch(self.key, {'tvrage': id}, max)
        print result

    def searchByReleaseName(self, name, max):
        result = self.api.getTorrentsSearch(self.key, {'release': name} , max)
        nlist = list()
        for keys in result['torrents'].iterkeys():
            for nK in result['torrents'][keys].iterkeys():
                nlist.append(result['torrents'][keys][nK])


        #return result
        print nlist
        #.itervalues().next()


test = BTNAPIClass()
test.searchByReleaseName('House.S08E12', 4)
#test.searchByTVDBId('7325', 2)


