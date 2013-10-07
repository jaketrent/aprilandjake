Mincer = require 'mincer'
nib = require 'nib'

Mincer.StylusEngine.registerConfigurator (style) ->
  style.use nib()

environment = new Mincer.Environment()

for path in ['css', 'js', 'templates']
  fullPath = "#{__dirname}/../static/#{path}"
  environment.appendPath fullPath

exports.server = Mincer.createServer environment
