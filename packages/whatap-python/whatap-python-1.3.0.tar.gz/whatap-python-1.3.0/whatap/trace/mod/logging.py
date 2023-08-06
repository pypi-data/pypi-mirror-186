from whatap.trace.trace_context_manager import TraceContextManager

logging_injection_processed = False
def instrument_logging(module):
    global logging_injection_processed
    def wrapper(fn):
        def trace(*args, **kwargs):
            if len(args) > 1:
                record = args[1]
                ctx = TraceContextManager.getLocalContext()
                if ctx:
                    setattr(record, "txid", str(ctx.id))
                else:
                    setattr(record, "txid", None)
            return fn(*args, **kwargs)
        
        return trace
    if not logging_injection_processed:
        module.RotatingFileHandler.format = wrapper(module.RotatingFileHandler.format)
        logging_injection_processed = True
