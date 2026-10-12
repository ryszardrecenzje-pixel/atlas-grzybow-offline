import 'package:flutter/material.dart';

class SafetyBanner extends StatelessWidget {
  final bool compact;

  const SafetyBanner({super.key, this.compact = false});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      color: Colors.red.shade900,
      padding: EdgeInsets.symmetric(
        horizontal: 16,
        vertical: compact ? 10 : 14,
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Icon(Icons.warning_amber_rounded, color: Colors.white, size: 28),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              compact
                  ? 'Nigdy nie jedz grzyba tylko na podstawie aplikacji!'
                  : 'UWAGA!\nNigdy nie jedz grzyba tylko na podstawie wyniku aplikacji.\nW razie jakichkolwiek wątpliwości – nie zbieraj.',
              style: const TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
                fontSize: 14,
                height: 1.3,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
