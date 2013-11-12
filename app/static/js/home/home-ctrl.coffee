angular.module('aj.home').controller 'HomeCtrl', ($scope, $http, Youtube, Colorwheelie) ->

  $scope.youtube = youtube = new Youtube()
  youtube.fetch()

  $scope.colorwheelie = colorwheelie = new Colorwheelie()
  colorwheelie.fetch()



#  $http.jsonp('http://gdata.youtube.com/feeds/api/playlists/PLbWbiOD0YMByR_l4GCzD7V3_d54HF9fZ9?v=2&alt=jsonc&orderby=reversedPosition&max-results=10&callback=JSON_CALLBACK')
#    .success((data, status, headers, config) ->
#      console.log data.data.items
#      $scope.videos = data.data.items
#    ).error((data, status, headers, config) ->
#      console.log('ERROR')
#      console.log(data)
#  )