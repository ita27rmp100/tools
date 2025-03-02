var express = require('express');
let mysql = require("mysql");
var router = express.Router();
const session = require('express-session');

// DB connection
let connection = mysql.createConnection({
  host:"127.0.0.1",
  user:'root',
  database:"shortlnk",
  password:'',
})
var links={},Llink=[],Slink=[]
function getLinks(){
  connection.query('select * from links',function(error,results,fields) {
    Llink = results.map(row => row.Llink)
    Slink = results.map(row => row.Slink)
    for(i=0;i<(Object.keys(Slink).length);i++){
      links[Llink[i]]=Slink[i]
    }
  })
}

/* GET home page. */
router.get('/:lnk?', function(req, res, next) {
  let slink = ''
  if(req.session.getSlink){
    slink = req.session.slink
  }
  req.session.goLink = true
  if(req.session.goLink){
    slink = req.params.lnk
    for (let i = 0; i < Slink.length; i++) {
      if(links[Llink[i]]==slink){
        res.redirect(links[Llink[i]])
      }
    }
    if (i==Slink.length) {
      res.send("This short link doesn't exist")
    }
  }
  res.render('index');
});

module.exports = router;
