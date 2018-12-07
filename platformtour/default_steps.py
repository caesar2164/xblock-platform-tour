DEFAULT_STEPS = [
    {
        'key': 'intro',
        'title': 'Welcome / Intro',
        'selector': 'button.navmaker',
        'dataIntro': 'Welcome to the platform walkthrough tour! Let's start by exploring the tabs at the top of the page.',
        'dataPosition': 'right',
    },
    {
        'key': 'course_tab',
        'title': 'Course Tab',
        'selector': '.course-tabs',
        'find': 'a:contains('Course')',
        'dataIntro': 'You are in the Course tab, where all the materials are found.',
        'dataPosition': 'right',
    },
    {
        'key': 'course_content',
        'title': 'Course Content',
        'selector': 'div#seq_content',
        'dataIntro': 'You are looking at content in a page, or unit.',
        'dataPosition': 'top',
    },
    {
        'key': 'unit_breadcrumb',
        'title': 'Unit Breadcrumb',
        'selector': '.nav-item.nav-item-sequence',
        'dataIntro': 'Notice the trail of breadcrumb links above the content. You are currently on a page, or unit...',
        'dataPosition': 'below',
    },
    {
        'key': 'subsection_breadcrumb',
        'title': 'Subsection Breadcrumb',
        'selector': '.nav-item.nav-item-section',
        'dataIntro': '...in a lesson, or subsection...',
        'dataPosition': 'below',
    },
    {
        'key': 'section_breadcrumb',
        'title': 'Section Breadcrumb',
        'selector': '.nav-item.nav-item-chapter',
        'dataIntro': '...in a module, or section. Clicking on a breadcrumb will take you to your course's table of contents, and drop you onto the portion related to the section or subsection you clicked on.',
        'dataPosition': 'right',
    },
    {
        'key': 'course_breadcrumb',
        'title': 'Course Breadcrumb',
        'selector': '.nav-item.nav-item-course',
        'dataIntro': 'This 'Course' link will also take you to the table of contents, but to the beginning, as opposed to a specific section or subsection.',
        'dataPosition': 'right',
    },
    {
        'key': 'filmstrip',
        'title': 'Film Strip Navigator',
        'selector': '#sequence-list',
        'dataIntro': 'Every lesson or subsection is structured as a sequence of pages, or units. Each button on this navigator corresponds to a page of content. You should go through the pages from left to right.',
        'dataPosition': 'left',
    },
    {
        'key': 'filmstrip_first_tab',
        'title': 'First Page Tab',
        'selector': '#tab_0',
        'dataIntro': 'You are currently viewing the first page of content.',
        'dataPosition': 'left',
    },
    {
        'key': 'filmstrip_second_tab',
        'title': 'Second Page Tab',
        'selector': '#tab_1',
        'dataIntro': 'Move to the next page of content by clicking the icon in the highlighted tab...',
        'dataPosition': 'left',
    },
    {
        'key': 'filmstrip_next_arrow',
        'title': 'Next Arrow',
        'selector': '.sequence-nav',
        'find': '.sequence-nav-button.button-next',
        'dataIntro': '...or the arrow to the right.',
        'dataPosition': 'left',
    },
    {
        'key': 'bookmarking',
        'title': 'Bookmarking',
        'selector': '.bookmark-button-wrapper',
        'dataIntro': 'If you want to get back later to the content on a particular page, or you want to save it as something important, bookmark it. A Bookmarks folder on your course home page will contain a link to any page you bookmark for easy access later.',
        'dataPosition': 'right',
    },
    {
        'key': 'course_progress',
        'title': 'Course Progress',
        'selector': '.course-tabs',
        'find': 'a:contains('Progress')',
        'dataIntro': 'Visit the Progress page to check your scores on graded content in the course.',
        'dataPosition': 'left',
    },
    {
        'key': 'discussion_forum',
        'title': 'Discussion Forum',
        'selector': '.course-tabs',
        'find': 'a:contains('Discussion')',
        'dataIntro': 'For course-specific questions, click on the \'Discussion\' tab to post your question to the forum. Peers and course teams may be able to answer your question there.',
        'dataPosition': 'left',
    },
    {
        'key': 'help_link',
        'title': 'Help Link',
        'selector': 'a.doc-link',
        'dataIntro': 'For any technical issues or platform-specific questions, click on the \'Help\' link to access the Help Center or contact support.',
        'dataPosition': 'bottom',
    },
    {
        'key': 'tour_done',
        'title': 'End of Platform Tour',
        'selector': 'div.course-wrapper',
        'dataIntro': 'That concludes the platform tour. \n\n Click Done to close this walkthrough.',
        'dataPosition': 'top',
    },
]

def get_choices(keys):
    choices_list = []
    for step in DEFAULT_STEPS:
        key = step.get('key')
        title = step.get('title')
        if key and title:
            _append_choice(key, title, keys, choices_list)
    _append_choice('custom', 'Custom (Advanced Users)', keys, choices_list)
    return choices_list

def _append_choice(key, title, keys, choices_list):
    is_choice_enabled = key in keys
    choice = {
        'key': key,
        'title': title,
        'enabled': is_choice_enabled
    }
    choices_list.append(choice)

def get_default_keys():
    keys_list = []
    for step in DEFAULT_STEPS:
        keys_list.append(step.get('key'))
    return keys_list

def get_display_steps(keys):
    step_list = []
    for step in DEFAULT_STEPS:
        if step.get('key') in keys:
            step_list.append(step)
    return step_list
