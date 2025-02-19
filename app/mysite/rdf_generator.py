from rdflib import Graph, Literal, Namespace, RDF, URIRef
from mysite.models import MedicinalProduct, Substance, Manufacturer
from django.conf import settings
from django.core.management.base import BaseCommand
import rdflib


def generate_rdf():
   # กำหนด Namespace สำหรับ IDMP Ontology
    IDMP = Namespace("http://www.example.org/idmp#")

    # สร้าง RDF Graph
    g = Graph()
    g.bind("idmp", IDMP)

    # ดึงข้อมูลจาก Model
    products = MedicinalProduct.objects.all()

    for product in products:
        product_uri = URIRef(f"http://example.org/idmp/{product.id}")

        # เพิ่ม Medicinal Product
        g.add((product_uri, RDF.type, IDMP.MedicinalProduct))
        g.add((product_uri, IDMP.name, Literal(product.name)))
        g.add((product_uri, IDMP.registrationNumber,
              Literal(product.registration_number)))

        # เพิ่ม Manufacturer
        manufacturer_uri = URIRef(
            f"http://example.org/idmp/manufacturer/{product.manufacturer.id}")
        g.add((manufacturer_uri, RDF.type, IDMP.Manufacturer))
        g.add((manufacturer_uri, IDMP.name, Literal(product.manufacturer.name)))
        g.add((product_uri, IDMP.manufacturedBy, manufacturer_uri))

        # เพิ่ม Substance
        # substances = Substance.objects.filter(medicinalproduct=product)
        # for substance in substances:
        #     substance_uri = URIRef(
        #         f"http://example.org/idmp/substance/{substance.id}")
        #     g.add((substance_uri, RDF.type, IDMP.Substance))
        #     g.add((substance_uri, IDMP.name, Literal(substance.name)))
        #     g.add(triple=(product_uri, IDMP.containsSubstance, substance_uri))

    # บันทึก RDF เป็นไฟล์ Turtle
    rdf_file_path = settings.BASE_DIR / "export" / "medicinal_products.ttl"
    g.serialize(destination=str(rdf_file_path), format="turtle")

    print(f"✅ RDF Exported to: {rdf_file_path}")
    return rdf_file_path
