const fs = require('fs')
const util = require('util')
const path = require('path')
const config = require('config')
const {ncp} = require('ncp')

const mkdir = util.promisify(fs.mkdir)
const exists = util.promisify(fs.exists)
const copyFolder = util.promisify(ncp)

const PROJECT_STORAGE = config.get('project-storage')

/**
 * create new project
 * @param {String} name name of the project
 */
module.exports.newProject = async (name) => {
  if (!name) throw new AppError('name is required')

  const projectPath = path.join(PROJECT_STORAGE, name)
  const templatePath = path.join(__dirname, 'templates')
  
  if (await exists(projectPath)) throw new AppError('project is existen')

  await mkdir(projectPath)
  await copyFolder(templatePath, projectPath) // write template to new project

  return 'done'
}