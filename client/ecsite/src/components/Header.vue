<template>
<header>
<!-- ヘッダー -->
  <div class="headerClass">
    <!-- ロゴ表示エリア -->
    <div class="header-logo-area">
      <a hlef="#" v-on:click="moveHome()">
        <img class="header-logo-icon" src="..//assets//mira_logo.png" alt="header_logo" />
      </a>
    </div>
    <!-- 検索エリア -->
    <div class="header-searchbar-area">
      <div class="form-group  d-flex">
        <select class="form-select selecteBox1" aria-label="Default select example" v-model="lergeCategoryCode">
          <option value="" selected>大分類</option>
          <option v-for="(item,index) in lergeCategoryList" :key="index" :value="item.code">{{item.text}}</option>
        </select>
        <!-- 選択肢ボックス2 computedにする -->
        <select class="form-select selecteBox2" aria-label="Default select example" v-model="mediumCategoryCode">
          <option value="" selected>中分類</option>
          <!-- ハンズオン -->
          <option v-for="(item,index) in filterdMediumCategory" :key="index" :value="item.code">{{item.text}}</option>
        </select>
        <!-- 入力欄 -->
        <input class="form-control input-lg header-input" type="search" style="min-width: 300px;" v-model="searchWord"  placeholder="検索条件を入力" aria-label="Search">
        <!-- 検索ボタン -->
        <button class="btn btn-outline-success btn-light" @click="search()">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg>
        </button>
      </div>
    </div>
    <!-- カートボタン -->
    <div class="header-cart-area">
      <button class="btn btn-outline-success btn-light" @click="cart()">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart" viewBox="0 0 16 16">
          <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
        </svg>
      </button>
    </div>
  </div>
</header>

</template>

<script>
export default {
  name: 'HeaderComponent',
  data () {
    // テンプレート内で保有するデータ
    return {
      searchWord: '',
      lergeCategoryList: [],
      mediumCategoryList: [],
      lergeCategoryCode: '',
      mediumCategoryCode: ''
    }
  },
  props: {
    // 親要素から受け取るプロパティの定義
  },
  computed: {
    // 算出プロパティ(処理結果がキャッシュされ、入力値が変更されたときのみ再計算)
    filterdMediumCategory: function () {
      return this.mediumCategoryList
    }
  },
  mounted: function () {
    // 選択肢ボックスの中身を設定
    this.lergeCategoryList = [
      { code: '01', text: '周辺機器' },
      { code: '02', text: 'オフィス用品' },
      { code: '03', text: '家電' }
    ]
    this.mediumCategoryList = [
      { code: '01', text: 'ノートパソコン', parentCode: '01' },
      { code: '02', text: 'デスクトップパソコン', parentCode: '01' },
      { code: '03', text: 'ディスプレイ', parentCode: '01' },
      { code: '04', text: 'ノート', parentCode: '02' },
      { code: '05', text: '手帳', parentCode: '02' },
      { code: '06', text: '筆記用具', parentCode: '02' },
      { code: '07', text: '電子レンジ', parentCode: '03' },
      { code: '08', text: '冷蔵庫', parentCode: '03' },
      { code: '09', text: 'エアコン', parentCode: '03' }

    ]
  },
  methods: {
    // メソッド(毎回呼び出す度に処理を実行)
    /**
     * ロゴアイコンクリック時ホームへ飛ばす
     */
    moveHome () {
      this.$router.push({ path: '/' })
      this.$router.go(0)
    },
    cart () {
      this.$router.push({ path: '/cart' })
    },
    /**
     * 検索ボタンを押下
     */
    async search () {
      try {
        // itemSearchへ遷移
        this.$router.push({ path: '/', query: { searchWord: this.searchWord, lergeCategoryCode: this.lergeCategoryCode, mediumCategoryCode: this.mediumCategoryCode } })
        this.$router.go(0)
      } catch (error) {
      }
    }
  }
}
</script>

<style scoped>
a{
  cursor: pointer;
}
.headerClass {
  height:64px;
  width:100%;
  display:flex;
  /* justify-content: space-between; */
  color: white;
  background-color: white;
}
.header-logo-area{
  display:flex;
}
.header-logo-icon{
  width:100%;
  height:100%;
}

.header-searchbar-area{
  width:60%;
  height: 100%;
  padding-top: 1rem;
}

.header-cart-area{
  height: 100%;
  padding-top: 1rem;
  padding-right: 2rem;
  margin: 0 0 0 auto;
}

.header-input{
  width:100%;
  padding-left:1rem;
}
.selecteBox1{
  width:12rem;
}
.selecteBox2{
  width:14rem;
}
</style>
