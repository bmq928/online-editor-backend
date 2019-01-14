const express = require('express')
const helmet = require('helmet')
const cors = require('cors')

const app = express()

app.use(cors())
app.use(helmet())

module.exports = app