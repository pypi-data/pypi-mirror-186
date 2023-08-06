$('.score-bar').each(function (index, bar) {

  var values = $(bar).find('.bar-value').map(function () {
    return parseFloat($(this).text(), 10);
  }).get();

  var trace1 = {
    x: [values[0]],
    y: [''],
    name: 'Good',
    orientation: 'h',
    marker: {
      color: '#009D89',
      width: 2
    },
    type: 'bar',
    hoverinfo: 'x',
  };

  var trace2 = {
    x: [values[1]],
    y: [''],
    name: 'Warning',
    orientation: 'h',
    type: 'bar',
    marker: {
      color: '#FCB800',
      width: 2
    },
    hoverinfo: 'x',
  };

  var trace3 = {
    x: [values[2]],
    y: [''],
    name: 'Critical',
    orientation: 'h',
    type: 'bar',
    marker: {
      color: '#FF0153',
      width: 2
    },
    hoverinfo: 'x',
  };

  var data = [trace1, trace2, trace3];

  var layout = {
    showlegend: false,
    margin: {
      r: 0,
      t: 0,
      b: 0,
      l: 0,
      pad: 0,
    },
    barmode: 'stack',
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    bargap: 0.7,
    xaxis: {
      zeroline: false,
      showline: false,
      fixedrange: true,
    },
    yaxis: {
      fixedrange: true,
    }
  };


  var config = {
    displayModeBar: false,
    responsive: true,
  };

  if (bar.getAttribute('data-height')) {
    layout.height = bar.getAttribute('data-height');
  }

  if (bar.getAttribute('data-width')) {
    layout.width = bar.getAttribute('data-width');
  }

  Plotly.newPlot(bar, data, layout, config);
});
