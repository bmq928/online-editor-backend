const router = require('express').Router()
const controller = require('./controller')

router.post('/save', async (req, res) => {
  const { fileName, code, project } = req.body
  try {
    await controller.save(project, fileName, code)
    res.status(200).json({message: 'done'})
  } catch (error) {
    if (!error.isOperational) throw error
    res.status(400).json({ message: error.message })
  }
})

module.exports = router