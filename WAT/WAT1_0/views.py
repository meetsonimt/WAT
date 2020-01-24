from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

def index(request):
    context = dict()
    term = None
    if request.GET.get('URL'):
        url = request.GET.get('URL')
        radio_value = request.GET.get('inlineDefaultRadiosExample')
        if radio_value == "searchRadio":
            term = request.GET.get('term')
        radio_value1 = request.GET.get('inlineDefaultRadiosExample')
        context.update({
            'url' : url,
            'IsSearch' : radio_value,
            'ISMonitor' : radio_value1,
            'term' : term,
            'radio_value' : radio_value
        })
    
    json_load = {"entries": [
      {
        "pageref": "page_2",
        "startedDateTime": "2020-01-23T15:16:11.417+05:30",
        "request": {
          "bodySize": 0,
          "method": "POST",
          "url": "https://www.google.com/gen_204?oq=&gs_l=psy-ab.22...0.0..46969...0.0..0.0.0.......0......gws-wiz.gmOGMBLcfv0&ei=MmspXtfpMIrt5gLjxbPoDg",
          "httpVersion": "HTTP/2",
          "headers": [
            {
              "name": "Host",
              "value": "www.google.com"
            },
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
            },
            {
              "name": "Accept",
              "value": "*/*"
            },
            {
              "name": "Accept-Language",
              "value": "en-US,en;q=0.5"
            },
            {
              "name": "Accept-Encoding",
              "value": "gzip, deflate, br"
            },
            {
              "name": "Referer",
              "value": "https://www.google.com/"
            },
            {
              "name": "Content-Type",
              "value": "text/plain;charset=UTF-8"
            },
            {
              "name": "Content-Length",
              "value": "0"
            },
            {
              "name": "Origin",
              "value": "https://www.google.com"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Cookie",
              "value": "NID=196=PE4-ruZyGpGeQJPr_ul0hzdl5_L583VPNDu9Oi_uaH7qobZchWPF2rKAyWHwgsUckMX5V4eU76kssuKFYA92HNUAsZvjGlQKsvhaWYwZJNmjU_x6OPitBdVBjsvMQJ6EPDx3dwzaK8pwMJSAmZ1vsuyB3obgDq8NlXtwBpQvHQE; ANID=AHWqTUnOHyVYwlOmbe8jfBnsUqx-cNVz2zYbr1WBmVQHGQ7gmDiGd83eez6zwdj6; 1P_JAR=2020-1-23-9"
            },
            {
              "name": "TE",
              "value": "Trailers"
            }
          ],
          "cookies": [
            {
              "name": "NID",
              "value": "196=PE4-ruZyGpGeQJPr_ul0hzdl5_L583VPNDu9Oi_uaH7qobZchWPF2rKAyWHwgsUckMX5V4eU76kssuKFYA92HNUAsZvjGlQKsvhaWYwZJNmjU_x6OPitBdVBjsvMQJ6EPDx3dwzaK8pwMJSAmZ1vsuyB3obgDq8NlXtwBpQvHQE"
            },
            {
              "name": "ANID",
              "value": "AHWqTUnOHyVYwlOmbe8jfBnsUqx-cNVz2zYbr1WBmVQHGQ7gmDiGd83eez6zwdj6"
            },
            {
              "name": "1P_JAR",
              "value": "2020-1-23-9"
            }
          ],
          "queryString": [
            {
              "name": "oq",
              "value": ""
            },
            {
              "name": "gs_l",
              "value": "psy-ab.22...0.0..46969...0.0..0.0.0.......0......gws-wiz.gmOGMBLcfv0"
            },
            {
              "name": "ei",
              "value": "MmspXtfpMIrt5gLjxbPoDg"
            }
          ],
          "headersSize": 755
        },
        "response": {
          "status": 204,
          "statusText": "No Content",
          "httpVersion": "HTTP/2",
          "headers": [
            {
              "name": "content-type",
              "value": "text/html; charset=UTF-8"
            },
            {
              "name": "date",
              "value": "Thu, 23 Jan 2020 09:46:11 GMT"
            },
            {
              "name": "server",
              "value": "gws"
            },
            {
              "name": "content-length",
              "value": "0"
            },
            {
              "name": "x-xss-protection",
              "value": "0"
            },
            {
              "name": "x-frame-options",
              "value": "SAMEORIGIN"
            },
            {
              "name": "alt-svc",
              "value": "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000"
            },
            {
              "name": "X-Firefox-Spdy",
              "value": "h2"
            }
          ],
          "cookies": [],
          "content": {
            "mimeType": "text/html; charset=UTF-8",
            "size": 0,
            "text": ""
          },
          "redirectURL": "",
          "headersSize": 384,
          "bodySize": 384
        },
        "cache": {},
        "timings": {
          "blocked": 0,
          "dns": 0,
          "connect": 0,
          "ssl": 0,
          "send": 0,
          "wait": 303,
          "receive": 0
        },
        "time": 303,
        "_securityState": "secure",
        "serverIPAddress": "172.217.13.228",
        "connection": "443"
      },
      {
        "pageref": "page_2",
        "startedDateTime": "2020-01-23T15:16:11.426+05:30",
        "request": {
          "bodySize": 0,
          "method": "GET",
          "url": "http://amazon.com/",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Host",
              "value": "amazon.com"
            },
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
            },
            {
              "name": "Accept",
              "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            {
              "name": "Accept-Language",
              "value": "en-US,en;q=0.5"
            },
            {
              "name": "Accept-Encoding",
              "value": "gzip, deflate"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Upgrade-Insecure-Requests",
              "value": "1"
            }
          ],
          "cookies": [],
          "queryString": [],
          "headersSize": 331
        },
        "response": {
          "status": 301,
          "statusText": "Moved Permanently",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Server",
              "value": "Server"
            },
            {
              "name": "Date",
              "value": "Thu, 23 Jan 2020 09:46:11 GMT"
            },
            {
              "name": "Content-Type",
              "value": "text/html"
            },
            {
              "name": "Content-Length",
              "value": "179"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Location",
              "value": "https://amazon.com/"
            }
          ],
          "cookies": [],
          "content": {
            "mimeType": "text/html; charset=UTF-8",
            "size": 365608,
            "comment": "Response bodies are not included."
          },
          "redirectURL": "https://amazon.com/",
          "headersSize": 188,
          "bodySize": 91239
        },
        "cache": {},
        "timings": {
          "blocked": 404,
          "dns": 0,
          "connect": 203,
          "ssl": 0,
          "send": 0,
          "wait": 205,
          "receive": 0
        },
        "time": 812,
        "_securityState": "insecure",
        "serverIPAddress": "176.32.103.205",
        "connection": "80"
      },
      {
        "pageref": "page_2",
        "startedDateTime": "2020-01-23T15:16:12.040+05:30",
        "request": {
          "bodySize": 0,
          "method": "GET",
          "url": "https://amazon.com/",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Host",
              "value": "amazon.com"
            },
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
            },
            {
              "name": "Accept",
              "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            {
              "name": "Accept-Language",
              "value": "en-US,en;q=0.5"
            },
            {
              "name": "Accept-Encoding",
              "value": "gzip, deflate, br"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Upgrade-Insecure-Requests",
              "value": "1"
            }
          ],
          "cookies": [],
          "queryString": [],
          "headersSize": 335
        },
        "response": {
          "status": 301,
          "statusText": "Moved Permanently",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Server",
              "value": "Server"
            },
            {
              "name": "Date",
              "value": "Thu, 23 Jan 2020 09:46:13 GMT"
            },
            {
              "name": "Content-Type",
              "value": "text/html"
            },
            {
              "name": "Content-Length",
              "value": "179"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Location",
              "value": "https://www.amazon.com/"
            }
          ],
          "cookies": [],
          "content": {
            "mimeType": "text/html; charset=UTF-8",
            "size": 365608,
            "comment": "Response bodies are not included."
          },
          "redirectURL": "https://www.amazon.com/",
          "headersSize": 192,
          "bodySize": 91243
        },
        "cache": {},
        "timings": {
          "blocked": 864,
          "dns": 0,
          "connect": 209,
          "ssl": 654,
          "send": 0,
          "wait": 209,
          "receive": 0
        },
        "time": 1936,
        "_securityState": "secure",
        "serverIPAddress": "176.32.103.205",
        "connection": "443"
      }
      ]
  }
    
    
    dump_josn = json.dumps(json_load)
    josn_data = json.loads(dump_josn)
    return render(request,"index.html",{'josn_data':josn_data['entries']})

def test(request):
    questions=None
    name = None
    if request.GET.get('search'):
        search = request.GET.get('search')
        #questions = Queries.objects.filter(query__icontains=search)

        name = request.GET.get('name')
        #query = Queries.object.create(query=search, user_id=name)
        #query.save()

    return render(request, 'test.html',{
        'questions': name,
    })