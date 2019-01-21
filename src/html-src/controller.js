const config = require('config')
const fs = require('fs')
const util = require('util')
const path = require('path')

const readFile = util.promisify(fs.readFile)

const PROJECT_STORAGE = config.get('project-storage')


/**
 * server content that html require such as <script> or <link>
 * @param {String} project
 * @param {String} file
 * @returns {String}
 */
module.exports.loadFile = async (project, file) => {
  if (!project) throw new AppError('project is required')
  if (!file) throw new AppError('file is required')

  try {
    const filePath = path.join(PROJECT_STORAGE,project, file)
    const data = await readFile(filePath, { encoding: 'utf8' })

    return data
  } catch (error) {
    throw new AppError('file is not found')
  }
}