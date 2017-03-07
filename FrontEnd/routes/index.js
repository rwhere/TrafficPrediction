var express = require('express');
var router = express.Router();
var mainRoot = require('../rootDir');

router.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

/* GET home page. */
router.get('/', function(req, res, next) {
    res.sendFile('TrainMe.html', {root : mainRoot.MAIN_ROOT + mainRoot.PATH_SEPARATOR + 'public' + mainRoot.PATH_SEPARATOR});
});

module.exports = router;



