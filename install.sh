#!/bin/bash
git submodule init
git submodule update
git clone git@github.com:JackonYang/media-of-lean-read.git media
python manage.py syncdb
python manage.py loaddata media/db_bak.json
