import requests
import time

def view():
    print
    print (" --------------------------------------------")
    print (" viewbot v.1.0.0")
    print (" --------------------------------------------\n")
    listingURL = input(" Link : https://www.ebay.co.uk/itm/146160723652")
    print
    # viewCount = int(raw_input(" How many views? : "))
    viewCount = int(input(" How many views? : 100"))

    print
    print (" Watching ... ")
    print (" Do not close this window. ")

    print
    start_time = time.time()
    for i in range(viewCount):
        r = requests.get(listingURL)
    
    print (" Task completed! ")
    viewTime = float(time.time() - start_time)
    print(" Total time : " + " %s sec" % viewTime)
    viewRate = float(viewCount / viewTime)
    print (" View rate  : " +  " %s views/sec" % viewRate)
    print
    print
    
    # todo : iterate through other links in txt file, multithread, proxy support


if __name__ == '__main__':
  view()

