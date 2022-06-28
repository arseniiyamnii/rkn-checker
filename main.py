import time, re, yaml, requests, os
from queue import Queue
from threading import Thread
from datetime import datetime

def telegram_post(domain):
    requests.post("https://api.telegram.org/bot"+os.environ["TELEGRAM_BOT_TOKEN"]+"/sendMessage",
                  headers={"Content-type":"application/json"},
                  json={"chat_id": os.environ["TELEGRAM_CHAT_ID"],
                        "text": os.environ["TELEGRAM_START_MESSAGE"]+domain+os.environ["TELEGRAM_END_MESSAGE"]+str(datetime.now())})

def test_domain(domain,n=0):
    try:
        requests.get('http://'+domain+'/js/mirror.js', timeout=int(os.environ["REQUEST_TIMEOUT"])).content
        return("active")
    except:
        if n==0: return("banned")
        return(test_domain(domain,n-1))

def worker(q):
    while True:
        time.sleep(int(os.environ["SLEEP_DELAY"]))
        domain=q.get()
        status=test_domain(domain,int(os.environ["RETRY_TIMES"])-1)
        if status == "active": q.put(domain)
        if status == "banned": telegram_post(domain)
        q.task_done()

if __name__ == "__main__":
    file=yaml.safe_load(
            requests.get(os.environ["FILELINK"],
                         timeout=10,
                         headers={"PRIVATE-TOKEN": os.environ['ACCESS_TOKEN']}).content)["web"]
    pattern = re.compile(os.environ["REGEX_PATTERN"])
    active=[file[i]["name"] for i in range(len(file)) if file[i]["state"]=="active" and pattern.match(file[i]["name"])]
    q=Queue()
    print(len(active))
    for domain in active:
        q.put(domain)
    threads=[None]*int(os.environ["THREADS_N"])
    for i in range(int(os.environ["THREADS_N"])):
        threads[i]=Thread(target=worker, args=[q]).start()
