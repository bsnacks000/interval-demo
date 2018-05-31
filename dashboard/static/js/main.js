// imports --> boiler_chart, pump_chart, register_handler

$(document).ready(function(){
  // javascript make do the great app in here!!

  // register event handlers for the two dropdown forms... on event will construct get-request
  // from the form data (bdbid) which is used as a query get filter for pumps or boilers
  // success will render appropriate plotly chart on the target-div

  var div_target_id = 'plotly-chart';
  var boiler_id = $('#boiler-dropdown');
  var pump_id = $('#pump-dropdown');

  register_handler('boilers', boiler_chart, boiler_id, div_target_id);
  register_handler('pumps', pump_chart, pump_id, div_target_id);


});
