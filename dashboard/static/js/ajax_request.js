// generic ajax request that handles chart construction

function ajax_request(endpoint, chart_method, target_id){

  $.ajax({
    method:"GET",
    url: endpoint,
    success: function(data){
      console.log(data)
      chart_method(target_id, data);
    },
    error: function(error_data){
      console.log('error')
      console.log(error_data)
    }
  });
}
