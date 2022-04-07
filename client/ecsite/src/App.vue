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
    // HelloWorld,
    Header
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
.appView{
  padding-right: 10rem;
  padding-left: 10rem;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
