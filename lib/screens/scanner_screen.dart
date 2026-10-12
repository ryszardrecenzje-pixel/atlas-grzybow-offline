import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:permission_handler/permission_handler.dart';
import '../services/classifier_service.dart';
import '../widgets/safety_banner.dart';
import '../database/database_helper.dart';
import '../models/grzyb.dart';
import 'detail_screen.dart';

class ScannerScreen extends StatefulWidget {
  const ScannerScreen({super.key});

  @override
  State<ScannerScreen> createState() => _ScannerScreenState();
}

class _ScannerScreenState extends State<ScannerScreen> {
  CameraController? _controller;
  List<CameraDescription>? _cameras;
  bool _isReady = false;
  bool _isClassifying = false;
  List<Map<String, dynamic>> _results = [];
  final ClassifierService _classifier = ClassifierService();
  String? _error;

  @override
  void initState() {
    super.initState();
    _init();
  }

  Future<void> _init() async {
    await _classifier.loadModel();

    final status = await Permission.camera.request();
    if (!status.isGranted) {
      setState(() => _error = 'Brak uprawnień do kamery');
      return;
    }

    try {
      _cameras = await availableCameras();
      if (_cameras == null || _cameras!.isEmpty) {
        setState(() => _error = 'Nie znaleziono kamery');
        return;
      }

      _controller = CameraController(
        _cameras!.first,
        ResolutionPreset.medium,
        enableAudio: false,
      );

      await _controller!.initialize();
      if (mounted) {
        setState(() => _isReady = true);
      }
    } catch (e) {
      setState(() => _error = 'Błąd kamery: $e');
    }
  }

  Future<void> _captureAndClassify() async {
    if (_controller == null || !_controller!.value.isInitialized) return;
    if (_isClassifying) return;

    setState(() {
      _isClassifying = true;
      _results = [];
    });

    try {
      final XFile file = await _controller!.takePicture();
      final Uint8List bytes = await file.readAsBytes();
      final results = await _classifier.classify(bytes);

      if (mounted) {
        setState(() {
          _results = results;
          _isClassifying = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isClassifying = false;
          _error = 'Błąd klasyfikacji: $e';
        });
      }
    }
  }

  Future<void> _openDetail(String label) async {
    final all = await DatabaseHelper.instance.getAllGrzyby();
    Grzyb? found;
    try {
      found = all.firstWhere(
        (g) => g.nazwaPolska.toLowerCase() == label.toLowerCase(),
      );
    } catch (_) {
      found = null;
    }

    if (found != null && mounted) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(grzyb: found!)),
      );
    } else if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Brak szczegółów dla: $label')),
      );
    }
  }

  @override
  void dispose() {
    _controller?.dispose();
    _classifier.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Skaner grzybów'),
        backgroundColor: Colors.green.shade800,
        foregroundColor: Colors.white,
      ),
      body: Column(
        children: [
          const SafetyBanner(compact: true),
          if (_error != null)
            Expanded(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Text(
                    _error!,
                    textAlign: TextAlign.center,
                    style: const TextStyle(fontSize: 16, color: Colors.red),
                  ),
                ),
              ),
            )
          else if (!_isReady)
            const Expanded(
              child: Center(child: CircularProgressIndicator()),
            )
          else ...[
            Expanded(
              flex: 3,
              child: Stack(
                fit: StackFit.expand,
                children: [
                  CameraPreview(_controller!),
                  if (_isClassifying)
                    Container(
                      color: Colors.black54,
                      child: const Center(
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            CircularProgressIndicator(color: Colors.white),
                            SizedBox(height: 16),
                            Text(
                              'Analizuję...',
                              style: TextStyle(color: Colors.white, fontSize: 18),
                            ),
                          ],
                        ),
                      ),
                    ),
                ],
              ),
            ),
            Expanded(
              flex: 2,
              child: Container(
                width: double.infinity,
                color: Colors.grey.shade100,
                padding: const EdgeInsets.all(16),
                child: Column(
                  children: [
                    if (_results.isEmpty && !_isClassifying)
                      const Expanded(
                        child: Center(
                          child: Text(
                            'Skieruj aparat na grzyba\ni naciśnij przycisk',
                            textAlign: TextAlign.center,
                            style: TextStyle(fontSize: 16, color: Colors.grey),
                          ),
                        ),
                      )
                    else if (_results.isNotEmpty)
                      Expanded(
                        child: ListView.builder(
                          itemCount: _results.length,
                          itemBuilder: (context, index) {
                            final r = _results[index];
                            final conf = (r['confidence'] as double) * 100;
                            return Card(
                              child: ListTile(
                                title: Text(
                                  r['label'] as String,
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold),
                                ),
                                subtitle: LinearProgressIndicator(
                                  value: r['confidence'] as double,
                                  backgroundColor: Colors.grey.shade300,
                                  color: conf > 50
                                      ? Colors.green
                                      : Colors.orange,
                                ),
                                trailing: Text(
                                  '${conf.toStringAsFixed(0)}%',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold),
                                ),
                                onTap: () =>
                                    _openDetail(r['label'] as String),
                              ),
                            );
                          },
                        ),
                      ),
                    const SizedBox(height: 8),
                    SizedBox(
                      width: double.infinity,
                      height: 52,
                      child: ElevatedButton.icon(
                        onPressed: _isClassifying ? null : _captureAndClassify,
                        icon: const Icon(Icons.camera),
                        label: Text(
                          _isClassifying ? 'Analizuję...' : 'Rozpoznaj grzyba',
                          style: const TextStyle(fontSize: 16),
                        ),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.green.shade700,
                          foregroundColor: Colors.white,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                        ),
                      ),
                    ),
                    if (!_classifier.isModelLoaded)
                      Padding(
                        padding: const EdgeInsets.only(top: 8),
                        child: Text(
                          'Tryb demo (brak modelu TFLite)',
                          style: TextStyle(
                              fontSize: 12, color: Colors.grey.shade600),
                        ),
                      ),
                  ],
                ),
              ),
            ),
          ],
        ],
      ),
    );
  }
}
