$( document ).ready(function() {
  
	 $.ajax({
	    url: "/api/news",
	    contentType: "application/json",
	    dataType: 'json',
	    success: setupData
   	})

	 $("text").on("click", function(){
  		console.log(this);
		});

	function setupData(result){
	    var newsData = result['data'];
	    var words = newsData['keywords'];

	    displayAllArticles(words);

	    var dataCloud = [];

	    for(i in words){
	    	if(words[i]['compteur'] > 2){
		    	dataCloud.push({
		    		'name':i,
		    		'weight':words[i]['compteur']
		    	})
		    }
	    }

	    displayNews(dataCloud);
	 
	}

	function displayAllArticles(words){

		var div = $("#tableauArticles").html("");
    	div.append("<table></table");
    	var tab = $("#tableauArticles table");
    	var cpt = 0;
    	var link;
    	tab.append("<tr><th>Mots</th><th>Liens</th></tr>");

		for(i in words){
			if(words[i]['compteur'] > 2 ){
				words[i]['url'].forEach((element) => {
					if(cpt%2 == 0)
						link = element;
					else{
						
						var newLine = "<tr><td class='newspaper'>"+i+"</td><td><a target='_blank'href='" + link + "'>"+element+"</a></td></tr>"
       					tab.append(newLine);

					}
					cpt++;
				}); 
	
			
			}
		}
	}


	function displayNews(dataCloud){
		Highcharts.chart('nuage', {
		    series: [{
		        type: 'wordcloud',
		        data: dataCloud,
		        name: 'Occurrences'
		    }],
		    title: {
		        text: ''
		    }
			});

	}


});