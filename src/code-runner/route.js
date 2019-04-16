const route = require('express').Router();
const controller = require('./controller');

route.get('/', async (req, res) => {
  const { file, project } = req.query;

  try {
    const data = await controller.execute(project, file, req.decoded.username);
    res.status(200).json({ data })
  } catch (error) {
    if (!error.isOperational) throw error;
    res.status(400).json({ message: error.message })
  }
});

module.exports = route;