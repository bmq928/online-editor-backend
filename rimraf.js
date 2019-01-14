const config = require('config')
const LOG_FOLDER = config.get('logPath')
const rimraf = require('rimraf')

if(process.env.NODE_ENV !== 'production') {
  rimraf.sync(`${LOG_FOLDER}/*`)
}