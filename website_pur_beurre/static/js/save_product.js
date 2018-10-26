$(function() {
    $('.button_save').click(function() {
        id_food = $(this).closest("form").attr('id');
        csrf = $("[name='csrfmiddlewaretoken']").val();
        $.ajax({
            headers: {  'Access-Control-Allow-Origin': 'http://127.0.0.1:8000' },
            url: '/save_food',
            data: {'id_food' : id_food, 'csrfmiddlewaretoken': csrf},
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
                console.log('***********************')
                selector = "#"+id_food
                console.log(selector)
                $(selector).css("display", "none");

            },
            error: function(error) {
                console.log('***********************')
                selector = "#"+id_food
                console.log(selector)
                $(selector).css("display", "none");
            }
        });
    });
});