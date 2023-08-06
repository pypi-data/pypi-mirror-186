import requests

def help():
  print('''
  buildlink : buildlink is a python program which helps you to shorten link with a single command without any registration or using any API Key.
           Its also provide option to expand any link available on internet.
    Functions :
           shorten(link=url_to_shorten , service , alias) :  return list containing shortening links [ if no option provided ], else in string
           expand(url) : to expand any shorten link available on internet. : return string with long expanded URL

      Options for service :
        1. tinyurl
        2. isgd
        3. clckru
        4. chilpit
        5. daga
      
      alias - value of alias must be less than 30 characters
      
    Author : Devesh Singh [ Github : @TechUX | Instagram : @devesh92744 ]
    Github : https://github.com/TechUX/buildlink for latest documentation
    
  ''')
  
def expand(url):
  try:
    resp = requests.get(url)
    if(resp.status_code == 200):
      if(resp.url == url):
        return "Link Already in Original Form"
      else :
        return resp.url
  except requests.exceptions.MissingSchema :
    return "[ERROR] Please input complete Link with http / https also !"
  except:
    return url

def shorten(link,service=None,alias=None):
  try:
    requests.get(link)
  except requests.exceptions.MissingSchema :
    return "[ERROR] Please input complete Link with http / https also !"
  except requests.exceptions.ConnectionError :
    return "[ERROR] Please check the correct format of  entered url"

  shortenList = []
  apiUrls = {
    "tinyurl": "https://tinyurl.com/api-create.php",
    "isgd": "https://is.gd/create.php?format=simple",
    "clckru": "https://clck.ru/--",
    "chilpit": "http://chilp.it/api.php",
    "daga": "https://da.gd/shorten"
  }
  if service:
    alias = None

  if alias:
    if len(alias) > 30 :
      return "[ERROR] Alias length should be less than 30 character"
    return requests.get("https://is.gd/create.php?format=simple&url="+link+"&shorturl="+str(alias)).text

  if service is None:
    for i in apiUrls:
      shortenList.append(requests.get(apiUrls[i],params={"url": link}).text)
    return shortenList
  elif service in apiUrls:
    return requests.get(apiUrls[service],params={"url": link}).text

def main():
  print("\t buildlink\n")
  print('''[1] Shorten Link
[2] Expand Shorten Link
[3] Help
''')
  ch = input("[→] Choose option [1/2/3]: ")
  if ch == "1":
    link = input("\n[→] Enter the Long URL : ")
    print("\n"+"\n".join(shorten(link)))
  elif ch=="2":
    link = input("\n[→] Enter shorten url : ")
    print("\nExpanded URL is : "+expand(link))
  elif ch=="3":
    help()
  else :
    print("\n[ERROR] Please Enter correct option number")

if __name__ == "__main__":
  main()
