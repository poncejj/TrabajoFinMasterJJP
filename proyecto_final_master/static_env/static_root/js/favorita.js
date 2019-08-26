(function () {
  $('.table').DataTable();
  let markers = [];
  var sPath = window.location.pathname;
	$('a[href="'+ sPath +'"].nav-link').addClass('active');
  $('.datepicker').datepicker({
            format:'yyyy-mm-dd'
        });
    $( ".slider" ).slider({
	 	range: false,
      	min: 0,
      	max: 1,
      	step: 0.1,
      create: function() {
      	var obj = $(this).children().data('val');
        $(this).children().text( $( this ).slider( "value" ) );
      	$('#'+ obj).val( $( this ).slider( "value" ));
      },
      slide: function( event, ui ) {
        var obj = $(this).children().data('val');
        $(this).children().text( ui.value );
      	$('#' + obj).val( ui.value);
      }
    });
    $('input[type="checkbox"]','#id_routes').click(function(){
      var routeName = $(this).val()
      if($(this).prop("checked") == true){
          addMarkers(routeName);
          addDrivers(routeName);
          addItems(routeName);
          addDistances(routeName);
      }
      else if($(this).prop("checked") == false){
          removeMarkers(routeName);
          removeSelector(routeName, 'id_markers');
          removeSelector(routeName, 'id_drivers');
          removeSelector(routeName, 'id_items');
          removeSelector(routeName, 'id_stores');
          removeSelector(routeName, 'id_distances');
      }
  });
}())

function redirect_url(url){
	document.location.href = url;
}

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function addMarkers(routeName) {
  var c = coordinates[routeName]
  var pinColor = getRandomColor();
  c.forEach(function (item, index) 
  { 
    var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+ index +"|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34));
    var myLatLng = { lat: item[1][0], lng: item[1][1] };
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      draggable: true,
      animation: google.maps.Animation.DROP,
      icon: pinImage,
      title: routeName
    });
    
    markers.push(marker);

    $('#id_stores').append($("<option></option>").attr("value",routeName)
      .text(routeName + ', Store ' + item[0] + ', Coordinates ' + '(' + item[1] + ')' )); 
  });
}

function removeMarkers(routeName) {
  var markers2 = []
  for( var i = 0; i < markers.length; i++){ 
    if ( markers[i].title === routeName) {
      markers[i].setMap(null);
    }
    else{
      markers2.push(markers[i]);
    }
  }
  markers = markers2;
  markers2 = [];
}

function addDrivers(routeName) {
  var d = drivers[routeName]
  $.each(d, function(key, value) {   
   $('#id_drivers')
      .append($("<option></option>")
      .attr("value",routeName)
      .text(value)); 
  });
}

function addItems(routeName) {
  var i = items[routeName]
  $.each(i, function(key, value) { 

   $('#id_items')
      .append($("<option></option>")
      .attr("value",routeName)
      .text('Store ' + value[0] + ', Item ' + value[1] + ', Quantity: ' + value[2])); 
  });
}

function addStores(routeName) {
  var s = stores[routeName]
  $.each(s, function(key, value) { 
   $('#id_stores')
      .append($("<option></option>")
      .attr("value",routeName)
      .text(routeName + ', Store ' + value)); 
  });
}

function addDistances(routeName) {
   $('#id_distances')
      .append($("<option></option>")
      .attr("value",routeName)
      .text(routeName + ', Distance: ' + distances[routeName])); 
}

function removeSelector(routeName, selector) {
  $("#" + selector + " option[value='"+ routeName +"']").each(function() {
      $(this).remove();
  });
}