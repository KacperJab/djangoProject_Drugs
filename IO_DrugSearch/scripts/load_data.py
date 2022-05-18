import decimal

from IO_DrugSearch.models import Lek, SzczegolyRefundacji
import csv

from IO_DrugSearch.serializers import LekSerializer


def run():
    # Lek.objects.all().delete()
    # SzczegolyRefundacji.objects.all().delete()

    # wczytywanie refundacji
    with open('/Users/kacperjablonski/PycharmProjects/djangoProject1/IO_DrugSearch/scripts/ref_short.csv',
              errors='ignore', encoding='UTF-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        # SzczegolyRefundacji.objects.all().delete()
        rowid = 0
        for row in reader:
            if rowid % 3 == 0:
                continue
            print(row)
            s = row[5]
            doplata = 0
            try:
                doplata = float(s)
            except:
                doplata = 0
            print(doplata)
            refundacja = SzczegolyRefundacji(
                identyfikator_leku=row[1],
                zakres_wskazan=row[2],
                zakres_wskazan_pozarejestracyjnych=row[3],
                poziom_odplatnosci=row[4],
                wysokosc_doplaty=doplata,
            )
            refundacja.save()

    with open('/Users/kacperjablonski/PycharmProjects/djangoProject1/IO_DrugSearch/scripts/drugs_short.csv',
              errors='ignore', encoding='UTF-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        # Lek.objects.all().delete()

        rowid = 0
        for row in reader:
            if rowid % 2 == 0:
                continue
            print(row)
            rowid += 1
            # genre, _ = Genre.objects.get_or_create(name=row[-1])
            lek = Lek(
                nazwa_leku=row[0],
                substancja_czynna=row[1],
                postac=row[2],
                dawka_leku=row[3],
                zawartosc_opakowania=row[4],
                identyfikator_leku=row[5],
                id=row[6]
            )
            lek.save()

    leki = Lek.objects.all()

    szczegoly = SzczegolyRefundacji.objects.all()

    for lek in leki:
        refunds = SzczegolyRefundacji.objects.filter(identyfikator_leku=lek.identyfikator_leku)
        for refun in refunds:
            lek.refundacje.add(refun)
