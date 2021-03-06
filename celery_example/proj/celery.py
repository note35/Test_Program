from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery(
    'proj',
    broker='redis://localhost:6379//',
    backend='db+sqlite:///results.sqlite',
    include=['proj.tasks']
)
#app.config_from_object('celeryconfig')
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
