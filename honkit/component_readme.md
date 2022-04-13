# アプリケーションコード修正(コンポーネント)

## 当画面に関連するソースファイル
  src\App.vue←修正対象

  src\components\Header.vue

  src\router\index.js

  修正する前に一度、状況を確認してみましょう。

  http://localhost:8080/

  画面としては何もない状態であることがわかったかと思います。

  ![gras](img/component1.jpg)

  確認できたところで、あらためて修正をすすめていきましょう！

  


# ヘッダーをインポートして画面に配置しよう。

src\App.vue にヘッダー用のコンポーネントをインポートし、

画面上に配置します。

1. Ctrl+P を押下してファイル検索を表示し、「App.vue」を開く

2. ソースを以下のように修正してください。

修正前

```javascript
<template>
  <div id="app">
    <router-view class="appView"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>
```

修正後

```javascript
<template>
  <div id="app">
    <Header />
    <router-view class="appView"/>
  </div>
</template>

<script>
// Header.vueをインポート
import Header from './components/Header'
// components にHeader追加する
export default {
  name: 'App',
  components: {
    Header
  }
}
</script>
```

1. 画面上部にヘッダーが実装できました。

  ![gras](img/component2.jpg)

  vueファイルは主に
  
  ・templateタグ：html要素を記述する
  
  ・scriptタグ：javascriptの処理を記述する
  
  ・styleタグ：cssを記述する
  
  の三つのタグからなります。
  
  これらを合わせて一つのコンポーネントとして作成し、
  
  それら組み合わせて1つのページを作るのがVue.jsの大枠の考え方です。

  コンポーネントを呼び出すにはまずscriptタグ内で呼び出すコンポーネントのvueファイルをインポートし、components要素内に使用するコンポーネント名を記載します。
  
  その後templateタグ内で、呼び出すコンポーネント名をそのままタグとして記載してあげれば、その場所に子コンポーネントが挿入されます。



  # ルーティングの説明

  app.vueの以下の部分(Vue Router)

```javascript
  <div id="app">
    <router-view class="appView"/>
  </div>
```

 Vue Routerとは、 Vue.jsを利用したSPA構築で、ルーティング制御をするための公式プラグインです
 
 src\router\index.js内に、アプリケーションのルーティングを記述しています。

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import itemSearch from '../views/itemSearch.vue'
import Cart from '../views/Cart.vue'
import DetailView from '../views/detailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: itemSearch
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart
  },
  {
    path: '/detail',
    name: 'detail',
    component: DetailView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```
 pathに書かれたURLにアクセスすると、componentに設定されたページ内容を
 
 「router-view」のエリアで表示します。

 ```javascript
<template>
  <div id="app">
    <Header />
    <router-view class="appView"/>
  </div>
</template>

```

今回の場合は上記記述によって、ヘッダーは常に共通のものが表示、URLが変更されると

「router-view」の内容がそのURLに設定されたページを表示してくれます。

