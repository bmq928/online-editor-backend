const express = require('express')
const helmet = require('helmet')
const cors = require('cors')

const app = express()

const project = require('./project')

app.use(cors())
app.use(helmet())
if (process.env.NODE_ENV === 'production') {
  app.use(morgan('combined', { stream: fs.createWriteStream(REQUEST_LOG) }))
}

//api
app.use('/project', project.route)


module.exports = app