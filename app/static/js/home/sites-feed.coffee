angular.module('aj.home').factory 'SitesFeed', (Model) ->

  class SitesFeed extends Model

    url: 'http://aprilandjake-data.herokuapp.com/sites?callback=JSON_CALLBACK'

    deserialize: (data) ->
      @set 'sites', data.sites