
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var pinterest = require('./routes/pinterest');
var cons = require('consolidate');
var http = require('http');
var swig = require('swig');
var path = require('path');

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.engine('.html', cons.swig);
  app.set('view engine', 'html');
  app.use(express.favicon(__dirname + '/static/images/favicon.png'));
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(require('less-middleware')({ src: __dirname + '/static' }));
  app.use(express.static(path.join(__dirname, 'static')));
});

swig.init({
  root: __dirname + '/views',
  cache: false, // TODO -- false for dev and true for production
  allowErrors: true
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);
app.get('/ws/pinterest', pinterest.list);

http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
