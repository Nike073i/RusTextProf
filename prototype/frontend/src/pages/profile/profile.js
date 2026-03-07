//= pages/profile/partials/prediction/prediction.js
const { renderPrediction, getLastPrediction } = predictionjs();

//= pages/profile/partials/metrics/profile__metrics.js
const renderMetrics = profile__metricsjs();

$(document).ready(function () {
    const prediction = getLastPrediction();
    if (!prediction) return;

    const data = JSON.parse(prediction);

    $('#predictionSourceText').text(data.text);
    renderPrediction({ gender_prediction: data.gender_prediction, age_prediction: data.age_prediction });
    renderMetrics(data.metrics);

    $('#predictionPlaceholder').addClass('hidden');
    $('#predictionResult').removeClass('hidden');
    $('#predictionMetrics').removeClass('hidden');
});