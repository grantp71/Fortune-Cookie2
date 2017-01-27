#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    #TODO list of possible fortunes
    fortunes = [
        "Win at Winning",
        "Japan good / Gina bad",
        "Don't Be Stupid",
        "That Sounds Stupid",
        "Weak Green Tea - So Weak",
        "NAFTA..perhaps you've heard of it",
        "Weak! Weak! Weak!",
        "Grab It",
        "Don't be a Loser like Jeb",
        "Beautiful like nothing you've every seen",
        "You are Great and not a Loser",
        "Build It",
        "Taxes? Nobody's Interested",
        "She'll let you",
        "Big Hands Little Marco",
        "Politically Correct",
        "Ask Putin",
        "Bigly",
        "Politically Correct Big League",
        "So proud of you that you're not a Moron",
        "Lock Her Up",
        "Don't be a Moron be Smart like me",
        "Make It Great Again",
        "Moron, Stupid",
        "Renegotiate Smartly",
        "Tough to Drain the Swamp",
        "Tough",
        "Dangerous",
        "Bad",
        "Lightweight",
        "Amazing",
        "Yuge",
        "Tremendous",
        "Terrific",
        "Zero",
        "One Thousand Percent",
        "Out of Control",
        "Classy"
        ]

    #TODO randomly select a fortune
    index = random.randint(0, 37)
    return fortunes[index]
    #index = random.randint(0, 11)

    #return word[index]



class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h2>Fortune Cookie from Trump Tower Grill</h2>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        #fortune_sentence = + fortune
        fortune_paragraph = "<p>"  "Your fortune: " + fortune + "</p>"

        lucky_number = "<strong>" + str(random.randint(2, 100)) + "</strong>"
        number_sentence = 'Number 1 is taken, by me..I give you Lucky Number: ' + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_again_button = "<a href='.'><button>I'm not paying for that!</button></a>"

        content = header + fortune_paragraph + number_paragraph + cookie_again_button


        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
