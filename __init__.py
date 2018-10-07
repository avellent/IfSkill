# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Steven'

LOGGER = getLogger(__name__)


class IfSkill(MycroftSkill):
    def __init__(self):
        super(IfSkill, self).__init__(name="IfSkill")

    def initialize(self):
        definition_reason_intent = IntentBuilder("DefinitionReasonIntent"). \
            require("WhatKeyword").require("LionKeyword").optionally("ReasonKeyword").build()
        self.register_intent(definition_reason_intent, self.handle_definition_reason_intent)

    def handle_definition_reason_intent(self, message):
        reason_kw = message.data.get("ReasonKeyword")
        if reason_kw:
            self.speak_dialog("reason")
        else:
            self.speak_dialog("definition")

    def stop(self):
        pass


def create_skill():
    return IfSkill()
