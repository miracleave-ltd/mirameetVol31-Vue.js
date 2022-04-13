# アプリケーションコード修正
## ライフサイクルを使って初期描画処理を実装しよう。  
### カート画面上の現在固定値で表示している合計額を「合計値取得 method」と  
### ライフサイクルの「mounted」を使ってカート内の合計値を動的に取得してみましょう。  

1. データオブジェクトとして「totalPrice」を定義  
合計値を表示するためにまずはデータオブジェクトとして「totalPrice」を定義しましょう。  
定義時点ではまだカート内の合計値を取得することはできないので初期値として0を値としておきます。
```javascript
  data () {
    return {
      totalPrice: 0
    }
  }
```

2. methods に合計値を取得するメソッドを定義する。  
カート内のアイテムとして定義してある「items」の「price」を合計してその値を返すメソッドを定義しましょう。  
今回はjavascriptのfor文で「items」を回して「price」の合計値を返すようにしました。
```javascript
  methods: {
    getTotalPrice: function () {
      let total = 0
      for (const key in this.items) {
        const val = this.items[key]
        total += val.price
      }
      return total
    },
  }
```

3. ライフサイクルの「mounted」で合計値をセットする。  
先ほど定義した getTotalPrice メソッドを用いてデータオブジェクトの  
「totalPrice」に合計額を反映しましょう。
```javascript
  mounted () {
    this.totalPrice = this.getTotalPrice()
  }
```
