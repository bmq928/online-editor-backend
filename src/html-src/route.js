const route = require('express').Router()
const controller = require('./controller')

route.get('/load', async (req, res) => {
  const {project, file} = req.query

  try {
    const data = await controller.loadFile(project, file)
    res.status(200).json({data})
  } catch (error) {
    if (!error.isOperational) throw error
    res.status(400).json({ message: error.message })
  }
})

module.exports = route