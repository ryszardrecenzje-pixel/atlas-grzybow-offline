# Atlas Grzybów (Streamlit + AI)

Aplikacja webowa do rozpoznawania grzybów – rozbudowany atlas polskich gatunków + skaner AI.

## Ważne ostrzeżenie

**NIGDY nie jedz grzyba tylko na podstawie wyniku aplikacji.**

Identyfikacja AI nigdy nie jest w 100% pewna.  
Muchomor sromotnikowy i inne śmiertelnie trujące gatunki mogą być pomylone.  
W razie jakichkolwiek wątpliwości – **nie zbieraj**.

## Funkcje

- **26 gatunków** typowych dla Polski (jadalne, niejadalne, trujące, śmiertelnie trujące)
- Skaner AI (model Hugging Face: `dima806/mushrooms_image_detection`)
- Atlas z wyszukiwarką i filtrem statusu
- Look-alike (podobne gatunki)
- Silne ostrzeżenia bezpieczeństwa
- Tryb demo gdy model się nie załaduje

## Uruchomienie lokalne

```bash
git clone https://github.com/TWOJA_NAZWA/atlas-grzybow-streamlit.git
cd atlas-grzybow-streamlit
pip install -r requirements.txt
streamlit run app.py
```

## Wdrożenie na Streamlit Cloud

1. Wrzuć kod na publiczne repozytorium GitHub.
2. Wejdź na https://share.streamlit.io
3. New app → wybierz repozytorium → plik `app.py`
4. Deploy

**Uwaga:** Pierwsze uruchomienie na Cloud może potrwać dłużej (pobieranie modelu torch + transformers).

## Licencja

MIT
