const config = require('config')
const mongoose = require('mongoose')

const logger = require('../logger')
const User = require('./User')

module.exports.models = {
  User
}

module.exports.connect = () => {
  const uri = config.get('dbUri')

  mongoose.connect(uri, {useNewUrlParser: true})

  mongoose.connection.on("connected", function () {
    logger.info('database connect success')
  })

  mongoose.connection.on("disconnected", function () {
    logger.info('database is disconnected')
  })

  mongoose.connection.on("error", function (err) {
    throw err
  })
}