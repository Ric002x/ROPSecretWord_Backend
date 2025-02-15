from django.apps import AppConfig
from django.db.models.signals import post_migrate


class WordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'words'

    def ready(self):
        """Inicia o agendador apenas após as migrações serem concluídas."""
        from words import schedule

        def iniciar_scheduler(sender, **kwargs):
            print("🔄 Iniciando o scheduler após as migrações...")
            schedule.start()
            print("✅ Scheduler iniciado com sucesso!")

        post_migrate.connect(iniciar_scheduler, sender=self)
