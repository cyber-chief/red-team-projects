from googlesearch import search
import webbrowser

query = input("Query: ")
results = search(query, tld="co.in", num=10, stop=10, pause=2)

for i in results:
    webbrowser.open(i, new=2)