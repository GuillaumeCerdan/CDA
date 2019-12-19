

$(document).ready(function() {

    var array = [];

    var list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    var i = 0;

    $.each(list, function(index_list1) {

        array.push(list[index_list1]);

        while(i != 100000) {
            while(i != 10000) {
                while(i != 1000) {
                    while(i != 100) {
                        
                        i++;
                    }
                    i++;
                }
                i++;
            }
            i++;
        }

    });

    console.log(array);

});
