# -*- coding: utf-8 -*-
"""
serialize json
"""
import json


class SerializeJson:
    # metoda statyczna
    @staticmethod
    def run(deserializeddata, filelocation):
        print("let's serialize something")
        lst = []
        # TODO – do modyfikacji
        for dep in deserializeddata.data:
            labels = [
                "Kod_TERYT",
                "Województwo",
                "Powiat",
                "typ_JST",
                "nazwa_urzędu_JST",
                "miejscowość",
            ]
            obiekt = {
            }
            if "telefon" in dep:
                obiekt["telefon_z_numerem_kierunkowym"] = str(dep['telefon kierunkowy']).strip(
                ) + " " if 'telefon kierunkowy' in dep else "" + str(dep['telefon']).strip()

            for label in labels:
                if label in dep:
                    obiekt[label] = dep[label]

            lst.append(obiekt)

        jsontemp = {"departaments": lst}
        with open(filelocation, 'w', encoding='utf-8') as f:
            json.dump(jsontemp, f, ensure_ascii=False)
