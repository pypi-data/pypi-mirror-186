(function () {
  var kpiScores = {{ kpi_scores|tojson }};
  var comparisonKpiScores = {{ comparison_kpi_scores|tojson }}
  var kpis = {{ kpi_set_entries|map(attribute='kpi')|sort(attribute='name')|map(attribute='name')|list|tojson }};

  var scores = kpis
    .map(function (kpi) {return kpiScores[kpi];})
    .filter(function(score) { return score != null; });
  var comparisonScores = kpis
    .map(function (kpi) {return comparisonKpiScores[kpi];})
    .filter(function(score) { return score != null; });

  kpis = kpis.filter(function(kpi) { return kpiScores[kpi] != null; })

  var data = [];
  {% if (compare_bin is defined and compare_bin is not none) or compare_to is not none %}
  if (Object.keys(comparisonKpiScores).length > 0) {
    data.push({
      type: 'scatterpolar',
      r: comparisonScores,
      theta: kpis,
      fill: 'toself',
      {% if compare_bin is defined and compare_bin is not none %}
      name: new Date('{{ compare_bin.start_date.isoformat() }}').toLocaleString()
      {% else %}
      name: '{{ compare_to }}'
      {% endif %}
    });
  }
  {% endif %}
  data.push({
    type: 'scatterpolar',
    r: scores,
    theta: kpis,
    fill: 'toself',
    name: 'Current evaluation'
  });

  var layout = {
    polar: {
      radialaxis: {
        visible: true,
        range: [0, 100]
      }
    },
    showlegend: true,
    legend: {
      xanchor: 'right',
      x: 1.2,
      y: 1.2
    },
    margin: {
      t: 0,
      l: 15,
      r: 0,
      b: 30,
    }
  }

  Plotly.newPlot("timeseries_source_score", data, layout);
})();
