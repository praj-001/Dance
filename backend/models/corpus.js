const mongoose = require("mongoose");
let Schema = mongoose.Schema;

let corpusSchema = new Schema({
    meetId: {
        type: String,
        required: true,
    },
    corpus: {
        type: String,
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

mongoose.models = {};

let Corpus = mongoose.model("Corpus", corpusSchema);

module.exports = Corpus;