const route = require('express').Router()
const controller = require('./controller')

route.get('/new', async (req, res) => {
  const { name } = req.query

  try {
    const data = await controller.newProject(name)
    res.status(200).json({ data })
  } catch (error) {

    if (!error.isOperational) throw error
    res.status(400).json({ message: error.message })
    
  }
})


module.exports = route