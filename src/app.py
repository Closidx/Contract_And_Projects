import time
from datetime import datetime
from database.config import Database
from database.models import Project, Contract


class App:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def create_contract(self, name):
        contract = Contract(name=name, status="draft")
        self.db.session.add(contract)
        self.db.session.commit()

    def confirm_contract(self, contract_id):
        contract = self.db.session.query(Contract).filter(Contract.id == contract_id).first()
        contract.status = "active"
        contract.signed_at = datetime.now()
        self.db.session.commit()

    def complete_contract(self, contract_id):
        contract = self.db.session.query(Contract).filter(Contract.id == contract_id).first()
        contract.status = "completed"
        self.db.session.commit()

    def add_contract_to_project(self, contract_id, project_id):
        contract = self.db.session.query(Contract).filter(Contract.id == contract_id).first()
        project = self.db.session.query(Project).filter(Project.id == project_id).first()

        if not contract or not project:
            print("Contract or project not found")
            return

        if contract.status != "active":
            print("Contract must be active")
            return

        if len(project.contracts) >= 1:
            print("Project can have only one active contract")
            return

        contract.project = project
        self.db.session.commit()

    def create_project(self, name):
        project = Project(name=name)
        self.db.session.add(project)
        self.db.session.commit()

    def print_projects(self):
        projects = self.db.session.query(Project).all()
        for project in projects:
            print(f"ID: {project.id}, Name: {project.name}")

    def print_contracts(self):
        contracts = self.db.session.query(Contract).all()
        for contract in contracts:
            print(f"ID: {contract.id}, Name: {contract.name}, Status: {contract.status}")