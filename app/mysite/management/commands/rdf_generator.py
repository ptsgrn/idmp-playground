from django.core.management.base import BaseCommand
from mysite.rdf_generator import generate_rdf


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        exported_file_path = generate_rdf()
        self.stdout.write(self.style.SUCCESS(f"✅ RDF Exported! {exported_file_path}"))