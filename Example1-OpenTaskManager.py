# -*- coding: utf-8 -*-
"""
@author: Emilio Moretti
Copyright 2013 Emilio Moretti <emilio.morettiATgmailDOTcom>
This program is distributed under the terms of the GNU Lesser General Public License.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from AutoHotPy import AutoHotPy

def openTaskManager(autohotpy,event):
    """
    This function is called when you press DELETE key
    """
    if (autohotpy.CTRL.isPressed() & autohotpy.ALT.isPressed()):  #check if ctrl and alt are also pressed
        autohotpy.ALT.up()        #release alt
        autohotpy.sleep() #don't forget to sleep when you manually send a "down" state
        autohotpy.LEFT_SHIFT.down()
        autohotpy.sleep() 
        autohotpy.ESC.down()
        autohotpy.sleep() 
        autohotpy.LEFT_SHIFT.up()
        autohotpy.ESC.up()

if __name__=="__main__":
    auto = AutoHotPy()
    auto.registerExit(auto.ESC)   # Registering an end key is mandatory to be able tos top the program gracefully
    # In win7 the task manager is launched when you press Ctrl + Shift + ESC
    # I don't like that. Lets call the task manager when you press Ctrl + Alt + Supr
    auto.registerForKeyDown(auto.DELETE,openTaskManager)   
    auto.start()
