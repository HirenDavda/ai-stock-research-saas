function success(res, data, requestId) {
    return res.json({
        success: true,
        data,
        error: null,
        requestId
    });
}

function failure(res, error, requestId, status = 500) {
    return res.status(status).json({
        success: false,
        data: null,
        error,
        requestId
    });
}

module.exports = {
    success,
    failure
}


