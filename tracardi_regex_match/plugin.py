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


class SearchAction(ActionRunner):

    def __init__(self, **kwargs):
        self.config = Configuration(**kwargs)

    async def run(self, payload):
        dot = self._get_dot_accessor(payload)
        text = dot[self.config.text]
        result = search(self.config.pattern, text)
        if result is not None:
            if len(result) == len(self.config.groups_name):
                dictionary = {}
                for i,d in zip(result,self.config.groups_name):
                    dictionary[d] = i
            else:
                raise ValueError("The number of groups in regex must be the same as in groups_name")
        else:
            raise ValueError("regex couldn't find anything matching the pattern from supplied string.")

        return Result(port="payload", value=dictionary)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_regex_match.plugin',
            className='MachAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={"pattern": "<pattern>",
                  "text": "<text or path to text>",
                  "groups": ["group A", "group B"]}
        ),
        metadata=MetaData(
            name='tracardi-regex-match',
            desc='The purpose of this plugin is use regex.match to return matched data.',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
