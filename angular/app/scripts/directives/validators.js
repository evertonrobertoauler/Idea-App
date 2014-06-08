'use strict';

angular.module('ideaApp')
  .directive('validators', function($compile, $parse) {
    return {
      restrict: 'A',
      terminal: true,
      priority: 100000,
      link: function(scope, elem) {
        var validators = $parse(elem.attr('validators'))(scope);
        elem.removeAttr('validators');

        var angularDirectives = ['required', 'minlength', 'maxlength', 'pattern'];

        (validators || []).forEach(function(validator) {

          var directive = '' + validator.type;

          if (angularDirectives.indexOf(validator.type) !== -1) {
            directive = 'ng-' + validator.type;
          }

          elem.attr(directive, validator.condition || 'true');
        });

        $compile(elem)(scope);
      }
    };
  });
