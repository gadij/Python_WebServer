def payload_check(payload):
    error = {"is_error": False, "err_message": ""}
    if not payload:
        error['is_error'] = True
        error['err_message'] = 'Must supply message object: {content: ..., to: ...}'
    if payload.get("to") is None:
        error['is_error'] = True
        error['err_message'] = "Must have a 'to' field in the message"
    if not isinstance(payload.get("to"), int):
        error['is_error'] = True
        error['err_message'] = "The field: 'to' must be an Integer"
    return error
