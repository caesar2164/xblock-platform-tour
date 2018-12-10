"""
This is the core logic for the Platform Tour xblock, which introduces students to
a course through a digital tour.
"""
import json
import pkg_resources

from django.template import Context
from django.template.loader import get_template
from xblock.core import XBlock
from xblock.fields import List
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment

import default_steps

def _resource_string(path):
    """
    Handy helper for getting resources from our kit.
    """
    data = pkg_resources.resource_string(__name__, path)
    return data.decode('utf8')


class PlatformTourXBlock(XBlock):
    """
    Allows students to tour through the course and get familiar with the
    platform.
    """

    display_name = String(
        display_name=('Display Name'),
        help=(
            'The title for this component'
        ),
        default='Platform Tour',
        scope=Scope.settings,
    )
    button_label = String(
        display_name=('Button label'),
        help=(
            'The text that will appear on the button on which learners click'
            ' to start the Platform Tour.'
        ),
        default='Begin Platform Tour',
        scope=Scope.settings,
    )
    intro = String(
        display_name=('Introduction text'),
        help=(
            'The introduction that will precede the button'
            ' and explain its presence to the user'
        ),
        default='Click the button below to learn how to navigate the platform.',
        scope=Scope.settings,
    )
    enabled_default_steps = List(
        display_name=('Choose the steps for the Platform Tour'),
        help=(
            'List representing steps of the tour'
        ),
        default=[],
        multiline_editor=True,
        scope=Scope.settings,
        resettable_editor=False,
    )
    custom_steps = List(
        display_name=('Custom steps for the platform tour'),
        help=(
            'JSON dictionaries representing additional steps of the tour'
        ),
        default=[],
        multiline_editor=True,
        scope=Scope.settings,
    )

    def build_fragment(
        self,
        template,
        context_dict,
        initialize_js_func,
        additional_css=[],
        additional_js=[],
    ):
        context = Context(context_dict)
        fragment = Fragment(template.render(context))
        for item in additional_css:
            url = self.runtime.local_resource_url(self, item)
            fragment.add_css_url(url)
        for item in additional_js:
            url = self.runtime.local_resource_url(self, item)
            fragment.add_javascript_url(url)
        fragment.initialize_js(initialize_js_func)
        return fragment

    def student_view(self, context=None):
        """
        The primary view of the PlatformTourXBlock, shown to students
        when viewing courses.
        """
        step_choice_dict = default_steps.get_display_steps(self.enabled_default_steps)
        if 'custom' in self.enabled_default_steps:
            step_choice_dict.extend(self.custom_steps)
        steps = json.dumps(step_choice_dict)

        context = context or {}
        context.update(
            {
                'display_name': self.display_name,
                'button_label': self.button_label,
                'intro': self.intro,
                'steps': steps,
            }
        )
        template = get_template('platformtour.html')
        fragment = self.build_fragment(
            template,
            context,
            initialize_js_func='PlatformTourXBlock',
            additional_css=[
                'static/css/platformtour.css',
            ],
            additional_js=[
                'static/js/src/intro.js',
                'static/js/src/platformtour.js',
            ],
        )
        return fragment

    def studio_view(self, context=None):
        """
        Build the fragment for the edit/studio view
        Implementation is optional.
        """
        step_choice_keys = self.enabled_default_steps or default_steps.get_default_keys()
        context = context or {}
        context.update(
            {
                'display_name': self.display_name,
                'button_label': self.button_label,
                'intro': self.intro,
                'enabled_default_steps': default_steps.get_choices(step_choice_keys),
                'custom_steps': json.dumps(self.custom_steps),
            }
        )
        template = get_template('platformtour_studio.html')
        fragment = self.build_fragment(
            template,
            context,
            initialize_js_func='PlatformTourStudioUI',
            additional_css=[
                'static/css/platformtour_studio.css',
            ],
            additional_js=[
                'static/js/src/platformtour_studio.js',
            ],
        )
        return fragment

    @XBlock.json_handler
    def studio_view_save(self, data, suffix=''):
        """
        Save XBlock fields
        Returns: the new field values
        """

        self.display_name = data['display_name']
        self.button_label = data['button_label']
        self.intro = data['intro']
        self.enabled_default_steps = data['enabled_default_steps']
        self.custom_steps = data['custom_steps']

        return {
            'display_name': self.display_name,
            'button_label': self.button_label,
            'intro': self.intro,
            'enabled_default_steps': self.enabled_default_steps,
            'custom_steps': self.custom_steps,
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """
        A canned scenario for display in the workbench.
        """
        return [
            ("PlatformTourXBlock",
             """<platformtour/>
             """),
            ("Multiple PlatformTourXBlock",
             """<vertical_demo>
                <platformtour/>
                <platformtour/>
                <platformtour/>
                </vertical_demo>
             """),
        ]
