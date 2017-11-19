function keyDown(e){
	if(e.keyCode == 13){
		search();
	}
}

function search()
{
	console.log("searching...");
	var res = document.getElementById("results");
	res.innerHTML = "Fetchin Results";
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	       console.log(xhttp.responseText);
	       var results = xhttp.responseText;
	       results = results.substr(1);
	       results = results.split(',');
	       var data = '';
	       let count = Math.floor((results.length)/6);
	       for(let i =0; i<count; i++)
	       {
	       		data = data + '<div class="eachResult">'+
									'<div class="authorInfo">'+ results[i*6]+'[ '+results[i*6+1]+' - '+results[i*6+2]+' ]</div>'+
									'<div class="authorPubInfo">'+
										'<div>Total Piblication: '+results[i*6+3]+'</div>'+
										'<div>Citation count: '+results[i*6+4]+'</div>'+
										'<div>Average Citation: '+results[i*6+5]+'</div>'+
									'</div>'+
								'</div>';
	       }
	       if(data == '')
	       		data = "No Results Found";
	       res.innerHTML = data;
	    }
	};
	var query = document.getElementById("searchBox").value;
	console.log(query);
	xhttp.open("GET", "?query=" + query, true);
	xhttp.send();
}