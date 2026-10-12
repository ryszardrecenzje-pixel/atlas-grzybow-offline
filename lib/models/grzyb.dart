class Grzyb {
  final int id;
  final String nazwaPolska;
  final String nazwaLacinska;
  final String status; // jadalny | niejadalny | trujacy | smiertelnie_trujacy
  final String opis;
  final String siedlisko;
  final String sezon;
  final String lookAlikes;
  final String imageAsset;

  Grzyb({
    required this.id,
    required this.nazwaPolska,
    required this.nazwaLacinska,
    required this.status,
    required this.opis,
    required this.siedlisko,
    required this.sezon,
    required this.lookAlikes,
    required this.imageAsset,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'nazwa_polska': nazwaPolska,
      'nazwa_lacinska': nazwaLacinska,
      'status': status,
      'opis': opis,
      'siedlisko': siedlisko,
      'sezon': sezon,
      'look_alikes': lookAlikes,
      'image_asset': imageAsset,
    };
  }

  factory Grzyb.fromMap(Map<String, dynamic> map) {
    return Grzyb(
      id: map['id'] as int,
      nazwaPolska: map['nazwa_polska'] as String,
      nazwaLacinska: map['nazwa_lacinska'] as String,
      status: map['status'] as String,
      opis: map['opis'] as String? ?? '',
      siedlisko: map['siedlisko'] as String? ?? '',
      sezon: map['sezon'] as String? ?? '',
      lookAlikes: map['look_alikes'] as String? ?? '',
      imageAsset: map['image_asset'] as String? ?? '',
    );
  }

  bool get isDangerous =>
      status == 'trujacy' || status == 'smiertelnie_trujacy';

  String get statusLabel {
    switch (status) {
      case 'jadalny':
        return 'Jadalny';
      case 'niejadalny':
        return 'Niejadalny';
      case 'trujacy':
        return 'Trujący';
      case 'smiertelnie_trujacy':
        return 'Śmiertelnie trujący';
      default:
        return status;
    }
  }
}
