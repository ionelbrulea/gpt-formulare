from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, BooleanObject, DictionaryObject

def fill_anexa4(data, template_path="Anexa4.pdf", output_path="Anexa4_Completata.pdf"):
    reader = PdfReader(template_path)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)

    field_map = {
        "SubNume": data.get("nume", ""),
        "SubPrenume": data.get("prenume", ""),
        "SubCNP": data.get("cnp", ""),
        "SubLocalitatea": data.get("localitate", ""),
        "SubStrada": data.get("strada", ""),
        "SubNr": data.get("numar", ""),
        "SubBl": data.get("bloc", ""),
        "SubSc": data.get("scara", ""),
        "SubEt": data.get("etaj", ""),
        "SubAp": data.get("apartament", ""),
        "SubJudSect": data.get("sector", ""),
        "SubTara": data.get("tara", ""),
        "SubCetatenia": data.get("cetatenie", ""),
    }

    writer.update_page_form_field_values(writer.pages[0], field_map)

    # Fortăm afișarea valorilor completate
    writer._root_object.update({
        NameObject("/AcroForm"): writer._add_object(DictionaryObject({
            NameObject("/NeedAppearances"): BooleanObject(True)
        }))
    })

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path