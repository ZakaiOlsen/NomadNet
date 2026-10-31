import RNS
import time
import os
import platform

import nomadnet
from nomadnet.ui import THEME_DARK, THEME_LIGHT
from nomadnet import NomadNetworkApp

COLORMODE_MONO = 1
COLORMODE_16   = 16
COLORMODE_88   = 88
COLORMODE_256  = 256
COLORMODE_TRUE = 2**24

IMGLOAD_NEVER  = 0x00
IMGLOAD_MANUAL = 0x01
IMGLOAD_AUTO   = 0x02
IMGLOAD_ALWAYS = 0x03

GLYPHSETS = {
    "plain": 1,
    "unicode": 2,
    "nerdfont": 3
}

if platform.system() == "Darwin":
    urm_char = " \uf0e0"
    ur_char = "\uf0e0 "
else:
    urm_char = " \uf003"
    ur_char = "\uf003 "

GLYPHS = {
    # Glyph name        # Plain      # Unicode      # Nerd Font
    ("check",           "=",         "\u2713",      "\u2713"),
    ("cross",           "X",         "\u2715",      "\u2715"),
    ("unknown",         "?",         "?",           "?"),
    ("encrypted",       "",          "\u26BF",      "\uf023"),
    ("plaintext",       "!",         "!",           "\uf06e "),
    ("arrow_r",         "->",        "\u2192",      "\u2192"),
    ("arrow_l",         "<-",        "\u2190",      "\u2190"),
    ("arrow_u",         "/\\",       "\u2191",      "\u2191"),
    ("arrow_d",         "\\/",       "\u2193",      "\u2193"),
    ("warning",         "!",         "\u26a0",      "\uf12a"),
    ("info",            "i",         "\u2139",      "\U000f064e"),
    ("unread",          "[!]",       "\u2709",      ur_char),
    ("divider1",        "-",         "\u2504",      "\u2504"),
    ("peer",            "[P]",       "\u24c5 ",     "\uf415"),
    ("node",            "[N]",       "\u24c3 ",     "\U000f0002"),
    ("page",            "",          "\u25a4 ",     "\uf719 "),
    ("speed",           "",          "\u25F7 ",     "\U000f04c5 "),
    ("decoration_menu", " +",        " +",          " \U000f043b"),
    ("unread_menu",     " !",        " \u2709",     urm_char),
    ("globe",           "",          "",            "\uf484"),
    ("sent",            "/\\",       "\u2191",      "\U000f0cd8"),
    ("papermsg",        "P",         "\u25a4",      "\uf719"),
    ("qrcode",          "QR",        "\u25a4",      "\uf029"),
    ("selected",        "[*] ",      "\u25CF",      "\u25CF"),
    ("unselected",      "[ ] ",      "\u25CB",      "\u25CB"),
    ("focus_arrow",     ">",         "\u25B8",      "\u25B8"),
    ("sep_dot",         "|",         "\u00B7",      "\u00B7"),
    ("connected",       "+",         "\u2713",      "\U000f0201"),
    ("disconnected",    "x",         "\u2717",      "\U000f0202"),
    ("file",            "[F]",       "\u25a4",      "\uf15b"),
    ("image",           "[I]",       "\u25a3",      "\uf1c5"),
    ("audio",           "[~]",       "\u266b",      "\uf1c7"),
    ("pin",             "*",         "\u2605",      "\uf08d"),
    ("copy",            "[C]",       "\u29c9",      "\uf0c5"),
    ("folder",          "[+]",       "\u25b8",      "\uf07b"),
    ("folder_open",     "[-]",       "\u25be",      "\uf07c"),
    ("fold_open",       "-",         "▾",      "▾"),
    ("fold_closed",     "+",         "▸",      "▸"),
    ("dropdown",        " [v]",      " ▾",          " "),
}

class AShellUI:

    def __init__(self):
        self.restore_ixon = False

        try:
            #rval = os.system("stty -a | grep \"\\-ixon\"")
            if rval == 0:
                pass

            else:
                os.system("stty -ixon")
                self.restore_ixon = True

        except Exception as e:
            RNS.log("Could not configure terminal flow control sequences, some keybindings may not work.", RNS.LOG_WARNING)
            RNS.log("The contained exception was: "+str(e))

        self.app = NomadNetworkApp.get_shared_instance()
        self.app.ui = self
        self.loop = None

        #self.loop = urwid.MainLoop(initial_widget, unhandled_input=self.unhandled_input, screen=self.screen, handle_mouse=mouse_enabled)


        #self.main_display.start()
        
        #self.loop.run()

        self.display_main(self.loop, None)

#    def unhandled_input(self, key):
#        if key == "ctrl q":   self.main_display.quit()
#        elif key == "ctrl e": pass

    def display_main(self, loop, user_data):
        import code
        code.interact(local=locals())
#        self.loop.widget = self.main_display.widget
#        if self.app.peer_settings_notice: self.main_display.show_notice(self.app.peer_settings_notice)
