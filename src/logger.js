const { createLogger, format, transports } = require('winston')
const { combine, timestamp, prettyPrint, colorize, json } = format
const config = require('config')
const path = require('path')
const appRootPath = require('app-root-path')
const LOG_FOLDER = path.join(appRootPath.toString(), process.env.PYTHON_LOG_PATH || config.get('logPath'))

const logger = createLogger({
  format: combine(
    timestamp(),
    prettyPrint(),
    colorize(),
    json()
  ),
  transports: [
    new transports.Console({
      level: 'debug',
      handleExceptions: true
    })
  ]
})

if (process.env.NODE_ENV === 'production') {
  logger.add(new transports.File({
    level: 'info',
    filename: path.join(LOG_FOLDER, 'activities.log')
  }))

  logger.add(new transports.File({
    level: 'error',
    filename: path.join(LOG_FOLDER, 'errors.log')
  }))
}

if (process.env.NODE_ENV === 'development') {
  logger.error = console.error
  logger.info = console.info
}

module.exports = logger