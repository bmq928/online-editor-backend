const fs = require('fs')
const util = require('util')
const path = require('path')
const config = require('config')
const { ncp } = require('ncp')

const mkdir = util.promisify(fs.mkdir)
const exists = util.promisify(fs.exists)
const copyFolder = util.promisify(ncp)
const readdir = util.promisify(fs.readdir)
const readFile = util.promisify(fs.readFile)

const PROJECT_STORAGE = config.get('project-storage')

/**
 * create new project
 * @param {String} name name of the project
 */
module.exports.newProject = async (name) => {
  if (!name) throw new AppError('name is required')

  const projectPath = path.join(PROJECT_STORAGE, name)
  const templatePath = path.join(__dirname, 'templates')

  if (await exists(projectPath)) throw new AppError('project is existed')

  await mkdir(projectPath)
  await copyFolder(templatePath, projectPath) // write template to new project

  return 'done'
}


/**
 * open project
 * @param {String} name name of the project
 * @returns {Array} list item in project
 */
module.exports.openProject = async (name) => {
  if (!name) throw new AppError('name is required')

  const projectPath = path.join(PROJECT_STORAGE, name)

  try {
    const items = await readdir(projectPath)
    console.log(items)
    return items
  } catch (error) {
    throw new AppError('project is not existed')
  }

}


/**
 * read file 
 * @param {String} dir
 * 
 * r@returns {String}
 */
module.exports.readFile = async (dir) => {
  if(!dir) throw new AppError('dir is required')
  
  const filePath = path.join(PROJECT_STORAGE, dir)
  if(!(await exists(filePath))) throw new AppError('file is not existed')
  
  const data = readFile(filePath, {encoding: 'utf8'})
  
  return data

}