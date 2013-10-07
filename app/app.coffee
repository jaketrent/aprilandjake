express = require 'express'
path = require 'path'

routes = require './controllers/routes'

app = express()

app.configure ->
  app.set 'port', process.env.PORT || 3000
  app.set 'views', "#{__dirname}/views"
  app.set 'view engine', 'jade'

  app.use express.favicon()
  app.use express.methodOverride()
  app.use express.logger 'dev'

  app.use express.bodyParser()

  app.use express.static path.join __dirname, 'static'
  app.use '/static', require('./middleware/mincer').server
  app.use app.router

  app.use express.errorHandler()

routes.route app

app.listen app.get('port'), ->
  console.log "Express server listening on port #{app.get('port')}"
