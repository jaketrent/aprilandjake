angular.module('aj.home').factory 'Colorwheelie', (Model) ->

  class Colorwheelie extends Model

    url: 'http://api.tumblr.com/v2/blog/colorwheelie.tumblr.com/posts/photo?api_key=BPbVt1ghZEsf4wIm9lf5wxXQPawks8YkbmrE4tWZZUanYKuuj5&limit=10&callback=JSON_CALLBACK'

    deserialize: (data) ->
      @set 'wheelies', data.response.posts