index = require './index'

exports.route = (app) ->

  app.get '/', index.home
