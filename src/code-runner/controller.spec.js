const controller = require('./controller')

describe('code runner route', () => {
  it('should throw error when wrong parameter', async () => {
    await expect(controller.execute())
    .rejects
    .toThrow('project is required')

    await expect(controller.execute('asdf'))
    .rejects
    .toThrow('file is required')

    await expect(controller.execute('asdf', 'adsf'))
    .rejects
    .toThrow('file is not exist')

    await expect(controller.execute('test-code-runner', 'test.txt'))
    .rejects
    .toThrow('type is not supported')
  })

  it('js file should return right', async () => {
    const data = await controller.execute('test-code-runner', 'test.js')
    expect(data).toEqual([{
      line: 'nah',
      error:false
    },{
      line: 'nah',
      error:false
    },{
      line: 'nah',
      error:false
    },{
      line: 'ReferenceError: asdfalsdkjf is not defined',
      error: true
    }])
  })

  it('python file should return right', async () => {
    
  })
})