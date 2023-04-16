import 'dart:core';

//ChatGPTより...
//以下は、Dartを使用して、シンプルなゲームのコード例です。
//このプログラムは、ターミナル上で動作し、ランダムに生成された数字を予測するゲームです。


import 'dart:io';
import 'dart:math';

void main() {

  final random = Random();
  final answer = random.nextInt(100) + 1;
  var guess;
  var count = 0;

  print('Welcome to the Guessing Game!');
  print('I am thinking of a number between 1 and 100.');

  do {
    stdout.write('Enter your guess (1-100): ');
    guess = int.tryParse(stdin.readLineSync()!);
    if (guess == null) {
      print('Invalid input. Please enter a number between 1 and 100.');
    } else if (guess < 1 || guess > 100) {
      print('Invalid input. Please enter a number between 1 and 100.');
    } else if (guess < answer) {
      print('Too low! Try again.');
      count++;
    } else if (guess > answer) {
      print('Too high! Try again.');
      count++;
    }
  } while (guess != answer);

  count++;
  print('Congratulations! You guessed the number in $count tries!');
}
