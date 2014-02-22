FROM 	nickpegg/uwsgi

RUN	apt-get update
RUN	apt-get install -y mtr-tiny iputils-ping

RUN	git clone https://github.com/nickpegg/lg.git /srv/lg
RUN 	pip install -r /srv/lg/requirements.txt

RUN	/srv/lg/extra/adduser.sh

WORKDIR	/srv/lg
CMD	uwsgi -p 16 -s 0.0.0.0:5000 --uid lg -w glass:app
EXPOSE	5000
