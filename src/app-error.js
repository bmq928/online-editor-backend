const logger = require('./logger')
/**
 * For handling error
 * 
 * @param {isOperational} Boolean show this error should send to client or not
 */
class AppError extends Error {
  constructor(msg, isOperational = true, reason='') {
    super(msg)
    this.isOperational = isOperational
    if(reason) this.reason = reason
  }
}

/**
 * For handling centrally error which is throwed from program
 * 
 * @param {AppError} error 
 */
const errorHandler = (error) => {
  logger.error(error)
}

module.exports = {
  AppError,
  errorHandler
}