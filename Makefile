build: ; \
    buildout -t 120 -q

clean: ; \
    rm -fr bin src eggs develop-eggs parts .installed.cfg .mr.developer.cfg; \
    rm -f `find . -name *.pyc`

pep8: ; \
    ./bin/pep8 --ignore=E501 webapp

jshint: ; \
    jshint webapp/cbmonitor/static/js/*.js

test_webapp: ; \
    ./bin/webapp test_coverage cbmonitor

test: pep8 jshint test_webapp;

update_templates: ; \
    sed -i "s|DEBUG = True|DEBUG = False|" webapp/settings.py; \
    sed -i "s|cbmonitor.db|$(CURDIR)/cbmonitor.db|" webapp/settings.py; \
    sed -i "s|MAKE_ROOT|"$(CURDIR)"|" nginx.template

run_fcgi: update_templates; \
    killall -q webapp; \
    ./bin/webapp syncdb --noinput; \
    ./bin/webapp runfcgi method=threaded socket=/tmp/cbmonitor.sock; \
    chmod a+rw /tmp/cbmonitor.sock; \
    cp nginx.template /etc/nginx/sites-available/cbmonitor.conf; \
    ln -fs /etc/nginx/sites-available/cbmonitor.conf /etc/nginx/sites-enabled/cbmonitor.conf; \
    /etc/init.d/nginx reload
