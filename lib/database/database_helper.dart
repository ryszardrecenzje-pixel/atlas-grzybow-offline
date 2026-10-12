import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/grzyb.dart';

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  DatabaseHelper._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('atlas_grzybow.db');
    return _database!;
  }

  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(
      path,
      version: 1,
      onCreate: _createDB,
    );
  }

  Future _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE grzyby (
        id INTEGER PRIMARY KEY,
        nazwa_polska TEXT NOT NULL,
        nazwa_lacinska TEXT NOT NULL,
        status TEXT NOT NULL,
        opis TEXT,
        siedlisko TEXT,
        sezon TEXT,
        look_alikes TEXT,
        image_asset TEXT
      )
    ''');

    await _insertSampleData(db);
  }

  Future _insertSampleData(Database db) async {
    final samples = [
      {
        'id': 1,
        'nazwa_polska': 'Borowik szlachetny',
        'nazwa_lacinska': 'Boletus edulis',
        'status': 'jadalny',
        'opis':
            'Kapelusz brązowy do ciemnobrązowego, gąbka najpierw biała, potem żółtawa. Trzon masywny z wyraźną białą siateczką w górnej części. Smak łagodny, orzechowy.',
        'siedlisko': 'Lasy liściaste i mieszane, często pod dębami i bukami',
        'sezon': 'VI–X',
        'look_alikes': 'Borowik szatański (trujący), goryczak żółciowy (niejadalny)',
        'image_asset': 'assets/images/borowik.jpg',
      },
      {
        'id': 2,
        'nazwa_polska': 'Muchomor sromotnikowy',
        'nazwa_lacinska': 'Amanita phalloides',
        'status': 'smiertelnie_trujacy',
        'opis':
            'Kapelusz oliwkowozielony do żółtozielonego, białe blaszki, biały pierścień i wyraźna pochwa u podstawy trzonu. Zapach młodych owocników słodkawy.',
        'siedlisko': 'Lasy liściaste, szczególnie pod dębami',
        'sezon': 'VII–X',
        'look_alikes': 'Gąska zielonka, czubajka kania, muchomor cytrynowy',
        'image_asset': 'assets/images/muchomor_sromotnikowy.jpg',
      },
      {
        'id': 3,
        'nazwa_polska': 'Kurka',
        'nazwa_lacinska': 'Cantharellus cibarius',
        'status': 'jadalny',
        'opis':
            'Owocnik lejkowaty, barwy żółtej do pomarańczowej. Blaszki zbiegające, grube, rozwidlone. Zapach owocowy.',
        'siedlisko': 'Lasy iglaste i mieszane',
        'sezon': 'VI–X',
        'look_alikes': 'Lisówka pomarańczowa (niejadalna)',
        'image_asset': 'assets/images/kurka.jpg',
      },
      {
        'id': 4,
        'nazwa_polska': 'Podgrzybek brunatny',
        'nazwa_lacinska': 'Imleria badia',
        'status': 'jadalny',
        'opis':
            'Kapelusz ciemnobrązowy, gąbka żółtawa, siniejąca po uszkodzeniu. Trzon brązowy, bez siateczki.',
        'siedlisko': 'Lasy iglaste, szczególnie sosnowe',
        'sezon': 'VI–XI',
        'look_alikes': 'Goryczak żółciowy (niejadalny)',
        'image_asset': 'assets/images/podgrzybek.jpg',
      },
      {
        'id': 5,
        'nazwa_polska': 'Muchomor czerwony',
        'nazwa_lacinska': 'Amanita muscaria',
        'status': 'trujacy',
        'opis':
            'Kapelusz czerwony z białymi kłaczkami, białe blaszki, pierścień i bulwiasta podstawa z obrączkami.',
        'siedlisko': 'Lasy iglaste i liściaste',
        'sezon': 'VII–X',
        'look_alikes': 'Muchomor królewski',
        'image_asset': 'assets/images/muchomor_czerwony.jpg',
      },
      {
        'id': 6,
        'nazwa_polska': 'Maślak zwyczajny',
        'nazwa_lacinska': 'Suillus luteus',
        'status': 'jadalny',
        'opis':
            'Kapelusz brązowy, śliski, gąbka żółta. Trzon z wyraźnym pierścieniem. Skórkę kapelusza zwykle ściąga się.',
        'siedlisko': 'Lasy sosnowe',
        'sezon': 'VI–X',
        'look_alikes': 'Maślak pstry',
        'image_asset': 'assets/images/maslak.jpg',
      },
      {
        'id': 7,
        'nazwa_polska': 'Czubajka kania',
        'nazwa_lacinska': 'Macrolepiota procera',
        'status': 'jadalny',
        'opis':
            'Duży kapelusz z brązowymi łuskami na jasnym tle, wolny pierścień, trzon z wzorem wężowym. Blaszki białe.',
        'siedlisko': 'Łąki, skraje lasów, polany',
        'sezon': 'VII–X',
        'look_alikes': 'Muchomor sromotnikowy (młode), czubajka czerwieniejąca',
        'image_asset': 'assets/images/kania.jpg',
      },
      {
        'id': 8,
        'nazwa_polska': 'Goryczak żółciowy',
        'nazwa_lacinska': 'Tylopilus felleus',
        'status': 'niejadalny',
        'opis':
            'Wygląda podobnie do borowika, ale gąbka różowieje, a smak jest bardzo gorzki. Trzon z ciemną siateczką.',
        'siedlisko': 'Lasy iglaste i mieszane',
        'sezon': 'VII–X',
        'look_alikes': 'Borowik szlachetny, podgrzybek',
        'image_asset': 'assets/images/goryczak.jpg',
      },
    ];

    for (final g in samples) {
      await db.insert('grzyby', g);
    }
  }

  Future<List<Grzyb>> getAllGrzyby() async {
    final db = await instance.database;
    final result = await db.query('grzyby', orderBy: 'nazwa_polska ASC');
    return result.map((map) => Grzyb.fromMap(map)).toList();
  }

  Future<Grzyb?> getGrzybById(int id) async {
    final db = await instance.database;
    final result = await db.query(
      'grzyby',
      where: 'id = ?',
      whereArgs: [id],
    );
    if (result.isNotEmpty) {
      return Grzyb.fromMap(result.first);
    }
    return null;
  }

  Future<List<Grzyb>> searchGrzyby(String query) async {
    final db = await instance.database;
    final result = await db.query(
      'grzyby',
      where: 'nazwa_polska LIKE ? OR nazwa_lacinska LIKE ?',
      whereArgs: ['%$query%', '%$query%'],
      orderBy: 'nazwa_polska ASC',
    );
    return result.map((map) => Grzyb.fromMap(map)).toList();
  }
}
