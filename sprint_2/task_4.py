class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        """
            :param name: name of employee
            :param hours: hours of work the employee
            :param rest_days: days of rest for the employee
            :param email: email of employee
        """
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, rest_days):
        hours = (7 - rest_days) * 8
        return cls(hours)

    @classmethod
    def get_email(cls, name):
        email = f"{name}@email.com"
        return cls(email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        summa = self.hours * self.hourly_payment
        return summa


