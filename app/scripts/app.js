'use strict';

angular
  .module('ideaApp', [
    'ngRoute', 'ngLocale', 'Idea', 'ui.select2', 'mgcrea.ngStrap'
  ])
  .config(function($provide, $routeProvider) {
    $provide.factory('$routeProvider', function() {
      return $routeProvider;
    });
  })
  .run(function($routeProvider, ideaResources) {
    ideaResources($routeProvider, '/api/resources.json');
  });
