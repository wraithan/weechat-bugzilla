# Copyright (c) 2013 by Wraithan <xwraithanx@gmail.com>

# History
# 2013-05-04, Wraithan <xwraithanx@gmail.com>
#   version 0.0.1: Initial implementation

import re

import weechat


SCRIPT_NAME = 'bugzilla'
SCRIPT_AUTHOR = 'Wraithan <xwraithanx@gmail.com>'
SCRIPT_VERSION = '0.0.1'
SCRIPT_LICENSE = 'MIT'
SCRIPT_DESC = "Create bugzilla links from 'bug <number>'"

settings = {}

if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                    SCRIPT_DESC, '', ''):

    for option, default_value in settings.iteritems():
        if weechat.config_get_plugin(option) == '':
            weechat.config_set_plugin(option, default_value)

    hooks = ('notify_message', 'notify_private', 'notify_highlight')

    for hook in hooks:
        weechat.hook_print('', hook, 'bug', 1, 'hook_print_callback', '')


def hook_print_callback(data, buffer, date, tags, displayed, highlight, prefix,
                        message):

    url = '{0}[http://bugzil.la/{1}]'
    for number in re.findall(r'bug (\d+)', message):
        weechat.prnt(buffer, url.format(weechat.color('yellow'), number))

    return weechat.WEECHAT_RC_OK
