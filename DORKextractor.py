from googlesearch import search
import pyfiglet
  
xdxd = pyfiglet.figlet_format("DORK extractor ", font = "slant"  )
print(xdxd) 
ydyd = pyfiglet.figlet_format("Coded w/ <3 By - @p474nj4y", font = "digital" )
print(ydyd)

def get_dorks(query,num_results=10):
    try:
        search_results = search(query,num_results=num_results)
        return search_results
    
    except Exception as e :
        print(f"an error occured :{e}")
        return []
    
if __name__ == "__main__" :
    queryy = input("enter what do u want to search > ")
    outputnum = int(input("enter num of results do u want > "))
    dorkk = get_dorks(queryy,outputnum)

    if dorkk :
        print("\nSearch results are here > ")

        for idx,url in enumerate(dorkk,start=1):
            print(f"{idx}.{url}")
    
    else :
        print("no results found !!!")
