class Consent:
    positive_response = "Great! Let's play again."
    negative_response = "Okay. It's sure been fun playing with you though!"

    def __init__(self, **kwargs):
        self.question = "Do you wanna play again? "
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def consent_check(self):
         consent = input(self.question)
         if "yes" in consent.lower() or "ya" in consent.lower() or "yeah" in consent.lower() or "yup" in consent.lower()  or "yep" in consent.lower() or "sure" in consent.lower():
            return True
         elif "no" in consent.lower() or "nah" in consent.lower():
            return False
         else:
            print("Sorry, I didn't get that.")
            return self.consent_check()

    
        
        
