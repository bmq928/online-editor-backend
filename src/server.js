const express = require('express')
const helmet = require('helmet')
const cors = require('cors')
const morgan = require('morgan')
const fs = require('fs')
const config = require('config')
const appRootPath = require('app-root-path')
const path = require('path')

const app = express()
const REQUEST_LOG = path.join(appRootPath.toString(), config.get('logPath'), 'request.log')
const PROJECT_STORAGE = config.get('project-storage')

const project = require('./project')
const htmlSrc = require('./html-src')
const codeRunner = require('./code-runner')


app.use(cors())
app.use(helmet({
  frameguard: {
    action: 'allow-from',
    domain: config.get('clientDomain')
  }
}))
app.use(express.static(PROJECT_STORAGE))
if (process.env.NODE_ENV === 'production') {
  app.use(morgan('combined', { stream: fs.createWriteStream(REQUEST_LOG) }))
}

//api
app.use('/project', project.route)
app.use('/html-src', htmlSrc.route)
app.use('/code-runner', codeRunner.route)

module.exports = app