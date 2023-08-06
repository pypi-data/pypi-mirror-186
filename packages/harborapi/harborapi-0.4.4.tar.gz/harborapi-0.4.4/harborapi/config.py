class BackoffConfig:
    max_retries: int = 3
    max_time: int = 60
    delay_factor: int = 2

    def get_max_retries(self):
        return self.max_retries

    def get_max_time(self):
        return self.max_time

    def get_delay_factor(self):
        return self.delay_factor


import backoff


config = BackoffConfig()


class Foo:
    @backoff.on_exception(
        backoff.expo,
        Exception,
        max_tries=config.get_max_retries,
        max_time=config.get_max_time,
        factor=config.get_delay_factor,
    )
    def foo(self) -> None:
        raise Exception("foo")


config.max_time = 1

f = Foo()
f.foo()
