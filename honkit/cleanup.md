# local環境のCleanUp

今回のハンズオンで使用した開発環境の削除を行います。

![gras](img/環境削除.png)

1. コンテナの停止  
以下コマンドでDockerコンテナを停止します。
```
$ docker-compose down
```
コンテナが停止しているか確認します。
```
$ docker-compose ps
Name   Command   State   Ports
  ------------------------------
```

2. イメージの削除
```
$ docker images                                                                                                                                   
REPOSITORY                                                                   TAG                                                     IMAGE ID     
  CREATED         SIZE
mirameetvol29_server                                                         latest                                                  ba2bac2d2844 
  4 days ago      197MB
mirameetvol29_client                                                         latest                                                  05b82c10dc6e 
  6 days ago      111MB
```
上記で確認できたIMAGE IDを利用して、ビルドされたイメージを削除します。
```
docker rmi -f [IMAGE ID]
```
次のようなメッセージが確認できたら、イメージが正常に削除出来ています。
```
Untagged: meetup_web...
```

3. フォルダの削除  
最後にフォルダを削除します。  

3.1. Macの場合  
```
# 一つ上の階層に移動
cd ../
# xxxxxxxxxxxフォルダが存在しているかを確認
ls
# xxxxxxxxxxxフォルダが存在している場合、下記コマンドを実行しフォルダを削除
rm -rf xxxxxxxxx
```

3.2. Windowsの場合  
```
# 一つ上の階層に移動
cd ../
# xxxxxxxxxxxフォルダが存在しているかを確認
dir
# xxxxxxxxxxxフォルダが存在している場合、下記コマンドを実行しフォルダを削除
rd /s /q xxxxxxxxxx
# PowerShellをご使用の方はこちらのコマンドをご使用下さい
Remove-Item xxxxxxxxxx -Recurse -Force
```

以上で本日のハンズオンは終了となります。皆様お疲れ様でした！