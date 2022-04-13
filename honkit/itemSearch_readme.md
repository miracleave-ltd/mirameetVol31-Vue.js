# アプリケーションコード修正(商品検索画面)

## 当画面に関連するソースファイル
  src\views\itemSearch.vue←修正対象

  修正する前に一度、状況を確認してみましょう。

  http://localhost:8080/

  画面としては、「商品検索画面」と表示されるのみで、商品一覧は検索されていないことがわかります。

  ![gras](img/itemSearch1.jpg)

  確認できたところで、あらためて修正をすすめていきましょう！


# created を使って画面初期表示時の処理を実装しよう。

1. Ctrl+P を押下してファイル検索を表示し、「itemSearch.vue」を開く

2. Ctrl ＋ F で検索欄を表示し、「created」内に初期表示時の処理を記述する。  
   今回は、クエリパラメータを受け取って検索処理を行う「search()」を初期表示時に実行するようにしてみます。
   以下を created に張り付けてください

変更前
```javascript
  created: function () {
    // 初期表示時処理
    console.log('created')
  },
```

変更後
```javascript
  created: function () {
    // 初期表示時処理
    console.log('created')
    this.search()
  },
```

   初期表示時にsearch()メソッドを呼び出すことによって、画面初期表示時に商品一覧の検索処理が行われるようになりました！
   
  ![gras](img/itemSearch2.jpg)

  大分類、中分類を選択したり、検索ワードを入れて検索ボタンを押下すると、絞り込まれたリストが表示されます。

  # created の処理についておさらい

  createdは画面初期表示時に走る処理です。正確に言うとインスタンスが生成され､データが初期化された後に実行されます。

  初期表示時のデータ初期化後に実施したい処理がある場合はこの中に処理をかいていくことで実現することができます。

  今回の場合は画面が初期表示される際に検索処理を行いたかったため、searchメソッドを呼び出すように変更しました。

  # mountedとの違い

  createdとmountedは共に画面初期表示時に走る処理です。では何が違うのでしょうか。
  
  mountedは、インスタンスが DOM 要素にマウントされた後に実行される処理です。

  getElementById等を使ってDOM要素にアクセスをしたい場合は、mountedに書くことが望ましいです。

  createdの時にgetElementById('hoge')でDOMの要素を取得しようとしても取得することはできません。

  mountedが実行されるタイミングではDOMの作成が完了しているのでDOMの要素が取得できるため
  
  getElementByIdだけではなくDOMに対してアクセスを行う「jQuery」もmounted時点で使用可能となります。

