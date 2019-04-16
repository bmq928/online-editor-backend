const http = require('http');
const config = require('config');

const PORT = config.get('port');
const app = require('./server');
const server = http.createServer(app);
// const db = require('./_db')
const { errorHandler } = require('./app-error');
const logger = require('./logger');

// db.connect()

// global.logger = logger
// global.AppError = AppError


process.on('unhandledRejection', (reason, p) => {
  throw reason
});
process.on('uncaughtException', (error) => {
  // I just received an error that was never handled, time to handle it and then decide whether a restart is needed
  errorHandler(error);
  console.log(error);
  if (!error.isOperational) throw error
  
});


server.listen(PORT, () => logger.info('app is starting on port ' + PORT));