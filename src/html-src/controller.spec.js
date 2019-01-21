const controller = require('./controller')

describe('html-src', () => {
  describe('public', () => {
    it('should return the right value in file', async () => {
      const val = await controller.loadFile('test-html-src', 'index.html')
      const expectVal = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Page Title</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" media="screen" href="styles.css" />
  <script src="scripts.js"></script>
</head>
<body>
  
</body>
</html>`
      expect(val).toEqual(expectVal)
    })

    it('should throw error when lack of project', async () => {
      try {
        await controller.loadFile()
      } catch (error) {
        expect(error.message).toEqual('project is required')
      }
    })

    it('should throw error when lack of file', async () => {
      try {
        await controller.loadFile('test-html-src')
      } catch (error) {
        expect(error.message).toEqual('file is required')
      }
    })

    it('should throw error when file is not found', async () => {
      try {
        await controller.loadFile('test-html-src', 'asjdlf')
      } catch(error) {
        expect(error.message).toEqual('file is not found')
      }
    })
  })
})