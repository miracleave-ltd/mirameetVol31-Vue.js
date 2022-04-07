import Vue from 'vue'

Vue.filter('money', function (value) {
  return value.toLocaleString()
})
