if not (callable({name}) or isinstance({name}, _notebook_type_store) or isinstance({name}, _notebook_module_type)):
    _notebook_log_error("""{err_msg}""")

