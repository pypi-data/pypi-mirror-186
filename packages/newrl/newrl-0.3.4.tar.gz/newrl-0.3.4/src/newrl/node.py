import requests


class Node():
    def __init__(self, url='http://devnet.newrl.net:8420'):
        self.url = url

    # Not being fond
    def get_block(self, block_index: str) -> dict:
        """Get a block from the chain

        Parameters
        ----------
        block_index : str
            Block index of the block to be queried 

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found 
        """
        path = F'/get-block?block_index={block_index}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    # Not being found
    def get_transaction(self, transaction_code: str) -> dict:
        """Get transaction details from the chain

        Parameters
        ----------
        transaction_code : str
            transaction code for transaction to be quiered 

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found
        """
        path = F'/get-transaction?transaction_code={transaction_code}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_wallet(self, wallet_address: str) -> dict:
        """"Get a wallet details from the chain

        Parameters
        ----------
        wallet_address : str
            Wallet address for details to be queried 

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found 

        Returns
        -------
        {
            "wallet_address" : str,
            "wallet_public" : str,
            "wallet_private" : null,
            "custodian_wallet" : str,
            "kyc_docs" : '[{
                "type" : int,
                "hash" : str
            }]',
            "owner_type" : int,
            "jurisdiction" int,
            "specific data" : dict,
            "person_id" : str
        }
        """
        path = F'/get-wallet?wallet_address={wallet_address}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_token(self, token_code: str) -> dict:
        """"Get a token details from the chain

        Parameters
        ----------
        token_code : str
            token code for details to be queried 

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found

        Returns
        -------
        {
            "tokencode" : str,
            "tokenname" : str,
            "tokentype" : int,
            "first_owner" : null,
            "custodian" : null,
            "legaldochash" : null,
            "amount_created" : int
            "sc_flag" : int
            "disallowed" : null
            "tokendecimal" : int 
            "parent_transaction_code" : null,
            "token_attribute" : '{}'
        } 
        """
        path = F'/get-token?token_code={token_code}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_balances(self, wallet_address: str, balance_type: str = 'TOKEN_IN_WALLET', token_code: str = 'NWRL') -> dict:
        """Get various balances of a token in wallet

        Parameters
        ----------
        wallet_address : str
            address of wallet to be queried 

        balance_type : str, one of ['TOKEN_IN_WALLET', 'ALL_TOKENS_IN_WALLET', 'ALL_WALLETS_FOR_TOKEN']
            balance type to be returned, default is 'TOKEN_IN_WALLET' 

        token_code : str  
            token code for balance to be returned, default is 'NWRL'

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found

        Returns
        -------
        {
            'balance' : int or list 
        }
        """
        balance_path = F'/get-balances?balance_type={balance_type}&token_code={token_code}&wallet_address={wallet_address}'
        response = requests.get(self.url + balance_path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_contract(self, contract_address: str):
        """Get contract details from the chain

        Parameters
        ----------
        contract_address : str
            contract adress of contract to be queried 

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found

        """
        path = F'/get-contract?contract_address={contract_address}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_trustscore_pid(self, destination_person_id: str, source_person_id: str = 'pi1111111111111111111111111111111111111112'):
        """Get a trust score. Default source_person_id is network trust manager

        Parameters
        ----------
        destination_person_id : str
            id of node to get trust score of 

        source_person_id : str
            id of node to get trust score from, default is  'pi1111111111111111111111111111111111111112'

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found

        """
        path = F'/get-trustscore-pid?destination_person_id={destination_person_id}&source_person_id={source_person_id}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_trustscore_wallets(self, src_wallet_address: str, dst_wallet_address: str):
        """Get a trust score

        Parameters
        ----------
        dst_wallet_address : str
            wallet address of node to get trust score of

        src_wallet_address : str
            wallet address of node to get trust score from 

        Raises
        ------
        Exception
            If the passed URL for the node cannot be found

        """
        path = F'/get-trustscore-pid?src_wallet_address={src_wallet_address}&dst_wallet_address={dst_wallet_address}'
        response = requests.get(self.url + path)
        if response.status_code != 200:
            raise Exception('Error calling node: ', response.text)
        return response.json()

    def get_sc_state(self, sc_state, contract_address, lookup_field, lookup_value):
        response = requests.get(
            self.url + f"/sc-state?table_name={sc_state}&contract_address={contract_address}&unique_column={lookup_field}&unique_value={lookup_value}")
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
