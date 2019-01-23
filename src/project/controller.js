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
const stat = util.promisify(fs.stat)
const FItem = require('./FItem')
const { AppError } = require('../app-error')

const PROJECT_STORAGE = config.get('project-storage')




/**
 * read file 
 * @param {String} dir
 * 
 * @returns {String}
 */
module.exports.readFile = async (dir) => {
  if (!dir) throw new AppError('dir is required')

  try {
    const filePath = path.join(PROJECT_STORAGE, dir)
    // if (!(await exists(filePath))) throw new AppError('file is not existed')

    const data = await readFile(filePath, { encoding: 'utf8' })

    return data
  } catch (error) {
    throw new AppError('file is not existed')
  }

}


/**
 * explore inside item of a folder
 * @param {String} dir
 * @returns {FItem}
 */
module.exports.readFolder = async (dir) => {
  if (!dir) throw new AppError('dir is required')

  try {
    const folderPath = path.join(PROJECT_STORAGE, dir)

    const insideItems = await readdir(folderPath)
    const insideItemsWithStat = await Promise.all(
      insideItems.map(async (i) => {
        const itemPath = path.join(folderPath, i)
        const rootIsFile = (await stat(itemPath)).isFile()
        // const parrentName = path.basename(folderPath)
        const relativePath = path.join(dir, i)

        return {
          itemPath: relativePath,
          rootIsFile
        }
      })
    )

    const insideFiles = insideItemsWithStat
      .filter(i => i.rootIsFile)
      .map(i => new FItem({
        rootName: path.basename(i.itemPath),
        path: i.itemPath,
        rootIsFile: true
      }))

    const insideFolders = insideItemsWithStat
      .filter(i => !i.rootIsFile)
      .map(i => new FItem({
        rootName: path.basename(i.itemPath),
        path: i.itemPath,
        rootIsFile: false
      }))

    return new FItem({
      rootName: path.basename(folderPath),
      path: dir,
      rootIsFile: false,
      files: insideFiles,
      folders: insideFolders
    })

  } catch (error) {
    throw new AppError('folder is not existed')
  }

}


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

  // const projectPath = path.join(PROJECT_STORAGE, name)

  try {
    const items = await module.exports.readFolder(name)
    return items
  } catch (error) {
    throw new AppError('project is not existed')
  }

}

/**
 * get the list of project storage in PROJECT_STORAGE
 * @returns {FItem[]} array of class FItem
 */
module.exports.listProject = async () => {
  const projectNames = await readdir(PROJECT_STORAGE)
  const projects = projectNames.map(
    name => new FItem({
      rootName: name,
      rootIsFile: false
    })
  )
  return projects
}