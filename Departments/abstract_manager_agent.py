from abc import ABC, abstractmethod
from files.backend.src.services.Technology_Department.automation.actions import hook

class AbstractManagerAgent(ABC):
    """
    Classe abstraite représentant un agent manager dans l'organisation.
    Tous les agents managers doivent hériter de cette classe et implémenter les méthodes abstraites.
    """

    def __init__(self, agent_id, name, department):
        self.agent_id = agent_id
        self.name = name
        self.department = department

    @abstractmethod
    def manage(self):
        """
        Méthode principale pour gérer les opérations du département.
        Chaque sous-classe doit implémenter cette méthode pour gérer les spécificités de son département.
        """
        pass

    @abstractmethod
    def report(self):
        """
        Méthode pour générer un rapport sur l'état du département ou du projet géré.
        Chaque sous-classe doit implémenter cette méthode pour fournir les informations pertinentes.
        """
        pass

    def get_details(self):
        """
        Retourne les détails de l'agent manager.
        """
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "department": self.department
        }

    def assign_task(self, task):
        """
        Assigne une tâche à un agent sous la responsabilité de ce manager.
        Cette méthode peut être surchargée pour des comportements spécifiques.
        :param task: Dictionnaire représentant la tâche à assigner
        """
        print(f"Tâche '{task['name']}' assignée par {self.name} dans le département {self.department}.")

