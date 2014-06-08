'use strict';

(function(angular) {

  var idea = angular.module('Idea', []);

  idea.factory('ideaResources', ['$http', '$route',
    function($http, $route) {
      return function($routeProvider, resourcesUrl) {

        $http.get(resourcesUrl).success(function(resources) {

          resources.routes.forEach(function(route) {
            $routeProvider.when(route.path, route.config);
          });

          $routeProvider.otherwise({
            redirectTo: resources.defaultPath,
          });

          $route.reload();
        });
      };
    }
  ]);
})(window.angular);
