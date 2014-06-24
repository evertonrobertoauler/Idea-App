'use strict';

angular.module('ideaApp')
  .controller('MainCtrl', function($scope, $http, $routeProvider, $idea) {
    $scope.title = 'Clicker';
    $scope.url = 'http://127.0.0.1:5000/api/';

    var resource = $idea($routeProvider, $scope, $scope.url);

    $scope.getResources = resource.getResources;

    $scope.getNavbar = resource.getNavbar;

    $scope.getResources();
    $scope.getNavbar();
  })
  .controller('ViewCtrl', function($scope, $http, $location, $ideaResource) {

    $scope.resource = $ideaResource;

    if ($ideaResource.init) {
      $ideaResource.init();
    }
  });
