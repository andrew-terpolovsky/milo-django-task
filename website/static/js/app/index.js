(function () {
    'use strict';

    angular
        .module('milo', [
            'ngResource'
        ])
        .config(configApp)
        .factory('UserModel', UserModel)
        .controller('ManageUserCtrl', ManageUserCtrl);

    configApp.$inject = ['$interpolateProvider', '$httpProvider', '$resourceProvider'];
    UserModel.$inject = ['$resource'];
    ManageUserCtrl.$inject = ['$scope', 'UserModel'];

    function configApp($interpolateProvider, $httpProvider, $resourceProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = "XMLHttpRequest";
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $interpolateProvider.startSymbol("{[");
        $interpolateProvider.endSymbol("]}");
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }

    function UserModel($resource) {
        return $resource('user/:id/', {id: '@id'});
    }

    function ManageUserCtrl($scope, UserModel) {
        $scope.manageUser = function (model) {
            $scope.model = model ? model : new UserModel();
            $("#userDialog").modal("show");
        };

        $scope.save = function () {
            $scope.model.$save().then(function (data) {
                window.location.reload();
            }, function(error) {
                $scope.model.errors = error.data;

            });
        }
    }
})();

