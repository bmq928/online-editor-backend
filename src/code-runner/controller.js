const path = require('path');
const config = require('config');
const fs = require('fs');
const util = require('util');
const jsRunner = require('./jsRunner');
const pyRunner = require('./pyRunner');
const {AppError} = require('../app-error');

const PROJECT_STORAGE = process.env.PYTHON_PROJECT_STORAGE ||config.get('project-storage');

const exists = util.promisify(fs.exists);

/**
 * execute the file and return
 * @param {String} project name of the project
 * @param {String} fileName name or relative path to the project
 * @returns {Object}
 */
module.exports.execute = async (project, fileName, user) => {
  if (!project) throw new AppError('project is required');
  if (!fileName) throw new AppError('file is required');

  const filePath = path.join(PROJECT_STORAGE, user, project, fileName);
  if(!(await exists(filePath))) throw new AppError('file is not exist');

  if(jsRunner.isJs(fileName)) return await jsRunner.exec(filePath);
  if(pyRunner.isPython(fileName)) return await pyRunner.exec(filePath);

  throw new AppError('type is not supported')
};