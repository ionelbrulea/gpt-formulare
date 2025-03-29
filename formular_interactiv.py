import streamlit as st
import json
from datetime import date

st.set_page_config(page_title="BrioForms – Date Înregistrare Firmă", layout="centered")
st.title("📝 Introducere Date – BrioForms")

st.header("🏢 Date firmă")
firma = {
    "denumire": st.text_input("Denumire firmă", "BRIO LOGIC SRL"),
    "forma_juridica": st.selectbox("Forma juridică", ["SRL", "PFA", "II", "SA", "SRL-D"], index=0),
    "capital_social": st.number_input("Capital social (lei)", min_value=0, value=200),
    "activitate_principala": {
        "cod_caen": st.text_input("Cod CAEN principal", "6201"),
        "denumire_caen": st.text_input("Denumire CAEN", "Activități de realizare a software-ului la comandă")
    },
    "sediu_social": {
        "tara": st.text_input("Țara", "România"),
        "judet": st.text_input("Județ/Sector", "București"),
        "sector": st.text_input("Sector", "5"),
        "localitate": st.text_input("Localitate", "București"),
        "strada": st.text_input("Strada", "Fabrica de Chibrituri"),
        "nr": st.text_input("Număr", "17-21"),
        "bloc": st.text_input("Bloc", "C2"),
        "scara": st.text_input("Scara", "1"),
        "etaj": st.text_input("Etaj", "2"),
        "apartament": st.text_input("Apartament", "2")
    }
}

st.header("👤 Date asociat unic / administrator")
asociat = {
    "nume": st.text_input("Nume", "Brulea"),
    "prenume": st.text_input("Prenume", "Ionel"),
    "cnp": st.text_input("CNP", "1720918280801"),
    "data_nasterii": st.date_input("Data nașterii", value=date(1972, 9, 18)),
    "locul_nasterii": st.text_input("Locul nașterii", "București"),
    "cetatenie": st.text_input("Cetățenie", "română"),
    "tip_act_identitate": st.selectbox("Tip act identitate", ["CI", "BI", "Pașaport"], index=0),
    "serie": st.text_input("Serie CI", "RZ"),
    "numar": st.text_input("Număr CI", "295862"),
    "eliberat_de": st.text_input("Eliberat de", "SPCLEP București"),
    "data_eliberarii": st.date_input("Data eliberării", value=date(2018, 4, 1)),
    "data_expirarii": st.date_input("Data expirării", value=date(2028, 4, 1)),
    "email": st.text_input("Email", "ionel@email.com"),
    "telefon": st.text_input("Telefon", "0712345678"),
    "functie": st.selectbox("Funcție în firmă", ["administrator", "asociat", "reprezentant"], index=0)
}

st.header("📄 Declarații și opțiuni")
declaratii = {
    "beneficiar_real": st.checkbox("Este beneficiar real?", value=True),
    "indeplineste_conditii_legale": st.checkbox("Îndeplinește condițiile legale (Anexa 4)?", value=True),
    "sediu_social_la_domiciliu": st.checkbox("Sediul social este la domiciliu?", value=True)
}

documente = {
    "act_constitutiv": st.selectbox("Model act constitutiv", ["unic_asociat_administrator", "asociati_multipli"], index=0),
    "contract_comodat": st.checkbox("Generare contract comodat", value=True)
}

if st.button("💾 Generează JSON complet"):
    date_complete = {
        "firma": firma,
        "asociat_unic": asociat,
        "declaratii": declaratii,
        "documente": documente
    }
    st.success("✅ Datele au fost generate cu succes.")
    st.code(json.dumps(date_complete, indent=2, default=str), language="json")