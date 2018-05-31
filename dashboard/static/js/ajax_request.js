// generic ajax request that handles chart construction

function ajax_get_request(endpoint, chart_method, target_id){
  // handles a single ajax get request. success renders and injects the plotly chart

  $.ajax({
    method:"GET",
    url: endpoint,
    success: function(data){
      console.log(data)
      chart_method(target_id, data);  // successful data hits a chart_method
    },
    error: function(error_data){
      console.log('error') // just log this error for now
      console.log(error_data)
    }
  });
}


function register_handler(api_endpoint_name, chart_method, dropdown_id, div_target_id){
  // register a jquery handler

  dropdown_id.on('change', function(e) {
    e.preventDefault();

    var id_str = dropdown_id.serialize(); // get the bdbid query string from the form
    var endpoint = '/dashboard/api/'+ api_endpoint_name +'/?'+ id_str // construct the api query

    console.log(endpoint)
    ajax_get_request(endpoint, chart_method, div_target_id)  // make the ajax request
  });

}
