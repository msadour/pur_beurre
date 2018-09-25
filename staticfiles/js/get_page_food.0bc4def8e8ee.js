//$(function() {
//    $('.img_food').click(function() {
//        name_food = $(this).closest("form").attr('id');
//        $.ajax({
//            headers: {  'Access-Control-Allow-Origin': 'http://127.0.0.1:8000' },
//            url: '/website_pur_beurre/go_page_food',
//            data: {'id_food' : id_food},
//            type: 'GET',
//            dataType: "json",
//            contentType : "application/json",
//            success: function(response) {
//                console.log('success')
//            },
//            error: function(error) {
//                console.log(error)
//                alert('error')
//            }
//        });
//    });
//});