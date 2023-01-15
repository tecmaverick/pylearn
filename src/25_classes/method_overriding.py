class vehicle:
    def start(self):
        print("engine started")

    def stop(self):
        print("engine stopped")


class car(vehicle):
    def open_boot(self):
        print("opening boot")

    # override start
    def start(self):
        # Calling the base class start() method, this is optional
        super().start()
        print("starting car")


car1 = car()
car1.start()
car1.open_boot()
car1.stop()
