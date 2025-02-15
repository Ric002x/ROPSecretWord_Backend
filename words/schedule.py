import logging
import random as rd

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django_apscheduler.models import DjangoJobExecution

from words.models import Word

logger = logging.getLogger(__name__)


def get_random_word():
    with open('words/dictionary.txt', 'r') as file:
        words = file.read().split('\n')
        random_word = rd.choice(words)
        return random_word


def update_word():
    if Word.objects.count() == 0:
        Word.objects.create(word='world')

    while True:
        word = get_random_word()
        if not Word.objects.filter(word=word).exists():
            break

    Word.objects.create(word=word)

    if Word.objects.count() > 50:
        oldest_word = Word.objects.order_by('id').first()
        if oldest_word:
            oldest_word.delete()


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects\
        .delete_old_job_executions(max_age)  # type: ignore


def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), 'default')

    scheduler.add_job(
        update_word,
        trigger=CronTrigger(hour=9, minute=56),
        id="update_word",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'update_word'.")

    scheduler.add_job(
        delete_old_job_executions,
        trigger=CronTrigger(
            day_of_week="sun", hour="00", minute="00"
        ),
        id="delete_old_job_executions",
        max_instances=1,
        replace_existing=True,
    )
    logger.info(
        "Added weekly job: 'delete_old_job_executions'."
    )

    register_events(scheduler)

    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler finalizado")
