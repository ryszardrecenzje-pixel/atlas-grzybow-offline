# Atlas Grzybów (Streamlit)

Aplikacja webowa do rozpoznawania grzybów – atlas + skaner zdjęć.

Działa online (Streamlit Community Cloud) lub lokalnie.

## Ważne ostrzeżenie

**NIGDY nie jedz grzyba tylko na podstawie wyniku aplikacji.**

Identyfikacja nigdy nie jest w 100% pewna.  
Muchomor sromotnikowy i inne śmiertelnie trujące gatunki mogą być pomylone.  
W razie jakichkolwiek wątpliwości – **nie zbieraj**.

## Uruchomienie lokalne

```bash
git clone https://github.com/TWOJA_NAZWA/atlas-grzybow-streamlit.git
cd atlas-grzybow-streamlit
pip install -r requirements.txt
streamlit run app.py
```

## Wdrożenie na Streamlit Cloud

1. Wrzuć kod na GitHub (publiczne repozytorium).
2. Wejdź na [share.streamlit.io](https://share.streamlit.io).
3. Połącz konto GitHub.
4. Wybierz repozytorium → plik `app.py`.
5. Kliknij **Deploy**.

## Funkcje

- Atlas gatunków z wyszukiwarką
- Skaner (upload zdjęcia lub aparat)
- Status jadalności + look-alike
- Silne ostrzeżenia bezpieczeństwa
- Tryb demo (bez modelu AI)

## Licencja

MIT
