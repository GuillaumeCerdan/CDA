var app = angular.module("dataShow", []);

app.controller("dataCtrl", function($scope, $http) {

    

    var init = function() {
        $http.get('assets/json/data.json').then(function(response) {
            console.log("response.data : " + JSON.stringify(response.data));
            $scope.data = response.data;
        });
    }

    init();
});