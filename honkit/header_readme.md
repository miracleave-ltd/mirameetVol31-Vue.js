# アプリケーションコード修正(ヘッダー)

## 当画面に関連するソースファイル
  src\components\Header.vue←修正対象

  修正する前に一度、状況を確認してみましょう。

  http://localhost:8080/

  「大分類」から、何か選択した状態で「中分類」のリストをクリックしてみてください。

  ![gras](img/mediumCategory1.jpg)

  フィルタリング処理が実装されておらず、大分類を変更しても中分類リストの選択肢一覧に変更がないことが分かったかと思います。

  確認できたところで、あらためて修正をすすめていきましょう！


# computed を使ってフィルタリング処理を実装しよう。

1. Ctrl+P を押下してファイル検索を表示し、「Header.vue」を開く

2. Ctrl ＋ F で検索欄を表示し、「filterdMediumCategory」内にフィルタリング処理を記述する。  
   中分類リストの選択肢内容を、大分類の選択値に基づいて動的にフィルタリング処理をかけてみましょう。
   以下を filterdMediumCategory に張り付けてください

```javascript
  filterdMediumCategory: function () {
      if (this.lergeCategoryCode === '') {
        return this.mediumCategoryList
      }
      return this.mediumCategoryList.filter((row) => {
        return row.parentCode === this.lergeCategoryCode
      })
    }
```

3. 先ほど修正した filterdMediumCategory によってヘッダーの中分類選択肢リストが、大分類リストの選択値によって、フィルタリングがかかるようになりました。

  ![gras](img/mediumCategory2.jpg)

  業務において、今回のようにデータに何かしらの処理を加えてから表示させたい。という場面があると思います。

  そんな時に使えるのがcomputedプロパティです。

  computedは一度計算後、同じ処理が呼び出された際も以前計算時にキャッシュされたデータを即時返すだけなので何度も同じ処理を行いません。
  
  キャッシュが削除され再度計算されるのは、依存するデータの値が更新されたときだけです。

  (今回でいうと大分類が選択し直されるタイミングで再計算されます)
  
  methodsは結果をキャッシュしないので、一度計算を行った場合でも、呼び出されるたびに再計算が行われます。
