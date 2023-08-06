# NWeb Client 

Client to access the NWeb-API


## Installation
```
pip install --upgrade nwebclient

```

```
python -m nwebclient help
```


## Beispiel
```
import nwebclient
```


```
class NWebClient
  """ Anstatt url kann auch ein Pfad zur einer JSON-Datei, die die Schluessel enthaelt, angegeben werden. """
  __init__(url, username,password)
  doc(id)
  docs(q)
  group(id)
  getOrCreateGroup(guid, title)
  downloadImages()

metric_val(endpointUrl:string, metricName:string, val:numeric)
```


Links: [Gitlab-Repo](https://gitlab.com/bsalgert/nwebclient) [PyPi-Package](https://pypi.org/project/nwebclient/)


---
Packaging: https://packaging.python.org/tutorials/packaging-projects/
