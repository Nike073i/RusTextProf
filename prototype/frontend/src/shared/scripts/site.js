$.blockUI.defaults = {
    ...$.blockUI.defaults,
    message: '<div class="loader"></div>',
    overlayCSS: {},
    css: {}
}

const createRequestHandler = ({ block, unblock, showError }) => (options) => {
    const defaultOptions = {
        error: function () { showError() },
        beforeSend: function () { block() },
        timeout: 5000,
    }
    return ({ data, processData }) => {
        $.ajax({
            ...defaultOptions,
            ...options,
            data,
            success: function (data) {
                processData(data);
                unblock();
            }
        })
    }
}