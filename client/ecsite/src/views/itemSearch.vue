<template>
  <div>
    <div class="container-fluid" style="padding-bottom:2rem;">
      <div class="row">
        <div class="col">
          <h1 class="text-left" style="padding: 20px">商品検索画面</h1>
        </div>
      </div>

      <div class="row">
        <div id="column" class="col column04">
          <ul>
            <li
              v-for="(item, index) in itemList"
              :key="index"
              class="text-center"
            >
              <!-- 商品画像 -->
              <a href="#" @click="detailMove(item.code)">
                <img :src="item.product_image" width="80%" height="80%" />
                <!-- 商品名 -->
                <p style="font-size: 2rem">{{ item.name }}</p>
                <!-- 商品値段 -->
                <span style="font-size: 1.5rem">￥{{ item.price | money }}</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'itemSearch',
  data () {
    // テンプレート内で保有するデータ
    return {
      title: '商品検索',
      searchWord: '',
      lergeCategoryCode: '',
      mediumCategoryCode: '',
      itemList: []
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
    console.log('created')
  },
  mounted: function () {
    // DOMのマウント終了後の処理
    console.log('mounted')
  },
  updated () {
    // DOMが再レンダリングされる際に走る
    console.log('updated!')
  },
  destroyed () {
    // インスタンスが破壊される際に走る
    console.log('destroyed!')
  },
  methods: {
    // メソッド(毎回呼び出す度に処理を実行)
    /**
     * 検索処理
     */
    async search () {
      try {
        // クエリパラメータより検索条件を取得
        // 検索ワード
        if (this.$route.query.searchWord === undefined) {
          this.searchWord = ''
        } else {
          this.searchWord = String(this.$route.query.searchWord)
        }
        // 大分類
        if (this.$route.query.lergeCategoryCode === undefined) {
          this.lergeCategoryCode = ''
        } else {
          this.lergeCategoryCode = String(
            this.$route.query.lergeCategoryCode
          )
        }
        // 中分類
        if (this.$route.query.mediumCategoryCode === undefined) {
          this.mediumCategoryCode = ''
        } else {
          this.mediumCategoryCode = String(
            this.$route.query.mediumCategoryCode
          )
        }
        // API呼び出し
        const param = {
          searchWord: this.searchWord,
          lergeCategoryCode: this.lergeCategoryCode,
          mediumCategoryCode: this.mediumCategoryCode
        }
        // 呼び出し先エンドポイント, リクエストパラメータ
        const response = await this.axios.get('search/', { params: { ...param } })

        // レスポンスを画面に反映する
        this.itemList = response.data
      } catch (error) {
        console.log('error', error)
      }
    },
    detailMove (itemCode) {
      this.$router.push({ path: '/detail', query: { itemCode } })
    }
  }
}
</script>

<style scoped>
#column ul {
  width: calc(100 + 20px);
  margin: 0 -10px;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
}

#column li {
  padding: 0 10px 20px;
  list-style: none;

  border: 1px solid gray;
}

#column li a,
#column li a:visited {
  text-decoration: none;
}

#column li p {
  font-size: 90%;
  margin-bottom: 3px;
}

.column04 li {
  width: calc(25% - 20px);
  min-width: 360px; /** 最低360px */
}

a:link {
  color: #0000ff;
}
a:visited {
  color: #000080;
}
a:hover {
  color: #ff0000;
}
a:active {
  color: #ff8000;
}
</style>
