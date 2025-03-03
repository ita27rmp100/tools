var express = require('express');
let mysql = require("mysql");
var router = express.Router();
const session = require('express-session');

// DB connection
let connection = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  database: "shortlnk",
  password: ""
});

var links = {}; // mapping: short link -> long link

// Load links from DB and map Slink to Llink
function getLinks(callback) {
  connection.query('SELECT * FROM links', function (error, results) {
    if (error) return callback(error);
    results.forEach(row => {
      links[row.Slink] = row.Llink;
    });
    callback(null);
  });
}

// Preload links (ensure error handling as needed)
getLinks(function(err) {
  if (err) console.error("Error loading links:", err);
});

/* GET home page. */
router.get('/:lnk?', function(req, res, next) {
  // Use the provided parameter as the short link
  let slink = req.params.lnk;
  req.session.goLink = true;

  if (slink !== undefined) {
    // If the mapping exists, redirect; otherwise show an error message.
    if (links[slink]) {
      return res.redirect(links[slink]);
    } else {
      return res.send("This short link doesn't exist");
    }
  } else {
    let slink = ''
    try {
      slink = req.session.slink
    } catch (error) {
      slink = ''
    }
    res.render('index', { slink: slink });
  }
});

module.exports = router;
