# コード修正(カート) 回答編  

## 修正対象のソース
* **src/views/Cart.vue**

答え合わせです！  
正解は**computed**になります！
早速、**computed**を使ってコード修正を行ってみましょう！

## ソースコードの修正 
mounted と handleDelete から合計値取得処理を削除して、getTotal method を computed内に書き換えます。  

* 修正後  
mounted  
this.totalPrice = this.getTotal()を削除
```javascript
    mounted: function () {
        // DOMのマウント終了後の処理
    },
```
methods  
getTotal()メソッドを削除。
```javascript
    getPrice (price, quantity) {
      return Number(price * quantity)
    },
    /**
     * 削除ボタン押下
     */
    handleDelete (index) {
      // storeから該当商品を削除
      this.$store.commit('deleteItem', index)
      /** 合計値取得処理 */
      this.totalPrice = this.getTotal()
    },
```
computed  
getTotal()処理を追加
```javascript
    computed: {
        getItemList () {
          return this.$store.getters.getItemList
        },
        getTotal () {
        　　let price = 0
        　　this.getItemList.forEach(element => {
            　　price += element.price * element.quantity
        　　})
        　　return price
        }
    },
```

templateタグ内で合計額表示している箇所の「totalPrice」を  
computed に定義した 「getTotal」 に書き換えます。

* 修正前

```html
<b-card-group>
    <b-card
    title="合計金額"
    style="max-width: 20rem;"
    >
    <b-card-text>￥{{ totalPrice | money }}円</b-card-text>
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

* 修正後

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
## 修正内容の確認  
ブラウザをリロードしてみて表示されている内容に問題がないか確認してみましょう。  
機能としては、修正前と同じく、商品をカートから削除した際に合計額が再計算されます。  
![gras](img/cart_handson_1.jpg)  
![gras](img/cart_handson_2.jpg)  
<br/>
ソースコード上では色々な場所から同じ処理を呼び出す事がなくなり、保守の観点でも修正箇所が減って可読性も上がりました。  
このように、プログラムの外部から見た動作を変えずにソースコードの内部構造を整理することを**リファクタリング**と言います。  
実務においてもリファクタリングを行う場面は多々あると思います。ぜひ覚えておいてください！  
