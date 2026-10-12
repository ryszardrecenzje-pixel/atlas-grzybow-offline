import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="Atlas Grzybów",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded",
)

GRZYBY = [
    {"id": 1, "nazwa_polska": "Borowik szlachetny", "nazwa_lacinska": "Boletus edulis", "status": "jadalny",
     "opis": "Kapelusz brązowy do ciemnobrązowy, gąbka najpierw biała, potem żółtawa. Trzon masywny z wyraźną białą siateczką. Smak łagodny, orzechowy. Król polskich grzybów.",
     "siedlisko": "Lasy liściaste i mieszane, pod dębami, bukami, świerkami", "sezon": "VI–XI",
     "look_alikes": "Borowik szatański (trujący), goryczak żółciowy (niejadalny)"},
    {"id": 2, "nazwa_polska": "Podgrzybek brunatny", "nazwa_lacinska": "Imleria badia", "status": "jadalny",
     "opis": "Kapelusz ciemnobrązowy, gąbka żółtawa siniejąca po uszkodzeniu. Trzon brązowy, bez siateczki. Bardzo popularny i smaczny.",
     "siedlisko": "Lasy iglaste i mieszane, szczególnie sosnowe", "sezon": "VI–XI",
     "look_alikes": "Goryczak żółciowy (niejadalny)"},
    {"id": 3, "nazwa_polska": "Kurka (Pieprznik jadalny)", "nazwa_lacinska": "Cantharellus cibarius", "status": "jadalny",
     "opis": "Owocnik lejkowaty, żółty do pomarańczowego. Blaszki zbiegające, grube, rozwidlone. Zapach owocowy.",
     "siedlisko": "Lasy iglaste i mieszane, bory sosnowe", "sezon": "VI–X",
     "look_alikes": "Lisówka pomarańczowa (niejadalna)"},
    {"id": 4, "nazwa_polska": "Maślak zwyczajny", "nazwa_lacinska": "Suillus luteus", "status": "jadalny",
     "opis": "Kapelusz brązowy, śliski, gąbka żółta. Trzon z wyraźnym pierścieniem. Skórkę kapelusza zwykle ściąga się.",
     "siedlisko": "Lasy sosnowe, piaszczyste gleby", "sezon": "VI–X",
     "look_alikes": "Maślak pstry, maślak ziarnisty"},
    {"id": 5, "nazwa_polska": "Czubajka kania", "nazwa_lacinska": "Macrolepiota procera", "status": "jadalny",
     "opis": "Duży kapelusz z brązowymi łuskami, wolny pierścień, trzon z wzorem wężowym. Blaszki białe. Bardzo smaczna.",
     "siedlisko": "Łąki, polany, skraje lasów", "sezon": "VII–X",
     "look_alikes": "Muchomor sromotnikowy (młode!), muchomor plamisty"},
    {"id": 6, "nazwa_polska": "Koźlarz babka", "nazwa_lacinska": "Leccinum scabrum", "status": "jadalny",
     "opis": "Kapelusz szarobrązowy do czarnobrązowego, gąbka biała ciemniejąca. Trzon biały z czarnymi kłaczkami.",
     "siedlisko": "Lasy liściaste, szczególnie pod brzozami", "sezon": "VI–X",
     "look_alikes": "Koźlarz czerwony"},
    {"id": 7, "nazwa_polska": "Koźlarz czerwony", "nazwa_lacinska": "Leccinum aurantiacum", "status": "jadalny",
     "opis": "Kapelusz pomarańczowoczerwony, gąbka biaława. Trzon z czerwonymi lub czarnymi kłaczkami. Miąższ sinieje.",
     "siedlisko": "Pod osikami i brzozami", "sezon": "VI–X",
     "look_alikes": "Koźlarz babka"},
    {"id": 8, "nazwa_polska": "Rydz (Mleczaj rydz)", "nazwa_lacinska": "Lactarius deliciosus", "status": "jadalny",
     "opis": "Kapelusz pomarańczowy z koncentrycznymi pręgami, po uszkodzeniu wydziela pomarańczowy sok.",
     "siedlisko": "Lasy iglaste, szczególnie sosnowe", "sezon": "VIII–X",
     "look_alikes": "Mleczaj świerkowy, krowiak podwinięty (trujący)"},
    {"id": 9, "nazwa_polska": "Opieńka miodowa", "nazwa_lacinska": "Armillaria mellea", "status": "jadalny",
     "opis": "Kapelusz miodowy z drobnymi łuskami, pierścień na trzonie. Rośnie kępami na pniakach. Wymaga dokładnego gotowania.",
     "siedlisko": "Pnie i korzenie drzew", "sezon": "IX–XI",
     "look_alikes": "Hełmówka jadowita (śmiertelnie trująca!)"},
    {"id": 10, "nazwa_polska": "Gąska zielonka", "nazwa_lacinska": "Tricholoma equestre", "status": "jadalny",
     "opis": "Kapelusz żółtozielony, blaszki żółte. Ceniona, ale w niektórych krajach uważana za potencjalnie toksyczną przy dużym spożyciu.",
     "siedlisko": "Bory sosnowe", "sezon": "IX–XI",
     "look_alikes": "Muchomor sromotnikowy (śmiertelnie trujący!)"},
    {"id": 11, "nazwa_polska": "Gołąbek wyborny", "nazwa_lacinska": "Russula vesca", "status": "jadalny",
     "opis": "Kapelusz różowawy lub brązowawy, blaszki białe, trzon biały. Smak łagodny.",
     "siedlisko": "Lasy liściaste i mieszane", "sezon": "VII–X",
     "look_alikes": "Gołąbki o ostrym smaku (niejadalne)"},
    {"id": 12, "nazwa_polska": "Maślak pstry", "nazwa_lacinska": "Suillus variegatus", "status": "jadalny",
     "opis": "Kapelusz żółtobrązowy, suchy, gąbka brudnożółta. Trzon bez pierścienia.",
     "siedlisko": "Lasy sosnowe", "sezon": "VI–X",
     "look_alikes": "Maślak zwyczajny"},
    {"id": 13, "nazwa_polska": "Siedzuń sosnowy (Szmaciak)", "nazwa_lacinska": "Sparassis crispa", "status": "jadalny",
     "opis": "Owocnik przypominający kalafior, kremowy do żółtawego. Rośnie u podstawy sosen.",
     "siedlisko": "Przy podstawie starych sosen", "sezon": "VIII–XI",
     "look_alikes": "Brak groźnych sobowtórów"},
    {"id": 14, "nazwa_polska": "Pieczarka łąkowa", "nazwa_lacinska": "Agaricus campestris", "status": "jadalny",
     "opis": "Kapelusz biały, blaszki różowe potem czarnobrązowe. Trzon z pierścieniem.",
     "siedlisko": "Łąki, pastwiska, ogrody", "sezon": "V–X",
     "look_alikes": "Muchomor sromotnikowy (młode!), pieczarka karbolowa"},
    {"id": 15, "nazwa_polska": "Borowik ceglastopory", "nazwa_lacinska": "Neoboletus luridiformis", "status": "jadalny",
     "opis": "Kapelusz ciemnobrązowy, gąbka ceglastoczerwona, trzon z czerwonawym odcieniem. Miąższ sinieje.",
     "siedlisko": "Lasy iglaste i mieszane", "sezon": "VII–X",
     "look_alikes": "Borowik szatański (trujący)"},
    {"id": 16, "nazwa_polska": "Goryczak żółciowy", "nazwa_lacinska": "Tylopilus felleus", "status": "niejadalny",
     "opis": "Wygląda jak borowik, ale gąbka różowieje, a smak jest bardzo gorzki. Trzon z ciemną siateczką.",
     "siedlisko": "Lasy iglaste i mieszane", "sezon": "VII–X",
     "look_alikes": "Borowik szlachetny, podgrzybek"},
    {"id": 17, "nazwa_polska": "Lisówka pomarańczowa", "nazwa_lacinska": "Hygrophoropsis aurantiaca", "status": "niejadalny",
     "opis": "Podobna do kurki, ale blaszki częstsze, bardziej pomarańczowe, miąższ cienki.",
     "siedlisko": "Lasy iglaste, na drewnie i ściółce", "sezon": "VII–XI",
     "look_alikes": "Kurka (pieprznik jadalny)"},
    {"id": 18, "nazwa_polska": "Muchomor czerwony", "nazwa_lacinska": "Amanita muscaria", "status": "trujacy",
     "opis": "Kapelusz czerwony z białymi kłaczkami, białe blaszki, pierścień i bulwiasta podstawa. Zatrucia neurologiczne.",
     "siedlisko": "Lasy iglaste i liściaste", "sezon": "VII–X",
     "look_alikes": "Muchomor królewski"},
    {"id": 19, "nazwa_polska": "Muchomor plamisty", "nazwa_lacinska": "Amanita pantherina", "status": "trujacy",
     "opis": "Kapelusz brązowy z białymi kłaczkami, wyraźna bruzda na brzegu. Trujący – zatrucia neurologiczne.",
     "siedlisko": "Lasy liściaste i mieszane", "sezon": "VII–X",
     "look_alikes": "Czubajka kania, muchomor czerwony"},
    {"id": 20, "nazwa_polska": "Borowik szatański", "nazwa_lacinska": "Rubroboletus satanas", "status": "trujacy",
     "opis": "Kapelusz jasny (szary/białawy), gąbka czerwona, trzon masywny z czerwoną siateczką. Silne zatrucia pokarmowe.",
     "siedlisko": "Lasy liściaste, ciepłolubne", "sezon": "VII–IX",
     "look_alikes": "Borowik szlachetny, borowik ceglastopory"},
    {"id": 21, "nazwa_polska": "Krowiak podwinięty (Olszówka)", "nazwa_lacinska": "Paxillus involutus", "status": "trujacy",
     "opis": "Kapelusz brązowy z podwiniętym brzegiem, blaszki zbiegające. Może powodować ciężkie reakcje immunologiczne.",
     "siedlisko": "Lasy liściaste i mieszane, pod brzozami", "sezon": "VII–X",
     "look_alikes": "Rydz, mleczaje"},
    {"id": 22, "nazwa_polska": "Muchomor sromotnikowy", "nazwa_lacinska": "Amanita phalloides", "status": "smiertelnie_trujacy",
     "opis": "Kapelusz oliwkowozielony, białe blaszki, pierścień i pochwa. Najgroźniejszy grzyb w Polsce – amatoksyny niszczą wątrobę.",
     "siedlisko": "Lasy liściaste, pod dębami", "sezon": "VII–X",
     "look_alikes": "Gąska zielonka, czubajka kania, pieczarka"},
    {"id": 23, "nazwa_polska": "Muchomor jadowity", "nazwa_lacinska": "Amanita virosa", "status": "smiertelnie_trujacy",
     "opis": "Całkowicie biały, z pochwą i pierścieniem. Równie niebezpieczny jak sromotnikowy.",
     "siedlisko": "Lasy liściaste i mieszane", "sezon": "VII–X",
     "look_alikes": "Pieczarka, młode purchawki"},
    {"id": 24, "nazwa_polska": "Hełmówka jadowita", "nazwa_lacinska": "Galerina marginata", "status": "smiertelnie_trujacy",
     "opis": "Mały, brązowy grzyb na drewnie, z pierścieniem. Zawiera amatoksyny. Łatwy do pomylenia z opieńkami.",
     "siedlisko": "Na martwym drewnie", "sezon": "V–XI",
     "look_alikes": "Opieńka miodowa"},
    {"id": 25, "nazwa_polska": "Zasłonak rudy", "nazwa_lacinska": "Cortinarius orellanus", "status": "smiertelnie_trujacy",
     "opis": "Kapelusz rdzawobrązowy, blaszki rdzave. Orellanina niszczy nerki. Objawy nawet po 2 tygodniach!",
     "siedlisko": "Lasy liściaste i mieszane", "sezon": "VIII–X",
     "look_alikes": "Kurka, podgrzybki"},
    {"id": 26, "nazwa_polska": "Piestrzenica kasztanowata", "nazwa_lacinska": "Gyromitra esculenta", "status": "smiertelnie_trujacy",
     "opis": "Owocnik pofałdowany, kasztanowaty (jak mózg). Gyromitryna. Dawniej jedzona – obecnie śmiertelnie niebezpieczna.",
     "siedlisko": "Lasy iglaste, wiosna", "sezon": "IV–V",
     "look_alikes": "Smardz (jadalny)"},
]

STATUS_LABELS = {
    "jadalny": ("Jadalny", "🟢"),
    "niejadalny": ("Niejadalny", "🟠"),
    "trujacy": ("Trujący", "🔴"),
    "smiertelnie_trujacy": ("Śmiertelnie trujący", "☠️"),
}
STATUS_COLORS = {
    "jadalny": "#2e7d32", "niejadalny": "#ef6c00",
    "trujacy": "#c62828", "smiertelnie_trujacy": "#b71c1c",
}

@st.cache_resource(show_spinner="Ładowanie modelu AI...")
def load_model():
    try:
        from transformers import pipeline
        classifier = pipeline(
            "image-classification",
            model="dima806/mushrooms_image_detection",
            top_k=5,
        )
        return classifier, None
    except Exception as e:
        return None, str(e)

def map_label_to_atlas(label: str):
    label_lower = label.lower().replace("_", " ")
    for g in GRZYBY:
        if label_lower in g["nazwa_lacinska"].lower() or g["nazwa_lacinska"].lower() in label_lower:
            return g
        if label_lower in g["nazwa_polska"].lower():
            return g
    for g in GRZYBY:
        genus = g["nazwa_lacinska"].split()[0].lower()
        if genus in label_lower:
            return g
    return None

def classify_image(image, classifier):
    results = classifier(image)
    output = []
    for r in results:
        matched = map_label_to_atlas(r["label"])
        output.append({"label_model": r["label"], "confidence": float(r["score"]), "matched": matched})
    return output

def demo_classify(image):
    candidates = random.sample(GRZYBY, k=min(3, len(GRZYBY)))
    confidences = [0.65, 0.22, 0.09]
    return [{"label_model": c["nazwa_lacinska"], "confidence": confidences[i] if i < len(confidences) else 0.05, "matched": c}
            for i, c in enumerate(candidates)]

def status_badge(status):
    label, emoji = STATUS_LABELS.get(status, (status, ""))
    color = STATUS_COLORS.get(status, "#666")
    return f'<span style="background-color:{color};color:white;padding:4px 12px;border-radius:20px;font-weight:bold;font-size:0.9em;">{emoji} {label}</span>'

def safety_banner(compact=False):
    if compact:
        st.error("⚠️ **Nigdy nie jedz grzyba tylko na podstawie aplikacji!**")
    else:
        st.error("""### ⚠️ UWAGA – BEZPIECZEŃSTWO
**Nigdy nie jedz grzyba tylko na podstawie wyniku tej aplikacji.**
Identyfikacja AI nigdy nie jest w 100% pewna.
Muchomor sromotnikowy i inne śmiertelnie trujące gatunki mogą być pomylone z jadalnymi.
W razie jakichkolwiek wątpliwości – **nie zbieraj**.""")

def find_grzyby(query, status_filter="Wszystkie"):
    q = query.lower().strip()
    result = GRZYBY
    if status_filter != "Wszystkie":
        status_map = {"Jadalne": "jadalny", "Niejadalne": "niejadalny", "Trujące": "trujacy", "Śmiertelnie trujące": "smiertelnie_trujacy"}
        result = [g for g in result if g["status"] == status_map.get(status_filter, "")]
    if q:
        result = [g for g in result if q in g["nazwa_polska"].lower() or q in g["nazwa_lacinska"].lower()]
    return result

def get_by_id(gid):
    for g in GRZYBY:
        if g["id"] == gid:
            return g
    return None

def show_grzyb_detail(g):
    st.markdown(f"## {g['nazwa_polska']}")
    st.markdown(f"*{g['nazwa_lacinska']}*")
    st.markdown(status_badge(g["status"]), unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"**Opis**  \n{g['opis']}")
    st.markdown(f"**Siedlisko**  \n{g['siedlisko']}")
    st.markdown(f"**Sezon**  \n{g['sezon']}")
    st.markdown(f"**Podobne gatunki (look-alikes)**  \n{g['look_alikes']}")
    if g["status"] in ("trujacy", "smiertelnie_trujacy"):
        st.error("☠️ **GATUNEK TRUJĄCY LUB ŚMIERTELNIE TRUJĄCY – NIE ZBIERAJ**")

# SIDEBAR
st.sidebar.title("🍄 Atlas Grzybów")
st.sidebar.markdown("---")
page = st.sidebar.radio("Przejdź do:", ["🏠 Start", "📷 Skaner AI", "📚 Atlas", "ℹ️ O aplikacji"], label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.caption(f"Gatunków w atlasie: **{len(GRZYBY)}**")
st.sidebar.caption("Wersja edukacyjna • Używaj odpowiedzialnie")

if page == "🏠 Start":
    st.title("🍄 Atlas Grzybów")
    st.markdown("### Rozpoznawaj grzyby ze zdjęcia + rozbudowany atlas polskich gatunków")
    safety_banner()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Gatunków w atlasie", len(GRZYBY))
    with col2:
        st.metric("Jadalne", sum(1 for g in GRZYBY if g["status"] == "jadalny"))
    with col3:
        st.metric("Trujące / śmiertelne", sum(1 for g in GRZYBY if g["status"] in ("trujacy", "smiertelnie_trujacy")))
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 📷 Skaner AI")
        st.write("Zrób zdjęcie lub wgraj fotkę – model AI zaproponuje gatunki.")
    with c2:
        st.markdown("#### 📚 Atlas")
        st.write("Przeglądaj gatunki, filtruj po statusie, sprawdzaj look-alike.")

elif page == "📷 Skaner AI":
    st.title("📷 Skaner AI")
    safety_banner(compact=True)
    st.markdown("Zrób zdjęcie aparatem lub wgraj gotowe zdjęcie grzyba. Model AI zaproponuje najbardziej prawdopodobne gatunki.")
    classifier, model_error = load_model()
    if classifier is None:
        st.warning(f"Model AI nie załadował się ({model_error}). Działa tryb demo.")
    else:
        st.success("Model AI gotowy (dima806/mushrooms_image_detection)")
    tab_cam, tab_upload = st.tabs(["Aparat", "Wgraj zdjęcie"])
    image = None
    with tab_cam:
        cam_photo = st.camera_input("Zrób zdjęcie grzyba")
        if cam_photo is not None:
            image = Image.open(cam_photo).convert("RGB")
    with tab_upload:
        uploaded = st.file_uploader("Wybierz plik (JPG / PNG)", type=["jpg", "jpeg", "png"])
        if uploaded is not None:
            image = Image.open(uploaded).convert("RGB")
    if image is not None:
        st.image(image, caption="Twoje zdjęcie", use_container_width=True)
        if st.button("🔍 Rozpoznaj grzyba", type="primary", use_container_width=True):
            with st.spinner("Analizuję zdjęcie modelem AI..."):
                results = classify_image(image, classifier) if classifier is not None else demo_classify(image)
            st.subheader("Wyniki rozpoznawania")
            st.caption("Model zwraca etykiety naukowe. Jeśli gatunek jest w atlasie – pokażemy szczegóły i status jadalności.")
            for r in results:
                conf_pct = int(r["confidence"] * 100)
                matched = r["matched"]
                with st.container(border=True):
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        if matched:
                            st.markdown(f"**{matched['nazwa_polska']}**")
                            st.markdown(f"*{matched['nazwa_lacinska']}*")
                            st.caption(f"Etykieta modelu: `{r['label_model']}`")
                        else:
                            st.markdown(f"**{r['label_model']}**")
                            st.caption("Brak dokładnego dopasowania w atlasie – sprawdź ręcznie")
                        st.progress(min(r["confidence"], 1.0), text=f"Pewność: {conf_pct}%")
                    with c2:
                        if matched:
                            st.markdown(status_badge(matched["status"]), unsafe_allow_html=True)
                            if st.button("Szczegóły", key=f"det_{matched['id']}_{conf_pct}"):
                                st.session_state["selected_id"] = matched["id"]
                                st.rerun()
            st.warning("⚠️ Nawet wysoka pewność modelu **nie oznacza**, że grzyb jest jadalny. Zawsze weryfikuj cechy diagnostyczne.")
    else:
        st.info("Dodaj zdjęcie, aby uruchomić rozpoznawanie.")

elif page == "📚 Atlas":
    st.title("📚 Atlas gatunków")
    safety_banner(compact=True)
    if "selected_id" in st.session_state:
        g = get_by_id(st.session_state.pop("selected_id"))
        if g:
            show_grzyb_detail(g)
            if st.button("← Wróć do listy"):
                st.rerun()
            st.stop()
    col_s, col_f = st.columns([2, 1])
    with col_s:
        query = st.text_input("🔍 Szukaj (nazwa polska lub łacińska)", "")
    with col_f:
        status_filter = st.selectbox("Filtr statusu", ["Wszystkie", "Jadalne", "Niejadalne", "Trujące", "Śmiertelnie trujące"])
    filtered = find_grzyby(query, status_filter)
    st.caption(f"Znaleziono: **{len(filtered)}** gatunków")
    for g in filtered:
        label, emoji = STATUS_LABELS.get(g["status"], (g["status"], ""))
        with st.expander(f"{emoji} **{g['nazwa_polska']}** — *{g['nazwa_lacinska']}*"):
            st.markdown(status_badge(g["status"]), unsafe_allow_html=True)
            st.markdown(f"**Opis**  \n{g['opis']}")
            st.markdown(f"**Siedlisko**  \n{g['siedlisko']}")
            st.markdown(f"**Sezon**  \n{g['sezon']}")
            st.markdown(f"**Podobne gatunki**  \n{g['look_alikes']}")
            if g["status"] in ("trujacy", "smiertelnie_trujacy"):
                st.error("☠️ Gatunek trujący / śmiertelnie trujący — nie zbieraj!")

elif page == "ℹ️ O aplikacji":
    st.title("ℹ️ O aplikacji")
    safety_banner()
    st.markdown(f"""
### Atlas Grzybów – Streamlit + AI

Aplikacja edukacyjna z:
- **{len(GRZYBY)} gatunkami** typowymi dla Polski (jadalne + trujące + look-alike)
- **Skanerem AI** opartym o model z Hugging Face (`dima806/mushrooms_image_detection`)
- Silnymi ostrzeżeniami bezpieczeństwa

**Model AI**  
Publiczny model Vision Transformer wytrenowany na tysiącach zdjęć grzybów.  
Zwraca nazwy naukowe – aplikacja mapuje je na atlas i pokazuje status jadalności.

**Ograniczenia**  
Model nie zna wszystkich polskich gatunków. Wynik to tylko podpowiedź.  
**Nigdy nie opieraj decyzji o zjedzeniu wyłącznie na aplikacji.**

---
Projekt ma charakter wyłącznie edukacyjny.
Autor nie ponosi odpowiedzialności za decyzje o zbieraniu lub spożywaniu grzybów.
""")
