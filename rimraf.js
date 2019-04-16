const config = require('config');
const rimraf = require('rimraf');

const LOG_FOLDER = process.env.PYTHON_LOG_PATH || config.get('logPath');
const PROJECT_STORAGE = process.env.PYTHON_PROJECT_STORAGE || config.get('project-storage');


if(process.env.NODE_ENV !== 'production') {
  rimraf.sync(`${LOG_FOLDER}/*`)
}
rimraf.sync(`${PROJECT_STORAGE}/*`);