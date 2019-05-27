const WebSocket = require('ws');
const logger = require('./logger');
module.exports = wsServer;

function wsServer(express, port) {
	express._activeSockets = {};
	let wss = new WebSocket.Server({
		server: express.listen(port, () => {
			logger.info("Websocket server listening on port ", port);
		})
	});
	wss.on('connection', ws => {
		logger.info("New client ws connection");
		ws.on('message', msg => {
			try {
				let msgObj = JSON.parse(msg);
				switch (msgObj.type) {
					case 'connect':
						let id = msgObj.wiId;
						express._activeSockets[id] = ws;
						ws._wiId = msgObj.wiId;
						logger.info('added new socket connection to activeSockets');
						break;
					default :
						logger.info('mesage type is not mapped');
						break;
				}
			} catch (e) {
				logger.error(e);
			}
		});
		ws.on('close', (code, reason) => {
			logger.info('close', code, reason);
			let wiId = ws._wiId;
			if (wiId) {
				delete express._activeSockets[wiId];
			}
		});
	});
	// express.sendSoketMsg = send;
	//
	// function send(wiId, content) {
	// 	let ws = express._activeSockets[wiId];
	// 	ws && ws.send(typeof content === 'object' ? JSON.stringify(content) : content);
	// }
}