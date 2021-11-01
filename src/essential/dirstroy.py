#!/usr/bin/python
import sys
import getopt
import requests
import concurrent.futures

wordlist = ''
outputFile = ''
threads = 10
URL = ''
codes= [200,301,403,302]
results = []
recursion = False
extension = ''

def main(argv):
    global wordlist
    global outputFile
    global threads
    global URL
    global codes

    
    if len(argv) == 0:
        print('dirstroyer.py -u <url> -w <wordlist> ')
        sys.exit(2)
    
    try:
        opts,args = getopt.getopt(argv, "hw:o:t:u:sC:x:r", ["wordlist=", "outputfile=", "threads=","url=", "statuscodes=", "extensions", "recurse"])
    except getopt.GetoptError:
        print('dirstroyer.py -u <url> -w <wordlist> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('dirstroyer.py -u <url> -w <wordlist> ')
        elif opt in ('-w', "--wordlist"):
            wordlist = arg
        elif opt in ("-u", "--url"):
            URL = arg
        elif opt in ("-t", "--threads"):
            threads = arg
        elif opt in ("-o", "--outfile"):
            outputFile = arg
        elif opt in ("-sC", "--statuscodes"):
            codes = arg
        elif opt in ("-x", "--extensions"):
            extension = arg
        elif opt in ("-r", "--recurse"):
            recursion = True
   
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future = executor.submit(dirstroy)
        future.result()
    
def dirstroy():
    if wordlist == '':
        print("please set wordlist")
        sys.exit(2)
    elif URL == '':
        print("please set URL")
        sys.exit(2)
    if not URL.contains("http://") or not URL.contains("https://"):
        print("Malformed URL. Please enter http(s)://$url")
        sys.exit(2)
    f = open(wordlist, "r")
    if not outputFile == '':
        out = open(outputFile, "a")
    dirs = f.read().splitlines()
    while True:
        paths = findDirs(dirs, out)
        if len(paths) == len(results):
            break
        results = results + paths
        for path in paths:
            if "." in path:
                paths.remove(path)
        dirs = paths
    
def findDirs(dirs, out):
    foundDirs = []
    
    for direct in dirs:
        req = requests.get(url=URL+ "/" + direct, verify=False)
        if req.status_code in codes:
            foundDirs.append(direct)
            print("/"+ direct + " " + str(req.status_code))
            if not outputFile == '':
                out.write("/"+ direct + " " + str(req.status_code) + '\r\n')
    if extension:
        for direct in dirs:
            req = requests.get(url=URL + "/" + direct + extension, verify=False)
            if req.status_code in codes:
                foundDirs.append(direct + extension)
                print("/" + direct + extension + " " + str(req.status_code) + '\r\n')
                if not outputFile == '':
                    out.write("/" + direct + extension + " " + str(req.status_code) + '\r\n')
    return foundDirs
if __name__ == '__main__':
    main(sys.argv[1:])
