import wx

try:
    import poser
except ImportError:
    raise RuntimeError("Script must run in Poser.")


def generate_names(obj_list):
    if hasattr(obj_list, "__iter__"):
        for obj in obj_list:
            if hasattr(obj, "Name"):
                yield obj.Name()


def actor_choice(choicelist=None):
    """
    Demonstrates wx.control SingleChoiceDialog
    """
    if choicelist is None:
        choicelist = poser.Scene().Actors()

    choices = list(generate_names(choicelist))
    with wx.SingleChoiceDialog(None,
                               caption="My Actor Dialog",
                               message="Select one actor",
                               choices=choices,
                               style=wx.CHOICEDLG_STYLE
                               ) as dlg:
        if dlg.ShowModal() == wx.ID_OK:
            return dlg.GetStringSelection()
        else:
            return None


def actor_choices(choicelist=None):
    """
    Demonstrates wx.control MultiChoiceDialog
    """
    if choicelist is None:
        choicelist = poser.Scene().Actors()

    choices = list(generate_names(choicelist))
    with wx.MultiChoiceDialog(None,
                              caption="My Actor Dialog",
                              message="Select one actor",
                              choices=choices,
                              style=wx.CHOICEDLG_STYLE
                              ) as dlg:
        if dlg.ShowModal() == wx.ID_OK:
            return [choices[i] for i in dlg.GetSelections()]
        else:
            return None


actorname = actor_choice()
print("Selected Actors:", actorname if actorname is not None else "None")

actornames = actor_choices()
print("Selected Actors:", actornames if actornames is not None else "None")
