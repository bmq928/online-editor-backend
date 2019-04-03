const fs = require('fs')
const util = require('util')
const path = require('path')
const config = require('config')
const { ncp } = require('ncp')
const _ = require('lodash')
const rimraf = require('rimraf')

const mkdir = util.promisify(fs.mkdir)
const exists = util.promisify(fs.exists)
const copyFolder = util.promisify(ncp)
const readdir = util.promisify(fs.readdir)
const readFile = util.promisify(fs.readFile)
const stat = util.promisify(fs.stat)
const FItem = require('./FItem')
const { AppError } = require('../app-error')
const { models } = require('../_db')
const rm = util.promisify(rimraf)

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
 * @param {String} projectName name of the project
 * @param {String} username owner of project
 */
module.exports.newProject = async (projectName, username) => {
  if (!projectName) throw new AppError('projectName is required')

  const projectPath = path.join(PROJECT_STORAGE, projectName)
  const templatePath = path.join(__dirname, 'templates')

  if (await exists(projectPath)) throw new AppError('project is existed')

  await mkdir(projectPath)
  await copyFolder(templatePath, projectPath) // write template to new project

  const user = await models.User
    .findOne({ username })
    .select('listProject')
    .exec()

  
  if(!user.listProject.includes(projectName)){
    user.listProject.push(projectName)
    await user.save()
  }
  
  return 'done'
}

/**
 * remove project
 * @param {String} name name of the project
 */
module.exports.deleteProject = async (name) => {
  if (!name) throw new AppError('name is required')

  const projectPath = path.join(PROJECT_STORAGE, name)


  if (!(await exists(projectPath))) throw new AppError('project isn\'t existed')
  await rm(projectPath)


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
 * @param {String} user 
 * @returns {FItem[]} array of class FItem
 */
module.exports.listProject = async (user) => {
  if (!user) throw new AppError('user is required')

  const { listProject: allowProjForUser } = await models.User
    .findOne({ username: user })
    .select('listProject')
    .exec()

  const projectNames = await readdir(PROJECT_STORAGE)
  const projects = projectNames
    .filter(proj => allowProjForUser.includes(proj))
    .map(name => new FItem({
      rootName: name,
      rootIsFile: false
    }))


  return projects
}