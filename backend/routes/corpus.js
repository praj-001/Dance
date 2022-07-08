const express = require('express');
const router = express.Router();

const { newCorpus} = require('../controllers/corpusController');

router.route('/corpus').get(newCorpus);

module.exports = router;