from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass
    
class MomoPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Momo."
    
    def refund(self, amount):
        return f"Refunded {amount} to Momo account."
    
class ZaloPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Zalo."
    
    def refund(self, amount):
        return f"Refunded {amount} to Zalo account."
    
if __name__ == "__main__":
    momo = MomoPayment()
    zalo = ZaloPayment()

    print(momo.pay(100))
    print(momo.refund(50))
    print(zalo.pay(75))
    print(zalo.refund(25))