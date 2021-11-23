from abc import ABC, abstractmethod


class AuditTrail:
    def record(self):
        print('Record...')


class Task(ABC):
    def __init__(self) -> None:
        self.audit_trail = AuditTrail()

    def execute(self):
        self.audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass


class GenerateReportTask(Task):
    def _do_execute(self):
        print('Generate Report')


class TransferMoneyTask(Task):
    def _do_execute(self):
        print('Transfer Money')


transfer_money = TransferMoneyTask()
transfer_money._do_execute()
transfer_money.execute()
generate_report = GenerateReportTask()
generate_report._do_execute()
generate_report.execute()