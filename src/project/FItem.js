
/**
 * File or Foler
 */
module.exports = class FItem {
  constructor(options) {

    if(!options.rootName) throw new AppError('rootName is required', false)

    this.rootName = options.rootName
    this.path = options.path || '/'+options.rootName
    this.rootIsFile = !!(options.rootIsFile)
    this.files = options.files || []
    this.folders = options.folders || []
  }
}