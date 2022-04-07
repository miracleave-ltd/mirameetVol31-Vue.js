const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    watchOptions: {
      poll: true
    }
  },
  devServer: {
    proxy: {
      '^/product/': {
        target: 'http://localhost:8040',
        logLevel: 'debug',
        pathRewrite: { '^/product/': '/product/' }
      }
    }
  }
})
