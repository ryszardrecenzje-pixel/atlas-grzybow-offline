import streamlit as st
from PIL import Image
import random

# ============================================================
# KONFIGURACJA STRONY
# ============================================================
st.set_page_config(
    page_title="Atlas Grzybów",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# BAZA GATUNKÓW (możesz łatwo rozbudować)
# ============================================================
GRZYBY = [
    {
        "id": 1,
        "nazwa_polska": "Borowik szlachetny",
        "nazwa_lacinska": "Boletus edulis",
        "status": "jadalny",
        "opis": "Kapelusz brązowy do ciemnobrązowego, gąbka najpierw biała, potem żółtawa. Trzon masywny z wyraźną białą siateczką w górnej części. Smak łagodny, orzechowy.",
        "siedlisko": "Lasy liściaste i mieszane, często pod dębami i bukami",
        "sezon": "VI–X",
        "look_alikes": "Borowik szatański (trujący), goryczak żółciowy (niejadalny)",
    },
    {
        "id": 2,
        "nazwa_polska": "Muchomor sromotnikowy",
        "nazwa_lacinska": "Amanita phalloides",
        "status": "smiertelnie_trujacy",
        "opis": "Kapelusz oliwkowozielony do żółtozielonego, białe blaszki, biały pierścień i wyraźna pochwa u podstawy trzonu. Zapach młodych owocników słodkawy.",
        "siedlisko": "Lasy liściaste, szczególnie pod dębami",
        "sezon": "VII–X",
        "look_alikes": "Gąska zielonka, czubajka kania, muchomor cytrynowy",
    },
    {
        "id": 3,
        "nazwa_polska": "Kurka",
        "nazwa_lacinska": "Cantharellus cibarius",
        "status": "jadalny",
        "opis": "Owocnik lejkowaty, barwy żółtej do pomarańczowej. Blaszki zbiegające, grube, rozwidlone. Zapach owocowy.",
        "siedlisko": "Lasy iglaste i mieszane",
        "sezon": "VI–X",
        "look_alikes": "Lisówka pomarańczowa (niejadalna)",
    },
    {
        "id": 4,
        "nazwa_polska": "Podgrzybek brunatny",
        "nazwa_lacinska": "Imleria badia",
        "status": "jadalny",
        "opis": "Kapelusz ciemnobrązowy, gąbka żółtawa, siniejąca po uszkodzeniu. Trzon brązowy, bez siateczki.",
        "siedlisko": "Lasy iglaste, szczególnie sosnowe",
        "sezon": "VI–XI",
        "look_alikes": "Goryczak żółciowy (niejadalny)",
    },
    {
        "id": 5,
        "nazwa_polska": "Muchomor czerwony",
        "nazwa_lacinska": "Amanita muscaria",
        "status": "trujacy",
        "opis": "Kapelusz czerwony z białymi kłaczkami, białe blaszki, pierścień i bulwiasta podstawa z obrączkami.",
        "siedlisko": "Lasy iglaste i liściaste",
        "sezon": "VII–X",
        "look_alikes": "Muchomor królewski",
    },
    {
        "id": 6,
        "nazwa_polska": "Maślak zwyczajny",
        "nazwa_lacinska": "Suillus luteus",
        "status": "jadalny",
        "opis": "Kapelusz brązowy, śliski, gąbka żółta. Trzon z wyraźnym pierścieniem. Skórkę kapelusza zwykle ściąga się.",
        "siedlisko": "Lasy sosnowe",
        "sezon": "VI–X",
        "look_alikes": "Maślak pstry",
    },
    {
        "id": 7,
        "nazwa_polska": "Czubajka kania",
        "nazwa_lacinska": "Macrolepiota procera",
        "status": "jadalny",
        "opis": "Duży kapelusz z brązowymi łuskami na jasnym tle, wolny pierścień, trzon z wzorem wężowym. Blaszki białe.",
        "siedlisko": "Łąki, skraje lasów, polany",
        "sezon": "VII–X",
        "look_alikes": "Muchomor sromotnikowy (młode), czubajka czerwieniejąca",
    },
    {
        "id": 8,
        "nazwa_polska": "Goryczak żółciowy",
        "nazwa_lacinska": "Tylopilus felleus",
        "status": "niejadalny",
        "opis": "Wygląda podobnie do borowika, ale gąbka różowieje, a smak jest bardzo gorzki. Trzon z ciemną siateczką.",
        "siedlisko": "Lasy iglaste i mieszane",
        "sezon": "VII–X",
        "look_alikes": "Borowik szlachetny, podgrzybek",
    },
    {
        "id": 9,
        "nazwa_polska": "Koźlarz babka",
        "nazwa_lacinska": "Leccinum scabrum",
        "status": "jadalny",
        "opis": "Kapelusz szarobrązowy do czarnobrązowego, gąbka biała, ciemniejąca. Trzon biały z czarnymi kłaczkami.",
        "siedlisko": "Lasy liściaste, szczególnie pod brzozami",
        "sezon": "VI–X",
        "look_alikes": "Koźlarz czerwony",
    },
    {
        "id": 10,
        "nazwa_polska": "Pieprznik jadalny",
        "nazwa_lacinska": "Cantharellus cibarius",
        "status": "jadalny",
        "opis": "Inna nazwa kurki. Owocnik lejkowaty, żółty, blaszki zbiegające.",
        "siedlisko": "Lasy iglaste i mieszane",
        "sezon": "VI–X",
        "look_alikes": "Lisówka pomarańczowa",
    },
]

STATUS_LABELS = {
    "jadalny": ("Jadalny", "🟢"),
    "niejadalny": ("Niejadalny", "🟠"),
    "trujacy": ("Trujący", "🔴"),
    "smiertelnie_trujacy": ("Śmiertelnie trujący", "☠️"),
}

STATUS_COLORS = {
    "jadalny": "#2e7d32",
    "niejadalny": "#ef6c00",
    "trujacy": "#c62828",
    "smiertelnie_trujacy": "#b71c1c",
}


# ============================================================
# FUNKCJE POMOCNICZE
# ============================================================
def status_badge(status: str) -> str:
    label, emoji = STATUS_LABELS.get(status, (status, ""))
    color = STATUS_COLORS.get(status, "#666")
    return f"""
    <span style="
        background-color:{color};
        color:white;
        padding:4px 12px;
        border-radius:20px;
        font-weight:bold;
        font-size:0.9em;
    ">{emoji} {label}</span>
    """


def safety_banner(compact: bool = False):
    if compact:
        st.error("⚠️ **Nigdy nie jedz grzyba tylko na podstawie aplikacji!**")
    else:
        st.error(
            """
            ### ⚠️ UWAGA – BEZPIECZEŃSTWO
            
            **Nigdy nie jedz grzyba tylko na podstawie wyniku tej aplikacji.**
            
            Identyfikacja AI / zdjęciowa nigdy nie jest w 100% pewna.  
            Muchomor sromotnikowy i inne śmiertelnie trujące gatunki mogą być pomylone z jadalnymi.
            
            W razie jakichkolwiek wątpliwości – **nie zbieraj**.
            """
        )


def demo_classify(image: Image.Image) -> list[dict]:
    """Prosty tryb demo – losowe wyniki z bazy (do czasu dodania prawdziwego modelu)."""
    # W przyszłości tutaj można podłączyć prawdziwy model (TensorFlow, ONNX, API itd.)
    candidates = random.sample(GRZYBY, k=min(3, len(GRZYBY)))
    confidences = [0.72, 0.18, 0.07]
    results = []
    for i, g in enumerate(candidates):
        results.append(
            {
                "nazwa": g["nazwa_polska"],
                "lacinska": g["nazwa_lacinska"],
                "status": g["status"],
                "confidence": confidences[i] if i < len(confidences) else 0.05,
                "id": g["id"],
            }
        )
    return results


def find_grzyb(query: str) -> list[dict]:
    q = query.lower().strip()
    if not q:
        return GRZYBY
    return [
        g
        for g in GRZYBY
        if q in g["nazwa_polska"].lower() or q in g["nazwa_lacinska"].lower()
    ]


def get_by_id(gid: int) -> dict | None:
    for g in GRZYBY:
        if g["id"] == gid:
            return g
    return None


# ============================================================
# SIDEBAR – NAWIGACJA
# ============================================================
st.sidebar.title("🍄 Atlas Grzybów")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Przejdź do:",
    ["🏠 Start", "📷 Skaner", "📚 Atlas", "ℹ️ O aplikacji"],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.caption("Wersja edukacyjna • Używaj odpowiedzialnie")


# ============================================================
# STRONA: START
# ============================================================
if page == "🏠 Start":
    st.title("🍄 Atlas Grzybów")
    st.markdown("### Rozpoznawaj grzyby ze zdjęcia i przeglądaj atlas")

    safety_banner()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📷 Skaner")
        st.write("Zrób zdjęcie lub wgraj fotkę grzyba i zobacz propozycje gatunków.")
        if st.button("Przejdź do skanera", use_container_width=True, type="primary"):
            st.session_state["goto"] = "📷 Skaner"
            st.rerun()

    with col2:
        st.markdown("#### 📚 Atlas")
        st.write("Przeglądaj gatunki, szukaj po nazwie i sprawdzaj look-alike.")
        if st.button("Przejdź do atlasu", use_container_width=True):
            st.session_state["goto"] = "📚 Atlas"
            st.rerun()

    st.markdown("---")
    st.info(
        f"W bazie znajduje się obecnie **{len(GRZYBY)} gatunków**. "
        "Możesz łatwo rozbudować listę w pliku `app.py`."
    )


# ============================================================
# STRONA: SKANER
# ============================================================
elif page == "📷 Skaner":
    st.title("📷 Skaner grzybów")
    safety_banner(compact=True)

    st.markdown("Zrób zdjęcie aparatem lub wgraj gotowe zdjęcie grzyba.")

    tab_cam, tab_upload = st.tabs(["Aparat", "Wgraj zdjęcie"])

    image = None

    with tab_cam:
        cam_photo = st.camera_input("Zrób zdjęcie grzyba")
        if cam_photo is not None:
            image = Image.open(cam_photo)

    with tab_upload:
        uploaded = st.file_uploader(
            "Wybierz plik (JPG / PNG)",
            type=["jpg", "jpeg", "png"],
        )
        if uploaded is not None:
            image = Image.open(uploaded)

    if image is not None:
        st.image(image, caption="Twoje zdjęcie", use_container_width=True)

        if st.button("🔍 Rozpoznaj grzyba", type="primary", use_container_width=True):
            with st.spinner("Analizuję zdjęcie..."):
                results = demo_classify(image)

            st.success("Wyniki (tryb demo – nie jest to prawdziwy model AI):")
            st.caption(
                "To przykładowe wyniki. W przyszłości można podłączyć prawdziwy model klasyfikacji."
            )

            for r in results:
                conf_pct = int(r["confidence"] * 100)
                label, emoji = STATUS_LABELS.get(r["status"], (r["status"], ""))

                with st.container(border=True):
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(f"**{r['nazwa']}**  \n*{r['lacinska']}*")
                        st.progress(r["confidence"], text=f"Pewność: {conf_pct}%")
                    with c2:
                        st.markdown(status_badge(r["status"]), unsafe_allow_html=True)
                        if st.button("Szczegóły", key=f"det_{r['id']}"):
                            st.session_state["selected_id"] = r["id"]
                            st.session_state["goto"] = "📚 Atlas"
                            st.rerun()

            st.warning(
                "⚠️ Pamiętaj: nawet wysoka „pewność” nie oznacza, że grzyb jest jadalny. "
                "Zawsze weryfikuj cechy diagnostyczne."
            )
    else:
        st.info("Dodaj zdjęcie, aby uruchomić rozpoznawanie.")


# ============================================================
# STRONA: ATLAS
# ============================================================
elif page == "📚 Atlas":
    st.title("📚 Atlas gatunków")
    safety_banner(compact=True)

    # Jeśli przyszliśmy ze skanera z wybranym ID
    if "selected_id" in st.session_state:
        g = get_by_id(st.session_state["selected_id"])
        if g:
            st.session_state.pop("selected_id", None)
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

            st.markdown("---")
            if st.button("← Wróć do listy"):
                st.rerun()
            st.stop()

    # Wyszukiwarka
    query = st.text_input("🔍 Szukaj grzyba (nazwa polska lub łacińska)", "")
    filtered = find_grzyb(query)

    st.caption(f"Znaleziono: {len(filtered)} gatunków")

    for g in filtered:
        label, emoji = STATUS_LABELS.get(g["status"], (g["status"], ""))
        with st.expander(f"{emoji} **{g['nazwa_polska']}** — {g['nazwa_lacinska']}"):
            st.markdown(status_badge(g["status"]), unsafe_allow_html=True)
            st.markdown(f"**Opis**  \n{g['opis']}")
            st.markdown(f"**Siedlisko**  \n{g['siedlisko']}")
            st.markdown(f"**Sezon**  \n{g['sezon']}")
            st.markdown(f"**Podobne gatunki**  \n{g['look_alikes']}")

            if g["status"] in ("trujacy", "smiertelnie_trujacy"):
                st.error("☠️ Gatunek trujący / śmiertelnie trujący — nie zbieraj!")


# ============================================================
# STRONA: O APLIKACJI
# ============================================================
elif page == "ℹ️ O aplikacji":
    st.title("ℹ️ O aplikacji")
    safety_banner()

    st.markdown(
        """
        ### Atlas Grzybów
        
        Prosta aplikacja edukacyjna stworzona w **Streamlit**.
        
        **Funkcje:**
        - Atlas gatunków z opisami i statusem jadalności
        - Skaner zdjęć (tryb demo)
        - Ostrzeżenia bezpieczeństwa
        
        **Jak dodać więcej gatunków?**  
        Edytuj listę `GRZYBY` w pliku `app.py`.
        
        **Jak podłączyć prawdziwy model AI?**  
        W funkcji `demo_classify()` możesz wstawić wywołanie modelu 
        (TensorFlow, ONNX Runtime, Hugging Face, własne API itd.).
        
        ---
        
        Projekt ma charakter **wyłącznie edukacyjny**.  
        Autor nie ponosi odpowiedzialności za decyzje o zbieraniu lub spożywaniu grzybów.
        """
    )


# Obsługa szybkiego przejścia z przycisków na stronie Start
if "goto" in st.session_state:
    # Streamlit radio nie da się ustawić programowo w prosty sposób,
    # więc po prostu czyścimy flagę – użytkownik klika w sidebar.
    del st.session_state["goto"]
