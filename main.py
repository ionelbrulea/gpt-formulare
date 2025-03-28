import streamlit as st
import ast
import re
import base64
import streamlit.components.v1 as components

from generate_pdf import create_pdf
from agent import gpt_collect_info
from fill_anexa4 import fill_anexa4

st.set_page_config(page_title="GPT Agent – Completare Formulare", layout="centered")
st.title("🧠 GPT Agent – Completare Anexa 4")
st.markdown("Completează automat formularul **Anexa 4** cu ajutorul GPT.")

if "raspuns" not in st.session_state:
    st.session_state["raspuns"] = ""

prompt = st.text_area("📩 Scrie ce dorești să completezi în Anexa 4")

if st.button("💬 Răspunde GPT"):
    if prompt.strip():
        st.session_state["raspuns"] = gpt_collect_info(prompt)
        st.markdown("### 📥 Răspunsul GPT:")
        st.code(st.session_state["raspuns"], language="python")
    else:
        st.warning("Scrie un mesaj mai întâi.")

if st.session_state["raspuns"]:
    st.markdown("---")
    st.subheader("📄 Completare automată Anexa 4")

    if st.button("🧾 Generează Anexa 4 completată"):
        try:
            match = re.search(r"{.*}", st.session_state["raspuns"], re.DOTALL)
            if match:
                dict_text = match.group(0)
                parsed_data = ast.literal_eval(dict_text)
                path = fill_anexa4(parsed_data)
                with open(path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700px" type="application/pdf"></iframe>'
                    st.markdown("### 📄 Previzualizare document completat:")
                    components.html(pdf_display, height=700)
                    st.download_button("⬇️ Descarcă PDF completat", base64_pdf, file_name="Anexa4_Completata.pdf", mime="application/pdf")
            else:
                st.error("❌ Nu s-a găsit un dicționar valid în răspunsul GPT.")
        except Exception as e:
            st.error(f"❌ Eroare la completare: {e}")