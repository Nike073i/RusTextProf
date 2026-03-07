$(document).ready(function () {
    //= pages/home/partials/analyze/home__bindrequests.js
    const {
        block, unblock, showError, requestHandler
    } = home__bindrequestsjs();

    const getAvailableModelsRequest = requestHandler({
        url: '__BACKEND_URL__/api/v1/profiling/available-models',
        dataType: 'json',
        converters: {
            "text json": function (text) {
                const data = JSON.parse(text);

                if (!data || data.available_models === undefined) {
                    console.error('Empty response received');
                    throw new Error();
                }
                return data;
            }
        },
    });

    const predictRequest = requestHandler({
        url: '__BACKEND_URL__/api/v1/profiling/predict',
        dataType: 'json',
        contentType: 'application/json',
        type: 'POST',
        error: function (jqXHR) {
            const errorOptions = {};
            if (jqXHR.status === 412) {
                const errorData = jqXHR.responseJSON.error;
                errorOptions.message = errorData.details.errors.join('\n');
                errorOptions.header = errorData.message;
                errorOptions.closable = true;
            }
            showError(errorOptions);
        },
        timeout: 15000
    })

    const exampleRequest = (example, onExampleLoaded) => {
        const request = requestHandler({ url: example });
        request({ processData: onExampleLoaded });
    };

    //= pages/home/partials/examples/home__examples.js
    const showSelectExampleModal = home__examplesjs({
        block,
        unblock,
    });

    //= pages/profile/partials/prediction/prediction.js
    const { renderPrediction, getLastPrediction, setLastPrediction } = predictionjs();

    const STATUS_PREDICTION_UPDATED_EVENT = "status.prediction.updated";
    const NOTIFY_PREDICTION_UPDATED_EVENT = "notify.prediction.updated";

    const predict = (data) => predictRequest({
        data: JSON.stringify(data),
        processData: function (response) {
            setLastPrediction(response, data.text);
            $(document).trigger(STATUS_PREDICTION_UPDATED_EVENT);
        }
    });

    const $predictionSummary = $('#predictionSummary');

    $(document).bind(STATUS_PREDICTION_UPDATED_EVENT, function () {
        $predictionSummary.trigger(NOTIFY_PREDICTION_UPDATED_EVENT)
    });

    //= pages/home/partials/analyze/home__analyze.js
    const {
        setModels
    } = home__analyzejs({
        selectExample: (callback) => {
            showSelectExampleModal(example => exampleRequest(example, callback));
        }, submitForm: predict
    });


    function showPredictionSummary() {
        const prediction = getLastPrediction();

        if (!prediction) return;

        const data = JSON.parse(prediction);
        renderPrediction({ gender_prediction: data.gender_prediction, age_prediction: data.age_prediction });
        $predictionSummary.removeClass('hidden');
    }

    $predictionSummary.on(NOTIFY_PREDICTION_UPDATED_EVENT, showPredictionSummary);

    showPredictionSummary();
    getAvailableModelsRequest({ processData: data => setModels(data.available_models) });
});