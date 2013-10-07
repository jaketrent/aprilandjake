index = require './index'

exports.route = (app) ->

  app.get '/', index.index
  app.get '/templates/*.html', index.partials
