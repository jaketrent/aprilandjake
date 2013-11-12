angular.module('aj.home').factory 'GooglePlusPhotoFeed', (Model) ->

  class GooglePlusPhotoFeed extends Model

    url: 'https://www.googleapis.com/plus/v1/people/115032056022257436849/activities/public?maxResults=10&key=AIzaSyCNZ96JDofdI_c4BRpxGg8mlifPuROsKCU&callback=JSON_CALLBACK'

    max: 43

    deserialize: (data) ->
      photos = []
      albums = _.uniq(_.filter(data.items, (item) ->
        # only album posts
        # && only albums I post
        item.object.attachments[0].objectType is 'album' and item.actor.id is '115032056022257436849';
      ), (item) ->
        # de-dup albums
        item.object.attachments[0].url
      )

      for album in albums
        photos.push album.object.attachments[0].thumbnails

      @set 'photos', _.flatten(photos, true).slice 0, @max