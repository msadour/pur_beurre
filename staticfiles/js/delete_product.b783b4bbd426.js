$(function() {
    $('.button_delete').click(function() {
        id_food = $(this).closest("form").attr('id');
        $.ajax({
            headers: {  'Access-Control-Allow-Origin': 'http://127.0.0.1:8000' },
            url: '/website_pur_beurre/delete_food',
            data: {'id_food' : id_food},
            type: 'GET',
            dataType: "json",
            contentType : "application/json",
            success: function(response) {
                food_name = response['food'];
                alert('Vous avez supprimé : ' + food_name);
            },
            error: function(error) {
                console.log(error)
                //alert('error')
            }
        });
    });
});