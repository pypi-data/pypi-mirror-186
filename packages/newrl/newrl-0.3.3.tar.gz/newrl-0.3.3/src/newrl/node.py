import requests


class Node():
    def __init__(self, url='http://devnet.newrl.net:8420'):
        self.url = url

    def get_balance(self, balance_type, wallet_address, token_code):
        balance_path = F'/get-balances?balance_type={balance_type}&token_code={token_code}&wallet_address={wallet_address}'
        response = requests.get(self.url + balance_path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()['balance']
    
    def get_sc_state(self, sc_state, contract_address, lookup_field, lookup_value):
        response = requests.get(self.url + f"/sc-state?table_name={sc_state}&contract_address={contract_address}&unique_column={lookup_field}&unique_value={lookup_value}")
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def submit_transaction(self, transaction):
        path = '/submit-transaction'
        response = requests.post(
            self.url + path, json=transaction)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()
    
    def submit_transactions(self, transactions):
        path = '/submit-transaction-batch'
        response = requests.post(
            self.url + path, json=transactions)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()