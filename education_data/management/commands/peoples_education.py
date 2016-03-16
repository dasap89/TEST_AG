from django.core.management.base import BaseCommand, CommandError
from education_data.models import People, Education


class Command(BaseCommand):
    help = 'Select education of people'

    def add_arguments(self, parser):
        parser.add_argument('education', nargs='+', type=str)

    def handle(self, *args, **options):
        for education in options['education']:
            try:
                ed = Education.objects.get(education=education)
                people_education = ed.people.all()
            except Education.DoesNotExist:
                raise CommandError('Education "%s" does not exist' % education)

            self.stdout.write(
                'All people who has "%s" education are %s' % (education,
                                                              people_education)
                )
