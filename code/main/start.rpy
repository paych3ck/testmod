init python:
    mods["thld_start"] = u"{font=[thld_main_menu_font]}{size=40}SSSSSS{/font}{/size}"

    try:
        modsImages["thld_start"] = (THLD_GUI_PATH + "misc/thld_tabular_list_preview.png", False)

    except:
        pass

label thld_start:
    $ thld_set_time(THLD_TIMEOFDAY_PROLOGUE)
    $ thld_onload("lock")
    $ thld_set_dynamic_cursor("main_menu")
    $ thld_screens_save_act()
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    scene thld_main_menu_background
    show thld_intro_logo at truecenter
    show thld_blank_skip
    with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    play sound thld_intro_sample
    $ renpy.pause(8, hard=True)
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    $ thld_set_mode_adv()

    label thld_after_intro:
        $ thld_onload("unlock")
        stop sound
        $ renpy.transition(Dissolve(2))
