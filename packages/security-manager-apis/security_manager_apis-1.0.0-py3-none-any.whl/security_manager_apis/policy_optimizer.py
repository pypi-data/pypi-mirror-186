import requests
import authenticate_user
from security_manager_apis.get_properties_data import get_properties_data


class PolicyOptimizerApis():

    def __init__(self, host: str, username: str, password: str, verify_ssl: bool, domain_id: str, workflow_name: str,
                 suppress_ssl_warning=False):
        """ User needs to pass host,username,password,and verify_ssl as parameters while
            creating instance of this class and internally Authentication class instance
            will be created which will set authentication token in the header to get firemon API access
        """
        if suppress_ssl_warning:
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        self.parser = get_properties_data()
        self.api_instance = authenticate_user.Authentication(host, username, password, verify_ssl)
        self.headers = self.api_instance.get_auth_token()
        self.host = host
        self.verify_ssl = verify_ssl
        self.api_resp = ''
        self.domain_id = domain_id
        self.workflow_id = self.get_workflow_id_by_workflow_name(domain_id, workflow_name)

    def create_po_ticket(self, request_body: dict) -> int:
        """
        Method to create Policy Optimizer ticket
        :param request_body: JSON body for ticket.
        :return: Response code
        """
        endpoint = self.parser.get('REST', 'create_po_ticket').format(self.host, self.domain_id)
        try:
            resp = requests.post(url=endpoint, headers=self.headers, json=request_body, verify=self.verify_ssl)
            resp.raise_for_status()
            return resp.status_code
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred creating Policy Optimizer ticket: {0}\nMessage: {1}".format(e, e.response.text))

    def get_po_ticket(self, ticket_id: str) -> dict:
        """
        Method to retrieve Policy Optimizer ticket JSON
        :param ticket_id: ID of ticket
        :return: JSON of ticket
        """
        endpoint = self.parser.get('REST', 'get_po_ticket').format(self.host, self.domain_id, self.workflow_id, ticket_id)
        try:
            resp = requests.get(url=endpoint, headers=self.headers, verify=self.verify_ssl)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred retrieving Policy Optimizer ticket: {0}\nMessage: {1}".format(e, e.response.text))

    def assign_po_ticket(self, ticket_id: str, user_id: str) -> int:
        """
        Method to assign user to Policy Optimizer ticket
        :param ticket_id: ID of ticket
        :param user_id: ID of user
        :return: Response code
        """
        ticket_json = self.get_po_ticket(ticket_id)
        workflow_packet_task_id = self.get_workflow_packet_task_id(ticket_json)
        workflow_task_id = self.get_workflow_task_id(ticket_json)
        endpoint = self.parser.get('REST', 'assign_po_ticket').format(self.host, self.domain_id, self.workflow_id, workflow_task_id, ticket_id, workflow_packet_task_id)
        try:
            resp = requests.put(url=endpoint, headers=self.headers, data=user_id, verify=self.verify_ssl)
            resp.raise_for_status()
            return resp.status_code
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred assigning Policy Optimizer ticket: {0}\nMessage: {1}".format(e, e.response.text))

    def complete_po_ticket(self, ticket_id: str, decision: dict) -> int:
        """
        Method to complete a Policy Optimizer ticket
        :param ticket_id: ID of ticket
        :param decision: Decision JSON
        :return: Response code
        """
        ticket_json = self.get_po_ticket(ticket_id)
        workflow_packet_task_id = self.get_workflow_packet_task_id(ticket_json)
        workflow_task_id = self.get_workflow_task_id(ticket_json)
        endpoint = self.parser.get('REST', 'complete_po_ticket').format(self.host, self.domain_id, self.workflow_id, workflow_task_id, ticket_id, workflow_packet_task_id, 'complete')
        try:
            resp = requests.put(url=endpoint, headers=self.headers, json=decision, verify=self.verify_ssl)
            resp.raise_for_status()
            return resp.status_code
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred completing Policy Optimizer ticket: {0}\nMessage: {1}".format(e, e.response.text))

    def cancel_po_ticket(self, ticket_id: str) -> int:
        """
        Method to cancel a Policy Optimizer ticket
        :param ticket_id: ID of ticket
        :return: Response code
        """
        ticket_json = self.get_po_ticket(ticket_id)
        workflow_packet_task_id = self.get_workflow_packet_task_id(ticket_json)
        workflow_task_id = self.get_workflow_task_id(ticket_json)
        endpoint = self.parser.get('REST', 'complete_po_ticket').format(self.host, self.domain_id, self.workflow_id, workflow_task_id, ticket_id, workflow_packet_task_id, 'cancelled')
        try:
            resp = requests.put(url=endpoint, headers=self.headers, json={}, verify=self.verify_ssl)
            resp.raise_for_status()
            return resp.status_code
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred cancelling Policy Optimizer ticket: {0}\nMessage: {1}".format(e, e.response.text))

    def siql_query_po_ticket(self, parameters: dict) -> dict:
        """
        Method to execute SIQL query for Policy Optimizer tickets
        :param parameters: search parameters
        :return: Response JSON
        """
        endpoint = self.parser.get('REST', 'siql_query_po').format(self.host, self.domain_id)
        try:
            resp = requests.get(url=endpoint, headers=self.headers, params=parameters, verify=self.verify_ssl)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred executing SIQL query for Policy Optimizer tickets: {0}\nMessage: {1}".format(e, e.response.text))

    def logout(self) -> list:
        """
        Method to logout of session
        """
        self.headers['Connection'] = 'Close'
        endpoint = self.parser.get('REST', 'logout_api_url').format(self.host)
        try:
            resp = requests.post(url=endpoint, headers=self.headers, verify=self.verify_ssl)
            resp.raise_for_status()
            return [resp.status_code, resp.reason]
        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred logging out of session: {0}\nMessage: {1}".format(e, e.response.text))

    def get_workflow_packet_task_id(self, ticket_json: dict) -> str:
        """
        Retrieves workflowPacketTaskId value from current stage of provided ticket
        :param ticket_json: JSON of ticket, retrieved using pull_ticket function
        :return: workflowPacketTaskId of current stage for given ticket
        """
        curr_stage = ticket_json['status']
        workflow_packet_tasks = ticket_json['workflowPacketTasks']
        for t in workflow_packet_tasks:
            if t['workflowTask']['name'] == curr_stage:
                return str(t['id'])

    def get_workflow_task_id(self, ticket_json: dict) -> str:
        """
        Retrieves workflowTaskId value from current stage of provided ticket
        :param ticket_json: JSON of ticket, retrieved using pull_ticket function
        :return: workflowTaskId of current stage for given ticket
        """
        curr_stage = ticket_json['status']
        workflow_packet_tasks = ticket_json['workflowPacketTasks']
        for t in workflow_packet_tasks:
            if t['workflowTask']['name'] == curr_stage:
                return str(t['workflowTask']['id'])

    def get_workflow_id_by_workflow_name(self, domain_id: str, workflow_name: str) -> str:
        """ Takes domainId and workflow name as input parameters and returns you
            the workflowId for given workflow name """
        workflow_url = self.parser.get('REST', 'find_all_po_workflows_url').format(self.host, domain_id)
        try:
            self.api_resp = requests.get(url=workflow_url, headers=self.headers, verify=self.verify_ssl)
            self.api_resp.raise_for_status()
            count_of_workflows = self.api_resp.json().get('total')

            # Here, default pageSize is 10
            # CASE 1 :If total workflows > 10 then second call will be made to get all the remaining workflows
            # CASE 2 :No need to make a second call if total workflows < 10 as we already have all of them
            if (count_of_workflows > 10):
                parameters = {'includeDisabled': False, 'pageSize': count_of_workflows}
                self.api_resp = requests.get(url=workflow_url, headers=self.headers, params=parameters, verify=self.verify_ssl)
                self.api_resp.raise_for_status()

            list_of_workflows = self.api_resp.json().get('results')
            for workflow in list_of_workflows:
                if (workflow['workflow']['name'] == workflow_name):
                    workflow_id = workflow['workflow']['id']
                    return workflow_id

        except requests.exceptions.HTTPError as e:
            raise SystemExit("Exception occurred retrieving workflow ID: {0}\nMessage: {1}".format(e, e.response.text))
