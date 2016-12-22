from wfdb.extensions import celery


@celery.task()
def echo(msg):
    return msg