
function register_handler(api_endpoint_name, chart_method, dropdown_id, div_target_id){

  dropdown_id.on('change', function(e) {
    e.preventDefault();
    var id_str = dropdown_id.serialize(); // get the bdbid query string from the form
    var endpoint = '/dashboard/api/'+ api_endpoint_name +'/?'+ id_str
    console.log(endpoint)
    ajax_request(endpoint, boiler_chart, div_target_id)
  });

}


$(document).ready(function(){

  // javascript make do the great app in here
  // event handlers for the two dropdown forms... on event will send an ajax_request

  var div_target_id = 'plotly-chart'
  var boiler_id = $('#boiler-dropdown')
  var pump_id = $('#pump-dropdown')


  register_handler('boilers', boiler_chart, boiler_id, div_target_id)
  register_handler('pumps', pump_chart, pump_id, div_target_id)

  // boiler_id.on('change', function(e){
  //   e.preventDefault();
  //   //console.log(boiler_id.serialize())
  //   var id_str = boiler_id.serialize();
  //   // var target =
  //
  //   ajax_request('', boiler_chart, target_id)
  // });
  //
  // pump_id.on('change', function(e){
  //   e.preventDefault()
  //   console.log(pump_id.serialize())
  //   // parse the form get request url here
  //   ajax_request('', pump_chart, target_id)
  // });

});
