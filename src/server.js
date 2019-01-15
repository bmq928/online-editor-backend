const express = require('express')
const helmet = require('helmet')
const cors = require('cors')
const morgan = require('morgan')
const fs = require('fs')
const config = require('config')
const appRootPath = require('app-root-path')
const path = require('path')

const app = express()

const project = require('./project')
const REQUEST_LOG = path.join(appRootPath.toString(), config.get('logPath'), 'request.log')

app.use(cors())
app.use(helmet())
if (process.env.NODE_ENV === 'production') {
  app.use(morgan('combined', { stream: fs.createWriteStream(REQUEST_LOG) }))
}

//api
app.use('/project', project.route)


module.exports = app