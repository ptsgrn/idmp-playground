import os
import pandas as pd
from tqdm.autonotebook import tqdm
from django.core.management.base import BaseCommand
from mysite.models import Substance, Manufacturer, MedicinalProduct, PharmaceuticalProduct

tqdm.pandas()


class Command(BaseCommand):
    help = "Import drug data from CSV and map to IDMP Ontology"

    def handle(self, *args, **kwargs):
        df = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/e/2PACX-1vS2rVriTbJUSRknhvKS6EEpUQIdrp1ji8ve65AfM46PUOmMnH_qShJtDkZ1_Q8Rqiq_s4vsKx16OGts/pub?gid=0&single=true&output=csv')
        # headers: ['th', 'generic_name', 'manufacturer', 'Drugregistration', 'Trade_name', 'Year_published', 'Volume_no', 'Remark']

        def each_row(row):
            # ค้นหาหรือสร้าง Substance (สารออกฤทธิ์)
            substance, _ = Substance.objects.get_or_create(
                name=row['generic_name'])
            print(substance)

            # ค้นหาหรือสร้าง Manufacturer (ผู้ผลิต)
            manufacturer, _ = Manufacturer.objects.get_or_create(
                name=row['manufacturer'],
            )
            print(manufacturer)

            # ค้นหาหรือสร้าง Medicinal Product
            medicinal_product, _ = MedicinalProduct.objects.get_or_create(
                name=row['Trade_name'],
                registration_number=row['Drugregistration'] == "-" and f"na-{os.urandom(
                    15).hex()}" or row['Drugregistration'],
                manufacturer=manufacturer
            )

            # ค้นหาหรือสร้าง Pharmaceutical Product
            PharmaceuticalProduct.objects.get_or_create(
                medicinal_product=medicinal_product,
                dosage_form=row['Remark']
            )
            # self.stdout.write(self.style.SUCCESS(
            #     "✅ Data imported successfully!"))
            return row

        df.progress_apply(each_row, axis=1)
        # for row in tqdm(df.iterrows(), total=df.shape[0]):
        #   print(row)
        # ค้นหาหรือสร้าง Substance (สารออกฤทธิ์)
        # substance, _ = Substance.objects.get_or_create(
        #     name=row['ชื่อยา'])

        # # ค้นหาหรือสร้าง Manufacturer (ผู้ผลิต)
        # manufacturer, _ = Manufacturer.objects.get_or_create(
        #     name=row['ผู้ผลิต'],
        #     country=row['ประเทศ']
        # )

        # # ค้นหาหรือสร้าง Medicinal Product
        # medicinal_product, _ = MedicinalProduct.objects.get_or_create(
        #     name=row['ชื่อยา'],
        #     registration_number=row['เลขทะเบียน'],
        #     manufacturer=manufacturer
        # )

        # # ค้นหาหรือสร้าง Pharmaceutical Product
        # PharmaceuticalProduct.objects.get_or_create(
        #     medicinal_product=medicinal_product,
        #     dosage_form=row['รูปแบบยา']
        # )
        # self.stdout.write(self.style.SUCCESS(
        #     "✅ Data imported successfully!"))
