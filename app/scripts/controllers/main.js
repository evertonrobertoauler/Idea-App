'use strict';

angular.module('ideaApp')
  .controller('MainCtrl', function($scope) {
    $scope.title = 'Idea App';
  })
  .controller('IdeaCtrl', function($scope, $http) {
    $http.get('/api/view.json').success(function(view) {

      $scope.navbar = view.navbar;
      $scope.form = view.form;

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
  });
