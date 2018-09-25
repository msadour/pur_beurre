$('#input_search_food').autocomplete({
    source : function(requete, reponse){

        $.ajax({
                url : '/website_pur_beurre/get_list_foods',
                dataType : 'json',
//                data : {
//                    name_startsWith : $('#input_search_food').val(),
//                    maxRows : 15
//                },

                success : function(data){
                    console.log('******************--------------------')
                    reponse($.map(data.geonames, function(food){
                            return food.name + '(' + food.nutri_score + ')';
                        }));
                },
                error: function(error) {
                    console.log(error)
                    alert('error')
                }
            });
    },
    select : function(event, ui){ // lors de la sélection d'une proposition
        $('#input_search_food').val( ui.item.desc ); // on ajoute la description de l'objet dans un bloc
    }
});
