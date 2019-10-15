const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const util = require('util');

documents = fs.readdirSync("./sources/").filter(docName => path.extname(docName) == ".svg");

documents.forEach(function (docName) {		
	fs.stat(`./sources/${docName}`, (err,sourceStats) => { 
		var fileName = path.basename(docName, ".svg");

		if (err) {
			console.log(`Error loading source of ${ fileName }`);
			console.log(err);
			return;
		}
		
		fs.stat(`${ fileName }.pdf_tex`, (err,targetStats) => {
			if (err && (err.code !== 'ENOENT')) {
				console.log(`Error loading target of ${ fileName }`);
				console.log(err);
				return; 
			}
			
			if ( (! err) && (sourceStats.mtime < targetStats.mtime)) {
				console.log(`Found cached ${ fileName }`);
				return;
			}
				
		
			console.log(`Compiling ${ fileName }`);
			execSync(`inkscape ./sources/${ fileName }.svg -D --export-pdf=${ fileName }.pdf --export-latex`, (err, stdout, stderr) => {
			  if (err) {
				// node couldn't execute the command
				return;
			  }

			  // the *entire* stdout and stderr (buffered)
			  console.log(`stdout: ${stdout}`);
			  console.log(`stderr: ${stderr}`);
			});
		});
	});
});