$('.report-evolution').each(function () {
    let dates = $(this).find('.report-date').map(function () {
        return this.getAttribute('data-date');
    }).get();
    let scores = $(this).find('.report-score').map(function () {
        return parseFloat($(this).text());
    }).get();
    let urls = $(this).find('tr[data-report-url]').map(function () {
        return this.getAttribute('data-report-url');
    }).get();
    let formattedDates = $(this).find('.report-date').map(function () {
        ts = new Date($(this).text())
        return ts.toLocaleString();
    }).get();

    if (dates[0] > dates[1]) {
        formattedDates.reverse();
        scores.reverse();
        urls.reverse();
    }

    var colorscaleValue = [
        [0, '#FF0153'],
        [0.599, '#FF0153'],
        [0.6, '#FCB800'],
        [0.799, '#FCB800'],
        [0.8, '#009D89'],
        [1, '#009D89'],
    ];

    let trace = {
        x: formattedDates,
        y: scores,
        hoverinfo: 'text',
        hovertext: scores.map(function (score, i) {return formattedDates[i] + ': ' + score + '%'}),
        customdata: urls,
        type: 'bar',
        marker: {
            cmin: 0,
            cmax: 100,
            color: scores,
            colorscale: colorscaleValue,
            autocolor: false,
        }
    };

    let layout = {
        margin: {
            r: 0,
            t: 0,
            b: 180,
            pad: 4,
        },
        yaxis: {
            title: 'Score',
            range: [Math.max(Math.min(...scores)-10, 0), Math.max(...scores) + 5]
        },
        xaxis: {
            type: 'category',
            tickangle: -45,
        },
        showlegend: false,
    };

    let config = {
        displayModeBar: false,
        responsive: true,
    };

    Plotly.newPlot(this, [trace], layout, config);
    this.on('plotly_click', function (data) {
        if (data.points.length > 0 && data.points[0].customdata) {
            window.open(data.points[0].customdata, '_blank');
        }
    });
});
