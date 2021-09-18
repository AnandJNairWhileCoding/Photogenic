import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:social_media/Screens/main_screen.dart';
import 'package:social_media/Screens/sub-screens/login-screen.dart';
import 'package:social_media/Screens/sub-screens/splash-screen.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:social_media/services/google_auth.dart';


void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.light(),
      debugShowCheckedModeBanner: false,
      title: 'Photogenic',
      home: SplashScreen()
    );
  }
}

