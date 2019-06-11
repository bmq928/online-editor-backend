const path = require('path')
const execa = require('execa')
const exec = require('child_process').spawn;
const readline = require('readline');

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
module.exports.exec = async (dir, socket, key) => {
	// console.log(socket);
	let opts = {};
	if (socket) {
		let pythonProcess = exec('unbuffer', ['python', dir], {stdio: ['pipe', 'pipe', 'pipe'], ...opts})
		const rl = readline.createInterface({
			input: pythonProcess.stdout,
			prompt: "output> ",
			crlfDelay: 10000
		});
		rl.on('line', function (line) {
			socket.send(JSON.stringify({
				key: key,
				content: line.toString()
			}));
		});
		const rlerror = readline.createInterface({
			input: pythonProcess.stderr,
			prompt: "output> ",
			crlfDelay: 10000
		});
		rlerror.on('line', line => {
			socket.send(JSON.stringify({
				key: key,
				content: line.toString(),
				error: true
			}));
		});
		/*
		pythonProcess.stdout.on('data', data => {
			socket.send(JSON.stringify({
				key: key,
				content: data.toString()
			}));
		});
		pythonProcess.stderr.on('data', data => {
			socket.send(JSON.stringify({
				key: key,
				content: data.toString(),
				error: true
			}));
		});
		*/
		pythonProcess.on('exit', code => {
			let msg;
			msg =  "+--------------------------------------------------------+";
			msg += "|                           END                          |";
			msg += "+--------------------------------------------------------+";
			socket.send(JSON.stringify({
				key: key,
				content: msg.toString(),
				error: false
			}));
		});
	}
	return socket ? socket._wiId : "No socket connection"
	// try {
	// 	const resp = await execa.shell(`python3 ${dir}`)
	// 	return resp.stdout
	// 		.split('\n')
	// 		.filter(line => !!line)
	// 		.map(line => ({error: false, line}))
	//
	//
	// } catch (error) {
	// 	const ERR_MARKER = 'NameError'
	// 	const idxAppError = error.stderr.lastIndexOf(ERR_MARKER)
	// 	const errorMsg = error.stderr.slice(idxAppError + ERR_MARKER.length + 1)
	//
	// 	const succLines = error.stdout
	// 		.split('\n')
	// 		.filter(line => !!line)
	// 		.map(line => ({error: false, line}))
	// 	const errLine = {
	// 		line: errorMsg,
	// 		error: true
	// 	}
	//
	// 	return [...succLines, errLine]
	// }
};