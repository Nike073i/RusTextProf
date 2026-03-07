function home__bindrequestsjs() {

    const $textAnalyzeSection = $("#textAnalyzeSection");
    const $modalPrototype = $('#modalPrototype')

    function blockTextAnalyzeSection(options) {
        $textAnalyzeSection.block(options);
    }
    function unblockTextAnalyzeSection(options) {
        $textAnalyzeSection.unblock(options);
    }

    const showError = (props = {}) => {
        const {
            header = "Возникла ошибка",
            message = "Возникла непредвиденная ошибка. Попробуйте позднее",
            closable = false
        } = props;

        const $modal = $modalPrototype.clone();
        $modal.removeAttr('id');
        $modal.removeClass('hidden');

        const $header = $('<h3>', { class: "modal__header--error", text: header });
        const $message = $('<p>', { class: "error-message", text: message });

        $modal.find('.modal__header').append($header);
        $modal.find('.modal__body').append($message);

        if (closable) {
            const $closeButton = $('<button>', { text: "Закрыть", type: "button", class: "btn" });
            $closeButton.click(function () { unblockTextAnalyzeSection() })
            $closeButton.attr('data-variant', 'primary');

            $modal.find('.modal__footer').append($closeButton);
        }
        blockTextAnalyzeSection({
            message: $modal,
        });
    }

    const textAnalyzeRequestHandler = createRequestHandler({ block: blockTextAnalyzeSection, unblock: unblockTextAnalyzeSection, showError: showError });

    return {
        block: blockTextAnalyzeSection,
        unblock: unblockTextAnalyzeSection,
        showError,
        requestHandler: textAnalyzeRequestHandler
    }
}