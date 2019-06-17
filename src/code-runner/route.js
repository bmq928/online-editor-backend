const route = require('express').Router();
const controller = require('./controller');
const exec = require('child_process').exec;

route.get('/', async (req, res) => {
	// console.log(req.connection.server._activeSockets);
	// console.log(req.connection.server.sendSocketMsg(wiId, content));
	const {file, project, wiId, key} = req.query;

	try {
		const data = await controller.execute(project, file, req.decoded.username, req.connection.server._activeSockets[wiId], key);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});
route.get('/teminate', async (req, res) => {
	const {pid} = req.query;
	const command = 'kill -9 ' + pid;
	try {
		exec(command);
		res.status(200).json('Killed ' + pid);
	} catch (e) {
		res.status(200).json(e);
	}
});

// route.post('/', async (req, res) => {
// 	// console.log(req.connection.server._activeSockets);
// 	// console.log(req.connection.server.sendSocketMsg(wiId, content));
// 	const {file, project, wiId} = req.body;
// 	let socket = req.connection.server._activeSockets[wiId];
// 	try {
// 		const data = await controller.execute(project, file, req.decoded.username, socket);
// 		res.status(200).json({data})
// 	} catch (error) {
// 		if (!error.isOperational) throw error;
// 		res.status(400).json({message: error.message})
// 	}
// });

module.exports = route;