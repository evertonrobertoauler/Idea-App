'use strict';

angular.module('ideaApp')
  .controller('MainCtrl', function($scope) {
    $scope.title = 'Idea App';
  })
  .controller('IdeaCtrl', function($scope, $http) {

    $http.get('/api/navbar.json').success(function(navbar) {
      $scope.navbar = navbar;
    });

    $http.get('http://127.0.0.1:5000/api/form').success(function(form) {
      $scope.form = form;
    });

    $scope.submit = function() {
      console.log(JSON.stringify($scope.form));
    };

    $scope.reset = function() {
      ($scope.form.fields || []).forEach(function(field) {
        field.value = '';
      });
    };

    $scope.validate = function() {
      $scope.form.showErrors = true;
      return $scope.form.form.$valid;
    };
  });
