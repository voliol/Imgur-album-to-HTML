from imgurpython import ImgurClient
import time

album_id = "xhQHE";
author_name = "DS"

client_id = 'a61d36e6987f95d'
client_secret = '6c90b06ed1446874c81b8c69042a3f9bc77b8fc6'

client = ImgurClient(client_id, client_secret)

album = client.get_album(album_id)

f = open("to_html.html", "w")
f.write("<!DOCTYPE html><html lang=\"en\">\n"
        "<head>\n"
        "<meta charset=\"UTF-8\">\n"
        "<title>" + album.title + "</title>\n"
	"<link rel=\"stylesheet\" href=\"../style.css\">\n"
        "</head>\n")
f.write("<body>\n")

f.write("<h1>" + album.title + "</h1>\n")
f.write(album.description + "<br>\n")
t = time.strftime('%Y-%m-%d', time.gmtime(album.datetime))
f.write("By " + author_name + ", " + t + "<br>\n")
f.write("<hr>\n")

for image in album.images:
    link = image["link"]
    f.write("<img src=" + link + "><br>\n")
    desc = image["description"]
    if desc is not None:
        f.write(desc + "\n<br><br>\n")

f.write("<!DOCTYPE html><html lang=\"en\">\n"
        "<head><meta charset=\"UTF-8\"></head>\n")

f.write("</body>\n")
f.write("</html>")
f.close()

print("Done!")
    
