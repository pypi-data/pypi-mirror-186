(function (scope) {

    const formatSeriesName = (series) => {
        let result = ""
        if ("series name" in series.tags) {
            result = series.tags["series name"]
        }
        for (const [key, value] of Object.entries(series.tags)) {
            if (key === "series name") {
                continue
            }
            if (result !== "") {
                result = result + ","
            }
            result = result + `${key}=${value}`
        }
        if (series.field !== "value") {
            result = result + `::${series.field}`
        }
        return result
    }

    const getDisplayLength = () => {
        let length = 40
        document.cookie.split("; ").forEach(row => {
            if (row.startsWith("timeseer.series_name_display_length")) {
                length = parseInt(row.split("=")[1], 10)
            }
        })
        return length
    }

    const visualizeSeriesName = (series) => {
        let name = formatSeriesName(series);
        const displayLength = getDisplayLength()

        if (displayLength === 0 || name.length <= displayLength) {
            return { isAbbreviated: false, name }
        }

        const partialLength = Math.round(displayLength / 2)
        name = name.substring(0, partialLength) + "..." + name.substring(name.length - partialLength)
        return { isAbbreviated: true, name }
    }

    const updateBadActorsScores = (badActors) => {
        return badActors.map(badActor => ({
            ...badActor,
            tiles: badActor.tiles.map(tile => {
                let score = tile.score;
                if (tile.state == "bug") {
                    score = (tile.score + 1) / 2;
                } else if (tile.state == "no data") {
                    score = tile.score + 1;
                } else {
                    score = tile.score / 2;
                }
                return { ...tile, score: score };
            }),
        }));
    };

    function plotBadActors(badActors) {
        var series = [];
        var labels = [];
        var scores = [];
        var urls = [];
        var tickvals = [];
        var ticktext = [];
        var hovertexts = [];
        for (var i = 0; i < badActors.length; i++) {
            seriesVisualization = visualizeSeriesName(badActors[i].selector)
            tickvals.push(badActors[i].selector.seriesId)
            ticktext.push(seriesVisualization.name)
            series.push(badActors[i].selector.seriesId)
            scores.push(badActors[i].tiles.map(tile => tile.score))
            hovertexts.push(badActors[i].tiles.map(_ => seriesVisualization.name));
            urls.push(badActors[i].tiles.map(tile => tile.url))
            if (i === 0) {
                labels = badActors[i].tiles
                    .map(tile => {
                        const ts = new Date(tile.startDate)
                        if (isNaN(ts)) {
                            return "";
                        }
                        if (new Date(tile.endDate) - new Date(tile.startDate) < 86400000) {
                            return ts.toLocaleString();
                        } else {
                            return ts.toLocaleDateString();
                        }

                    })
            }
        }

        if (ticktext.length > 45) {
            var newTickVals = [];
            var newTickText = [];
            for (var i=0; i<ticktext.length; i++) {
                if (i % 3 === 0) {
                    newTickText.push(ticktext[i]);
                    newTickVals.push(tickvals[i]);
                }
            }
            ticktext = newTickText;
            tickvals = newTickVals;
        }

        var colorscaleValue = [
            [0, '#009D89'],
            [0.09, '#FDDB7F'],
            [0.5, '#FCB800'],
            [0.5, '#FF80A8'],
            [0.95, '#FF0153'],
            [1.0, '#C2C4C6'],
        ];

        var data = [
            {
                x: labels,
                y: series,
                z: scores,
                text: hovertexts,
                type: 'heatmap',
                customdata: urls,
                colorscale: colorscaleValue,
                showscale: false,
                zmin: 0,
                zmax: 1,
                hoverinfo: "x+text",
                xgap: 1,
                ygap: 1,
            }
        ];
        var layout = {
            xaxis: {
                type: 'category',
                tickangle: -45,
                automargin: true,
                tickmode: 'auto',
                nticks: 24,
                fixedrange: true,
                tickfont: {
                    color: 'gray',
                    size: 10,
                }
            },
            yaxis: {
                type: 'category',
                automargin: true,
                tickmode: 'array',
                fixedrange: true,
                tickvals: tickvals,
                ticktext: ticktext,
                tickfont: {
                    color: 'gray',
                    size: 10,
                }
            },
            margin: {
                r: 20,
                t: 20,
            },
            height: Math.min((series.length * 40) + 104, 700),
        };
        var config = {
            displayModeBar: false,
            responsive: true,
        };

        Plotly.newPlot('bad-actor-visualization', data, layout, config);
        document.getElementById('bad-actor-visualization').on('plotly_click', function (data) {
            if (data.points.length > 0 && data.points[0].customdata) {
                window.location.href = data.points[0].customdata;
            }
        });
    }

    scope.updateBadActorsScores = updateBadActorsScores;
    scope.plotBadActors = plotBadActors;
})(window);
