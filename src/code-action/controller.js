const config = require('config')
const path = require('path')
const fs = require('fs')
const util = require('util')

const { AppError } = require('../app-error')
const PROJECT_STORAGE = config.get('project-storage')

const exists = util.promisify(fs.exists)
const writeFile = util.promisify(fs.writeFile)

/**
 * @param {String} project
 * @param {String} fileName
 * @param {String} code
 * @returns {Object}
 */
module.exports.save = async (project, fileName, code) => {
  if(!project) throw new AppError('project is required')
  if(!fileName) throw new AppError('fileName is required')
  
  const filePath = path.join(PROJECT_STORAGE, project, fileName)
  if(!(await exists(filePath))) throw new AppError('file is not exist')

  await writeFile(filePath, code)

}