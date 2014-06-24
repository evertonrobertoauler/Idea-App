'use strict';

angular
  .module('ideaApp', [
    'ngRoute', 'ngLocale', 'Idea', 'ui.select2'
  ])
  .config(function($provide, $routeProvider, $httpProvider) {

    $httpProvider.defaults.withCredentials = true;

    $provide.factory('$routeProvider', function() {
      return $routeProvider;
    });
  });
