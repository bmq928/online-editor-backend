class AppError extends Error {
  constructor(msg, isOperational = true) {
    super(msg)
    this.isOperational = isOperational
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