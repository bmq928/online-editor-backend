const controller = require('./controller')

describe('project route', () => {
  describe('PUBLIC METHOD', () => {
    describe('openProject', () => {
      it('should return correct value', async () => {
        const data = await controller.openProject('test-open')
        const expected = ['index.html', 'scripts.js', 'styles.css']
        
        data.sort()
        expected.sort()
        expect(data).toEqual(expected)
        
      })
  
      it('should throw project is not exists', async () => {
        try {
          const data = await controller.openProject('not exist')
        } catch(error) {
          expect(error.message).toEqual('project is not existed')
        }
        
      })

      it('should throw no name is passed', async () => {
        try {
          const data = await controller.openProject()
        } catch(error) {
          expect(error.message).toEqual('name is required')
        }
        
      })
    })
  })
})