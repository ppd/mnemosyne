#
# review_controller.py <Peter.Bienstman@UGent.be>
#

from mnemosyne.libmnemosyne.component import Component


class ReviewController(Component):
    
    """Controls the behaviour of a widget which implements the ReviewWidget
    interface.
    
    """

    component_type = "review_controller"

    def __init__(self, component_manager):
        Component.__init__(self, component_manager)
        self.card = None

    def reset(self):
        raise NotImplementedError
    
    def reset_but_try_to_keep_current_card(self):

        """This is typically called after activities which invalidate the
        current queue, like 'Activate cards' or 'Configure'. For the best user
        experience, we try to keep the card that is currently being asked if
        possible.

        """
        
        raise NotImplementedError
    
    def heartbeat(self):

        """For code that needs to run periodically, e.g. to react to a change
        of date.

        """
        
        pass

    def new_question(self, learn_ahead=False):
        raise NotImplementedError    
        
    def show_answer(self):
        raise NotImplementedError

    def grade_answer(self, grade):
        raise NotImplementedError     

    def rebuild_queue(self):

        """Called when something in the GUI could have invalidated the queue.
        (e.g. card deletion).

        """

        sch = self.scheduler()
        sch.reset()
        sch.rebuild_queue()
        if not sch.in_queue(self.card):
            self.new_question()
        else:
            sch.remove_from_queue(self.card)

    def get_counters(self):

        "Returns tuple (scheduled_count, non_memorised_count, active_count). "
        
        raise NotImplementedError

    def reload_counters(self):
        
        "To be called when counters need to be reloaded from the database. "
        
        raise NotImplementedError       
    
    def update_dialog(self):
        raise NotImplementedError

    def update_statusbar(self, message=None):
        raise NotImplementedError 

    def is_question_showing(self):
        raise NotImplementedError

    def is_answer_showing(self):
        raise NotImplementedError  
