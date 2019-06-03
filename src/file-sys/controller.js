const util = require('util');
const path = require('path');
const rimraf = require('rimraf');
const config = require('config');
const fs = require('fs');

const {AppError} = require('../app-error');
const PROJECT_STORAGE = process.env.PYTHON_PROJECT_STORAGE || config.get('project-storage');


const removeItem = util.promisify(rimraf);
const exists = util.promisify(fs.exists);
const createFile = util.promisify(fs.writeFile);
const mkdir = util.promisify(fs.mkdir);
const readdir = util.promisify(fs.readdir);

/**
 * @param {String} project projectName
 * @param {String} fileName fileName
 */
module.exports.deleteFile = async (project, fileName, user) => {
	if (!project) throw new AppError('project is required');
	if (!fileName) throw new AppError('file name is required');

	const filePath = path.join(PROJECT_STORAGE, user, project, fileName);
	if (!(await exists(filePath))) throw new AppError('file is not exist');

	await removeItem(filePath);

	return 'done'
};

/**
 * @param {String} project projectName
 * @param {String} file fileName or a path to file e.g /folder/nah.py
 */
module.exports.newFile = async (project, file, user) => {
	if (!project) throw new AppError('project is required');
	if (!file) throw new AppError('file name is required');

	const filePath = path.join(PROJECT_STORAGE, user, project, file);
	const parentFolder = path.dirname(filePath);


	if (!(await exists(parentFolder))) throw new AppError('parent folder is not exist');
	if (await exists(filePath)) throw new AppError('file is exist');

	await createFile(filePath, '', {encoding: 'utf8'});
	return 'done'

};

/**
 * @param {String} project projectName
 * @param {String} folderName fileName
 */
module.exports.deleteFolder = async (project, folderName, user) => {
	if (!project) throw new AppError('project is required');
	if (!folderName) throw new AppError('folder name is required');

	const folderPath = path.join(PROJECT_STORAGE, user, project, folderName);
	if (!(await exists(folderPath))) throw new AppError('file is not exist');

	await removeItem(folderPath);

	return 'done'
};

/**
 * @param {String} project projectName
 * @param {String} folder folderName or path to folder e.x: /as/d/folderName
 */
module.exports.newFolder = async (project, folder, user) => {
	if (!project) throw new AppError('project is required');
	if (!folder) throw new AppError('folder name is required');

	const folderPath = path.join(PROJECT_STORAGE, user, project, folder);
	const parentFolder = path.dirname(folderPath);

	if (!(await exists(parentFolder))) throw new AppError('parent folder is not exist');
	if (await exists(folderPath)) throw new AppError('folder is exist');

	await mkdir(folderPath);
	await createFile(folderPath + '/__init__.py', '# do not edit', {encoding: 'utf8'});
	return 'done'
};

module.exports.readFolder = async (folder, user) => {
	if (!folder) throw new AppError('folder is required');
	const folderPath = path.join(PROJECT_STORAGE, user);
	let subdirs = await readdir(folderPath);
	console.log(subdir);
	return 'done';
};

module.exports.renameFile = async (project, file, newName, user) => {
	if (!project) throw new AppError('project is required');
	if (!file) throw new AppError('file name is required');
	if (!newName) throw new AppError('new name is required');
	const filePath = path.join(PROJECT_STORAGE, user, project, file);
	const newPath = path.join(PROJECT_STORAGE, user, project, newName);
	if (!fs.existsSync(filePath)) throw new AppError('file is not exsited');
	fs.renameSync(filePath, newPath);
	return 'done';
};

module.exports.renameFolder = async (project, folder, newName, user) => {
	if (!project) throw new AppError('project is required');
	if (!folder) throw new AppError('folder name is required');
	if (!newName) throw new AppError('new name is required');
	const folderPath = path.join(PROJECT_STORAGE, user, project, folder);
	const newFolderPath = path.join(PROJECT_STORAGE, user, project, newName);
	if (!fs.existsSync(folderPath)) throw new AppError('folder is not exsited');
	fs.renameSync(folderPath, newFolderPath);
	return 'done';
};