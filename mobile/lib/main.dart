// UI source placeholder only. Generate a Flutter project before integrating.
import 'package:flutter/material.dart';
void main() => runApp(const KrishiDhwaniApp());
class KrishiDhwaniApp extends StatelessWidget {
  const KrishiDhwaniApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
    title: 'KrishiDhwani',
    theme: ThemeData(colorSchemeSeed: Colors.green, useMaterial3: true),
    home: Scaffold(
      appBar: AppBar(title: const Text('KrishiDhwani')),
      body: const Center(child: Text('Prototype scaffold • No live node data')),
    ),
  );
}
