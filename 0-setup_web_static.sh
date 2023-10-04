#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static


sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
echo "Holberton" > "/data/web_static/releases/test/index.html"
rm -f "/data/web_static/current"; ln -s "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -hR ubuntu:ubuntu "/data/"
sudo chown -R "$USER":ubuntu "/data"


# Get the hostname of the serve
HOSTNAME=$(hostname)

# Define the Nginx configuration file path

sudo chown -R "$USER:$USER" "/etc/nginx"
sudo chown -R "$USER:$USER" "/var/www"
sudo chown -R "$USER:$USER" "/usr/share/nginx/html"

REDIRECT="\n\tlocation /redirect_me {\n\t\treturn 301 http://dev-israel.tech;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"
FILE="/etc/nginx/sites-available/default"

ERRORFILE="/usr/share/nginx/html/404error.html"
FOUR="Ceci n'est pas une page"
ERRORREDIRECT="\n\terror_page 404 /404error.html;\n\tlocation = /404error.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"


hbnb_static_serve="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"


sed -i "37i\ $hbnb_static_serve" "$FILE"
sed -i "37i\ $REDIRECT" "$FILE"
echo "$FOUR" > "$ERRORFILE"
sed -i "37i\ $ERRORREDIRECT" "$FILE"

#sudo sed -i "33i\ \n\t\tadd_header X-Served-By $HOSTNAME;\n\t" "$FILE"


sudo service nginx restart
