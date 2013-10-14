exports.index = (req, res) ->
  res.render 'layouts/aj'

exports.partials = (req, res) ->
  res.render "templates/#{req.params[0]}"
