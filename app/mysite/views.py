# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import MedicinalProduct, Substance, Manufacturer


def graph_data(request):
    nodes = []
    links = []

    # สร้างโหนด (Nodes) และความสัมพันธ์ (Links)
    for product in MedicinalProduct.objects.all():
        # เพิ่ม Node ของ Product
        nodes.append({"id": f"product-{product.id}",
                     "label": product.name, "type": "product"})

        # เพิ่ม Node ของ Manufacturer
        nodes.append({"id": f"manufacturer-{product.manufacturer.id}",
                      "label": product.manufacturer.name,
                      "type": "manufacturer"})
        links.append({"source": f"product-{product.id}",
                     "target": f"manufacturer-{product.manufacturer.id}"})

        # # เพิ่ม Node ของ Substance
        # for substance in product.substances.all():
        #     nodes.append({"id": f"substance-{substance.id}",
        #                  "label": substance.name, "type": "substance"})
        #     links.append({"source": f"product-{product.id}",
        #                  "target": f"substance-{substance.id}"})

    return JsonResponse({"nodes": nodes, "links": links})


def graph_view(request):
    return render(request, "graph.html")