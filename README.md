# info_catch
python3

apt install python3-pip

python3 -m pip install --upgrade pip

mkdir -p /data/python/venv/ && cd /data/python/venv/

pip3 install virtualenv

/usr/local/bin/virtualenv venv_info_catch

cd venv_info_catch/

apt-get update

apt install git

git clone https://github.com/Jaysong-org/info_catch.git

cd info_catch && ../bin/pip3 install -r requirements.txt

mkdir -p /data/log/python/info_catch
/data/python/venv/venv_info_catch/bin/python3 ../bin/celery -A info_catch  worker -l info &> /data/log/python/info_catch/worker.log  & 

apt-get update

apt-get install openssl libssl-dev
apt-get install libpcre3 libpcre3-dev
apt-get install zlib1g-dev

mkdir -p /usr/local/nginx && cd /usr/local/nginx/ && wget http://nginx.org/download/nginx-1.13.5.tar.gz

tar -xzvf nginx-1.13.5.tar.gz

cd nginx-1.13.5/ && mv * .. && cd ../ && rm -rf nginx-1.13.5.tar.gz

./configure --prefix=/usr/local/nginx --conf-path=/usr/local/nginx/nginx.conf --with-http_stub_status_module --with-http_ssl_module --with-http_realip_module

make -j4 && make install

vim ./conf/nginx.conf

mkdir sites-enabled && vim sites-enabled/info_catch.conf

mkdir -p /data/logs/nginx

./sbin/nginx -c ./conf/nginx.conf 
./sbin/nginx -t
./sbin/nginx -s reload

cd /data/python/venv/venv_info_catch/info_catch/

mkdir -p /data/python/venv/venv_info_catch/uwsgi

../bin/uwsgi --ini uwsgi.ini &> /dev/null &


附录 uwsgi.ini
```
#mysite_uwsgi.ini file
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = /data/python/venv/venv_info_catch/info_catch
# Django's wsgi file
module          = info_catch.wsgi
# the virtualenv (full path)
home            = /data/python/venv/venv_info_catch

# process-related settings
pidfile=/data/python/venv/venv_info_catch/uwsgi/info_catch.pid
# 指定IP端口
socket=0.0.0.0:8001
# 指定静态文件
static-map=/static=/data/python/venv/venv_info_catch/info_catch/static
# 启动uwsgi的用户名和用户组
#uid=root
#gid=root


# master
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = /data/python/venv/venv_info_catch/uwsgi/info_catch.sock
# ... with appropriate permissions - may be needed
chmod-socket    = 664
# clear environment on exit
vacuum          = true

```


附录  info_catch.conf

```
upstream info_catch {
                server 127.0.0.1:8001;
        }
server {
        listen       8000;
        server_name  47.100.136.167;
        access_log  /data/logs/nginx/info_catch.access.log  main;
        error_log /data/logs/nginx/info_catch.error.log error;
        charset     utf-8;

        add_header Access-Control-Allow-Origin $http_origin;
        add_header Access-Control-Allow-Credentials true;


                location / {
                        #proxy_set_header X-Real-IP $remote_addr;
                        #proxy_set_header   Host             $host;
                        #proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        #proxy_pass   http://info_catch;
                        #proxy_read_timeout 120;
                        #proxy_ignore_client_abort on;
                        include     uwsgi_params; # the uwsgi_params file you installed
                        uwsgi_pass 127.0.0.1:8001;
                }
}

```




