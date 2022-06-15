# local 環境の CleanUp

今回のハンズオンで使用した開発環境の削除を行います。

![gras](img/環境削除.png)

## コンテナの停止  
新しくターミナルを開き、以下コマンドで Docker コンテナを停止します。

```
docker-compose down
```

コンテナが停止しているか確認します。以下のコマンドを使用します。

```
docker-compose ps
```
以下の状態になれば、コンテナが停止しています。
```
Name   Command   State   Ports
  ------------------------------
```

## イメージの削除
以下コマンドを使用して、IMAGE IDを確認します。

```
docker images
```
```
REPOSITORY                                                                   TAG                                                     IMAGE ID
  CREATED         SIZE
mirameetvol29_server                                                         latest                                                  ba2bac2d2844
  4 days ago      197MB
mirameetvol29_client                                                         latest                                                  05b82c10dc6e
  6 days ago      111MB
```

上記で確認できた IMAGE ID を利用して、ビルドされたイメージを削除します。

```
docker rmi -f [IMAGE ID]
```

次のようなメッセージが確認できたら、イメージが正常に削除出来ています。

```
Untagged: meetup_web...
```

## フォルダの削除  
最後にフォルダを削除します。

以上で本日のハンズオンは終了となります。皆様お疲れ様でした！
