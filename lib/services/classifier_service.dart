import 'dart:typed_data';
import 'package:flutter/services.dart';
import 'package:tflite_flutter/tflite_flutter.dart';
import 'package:image/image.dart' as img;

class ClassifierService {
  Interpreter? _interpreter;
  List<String> labels = [];
  bool isModelLoaded = false;

  /// Ładuje model TFLite (jeśli istnieje).
  /// Jeśli model nie zostanie znaleziony – aplikacja działa w trybie demo.
  Future<void> loadModel() async {
    try {
      _interpreter = await Interpreter.fromAsset('assets/model/grzyby_model.tflite');
      final labelsData = await rootBundle.loadString('assets/model/labels.txt');
      labels = labelsData
          .split('\n')
          .map((e) => e.trim())
          .where((e) => e.isNotEmpty)
          .toList();
      isModelLoaded = true;
      print('Model TFLite załadowany pomyślnie (${labels.length} klas)');
    } catch (e) {
      print('Model niezaładowany – tryb demo: $e');
      isModelLoaded = false;
      // Etykiety demo
      labels = [
        'Borowik szlachetny',
        'Podgrzybek brunatny',
        'Kurka',
        'Muchomor sromotnikowy',
        'Muchomor czerwony',
        'Maślak zwyczajny',
        'Czubajka kania',
        'Goryczak żółciowy',
      ];
    }
  }

  /// Klasyfikuje obraz. Zwraca listę map: {'label': String, 'confidence': double}
  Future<List<Map<String, dynamic>>> classify(Uint8List imageBytes) async {
    if (!isModelLoaded || _interpreter == null) {
      // Tryb demo – przykładowe wyniki
      await Future.delayed(const Duration(milliseconds: 600));
      return [
        {'label': 'Borowik szlachetny', 'confidence': 0.68},
        {'label': 'Podgrzybek brunatny', 'confidence': 0.19},
        {'label': 'Goryczak żółciowy', 'confidence': 0.07},
      ];
    }

    try {
      // Dekoduj i przeskaluj obraz do 224x224
      final original = img.decodeImage(imageBytes);
      if (original == null) return [];

      final resized = img.copyResize(original, width: 224, height: 224);

      // Przygotuj tensor wejściowy (1, 224, 224, 3) – normalizacja 0-1
      final input = List.generate(
        1,
        (_) => List.generate(
          224,
          (y) => List.generate(
            224,
            (x) {
              final pixel = resized.getPixel(x, y);
              return [
                pixel.r / 255.0,
                pixel.g / 255.0,
                pixel.b / 255.0,
              ];
            },
          ),
        ),
      );

      // Wyjście
      final output = List.filled(1 * labels.length, 0.0).reshape([1, labels.length]);

      _interpreter!.run(input, output);

      // Zamień na listę wyników i posortuj
      final results = <Map<String, dynamic>>[];
      for (var i = 0; i < labels.length; i++) {
        results.add({
          'label': labels[i],
          'confidence': output[0][i] as double,
        });
      }

      results.sort((a, b) => (b['confidence'] as double).compareTo(a['confidence'] as double));
      return results.take(5).toList();
    } catch (e) {
      print('Błąd klasyfikacji: $e');
      return [];
    }
  }

  void dispose() {
    _interpreter?.close();
  }
}
