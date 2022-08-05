import wget,time,requests,urllib

			
def req_down():
    c=time.time()
    for i in range(100):
        try:
            req=requests.get(f"https://competent-euler-834b51.netlify.app/pages/{i}.html")
            print (i,req.ok)
        except:
            print(i,req.ok)
    print (time.time()-c)

def wget_down():
    c=time.time()
    for i in range(100):
            try:
                    req=wget.download(f"https://competent-euler-834b51.netlify.app/pages/{i}.html",f'{i}.html')
                    print (i,True)
            except:
                    print(i,False)
    print (time.time()-c)

def ulib_down():
    c=time.time()
    for i in range(100):
            try:
                    req=urllib.request.urlretrieve(f"https://competent-euler-834b51.netlify.app/pages/{i}.html","{i}ulib.html")
                    print (i,True)
            except:
                    print(i,False)
    print (time.time()-c)


ulib_down()
wget_down()
req_down()


