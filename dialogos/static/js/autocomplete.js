


$(document).ready(function($){
	console.log("ey");
	$('#id_title').click(function(){console.log("aqui");});
	$('#id_title').autocomplete({
		source: getData,
		select: getInfo,
		focus: foco
	});
	console.log("yo");
});


getData = function(request,response){
	var url = "https://api.themoviedb.org/3/search/movie?language=es&api_key=5216d9c936b95a2e739acb3c4b1b8adf&query=";
	var title = request.term;
	
	url += title;

	$.get(url,function(data){
		response($.map(data.results, function(item) {
			var date = new Date(item.release_date);
			var year = date.getFullYear();
			var label = item.title+ " ("+year+")";
            return { 
                label: label,
                value: item
            };
        }));
        
	})
}

function getInfo(event, ui){
	var title = ui.item.value.title;
	var date = ui.item.value.release_date;
	console.log(date);
	var id = ui.item.value.id;
	var poster_path = ui.item.value.poster_path;

	$('#id_title').val(title);
	$('#id_year').val(date);
	$('#id_tmdbId').val(id);
	$('#id_posterPath').val(poster_path);
	event.preventDefault();
}

function foco(event, ui){
	var title = ui.item.title;
	event.preventDefault();
}