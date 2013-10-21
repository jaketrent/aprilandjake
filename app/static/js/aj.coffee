#= require components/jquery/jquery

#= require_self

#= require_tree common
#= require_tree home

angular.module 'aj.vendor', ['ngRoute', 'angular-models']

angular.module 'aj', ['aj.vendor', 'aj.home']

angular.module('aj').config ($routeProvider, $locationProvider) ->

  $locationProvider.html5Mode true

  $routeProvider

    .when '/',
      controller: 'HomeCtrl'
      templateUrl: '/templates/home.html'

    .otherwise redirectTo: '/'
