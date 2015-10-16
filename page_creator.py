import argparse


start_html = "<html><body>"
end_html = "</body></html>"

def create_links(num_pages, page_name):
    #count = 0
    links = ""
    
    for count in  range(num_pages):
        links += "<a href='" + page_name + str(count) + ".html'>" + page_name + str(count) + "</a><br />"

    html = start_html + links + end_html
    
    for count in  range(num_pages):
        file_name = page_name + str(count) + ".html"
        with open(file_name, 'w') as f:
            f.write(html)
            

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number', default=5, type=int, help="Number of pages to create")
    parser.add_argument('filename', default="test", help="Base filename")
    args = parser.parse_args()
    
    create_links(args.number, args.filename)

    
        


#create_links(10, "test")

    
if __name__ == "__main__":
   main()
