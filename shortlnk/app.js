var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
let mysql = require("mysql");
let session = require("express-session")
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();
// set milldwares
app.use(session({
  secret:'c2hvcnRsbms' // shortlnk
}))
// DB connection
let connection = mysql.createConnection({
  host:"127.0.0.1",
  user:'root',
  database:"shortlnk",
  password:'',
})
var links = {}, Llink , Slink 
function getLinks(){
  connection.query('select * from users',function(error,results,fields) {
    Llink = results.map(row => row.Llink)
    Slink = results.map(row => row.Slink)
    for(i=0;i<(Object.keys(Slink).length);i++){
      links[Llink[i]]=Slink[i]
    }
  })
}
getLinks()
// function to generate random word 
function generateRandomWord() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let word = '';
  for (let i = 0; i < 5; i++) {
      word += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return word;
}
// forms
app.post('/',(req,res)=>{
  let body = req.body
  if(!(Object.keys(links).includes(body.Llink))){
    try {
      short = generateRandomWord()
      links[body.Llink] = short
      connection.query(`insert into links() value('${body.Llink}',${short})`)
    } catch (err) {
      short = generateRandomWord()
      links[body.Llink] = short
      connection.query(`insert into links() value('${body.Llink}',${short})`)
    }
  }
  res.session.slink = links[body.Llink]
  res.session.getSlink = true
  res.redirect('/')
})



// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
