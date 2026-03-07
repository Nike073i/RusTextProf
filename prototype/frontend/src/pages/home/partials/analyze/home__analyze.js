function home__analyzejs({ selectExample, submitForm }) {

    // input-text
    const $charCounter = $('#charCounter');
    const $inputText = $('#inputText');
    const UPDATE_COUNTER_DEBOUNCE_TIMEOUT = 250;
    const INPUT_TEXT_MAX_LENGTH = 10000;

    const setInputText = (text) => {
        const slice = text.slice(0, INPUT_TEXT_MAX_LENGTH);
        $inputText.val(slice).trigger('input');
    }
    const updateCounter = () => {
        const textLength = $inputText.val().length;
        $charCounter.text(textLength);
    };

    const debouncedUpdateCounter = $.debounce(UPDATE_COUNTER_DEBOUNCE_TIMEOUT, updateCounter);
    $inputText.on('input keyup paste change', debouncedUpdateCounter);


    // models
    const $modelSelector = $('#modelSelector');

    const setModels = (models) => {
        $modelSelector.empty();

        const $options = models.map(model =>
            $('<option>', {
                value: model.id,
                text: model.name
            })
        )
        $options[0].prop('selected', true);
        $modelSelector.append($options);
    }

    // example from local file
    $('#uploadBtn').click(function () {
        $('#fileInput').click();
    });

    $('#fileInput').on('change', function (e) {
        const file = e.target.files[0];

        if (!file) {
            return;
        }

        if (!file.name.endsWith('.txt')) {
            alert('Пожалуйста, выберите текстовый файл с расширением .txt');
            return;
        }

        const reader = new FileReader();

        reader.onload = function (e) {
            const content = e.target.result;
            setInputText(content)
        };

        reader.onerror = function () {
            alert('Ошибка при чтении файла');
        };

        reader.readAsText(file, 'UTF-8');
    });

    // example from www
    $('#selectExampleBtn').click(function () {
        selectExample(setInputText);
    });

    // predict
    $('#textAnalyzeForm').on('submit', function (e) {
        e.preventDefault();
        submitForm({ text: $inputText.val(), model_id: $modelSelector.val() });
    });

    return {
        setModels
    }
}