import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    itemList: [],
    productName: '',
    quanitiy: 1
  },
  getters: {
    getItemList (state) {
      return state.itemList
    }
  },
  mutations: {
    // 商品削除
    deleteItem (state, item) {
      // 引数で渡された行を削除
      state.itemList.splice(item, 1)
    },
    // 商品リスト初期化
    clearItem (state) {
      state.itemList = []
    }
  },
  actions: {
  },
  modules: {
  },
  plugins: [createPersistedState()]
})
