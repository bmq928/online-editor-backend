const fs = require('fs')
const util = require('util')
const path = require('path')
const config = require('config')

const mkdir = util.promisify(fs.mkdir)
const exists = util.promisify(fs.exists)

const PROJECT_STORAGE = config.get('project-storage')


module.exports.newProject = async (name) => {
  if(!name) throw new AppError('name is required')

  const projectPath = path.join(PROJECT_STORAGE, name)
  if(await exists(projectPath)) throw new AppError('project is existen')

  await mkdir(projectPath)

  return 'done'
}