import 'package:flutter/material.dart';
import '../database/database_helper.dart';
import '../models/grzyb.dart';
import 'detail_screen.dart';
import '../widgets/safety_banner.dart';

class AtlasScreen extends StatefulWidget {
  const AtlasScreen({super.key});

  @override
  State<AtlasScreen> createState() => _AtlasScreenState();
}

class _AtlasScreenState extends State<AtlasScreen> {
  List<Grzyb> _grzyby = [];
  List<Grzyb> _filtered = [];
  bool _loading = true;
  final _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    final data = await DatabaseHelper.instance.getAllGrzyby();
    setState(() {
      _grzyby = data;
      _filtered = data;
      _loading = false;
    });
  }

  void _onSearch(String query) {
    if (query.isEmpty) {
      setState(() => _filtered = _grzyby);
      return;
    }
    final lower = query.toLowerCase();
    setState(() {
      _filtered = _grzyby
          .where((g) =>
              g.nazwaPolska.toLowerCase().contains(lower) ||
              g.nazwaLacinska.toLowerCase().contains(lower))
          .toList();
    });
  }

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
        title: const Text('Atlas gatunków'),
        backgroundColor: Colors.green.shade800,
        foregroundColor: Colors.white,
      ),
      body: Column(
        children: [
          const SafetyBanner(compact: true),
          Padding(
            padding: const EdgeInsets.all(12),
            child: TextField(
              controller: _searchController,
              onChanged: _onSearch,
              decoration: InputDecoration(
                hintText: 'Szukaj grzyba...',
                prefixIcon: const Icon(Icons.search),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
                filled: true,
                fillColor: Colors.grey.shade100,
              ),
            ),
          ),
          Expanded(
            child: _loading
                ? const Center(child: CircularProgressIndicator())
                : _filtered.isEmpty
                    ? const Center(child: Text('Brak wyników'))
                    : ListView.builder(
                        itemCount: _filtered.length,
                        itemBuilder: (context, index) {
                          final g = _filtered[index];
                          return Card(
                            margin: const EdgeInsets.symmetric(
                                horizontal: 12, vertical: 6),
                            child: ListTile(
                              leading: CircleAvatar(
                                backgroundColor: _statusColor(g.status),
                                child: Text(
                                  g.nazwaPolska[0],
                                  style: const TextStyle(color: Colors.white),
                                ),
                              ),
                              title: Text(
                                g.nazwaPolska,
                                style: const TextStyle(
                                    fontWeight: FontWeight.bold),
                              ),
                              subtitle: Text(g.nazwaLacinska),
                              trailing: Container(
                                padding: const EdgeInsets.symmetric(
                                    horizontal: 8, vertical: 4),
                                decoration: BoxDecoration(
                                  color: _statusColor(g.status).withOpacity(0.15),
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: Text(
                                  g.statusLabel,
                                  style: TextStyle(
                                    color: _statusColor(g.status),
                                    fontWeight: FontWeight.w600,
                                    fontSize: 12,
                                  ),
                                ),
                              ),
                              onTap: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (_) => DetailScreen(grzyb: g),
                                  ),
                                );
                              },
                            ),
                          );
                        },
                      ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }
}
