from requests import put, get

url = 'http://localhost:5000/resource'

def test():
    print "Create"
    print put(url+'1', data={'data': 'Testing Flask'}).json()
    print put(url+'2', data={'data': 'RESTful API using Flask'}).json()
    print "Read"
    print get(url+'1').json()
    print get(url+'2').json()

def main():
    test()

if __name__ == "__main__":
    main()
