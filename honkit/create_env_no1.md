# 環境構築 その１ Django APIサーバーをDocker環境で準備

はじめに今回のハンズオンの環境構築を行いたいと思います。  
まずは、Vueの環境を立てる前にサーバーサイドとして使用する  
Djangoフレームワークを用いてAPIサーバーを準備します。

![gras](img/環境構築.png)

1. githubリポジトリにアクセス  
以下リンクよりデモアプリのあるGithubリポジトリにアクセスします。  
URL:https://github.com/miracleave-ltd/mirameetVol29
![gras](img/github_toppage.png)
2. ソースコードダウンロード  
Codeボタンより、Zipファイルをダウンロードします。
![gras](img/github_zip.png)

3. ソースコード展開  
ダウンロードしたZipファイルを任意のフォルダに展開してください。  
※次の手順を進めるに当たり、展開されたフォルダをVSCodeで開くようお願いします。  
![gras](img/open_in_vscode.png)

4. サーバーの起動  
一度ローカルでサーバーを立ち上げましょう。  
  4-1. Dockerのbuildと起動の確認  
  コマンドをVSCodeのターミナル上から実施し、Dockerの起動を行います。  
  以下イメージのように Creating <Dockerコンテナ名> ... done と表示されると成功  

  ```
  $ docker-compose up -d --build
  ```
  dockerが起動しているか以下のコマンドで確認してみましょう。
  ```
  $ docker-compose ps
                Name                            Command               State           Ports
  --------------------------------------------------------------------------------------------------
  mirameet_vol30_20220314_client_1   docker-entrypoint.sh node        Up      0.0.0.0:8080->8080/tcp
  mirameet_vol30_20220314_server_1   python manage.py runserver ...   Up      0.0.0.0:8040->8000/tcp
  ```
  state が Up となっていれば問題ありません。  
  4-2. スーパーユーザーの作成  
  以下コマンドを実施し、管理サイトにて使用するユーザー情報を作成します。
  ```
  docker-compose run web python manage.py createsuperuser
  ```

  設定する値はそれぞれ以下の通りです。
  - ユーザー名：admin
  - メールアドレス：未設定（そのままEnter）
  - パスワード：任意の値（単純すぎるものは警告が出ます）  
上記までの手順で、ブラウザに以下URLを入力することで画面を参照することが出来ます。  

