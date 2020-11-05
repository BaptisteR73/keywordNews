$( document ).ready(function() {
  
	 $.ajax({
	    url: "/api/news",
	    contentType: "application/json",
	    dataType: 'json',
	    success: setupData
   	})

	function setupData(result){
	
	    var newsData = result['data'];
	    var words = newsData['keywords'];
	    var dataCloud = [];

	    for(i in words){
	    	dataCloud.push({
	    		'name':i,
	    		'weight':words[i]['compteur']
	    	})
	    }

	    displayNews(dataCloud);
	 
	}

	function displayNews(dataCloud){
		Highcharts.chart('nuage', {
		    series: [{
		        type: 'wordcloud',
		        data: dataCloud,
		        name: 'Occurrences'
		    }],
		    title: {
		        text: 'Wordcloud'
		    }
			});

	}








});