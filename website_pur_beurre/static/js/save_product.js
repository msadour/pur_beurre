$(function() {
    $('.button_save').click(function() {
        id_food = $(this).closest("form").attr('id');
        $.ajax({
            headers: {  'Access-Control-Allow-Origin': 'http://127.0.0.1:8000' },
            url: '/website_pur_beurre/save_food',
            data: {'id_food' : id_food},
            type: 'GET',
            dataType: "json",
            contentType : "application/json",
            success: function(response) {
                error = response['error_user_food']
                food_name = response['food'];
                if (error == true){
                    alert('Vous avez deja sauvegardé cet aliment !');
                } else{
                    alert('Vous avez choisi : ' + food_name);
                }

            },
            error: function(error) {
                console.log(error)
                //alert('error')
            }
        });
    });
});