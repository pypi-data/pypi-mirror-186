import requests
import json
# add .parse in python3
import urllib

name = "nwebclient"

class NWebGroup:
    __client = None
    __data = None
    def __init__(self, client, data):
        self.__client = client
        self.__data = data
    def guid():
        return self.__data['guid']
    def title():
        return self.__data['title']
    def println(self):
        for key, value in self.__data.iteritems():
            print(key + ": " + value)
    def asDict(self):
        return self.__data;
    def docs(self):
        """
        :rtype: [NWebDoc]
        """
        contents = self.__client.req('api/documents/' + self.__data['group_id'])
        j =json.loads(contents);
        items = j['items'];
        #return j.items;
        return map(lambda x: NWebDoc(self.__client, x), items)
class NWebDoc:
    __client = None
    __data = None
    def __init__(self, client, data):
        self.__client = client
        self.__data = data
    def title(self):
        return self.__data['title']
    def name(self):
        return self.__data['name']
    def kind(self):
        return self.__data['kind']
    def content(self):
        return self.__data['content']
    def printInfo(self):
        s = "Doc-"+self.kind()+"(id:"+self.id()+", title: "+self.title()
        if (self.kind()=="image"):
            s+=" thumb: " + self.__data['thumbnail']['nn'] + " "
        s+=")"
        print(s)
    def id(self):
        return self.__data['document_id']
    def tags(self):
        return self.__data['tags']
    def println(self):
        print(self.__data)
        #for key, value in self.__data.iteritems():
        #    print key + ": " + value
    def downloadThumbnail(self, size = 'nn'):
        # TODO imple   
        path = 'image/'+self.id()+'/thumbnail/'+size+'/'+self.id()+'.jpg'
        return 0
    def setContent(self, content):
        self.__data['content'] = content
        self.__client.req('api/document/'+self.__data['document_id'], {
            'action': 'update',
            'content': content
        })
class NWebClient:
    __url = ""
    __user = ""
    __pass = ""
    ssl_verify = False
    def __init__(self, url, username = '', password = ''):
        """ Anstatt url kann auch ein Pfad zur einer JSON-Datei, die die Schluessel enthaelt, angegeben werden. """
        if (url[0] is '/'):
            j = json.loads(self.file_get_contents(url))
            self.__url = j['url']
            self.__user = j['username']
            self.__pass = j['password']
        else:
            self.__url = url
            self.__user = username
            self.__pass = password
    def file_get_contents(self, filename):
        with open(filename) as f:
            return f.read()
    def _appendGet(self, url, name, value):
        v = name + '=' + urllib.quote(value)
        if '?' in url:
          return url + '&' + v
        else:
          return url + '?' + v
    def reqToFile(self, path, name):
        url = self.__url + path
        url = self._appendGet(url, 'username', self.__user)
        url = self._appendGet(url, 'password', self.__pass)
        r = requests.get(url, stream=True, verify=self.ssl_verify) 
        if r.status_code == 200:
            with open(name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    def req(self, path, params = {}):
        if self.__user != "":
            params["username"]= self.__user
            params["password"]= self.__pass
        url = self.__url+path
        #print("NWEB-Client: " + url);
        res = requests.post(url, data=params, verify=self.ssl_verify)
        return res.text
    def doc(self, id):
        response = self.req("api/document/"+str(id), {format:"json"})
        #print(response)
        data = json.loads(response);
        return NWebDoc(self, data)
    def docs(self, q = ''):
        ja = self.req('w/api/docs?'+q);
        items = json.loads(ja)
        return map(lambda x: NWebDoc(self, x), items)
    def group(self, id): 
        data = json.loads(self.req("api/group/"+id, {format:"json"}))
        return NWebGroup(self, data)
    def getOrCreateGroup(self, guid, title):
        return "TODO"
    def downloadImages(self):
        # https://bsnx.net/4.0/w/api/docs?tag=Untertage
        docs = self.docs('kind=image&limit=1000')
        for doc in docs:
           self.reqToFile('image/'+str(doc.id())+'/orginal/web/'+str(doc.id())+'.jpg', str(doc.id())+ '.jpg')
           print("Download Image: " + str(doc.id()))

def metric_val(baseUrl, metricName, val):
    """ baseUrl: string = e.g. https://bsnx.net/metric-endpoint """
    requests.get(url=baseUrl, params= {'metric':metricName, 'val':val})
