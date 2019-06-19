const path = require('path')
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
module.exports.exec = async (dir, socket, key, cwd) => {
	let opts = {
		cwd: cwd
	};
	let pid = null;
	if (socket) {
		let pythonProcess = exec('unbuffer', ['python', dir], {stdio: ['pipe', 'pipe', 'pipe'], ...opts});
		pid = pythonProcess.pid;
		const rl = readline.createInterface({
			input: pythonProcess.stdout,
			prompt: "output> ",
			crlfDelay: 10000
		});
		rl.on('line', function (line) {
			socket.send(JSON.stringify({
				pid: pythonProcess.pid,
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
				pid: pythonProcess.pid,
				content: line.toString(),
				error: true
			}));
		});
		pythonProcess.on('exit', code => {
			let msg = "+-----------------------------------------------------------|*END*|-----------------------------------------------------------+";
			socket.send(JSON.stringify({
				key: key,
				content: msg.toString(),
				error: false
			}));
		});
	}
	return socket ? {wiId: socket._wiId, pid: pid} : "No socket connection"
};