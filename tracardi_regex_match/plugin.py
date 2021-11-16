from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_regex_match.model.model import Configuration
import re


def search(pattern, text):
    result = re.search(f"{pattern}", text)
    if result is None:
        return None
    return result.groups()


def validate(config: dict):
    return Configuration(**config)


class RegexMatchAction(ActionRunner):

    def __init__(self, **kwargs):
        self.config = validate(kwargs)

    async def run(self, payload):
        dot = self._get_dot_accessor(payload)
        text = dot[self.config.text]
        result = search(self.config.pattern, text)

        dictionary = {}
        if result is not None:
            for i, match in enumerate(result):
                dictionary[f"{self.config.group_prefix}-{i}"] = match
        else:
            self.console.warn("Regex couldn't find anything matching the pattern from supplied string.")
        return Result(port="payload", value=dictionary)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_regex_match.plugin',
            className='RegexMatchAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.6.0',
            license="MIT",
            author="Patryk Migaj",
            manual="regex/regex_match",
            init={
                "pattern": "<pattern>",
                "text": "<text or path to text>",
                "group_prefix": "Group"
            }
        ),
        metadata=MetaData(
            name='Regex match',
            desc='This plugin use regex matching and returns matched data.',
            type='flowNode',
            width=200,
            height=100,
            icon='regex',
            group=["Regex"]
        )
    )
