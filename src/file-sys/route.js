const route = require('express').Router();
const controller = require('./controller');


route.get('/remove-file', async (req, res) => {
	const {project, file} = req.query;
	try {
		const data = await controller.deleteFile(project, file, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});


route.get('/remove-folder', async (req, res) => {
	const {project, folder} = req.query;
	try {
		const data = await controller.deleteFolder(project, folder, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/new-file', async (req, res) => {
	const {project, file} = req.query;
	try {
		const data = await controller.newFile(project, file, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/new-folder', async (req, res) => {
	const {project, folder} = req.query;
	try {
		const data = await controller.newFolder(project, folder, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

module.exports = route;