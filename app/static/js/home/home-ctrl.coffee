angular.module('aj.home').controller 'HomeCtrl', ($scope, $http, Youtube, Colorwheelie, GooglePlusPhotoFeed) ->

  $scope.youtube = youtube = new Youtube()
  youtube.fetch()

  $scope.colorwheelie = colorwheelie = new Colorwheelie()
  colorwheelie.fetch()

  $scope.photofeed = photofeed = new GooglePlusPhotoFeed()
  photofeed.fetch()