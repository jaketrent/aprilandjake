angular.module('aj.home').factory 'Youtube', (Model) ->

  class Youtube extends Model

    url: 'http://gdata.youtube.com/feeds/api/playlists/PLbWbiOD0YMByR_l4GCzD7V3_d54HF9fZ9?v=2&alt=jsonc&orderby=reversedPosition&max-results=10&callback=JSON_CALLBACK'

    deserialize: (data) ->
      @set 'videos', data.data.items