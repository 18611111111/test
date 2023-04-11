import requests
result=""
for j in range(1,3):
    url="https://jsonplaceholder.typicode.com/posts/"+str(j)+"/comments"
    res=requests.get(url)
    for i in range(0,5):
      #print(res.json()[i]["email"])
      result+=res.json()[i]["email"]+"-"
print(result)