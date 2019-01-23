const path = require('path')
const fs = require('fs')
const util = require('util')

const readFile = util.promisify(fs.readFile)

/**
 * Check if the file is javascript or not
 * @param {String} fileName
 */
module.exports.isJs = (fileName) => {
  const ext = path.extname(fileName)
  return ext === '.js'
}

/**
 * return code js
 * @param {String} dir directory to the file
 * @returns {Object}
 */
module.exports.exec = async (dir) => {
  const code = await readFile(dir, { encoding: 'utf8' })
  const data = []
  const oldConsole = mockConsole(msg => data.push({
    line: msg,
    error: false
  }))


  try {
    eval(code)
  } catch (error) {
    // console.log(error)
    data.push({
      line: error.toString(),
      error: true
    })
  }

  restoreMockConsole(oldConsole)
  return data
}

const mockConsole = (fn) => {
  const old = {}
  for (const attr in console) {
    old[attr] = console[attr]
  }

  for (const attr in console) {
    if (attr !== 'error') console[attr] = fn
  }

  return old
}

const restoreMockConsole = (old) => {
  //restore
  for (const attr in old) {
    console[attr] = old[attr]
  }
}