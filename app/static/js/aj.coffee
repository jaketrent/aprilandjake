#= require components/jquery/jquery
#= require components/angular/angular
#= require components/angular-route/angular-route
#= require components/angular-models/dist/angular-models

#= require_self

#= require_tree common
#= require_tree home

angular.module 'aj.vendor', ['ngRoute']

angular.module 'aj', ['aj.vendor', 'aj.home']

angular.module('aj').config ($routeProvider, $locationProvider) ->

  $locationProvider.html5Mode true

  $routeProvider

    .when '/',
      controller: 'HomeCtrl'
      templateUrl: '/templates/home.html'

    .otherwise redirectTo: '/'
