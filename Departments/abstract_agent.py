from abc import ABC, abstractmethod
from files.backend.src.services.Technology_Department.automation.actions import hook

class AbstractAgent(ABC):
    """
    Classe abstraite représentant un agent dans l'organisation.
    Tous les agents doivent hériter de cette classe et implémenter les méthodes abstraites.
    """

    def __init__(self, agent_id, name, role):
        self.agent_id = agent_id
        self.name = name
        self.role = role

    @property
    def agent_details(self):
        """
        Propriété retournant les détails de l'agent.
        """
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "role": self.role
        }

    @abstractmethod
    def perform_task(self, task):
        """
        Méthode abstraite que tous les agents doivent implémenter pour accomplir une tâche.
        Chaque agent aura une implémentation différente de cette méthode en fonction de son rôle.
        :param task: La tâche à accomplir
        """
        pass

    @abstractmethod
    def report_status(self):
        """
        Méthode abstraite pour générer un rapport sur l'état ou l'avancement des tâches de l'agent.
        """
        pass

    def log_activity(self, activity):
        """
        Méthode concrète partagée par tous les agents pour enregistrer une activité.
        """
        hook("before_log_activity")
        hook("after_log_activity")

        print(f"Agent {self.name} a enregistré l'activité : {activity}")

    def log_error(self, activity):
        """
        Méthode concrète partagée par tous les agents pour enregistrer une erreur.
        """
        print(f"Agent {self.name} a enregistré l'activité : {activity}")

    def assign_role(self, new_role):
        """
        Méthode concrète pour changer le rôle d'un agent.
        :param new_role: Le nouveau rôle à assigner
        """
        self.role = new_role
        print(f"Le rôle de l'agent {self.name} a été mis à jour en '{new_role}'.")

    def display_info(self):
        """
        Méthode concrète pour afficher les informations de l'agent.
        """
        print(f"Agent ID: {self.agent_id}, Name: {self.name}, Role: {self.role}")
