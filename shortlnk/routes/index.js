var express = require('express');
let mysql = require("mysql");
var router = express.Router();
const session = require('express-session');
const { link } = require('fs');

// DB connection
let connection = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  database: "shortlnk",
  password: ""
});

var Llink = [], Slink = [];

// Load links from DB and map Slink to Llink
function getLinks() {
  connection.query('select * from links', function(error, results, fields) {
    if (error) {
      console.error("Error fetching links:", error);
      return;
    }
    Llink = results.map(row => row.Llink);
    Slink = results.map(row => row.Slink);
  });
}
getLinks();

/* GET home page. */
router.get('/:lnk?', function(req, res, next) {
  // Ignore favicon requests
  if (req.params.lnk === 'favicon.ico') {
    return res.status(204).end();
  }
  
  console.log(Llink, Slink);
  
  if (req.params.lnk !== undefined) {
    let i = Slink.indexOf(req.params.lnk);
    if(i==-1){
      res.status(404).send("THIS SHORT LINK DOESN'T EXIT IN OUR SYSTEM")
    }
    else{
      res.redirect(Llink[i])
    }
  } else {
    let slink = '', sessionLlink = '';
    try {
      slink = req.session.slink;
      sessionLlink = req.session.Llink;
    } catch (error) {
      slink = '';
    }
    res.render('index', { slink: slink, llink: sessionLlink });
  }
});

module.exports = router;
