var app = angular.module("dataShow", []);

app.controller("dataCtrl", function($scope, $http) {

    

    var init = function() {
        $http.get('assets/json/data.json').then(function(response) {
            angular.forEach(response.data, function(value, key) {
                value.labels = value.labels.split(', ');
            });
            $scope.data = response.data;
        });
        
    }

    init();
});