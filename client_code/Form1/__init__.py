from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Set 'name' to the text in the 'name_box'
    name = self.name_box.text
    # Set 'email' to the text in the 'email_box'
    email = self.email_box.text
    # Set 'feedback' to the text in the 'feedback_box'
    feedback = self.feedback_box.text
    anvil.server.call('add_feedback', name, email, feedback)
    # Show a popup that says 'Feedback submitted!'
    Notification("Feedback submitted!").show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()

  def feedback_box_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def email_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
