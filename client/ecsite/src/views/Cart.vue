<template>
    <div>
      <b-row>
        <b-col cols="10">
          <b-card-group
            deck
            v-for="(item,index) in getItemList"
            :key="index"
          >
            <b-container
              class="bv-example-row"
            >
              <b-row>
                <b-col
                  cols="8"
                >
                  <b-card
                    :img-src="item.imageUrl"
                    img-alt="Card image"
                    img-left class="mb-3"
                  >
                  <!-- 商品名 -->
                    <b-card-text>
                      {{ item.name }}
                    </b-card-text>
                    <b-card-text>
                      {{ item.description }}
                    </b-card-text>
                  </b-card>
                </b-col>
                <b-col>
                  <b-card
                    title="価格"
                  >
                  <!-- 個数 -->
                    <b-card-text>個数 {{ item.quantity}}</b-card-text>
                    <!-- 価格 -->
                    <b-card-text>￥{{ getPrice(item.price,item.quantity) | money }}</b-card-text>
                    <b-button
                     variant="primary"
                     @click.stop="handleDelete(item.index)"
                    >削除</b-button>
                  </b-card>
                </b-col>
              </b-row>
            </b-container>
          </b-card-group>
        </b-col>
        <b-col>
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
        </b-col>
      </b-row>
    </div>
</template>

<script>
export default {
  name: 'CartList',
  data () {
    return {
    }
  },
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
  created: function () {
    // 初期表示時処理
  },
  mounted: function () {
    // DOMのマウント終了後の処理
  },
  methods: {
    getPrice (price, quantity) {
      return Number(price * quantity)
    },
    /**
     * 削除ボタン押下
     */
    handleDelete (index) {
      // storeから該当商品を削除
      this.$store.commit('deleteItem', index)
    },
    /**
     * 購入ボタン押下
     */
    handleSubmit () {
      this.$swal({
        title: 'よろしいですか?',
        text: 'よろしければOKボタンを押してください',
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'OK'
      }).then((result) => {
        if (result.value) {
          // ダイアログを出して検索画面へ戻る
          this.$swal({
            title: '完了',
            icon: 'success',
            text: '購入処理が完了しました。',
            type: 'success',
            confirmButtonText: 'OK'
          }).then((info) => {
            this.clearItems()
            this.$router.push({ path: '/' })
          })
        }
      }).error((result) => {
        this.$swal(
          'エラーが発生しました。',
          '購入に失敗しました。',
          'error'
        )
      })
    },
    /**
     * 購入時商品リスト初期化
     */
    clearItems () {
      this.$store.commit('clearItem')
    }
  }
}
</script>
