# Vue.jsの機能を活用してコードの修正をしてみよう

1. 既存コードの問題確認  
カート画面上に商品詳細画面でカートに追加した商品が表示されています。画面右側に商品の合計値が表示されていますね。  
カートに入っている商品を削除してみると動的に合計額が変更されるのを確認できると思います。  
しかし、カート画面のソースを確認すると mounted の際にもhandleDelete method 内にも合計値取得処理が記載されていています。  
これだと合計値取得処理の実行箇所がまとまっておらずさらに削除ボタンのクリックイベントごとに毎回合計値取得処理が  
実行されることになってしまいますね・・・

```javascript
    mounted: function () {
        // DOMのマウント終了後の処理
        /** 合計値取得処理 */
        this.totalPrice = this.getTotal()
    },

    methods: {
        /**
         * 削除ボタン押下
         */
        handleDelete (index) {
          // storeから該当商品を削除
          this.$store.commit('deleteItem', index)
          /** 合計値取得処理 */
          this.totalPrice = this.getTotal()
        },

        /**
         *合計値取得 
         */
        getTotal () {
          let price = 0
          this.getItemList.forEach(element => {
            price += element.price * element.quantity
          })
          return price
        }
    },
```

今まで登場したVueの機能を使えば削除ボタンのクリックイベント発火時に毎回合計値取得処理を行う必要がなくなります。  
それは一旦何でしょう？beforeMount？mounted？computedでしょうか？

2. Vueの機能を使ってソースコードの修正  

それではリファクタリングしてみましょう。今回はVueの機能であるcomputedを使用します。  
mounted と handleDelete method から合計値取得処理を削除して、getTotal method を computed内に書き換えます。

```javascript
    mounted: function () {
        // DOMのマウント終了後の処理
    },

    methods: {
        /**
         * 削除ボタン押下
         */
        handleDelete (index) {
            // storeから該当商品を削除
            this.$store.commit('deleteItem', index)
        },
    },

    computed: {
        getTotal () {
        let price = 0
        this.getItemList.forEach(element => {
            price += element.price * element.quantity
        })
        return price
        }
    },
```

dataに定義していた totalPrice も削除。templateタグ内で合計額表示している箇所を computed に定義した getTotal に書き換えます。

```html
<b-card-group>
    <b-card
    title="合計金額"
    style="max-width: 20rem;"
    >
    <b-card-text>￥{{ getTotal | money }}円</b-card-text>
    <b-button
        variant="primary"
        @click.stop="handleSubmit"
        :disabled="getItemList.length === 0"
    >
        商品を購入
    </b-button>
    </b-card>
</b-card-group>
```
3. 修正内容の確認  
ブラウザをリロードしてみて表示されている内容に問題がないか確認してみましょう。  
ソースコード上ではVueの機能を使うことでロジックがまとまり、保守の観点でも修正箇所が減って可読性も上がりました。  
画面上では修正前と同じく商品の削除ボタンが押下されたたびに合計額が動的に変化するのが確認できると思います。