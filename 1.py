@Configlet(_rtype_=str, _on_default_=None)
def DIR_reproducer_273284():
    return get_context().get("DIR_reproducer_273284")

class CTX:
    def __init__(self, x):
        self.x = x
        self.prev_env_var = None
    def __enter__(self):
        self.prev_env_var = DIR_reproducer_273284()
        os.environ["DIR_reproducer_273284"] = self.x
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if self.prev_env_var:
            os.environ["DIR_reproducer_273284"] = self.prev_env_var
            return
        del os.environ["DIR_reproducer_273284"]
