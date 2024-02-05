"The alarm has been postponed {amount_minutes} minutes" 

class Alarm:
    def snooze(self, amount_minutes):
        print(f"The alarm has been postponed {amount_minutes} minutes")
        
clock = Alarm().snooze(10)