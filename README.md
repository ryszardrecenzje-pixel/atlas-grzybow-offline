# Atlas Grzybów Offline

Aplikacja mobilna (Android + iOS) do rozpoznawania grzybów **całkowicie offline**.

## Ważne ostrzeżenie bezpieczeństwa

**NIGDY nie jedz grzyba tylko na podstawie wyniku aplikacji.**

Identyfikacja AI nigdy nie jest w 100% pewna.  
Muchomor sromotnikowy i inne śmiertelnie trujące gatunki mogą być pomylone z jadalnymi.  
W razie jakichkolwiek wątpliwości – **nie zbieraj**.

Aplikacja służy wyłącznie jako pomoc edukacyjna i atlas.  
Autor nie ponosi odpowiedzialności za skutki użycia aplikacji do decyzji o zbieraniu lub spożywaniu grzybów.

## Funkcje

- Działa w 100% offline (po pierwszym uruchomieniu)
- Skaner ze zdjęcia / aparatu
- Atlas gatunków z opisami, statusem jadalności i look-alike’ami
- Lokalna baza SQLite
- Silne, wyraźne ostrzeżenia bezpieczeństwa
- Tryb demo (działa nawet bez modelu TFLite)

## Wymagania

- Flutter SDK 3.0+
- Android Studio / Xcode (do budowania na urządzenie)
- Telefon lub emulator

## Jak uruchomić

### Z archiwum ZIP

1. Rozpakuj archiwum:
```bash
unzip atlas-grzybow-offline.zip
cd atlas-grzybow-offline
```

2. Wygeneruj foldery platformowe (`android/`, `ios/`):
```bash
flutter create .
```
(To nie nadpisze istniejących plików w `lib/` i `assets/`.)

3. Zainstaluj zależności:
```bash
flutter pub get
```

4. (Opcjonalnie) Dodaj swój model TFLite:
- Umieść plik `grzyby_model.tflite` w katalogu `assets/model/`
- Upewnij się, że `labels.txt` ma etykiety w tej samej kolejności co wyjścia modelu

5. Uruchom:
```bash
flutter run
```

### Z GitHuba

1. Sklonuj repozytorium:
```bash
git clone https://github.com/TWOJA_NAZWA/atlas-grzybow-offline.git
cd atlas-grzybow-offline
```

2. Wygeneruj foldery platformowe:
```bash
flutter create .
```

3. Dalej jak w punktach 3–5 powyżej.

## Struktura projektu

```
lib/
├── main.dart
├── models/grzyb.dart
├── database/database_helper.dart
├── services/classifier_service.dart
├── screens/
│   ├── home_screen.dart
│   ├── atlas_screen.dart
│   ├── scanner_screen.dart
│   └── detail_screen.dart
└── widgets/safety_banner.dart

assets/
├── images/     ← zdjęcia grzybów do atlasu
├── model/      ← grzyby_model.tflite + labels.txt
└── data/
```

## Jak dodać własny model

1. Wytrenuj model klasyfikacji obrazów (zalecane: MobileNet / EfficientNet / ViT).
2. Skonwertuj do formatu TensorFlow Lite (`.tflite`).
3. Upewnij się, że rozmiar wejścia modelu to np. 224×224.
4. Umieść pliki w `assets/model/`.
5. Zaktualizuj listę etykiet w `labels.txt`.

Dopóki nie dodasz modelu, aplikacja działa w **trybie demo** (pokazuje przykładowe wyniki).

## Status jadalności w bazie

- `jadalny`
- `niejadalny`
- `trujacy`
- `smiertelnie_trujacy`

## Licencja

MIT License – zobacz plik `LICENSE`.

## Autor

Projekt edukacyjny. Używaj odpowiedzialnie.
