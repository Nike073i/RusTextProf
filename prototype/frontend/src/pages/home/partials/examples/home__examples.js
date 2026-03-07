function home__examplesjs({ unblock, block }) {

    const $modalExamples = $('#modalExamples');
    const $exampleSelector = $('#exampleSelector');

    function showModal(onExampleSelected) {

        $('#confirmExampleSelection').click(function () {
            const selectedExample = $exampleSelector.find(":selected").val();

            if (selectedExample === 'none') {
                unblock();
                return;
            }

            onExampleSelected(selectedExample);

        });
        $('#cancelExampleSelection').click(function () {
            unblock();
        });
        
        block({ message: $modalExamples });
    }

    return showModal;
}