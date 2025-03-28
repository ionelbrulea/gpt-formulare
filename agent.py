import openai
import streamlit as st

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def gpt_collect_info(user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ești un agent inteligent care ajută utilizatorul să completeze formularul oficial Anexa 4. "
                    "Pe baza textului primit de la utilizator, extrage doar datele relevante pentru completare, "
                    "și returnează-le într-un format de tip dicționar Python cu exact aceste câmpuri:\n\n"
                    "- nume\n- prenume\n- cnp\n- localitate\n- strada\n- numar\n- bloc\n- scara\n- etaj\n- apartament\n- sector\n- tara\n- cetatenie\n\n"
                    "Nu cere informații suplimentare, nu adăuga telefon, email sau altceva. Răspunde doar cu dicționarul."
                )
            },
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content