const Corpus = require('../models/corpus');
const spawn = require('child_process').spawn;

newCorpus = async (req, res, next) => {

    var process = spawn('python3', [__dirname + "/final.py"]);
    // var process = spawn('python3', [__dirname+"/trial.py",
    //     req.query.firstname,
    //     req.query.lastname]);

    process.stdout.on('data', function (data) {
        let transcript = data.toString().slice(55);
        let output = [];
        let i, j;
        for (i = 0, j = 0; j < transcript.length; ++j) {
            if (transcript[j] == 'S') {
                if (i != 0)
                    output.push(transcript.slice(i, j));
                i = j;
            }
        }
        output.push(transcript.slice(i));
        res.status(200).json({ output });
    })
}

module.exports = { newCorpus };