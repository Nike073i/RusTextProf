function predictionjs() {

    const profiles = {
        "young-man": "Молодой мужчина",
        "young-woman": "Молодая женщина",
        "old-man": "Взрослый мужчина",
        "old-woman": "Взрослая женщина",
    };

    function getProfileDescription({ gender_prediction, age_prediction }) {
        const age = age_prediction.label;
        const gender = gender_prediction.label;
        return profiles[`${age}-${gender}`];
    }

    function renderPrediction({ gender_prediction, age_prediction }) {
        $('#profileImage').prop('src', gender_prediction.label === 'man' ? "images/man.png" : "images/woman.png")
        $('#profileDescription').text(getProfileDescription({ gender_prediction, age_prediction }));

        const scales = [
            {
                scaleName: "Gender",
                indicators: gender_prediction,
            },
            {
                scaleName: "Age",
                indicators: age_prediction,
            }
        ]

        const toPercent = (value) => `${Math.round(value * 10_00) / 10}%`;

        scales.forEach(({ scaleName, indicators }) => {
            const selectElement = (name) => $(`#prediction${scaleName}${name}`);

            selectElement("Threshold").text(toPercent(indicators.threshold));
            selectElement("ValueId").text(toPercent(indicators.proba));
            selectElement("ScaleId").css({
                "--value": toPercent(indicators.proba),
                '--threshold': toPercent(indicators.threshold)
            })
        })
    }

    const LAST_PREDICTION_STORAGE_KEY = "last_prediction";

    const getLastPrediction = () => {
        return localStorage.getItem(LAST_PREDICTION_STORAGE_KEY);
    }

    const setLastPrediction = (prediction, text) => {
        prediction.text = text
        localStorage.setItem(LAST_PREDICTION_STORAGE_KEY, JSON.stringify(prediction));
    }

    return {
        renderPrediction,
        getLastPrediction,
        setLastPrediction
    }
}