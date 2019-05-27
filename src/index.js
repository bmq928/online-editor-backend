const http = require('http');
const config = require('config');

const PORT = process.env.PYTHON_PORT || config.get('port');
const app = require('./server');

const {errorHandler} = require('./app-error');


process.on('unhandledRejection', (reason, p) => {
	throw reason
});
process.on('uncaughtException', (error) => {
	// I just received an error that was never handled, time to handle it and then decide whether a restart is needed
	errorHandler(error);
	console.log(error);
	if (!error.isOperational) throw error

});

// server.listen(PORT, () => logger.info('app is starting on port ' + PORT));
const wsServer = require('./ws-server');
let server = new wsServer(http.createServer(app), PORT);