const controller = require('./controller')

describe('project route', () => {
  describe('PUBLIC METHOD', () => {
    describe('readFile', () => {
      it('should return correct value', async () => {
        const data = await controller.readFile('test-read-file/c.txt')
        expect(data).toEqual('asdf')
      })

      it('should throw item is not exists', async () => {
        try {
          const data = await controller.readFile('not exist')
        } catch (error) {
          expect(error.message).toEqual('file is not existed')
        }

      })

      it('should throw item is not folder', async () => {
        try {
          const data = await controller.readFile('not exist')
        } catch (error) {
          expect(error.message).toEqual('file is not existed')
        }

      })

      it('should throw no name is passed', async () => {
        try {
          const data = await controller.readFile()
        } catch (error) {
          expect(error.message).toEqual('dir is required')
        }

      })
    })

    describe('readFolder', () => {
      it('should return correct value', async () => {
        const data = await controller.readFolder('test-read-folder')

        expect(data.rootName).toEqual('test-read-folder')
        expect(data.path).toEqual('test-read-folder')
        expect(data.files.length).toEqual(2)
        expect(data.files.length).toEqual(2)
      })

      it('should throw folder is not exists', async () => {
        try {
          const data = await controller.readFile('not exist')
        } catch (error) {
          expect(error.message).toEqual('file is not existed')
        }
      })

      it('should throw folder is file', async () => {
        try {
          const data = await controller.readFile('test-read-folder')
        } catch (error) {
          expect(error.message).toEqual('file is not existed')
        }

      })

      it('should throw no name is passed', async () => {
        try {
          const data = await controller.readFile()
        } catch (error) {
          expect(error.message).toEqual('dir is required')
        }

      })
    })
  })
})