var amISafeHere = angular.module('CS499Hack3', []);
var url = 'http://127.0.0.1:8804';
amISafeHere.controller('Hack3Ctrl', function ($scope, $http) {
    $scope.TrainMe = function () {
        $http.get(url + "/train" + "?input=" + $('#input').val().replace(' ', '') + "&output=" + $('#output').val().replace(' ', ''))
            .then(function successCallback(response) {
                $scope.trainMessage = response.data;
            }, function errorCallback(response) {
                $scope.trainMessage = response.data;
            });
    };

    $scope.PredictMe = function () {
        $http.get(url + "/predict" + "?data=" + $('#input').val().replace(' ', ''))
            .then(function successCallback(response) {
                $scope.predictMessage = response.data;
            }, function errorCallback(response) {
                $scope.predictMessage = response.data;
            });
    };
});