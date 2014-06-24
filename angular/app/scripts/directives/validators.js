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
  })
  .directive('match', function($parse) {

    var link = function(scope, elem, attrs, ctrl) {

      if (!ctrl || !attrs.match) {
        return;
      }

      for (var i in scope.form.fields) {
        if (scope.form.fields[i].name === attrs.match) {
          attrs.match = 'form.fields[' + i + '].value';
        }
      }

      var field = $parse(attrs.match);

      var validator = function(value) {
        var temp = field(scope);
        var v = value === temp;
        ctrl.$setValidity('match', v);
        return value;
      };

      ctrl.$parsers.unshift(validator);
      ctrl.$formatters.push(validator);
      scope.$watch(attrs.match, function() {
        validator(ctrl.$viewValue);
      });
    };

    return {
      link: link,
      restrict: 'A',
      require: '?ngModel'
    };
  });
