<template>
  <div id="detail">
    <div class="row" style="padding-top:3rem;">
      <div class="col-sm detailImg">
        <img :src="img" />
      </div>
      <div class="col-sm">
        <div class="card">
          <!-- 商品名 -->
          <div class="card-header">
            {{ productName }}
          </div>
            <div class="card-body">
              <h5 class="card-title">商品詳細</h5>
              <!-- 商品説明 -->
              <p class="card-text">
                {{ description }}
              </p>
              <!-- 値段 -->
              <p class="card-text">
                ￥{{ price | money }}
              </p>
              <p class="card-text">
                <select class="quantity" v-model="quantity">
                  <option selected value="0" >0</option>
                  <option v-for="(amount, key) in 10" :key="key" :value="amount">{{ amount }}</option>
                </select>
              </p>
              <p class="card-text">
                <button class="btn btn-primary" :disabled="quantity === '0'" type="submit" @click="addItem()">
                  カートに入れる
                  <!-- ご注文 -->
                </button>
              </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductDetail',
  data () {
    return {
      itemCode: '',
      productName: '',
      title: '',
      description: '',
      price: '',
      quantity: '0',
      img: ''
    }
  },
  props: {
    // 親要素から受け取るプロパティの定義
  },
  computed: {
    // 算出プロパティ(処理結果がキャッシュされ、入力値が変更されたときのみ再計算)
  },
  created: function () {
    // 初期表示時処理
  },
  mounted: async function () {
    // クエリから商品コード受け取れない場合は検索画面へ戻る
    // 検索ワード
    if (this.$route.query.itemCode === undefined) {
      // アラート出して検索画面へ戻る
      this.$swal({
        title: 'エラー',
        icon: 'error',
        text: '商品コードが取得できません',
        type: 'error',
        confirmButtonText: 'OK'
      }).then((info) => {
        this.$router.push({ path: '/' })
      })
    }
    // クエリから商品コードを受け取ってAPIリクエストを行う
    this.itemCode = String(this.$route.query.itemCode)
    this.getDetailInfo()
  },
  methods: {
    /**
     * 商品情報取得
     */
    async getDetailInfo () {
      // API呼び出し
      // 呼び出し先エンドポイント, リクエストパラメータ
      const response = await this.axios.get(`detail/${this.itemCode}`)
      // 画面にレスポンス内容を反映する
      const data = response.data
      this.productName = data.name
      this.description = data.explanation
      this.price = data.price
      this.img = data.product_image
    },
    /**
     * カートに入れるボタン押下
     */
    addItem () {
      // storeに保存後ダイアログ表示して検索画面へ戻る
      this.$swal({
        title: '完了',
        icon: 'success',
        text: 'カートへ追加しました。',
        type: 'success',
        confirmButtonText: 'OK'
      }).then((info) => {
        this.$router.push({ path: '/' })
      })
    }
  }
}
</script>

<style scoped>
@media screen and (max-width: 300px) {
    h1 {
    color: rgb(19, 17, 17);
    position: relative;
    top: 200px;
    left: 10px;
    text-align-last: auto;
  }

  .detailImg {
    display:flex;
    width: 100%;
    max-height: 200px;
    object-fit: cover;
  }

  .card {
    text-align: left;
    top: 50px;
    right: 10%;
  }
  .card-header {
    text-align: center;
    font-size: 50px;
  }
  .card-title {
    text-align: left;
    font-size: 25px;
    margin-top: 15px;
  }
  .card-text {
    font-size: 15px;
    padding-top: 5px;
  }
  .product {
    font-size: 15px;
    text-align: center;
    margin-top: 60px;
  }
  .table {
    padding-bottom: 100px;
  }
  .cart-btn {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    width: 8em
  }
  .btn {
    padding: 10px;
    margin-right: 20px;
  }
}
.detailImg {
  display:flex;
  width: 100%;
  max-height: 800px;
  object-fit: cover;
}
.detailImg img{
  height: 100%;
  object-fit: cover;
}
.quantity {
  margin: 1%;
}
</style>
