Aşağıdaki komutlar ile Flask'imizi güncelleyelim:

pip3 install flask-mysql
pip3 install sqlalchemy
pip3 install Flask-SQLAlchemy

AWS konsola N.Virginia'dan bağlanalım.

EC2 ve RDS servislerini ayrı sekmelerde açalım.

Aşağıda linklerini verdiğim 2 siteyi açalım.
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
https://code.tutsplus.com/tr/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

1+=> güncellemek için;
sudo yum update -y
2+=> git yüklemek için;
sudo yum install git -y
3+=>flask yüklemek için;
sudo pip3 install flask

4:23
=>Flask-SQLAlchemy yüklemek için;
pip3 install flask-sqlalchemy
=>Flask-WTF yüklemek için;
pip3 install -U Flask-WTF

=>mariadb yüklemek
sudo yum install mariadb-server -y
-Start MariaDB service.
sudo systemctl start mariadb
-Check status of MariaDB service.
sudo systemctl status mariadb
-Enable MariaDB service, so that MariaDB service will be activated on restarts.
sudo systemctl enable mariadb