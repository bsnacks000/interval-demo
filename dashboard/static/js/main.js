$(document).ready(function(){

  // javascript make do the great app in here
  // event handlers for the two dropdown forms... on event will send an ajax_request

  var target_id = 'plotly-chart'

  $('#boiler-bdbid-dropdown').on('click', function(e){
    // parse the form get request url here
    ajax_request('', boiler_chart, target_id)
  });

  $('#pump-bdbid-dropdown').on('click', function(e){
    // parse the form get request url here
    ajax_request('', pump_chart, target_id)
  });

});
