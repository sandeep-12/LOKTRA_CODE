import sys
import urllib2
from bs4 import BeautifulSoup

param_length = len(sys.argv)
url = ""

def findTotalNumberOfResults():
    page = urllib2.urlopen(url)
    print("Loading URL : "+url)
    soup = BeautifulSoup(page, 'html.parser')
    if soup.find("span", {"class" : "numTotalResults"}) != None:
        results_count = soup.find("span", {"class" : "numTotalResults"}).getText()
        
        print("Total results found for your search keyword : "+results_count.split(" ")[-1].replace("+", ""))
    elif soup.find("div", {"class" : "rtCol"}) != None:
        print(soup.find("div", {"class" : "rtCol"}).getText())
    else:
        print("Techinal error occured")

def findAllTheResults():
    page = urllib2.urlopen(url)
    print("Loading URL : "+url)
    soup = BeautifulSoup(page, 'html.parser')

    if soup.find("div", {"class" : "rtCol"}) != None:
        print(soup.find("div", {"class" : "rtCol"}).getText())
    else :
        items = soup.findAll("div", {"class" : "gridBox"})
        no_of_items = len(items)
        print("Number of Items Found On Page : "+str(no_of_items))

        for i in range(no_of_items):
            #print("Loopingg....")
            item = items[i].find("div", {"class" : "gridItemBtm"})
            #print(item)
            if item != None:
                item_details = item.getText()
                item_details = item_details.strip()
                while item_details.find("\n\n") != -1:
                    item_details = item_details.replace("\n\n", "\n")
                details = item_details.split("\n")
                product_name = details[0]
                hidden_name = item.find("span", {"class" : "quickLookGridItemFullName"}).getText()
                if hidden_name != None:
                    product_name = hidden_name
                    details.remove(hidden_name);

                print("Item #"+str(i+1))
                print("Product Name :"+product_name)
                print("Price : "+details[1])
                print("Sold By : "+details[2])
                i = 3
                while i < len(details):
                    if details[i].find("hipping") != -1:
                        print("Shipping : "+details[i])
                    if details[i].find("store") != -1:
                        print("Available in : "+details[i])
                    i = i + 1
                print("##############")


#Main Code stats from here
if param_length == 2:
    search_keyword = sys.argv[1]
    print("You entered : "+search_keyword)
    url = "http://www.shopping.com/products?KW="+search_keyword
    findTotalNumberOfResults()
elif param_length == 3:
    search_keyword = sys.argv[1]
    try :
        page_number = sys.argv[2]
        url = "http://www.shopping.com/products~PG-"+page_number+"?KW="+search_keyword
        findAllTheResults()
    except ValueError:
        print("Invalid page number : Page number should be integer.")
else :
    print("Invalid parameter, accepts at max two parameter:\nsample query : python webCrawler.py <keyword> <page_number>")

                        
            
        




