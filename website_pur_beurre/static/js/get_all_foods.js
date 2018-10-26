$('.input_form_search_food').keyup(function(){
    var food_search = $(this).val()

    $.ajax({
        url : '/get_list_foods',
        dataType : 'json',
        data: {
          'food_search': food_search
        },

        success : function(response){
            $(".input_form_search_food").autocomplete({
                source: response['foods'],
            });
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
            //alert('error')
        }
    });
})



//$('.input_form_search_food').keyup(function(){
//    var food_search = $(this).val()
//
//    $('#input_form_search_food').autocomplete({
//        source : function(){
//            $.ajax({
//                url : '/get_list_foods',
//                dataType : 'json',
//                data: {
//                  'food_search': food_search
//                },
//
//                success : function(response){
//                    $(".input_form_search_food").autocomplete({
//                        source: response,
//                    });
//                },
//                error: function(error) {
//                    console.log('******************')
//                    console.log(error)
//                    alert('error')
//                }
//            });
//        },
//    });
//})