const path = require('path')
const execa = require('execa')



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
  try {
    const resp = await execa.shell(`python3 ${dir}`)
    return resp.stdout
      .split('\n')
      .filter(line => !!line)
      .map(line => ({ error: false, line }))


  } catch (error) {
    const ERR_MARKER = 'NameError'
    const idxAppError = error.stderr.lastIndexOf(ERR_MARKER)
    const errorMsg = error.stderr.slice(idxAppError + ERR_MARKER.length + 1)

    const succLines = error.stdout
      .split('\n')
      .filter(line => !!line)
      .map(line => ({ error: false, line }))
    const errLine = {
      line: errorMsg,
      error: true
    }

    return [...succLines, errLine]
  }
}