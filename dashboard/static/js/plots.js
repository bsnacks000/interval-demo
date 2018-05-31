// plotly construction
// callbacks for the ajax requests

function UnitRecord(unit_number, pre_arr, post_arr){
  // object prototype for a split record for a pump or boiler (or whatever) unit
  this.unit_number = unit_number
  this.pre = pre_arr
  this.post = post_arr
}


function _get_unique_values_from_keys(data_arr, keyname){
  // get all the unique values given the keys
  var vals =_.chain(data_arr).pluck(keyname).unique().value();
  return vals
}



function _split_dataset(data_arr, chart_type='pump'){
  // splits the flat dataset by boiler into pre and post
  //  { 1: { pre:[ ...records ], post:[ ...records ] },  2: { pre:[...records ], post:[...records ] }
  // create array of boiler/ pump numbers -- unique
  var identifiers = _get_unique_values_from_keys(data_arr, chart_type)

  var records = {}
  identifiers.forEach(function(elem){

    var res = _.filter(data_arr, function(d) { return d[chart_type] == elem });
    var pre = _.filter(res, function(d) { return d.pre_post == 1 })
    var post =_.filter(res, function(d) { return d.pre_post == 3 });


    records[elem] = new UnitRecord(elem, pre, post);

  });
  console.log(records)
  return records
}



function _convert_records_to_lists(records){
  // turns an array of object records into a object of lists
  var keys = Object.keys(records[0])

  result = {}
  keys.forEach(function(key){
    result[key] = records.map(function(rec){
      return rec[key]
    }, {});

  });

  // document.write(JSON.stringify(result))
  return result
}



function _make_pump_trace(records_unit_prepost, prepost_tag, plot_args){ // individual plot array of object

  // works with pre or post  data for a single boiler
  var plot_arrays = _convert_records_to_lists(records_unit_prepost); // object keyed for arrays
  var trace = {
    x: plot_arrays[plot_args.x],
    y: plot_arrays[plot_args.y],
    type: 'scatter',
    name: prepost_tag
  }
  return trace
  // plotly code return a single figure

}

function _make_boiler_trace(records_unit_prepost, prepost_tag, plot_args){

  var plot_arrays = _convert_records_to_lists(records_unit_prepost)

  var trace1 = {
    x: plot_arrays[plot_args.x],
    y: plot_arrays[plot_args.y],
    name: 'Usage',
    type: 'scatter'
  }

  var trace2 = {
    x: plot_arrays[plot_args.x],
    y: plot_arrays[plot_args.z],
    name: 'Temperature',
    yaxis: 'y2',
    type: 'scatter'
  }

  var traces = [trace1, trace2]
  return traces

}



function _$make_new_div(parent_id, tag){
  // creates a new div for each subplot that is a child of the target_id (master div in the template)
  // returns the div and the div's id string

  var unit_tag = 'plot-' + tag
  var new_div = '<div id='+ unit_tag + '></div>'
  parent_id = '#'+ parent_id;
  $(parent_id).prepend(new_div)

  return unit_tag  // this is the child divs id for Plotly
}



function make_pump_chart_inner(target_id, data, type_str, plot_args={}){
  // use the data to generate the plot for the the target_id string

  var records = _split_dataset(data, type_str)  //{1: UnitRecord, 2: UnitRecord}
  // _convert_records_to_lists(records[1].pre)

  // loop over records -- make pre and post plots for each record and append
  record_keys = Object.keys(records);
  record_keys.forEach(function(unit_number){
      // call _make_single_chart twice pre and post

      var preplot = _make_pump_trace(records[unit_number].pre, 'pre', plot_args)
      var postplot = _make_pump_trace(records[unit_number].post, 'post', plot_args)

      // assemble pre and post plots into 1 plot -- Plotly combine into a sublplot [ preplot, postplot ]
      var bothplots = [preplot, postplot]
      var title_string = type_str.charAt(0).toUpperCase() + type_str.substr(1)
      var layout = {title: title_string + ' ' + unit_number}

      // create a new div with a tag (using the unit number )
      tag = _$make_new_div(target_id, unit_number)

      // call plotly on new div
      Plotly.plot(tag, bothplots, layout)
  });
}


function make_boiler_chart_inner(target_id, data, type_str, plot_args={}){
  // use the data to generate the plot for the the target_id string

  var records = _split_dataset(data, type_str)  //{1: UnitRecord, 2: UnitRecord}
  // _convert_records_to_lists(records[1].pre)

  // loop over records -- make pre and post plots for each record and append
  record_keys = Object.keys(records);
  record_keys.forEach(function(unit_number){
      // call _make_single_chart twice pre and post
      var preplot = _make_boiler_trace(records[unit_number].pre, 'pre', plot_args)

      // assemble pre and post plots into 1 plot -- Plotly combine into a sublplot [ preplot, postplot ]
      //var bothplots = [preplot, postplot]
      var title_string = type_str.charAt(0).toUpperCase() + type_str.substr(1)
      var layout = {
          title: title_string + ' ' + unit_number + ' vs. Temperature',
          yaxis: {title: 'Usage'},
          yaxis2: {
            title: 'Temperature',
            overlaying: 'y',
            side:'right'
          }
        }
      // create a new div with a tag (using the unit number )
      tag = _$make_new_div(target_id, unit_number)

      // call plotly on new div
      Plotly.plot(tag, preplot, layout)
  });
}


function pump_chart(target_id, data){
  // calls make chart with pump string
  make_pump_chart_inner(target_id, data, 'pump', {x:'date_time', y: 'motor_on'})
}


function boiler_chart(target_id, data){
  //use the data to generate the plot for the given target_id string
  make_boiler_chart_inner(target_id, data, 'boiler', {x:'date_time', 'y': 'usage_ccf', 'z': 'temperature'})
}
