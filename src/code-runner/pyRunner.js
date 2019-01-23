const path = require('path')



/**
 * Check if the file is python or not
 * @param {String} fileName
 */
module.exports.isPython = (fileName) => {
  const ext = path.extname(fileName)
  return ext === '.py'
}


/**
 * return code python
 * @param {String} dir directory to the file
 * @returns {Object}
 */
module.exports.exec = async (dir) => {

}