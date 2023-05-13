# Flutter環境構築

下記のサイトよりFlutterのSDKをダウンロード
DLサイト : https://docs.flutter.dev/get-started/install

C:/srcディレクトリを作成し、展開したファイルをC:/src/に配置する

環境変数の設定
    新規→新しいユーザー変数→
    変数名：FLUTTER_PATH
    変数値：C:\src\flutter

    Pathを選択→編集→新規→
    「%FLUTTER_PATH%\bin」を入力→OK

再起動してから、コマンドプロンプトで「flutter」、「flutter doctor」を入力
結果が表示されればOK!
