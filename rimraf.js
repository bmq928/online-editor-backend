const config = require('config')
const rimraf = require('rimraf')

const LOG_FOLDER = config.get('logPath')
const PROJECT_STORAGE = config.get('project-storage')


if(process.env.NODE_ENV !== 'production') {
  rimraf.sync(`${LOG_FOLDER}/*`)
}
rimraf.sync(`${PROJECT_STORAGE}/*`)