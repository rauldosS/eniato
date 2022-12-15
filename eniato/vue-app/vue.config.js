const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')

const PORT = 8080

module.exports = {

  publicPath: `http://127.0.0.1:${PORT}`,
  outputDir: '../static_src/webpack_bundles/',

  chainWebpack: config => {
    config.optimization
      .splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: '../vue-app/webpack-stats.json' }])

    config.resolve.alias
      .set('__STATIC__', 'static')

    config.devServer
      .host('127.0.0.1')
      .port(PORT)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ 'Access-Control-Allow-Origin': ['*'] })
      .disableHostCheck(true)
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@account': path.join(__dirname, 'src/apps/account'),
        '@category': path.join(__dirname, 'src/apps/category'),
        '@transaction': path.join(__dirname, 'src/apps/transaction'),
        '@helpers': path.join(__dirname, 'src/lib/helpers'),
        '@eniato-ui': path.join(__dirname, 'src/lib/components/UI'),
        '@eniato-icons': path.join(__dirname, 'src/lib/icons')
      }
    }
  },
  assetsDir: undefined,
  runtimeCompiler: true,
  productionSourceMap: undefined,
  parallel: undefined,
  css: undefined
}
