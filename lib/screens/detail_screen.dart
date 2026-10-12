import 'package:flutter/material.dart';
import '../models/grzyb.dart';
import '../widgets/safety_banner.dart';

class DetailScreen extends StatelessWidget {
  final Grzyb grzyb;

  const DetailScreen({super.key, required this.grzyb});

  Color _statusColor(String status) {
    switch (status) {
      case 'jadalny':
        return Colors.green;
      case 'niejadalny':
        return Colors.orange;
      case 'trujacy':
        return Colors.red.shade700;
      case 'smiertelnie_trujacy':
        return Colors.red.shade900;
      default:
        return Colors.grey;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(grzyb.nazwaPolska),
        backgroundColor: Colors.green.shade800,
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (grzyb.isDangerous) const SafetyBanner(),
            Container(
              width: double.infinity,
              color: _statusColor(grzyb.status).withOpacity(0.15),
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  Text(
                    grzyb.nazwaPolska,
                    style: const TextStyle(
                      fontSize: 26,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 4),
                  Text(
                    grzyb.nazwaLacinska,
                    style: TextStyle(
                      fontSize: 16,
                      fontStyle: FontStyle.italic,
                      color: Colors.grey.shade700,
                    ),
                  ),
                  const SizedBox(height: 12),
                  Container(
                    padding: const EdgeInsets.symmetric(
                        horizontal: 16, vertical: 8),
                    decoration: BoxDecoration(
                      color: _statusColor(grzyb.status),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      grzyb.statusLabel.toUpperCase(),
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 1,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  _section('Opis', grzyb.opis),
                  const SizedBox(height: 20),
                  _section('Siedlisko', grzyb.siedlisko),
                  const SizedBox(height: 20),
                  _section('Sezon', grzyb.sezon),
                  const SizedBox(height: 20),
                  _section('Podobne gatunki (look-alikes)', grzyb.lookAlikes),
                  if (grzyb.isDangerous) ...[
                    const SizedBox(height: 32),
                    Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: Colors.red.shade50,
                        border: Border.all(color: Colors.red.shade700, width: 2),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: const Column(
                        children: [
                          Icon(Icons.dangerous, color: Colors.red, size: 40),
                          SizedBox(height: 8),
                          Text(
                            'GATUNEK TRUJĄCY LUB ŚMIERTELNIE TRUJĄCY',
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              color: Colors.red,
                              fontWeight: FontWeight.bold,
                              fontSize: 16,
                            ),
                          ),
                          SizedBox(height: 4),
                          Text(
                            'Nie zbieraj. Nie jedz.',
                            style: TextStyle(
                              color: Colors.red,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _section(String title, String content) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title,
          style: const TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.bold,
            color: Colors.green,
          ),
        ),
        const SizedBox(height: 6),
        Text(
          content.isEmpty ? 'Brak danych' : content,
          style: const TextStyle(fontSize: 15, height: 1.4),
        ),
      ],
    );
  }
}
