'use strict';

(function(angular) {

  var idea = angular.module('Idea', []);
  var url = '';

  idea
    .factory('$idea', function($http, $route, $injector) {
      return function($routeProvider, $scope, baseUrl) {

        url = baseUrl;

        return {
          getResources: function() {
            $http.get(url + 'resources/').success(function(resources) {
              resources.routes.forEach(function(route) {

                var resource = $injector.get(route.resource.service);

                resource.apply(null, route.resource.params);

                var config = {
                  templateUrl: '/views/view.html',
                  controller: 'ViewCtrl',
                  resolve: {
                    $ideaResource: resource.apply(null, route.resource.params),
                  },
                };

                $routeProvider.when(route.path, config);
              });

              $routeProvider.otherwise({
                redirectTo: resources.defaultPath,
              });

              $route.reload();
            });
          },
          getNavbar: function() {
            $http.get(url + 'navbar/').success(function(navbar) {
              $scope.navbar = navbar;
            });
          },
        };

      };
    })
    .factory('$ideaForm', function($q, $http, $location, $window) {
      return function(path) {
        return function() {
          var defer = $q.defer();

          $http.get(url + path).success(function(form) {

            form.reset = function() {
              (form.fields || []).forEach(function(field) {
                field.value = '';
              });
            };

            form.validate = function() {
              form.showErrors = true;
              return form.form.$valid;
            };

            form.save = function() {

              var data = {};

              (form.fields || []).forEach(function(field) {
                data[field.name] = field.value;
              });

              $http({
                method: form.submit.method,
                url: url + form.submit.path,
                data: data
              }).success(function(data) {
                if (data.resources) {
                  $window.location = data.path;
                } else {
                  $location.path(data.path);
                }
              }).error(function(data) {
                form.errors = data.errors;
              });
            };

            defer.resolve({
              form: form
            });
          });

          return defer.promise;
        };
      };
    })
    .factory('$ideaLogout', function($http, $window) {
      return function() {
        return function() {
          return {
            init: function() {
              $http({
                method: 'POST',
                url: url + 'logout/',
                data: {}
              }).success(function() {
                $window.location = '/';
              });
            },
          };
        };
      };
    });

})(window.angular);
