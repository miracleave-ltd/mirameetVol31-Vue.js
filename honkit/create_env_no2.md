# 環境構築 その2 Vue アプリケーションをDocker環境で準備

続いてVueアプリケーションの準備に移ります。  

![gras](img/環境構築.png)

Vueの環境構築はecsiteディレクトリ直下をvscodeで開くように注意してください。vscodeが正常に動作しないことがあります。  
以下がecsiteディレクトリになります。
```
mirameetVol31.-main/client/ecsite  
```

1. Dockerコンテナに入ってnpm installを実行  
Vueプロジェクトに必要なパッケージをインストールするためにまずは下記のコマンドでDockerコンテナに入ります。
```
$ docker-compose exec client sh
```
Dockerコンテナ内に入ったらnpmを使ってパッケージをインストールします。
```
/usr/src # npm install
```
npmでvue/cliをインストールします。
```
/usr/src # npm install -g @vue/cli
```

2. Vueアプリケーションサーバーをたてる  
npmでパッケージインストールが完了したら引き続きDocker内で  
以下コマンドでVueアプリケーションを立てましょう。ビルドには少々時間がかかります。
```
/usr/src # npm run serve
```

3. ブラウザから起動確認をしましょう。
2 の実装が完了したら以下のURLでブラウザ上から起動の確認を行ってください。  
url: http://localhost:8080